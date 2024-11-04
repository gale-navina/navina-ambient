from typing import List, Dict, Optional, Any, Union
from datetime import datetime, timedelta
from abc import ABC, abstractmethod
import pandas as pd
import pandera as pa
from pandera.typing import Series, DataFrame

from auto_documentation.labs.labs import SupportedBaseLabsNames, LabNames, BaseLab, LoincMapping, LabCategory, LoincLab
from auto_documentation.schemas import BaseLabSchema


# Base Processor
class LabProcessor(ABC):
    @abstractmethod
    def process(self, data: pd.DataFrame) -> Dict[LabNames, pd.DataFrame]:
        pass

    @staticmethod
    def _standardize_dataframe(df: pd.DataFrame) -> pd.DataFrame:
        if 'observationValue' not in df.columns and 'value' in df.columns:
            df['observationValue'] = df['value']
        return df

    @staticmethod
    def _prepare_lab_data(data: pd.DataFrame, lookback_days: Optional[int] = None) -> pd.DataFrame:
        """
        Standardized method to prepare lab data, handling both single values and history
        """
        if data.empty:
            return pd.DataFrame()

        if 'history' in data.columns:
            df = pd.DataFrame.from_records(data['history'].iloc[0])
        else:
            df = pd.DataFrame({
                'date': [data['date'].iloc[0]],
                'observationValue': [data['value'].iloc[0]],
                'originalValue': [data['originalValue'].iloc[0]],
                'observationNote': [None]
            })

        df['date'] = pd.to_datetime(df['date'])
        df = df.sort_values(by='date', ascending=False)

        if lookback_days is not None:
            cutoff_date = datetime.now().date() - timedelta(days=lookback_days)
            df = df[df['date'].dt.date >= cutoff_date]

        return df

    @staticmethod
    def _create_status_df(date: Any, status: str) -> pd.DataFrame:
        return pd.DataFrame({'date': date, 'observationValue': status}, index=[0])


class MultiTestProcessor(LabProcessor):
    """Base class for processors that handle multiple tests"""

    def __init__(self, test_names: List[LabNames]):
        self.test_names = test_names

    def process(self, data: pd.DataFrame) -> Dict[LabNames, pd.DataFrame]:
        result = {}
        for test_name in self.test_names:
            if (test_name.value in data.columns and
                    data[test_name.value].loc['value'] != 'NONE_ON_FILE'):
                result[test_name] = self._process_single_test(data, test_name.value)
        return result

    def _process_single_test(self, data: pd.DataFrame, test_name: str) -> pd.DataFrame:
        if 'history' in data[test_name].index:
            return pd.DataFrame(pd.DataFrame(data[test_name]['history']).iloc[0]).transpose()
        return pd.DataFrame(pd.DataFrame(data[test_name]).transpose()).rename(
            columns={'value': 'observationValue'})


class TrendAnalyzer:
    """Utility class for analyzing trends in lab values"""

    @staticmethod
    def analyze_trend(current: float, previous: float, stability_threshold: float = 0.5) -> str:
        if abs(current - previous) <= stability_threshold:
            return "stable"
        return "increasing" if current > previous else "decreasing"


# Modified Concrete Processors
class HbA1cProcessor(LabProcessor):
    def process(self, data: pd.DataFrame) -> Dict[LabNames, pd.DataFrame]:
        hba1c = self._prepare_lab_data(data, lookback_days=3 * 365).iloc[:2]
        if hba1c.empty:
            return {}

        diabetes_status, hba1c_trend = self._analyze_hba1c(hba1c)
        return {
            LabNames.HBA1C: hba1c,
            LabNames.DIABETES_STATUS: diabetes_status,
            LabNames.HBA1C_TREND: hba1c_trend
        }

    def _analyze_hba1c(self, hba1c: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
        latest_value = float(hba1c['observationValue'].iloc[0])
        latest_date = hba1c['date'].iloc[0]

        status = (
            "well controlled" if latest_value <= 7
            else "controlled" if 7 < latest_value < 8
            else "uncontrolled"
        )

        trend = ""
        if len(hba1c) > 1:
            prev_value = float(hba1c['observationValue'].iloc[1])
            trend = TrendAnalyzer.analyze_trend(latest_value, prev_value)

        return (
            self._create_status_df(latest_date, status),
            self._create_status_df(latest_date, trend)
        )


class EGFRProcessor(LabProcessor):
    def process(self, data: pd.DataFrame) -> Dict[LabNames, pd.DataFrame]:
        egfr = self._prepare_lab_data(data).iloc[:2]
        if egfr.empty:
            return {}

        ckd_status, egfr_trend = self._analyze_egfr(egfr)
        return {
            LabNames.EGFR_NAA: egfr,
            LabNames.CKD_STATUS: ckd_status,
            LabNames.EGFR_TREND: egfr_trend
        }

    def _analyze_egfr(self, egfr: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
        latest_value = float(egfr['observationValue'].iloc[0])
        latest_date = egfr['date'].iloc[0]

        status = (
            "Normal kidney function" if latest_value >= 90
            else "CKD stage 2" if 60 <= latest_value < 90
            else "CKD stage 3A" if 45 <= latest_value < 60
            else "CKD stage 3B" if 30 <= latest_value < 45
            else "CKD stage 4" if 15 <= latest_value < 30
            else "CKD stage 5"
        )

        trend = ""
        if len(egfr) > 1:
            prev_value = float(egfr['observationValue'].iloc[1])
            trend = TrendAnalyzer.analyze_trend(latest_value, prev_value, stability_threshold=0)

        return (
            self._create_status_df(latest_date, status),
            self._create_status_df(latest_date, trend)
        )


# Simplified Concrete Processors using MultiTestProcessor
class KidneyFunctionProcessor(MultiTestProcessor):
    def __init__(self):
        super().__init__([LabNames.ALB_CREA, LabNames.MICROALB])


class LipidProfileProcessor(MultiTestProcessor):
    def __init__(self):
        super().__init__([
            LabNames.TOTAL_CHOLESTEROL,
            LabNames.TRIGLYCERIDES,
            LabNames.LDL,
            LabNames.HDL
        ])


class CBCProcessor(MultiTestProcessor):
    def __init__(self):
        super().__init__([LabNames.HGB, LabNames.WBC, LabNames.PLT])


class LiverFunctionProcessor(MultiTestProcessor):
    def __init__(self):
        super().__init__([
            LabNames.ALT,
            LabNames.AST,
            LabNames.ALP,
            LabNames.BILIRUBIN,
            LabNames.ALBUMIN
        ])


class ThyroidProcessor(MultiTestProcessor):
    def __init__(self):
        super().__init__([LabNames.FT4])


class ElectrolytesProcessor(MultiTestProcessor):
    def __init__(self):
        super().__init__([
            LabNames.SODIUM,
            LabNames.POTASSIUM,
            LabNames.CHLORIDE
        ])


class GlucoseProcessor(LabProcessor):
    def process(self, data: pd.DataFrame) -> Dict[LabNames, pd.DataFrame]:
        glucose_df = self._prepare_lab_data(data)
        return {LabNames.GLUCOSE: glucose_df} if not glucose_df.empty else {}


class LabProcessingService:
    def __init__(self):
        self.processors = {
            SupportedBaseLabsNames.HBA1C: HbA1cProcessor(),
            SupportedBaseLabsNames.EGFR_NAA: EGFRProcessor(),
            SupportedBaseLabsNames.KIDNEY_FUNCTION: KidneyFunctionProcessor(),
            SupportedBaseLabsNames.LIPID_PROFILE: LipidProfileProcessor(),
            SupportedBaseLabsNames.CBC: CBCProcessor(),
            SupportedBaseLabsNames.LIVER_FUNCTION: LiverFunctionProcessor(),
            SupportedBaseLabsNames.THYROID: ThyroidProcessor(),
            SupportedBaseLabsNames.ELECTROLYTES: ElectrolytesProcessor(),
            SupportedBaseLabsNames.GLUCOSE: GlucoseProcessor()
        }
        self.loinc_mapping = LoincMapping()

    def process_labs(self, base_labs: List[BaseLab], loinc_labs: List[LoincLab]) -> pd.DataFrame:
        """Process and concat all labs"""
        base_labs_df = self._process_base_labs(base_labs)
        loinc_labs_df = self._process_loinc_labs(loinc_labs)
        return pd.concat([base_labs_df, loinc_labs_df], ignore_index=True)

    def _get_lab_category(self, lab_name: Union[str, SupportedBaseLabsNames, LabNames]) -> Optional[LabCategory]:
        """Helper method to get category for any type of lab name"""
        if isinstance(lab_name, (SupportedBaseLabsNames, LabNames)):
            lab_name = lab_name.value

        base_lab_mappings = {
            SupportedBaseLabsNames.HBA1C.value: LabCategory.DIABETES,
            SupportedBaseLabsNames.EGFR_NAA.value: LabCategory.KIDNEY,
            SupportedBaseLabsNames.KIDNEY_FUNCTION.value: LabCategory.KIDNEY,
            SupportedBaseLabsNames.LIPID_PROFILE.value: LabCategory.LIPIDS,
            SupportedBaseLabsNames.CBC.value: LabCategory.CBC,
            SupportedBaseLabsNames.LIVER_FUNCTION.value: LabCategory.LIVER,
            SupportedBaseLabsNames.THYROID.value: LabCategory.THYROID,
            SupportedBaseLabsNames.ELECTROLYTES.value: LabCategory.ELECTROLYTES,
            SupportedBaseLabsNames.GLUCOSE.value: LabCategory.DIABETES
        }

        if lab_name in base_lab_mappings:
            return base_lab_mappings[lab_name]

        _, category = self.loinc_mapping.categorize_lab(lab_name)
        return category

    def _process_base_labs(self, base_labs: List[BaseLab]) -> pd.DataFrame:
        """Process BaseLab format with category handling"""
        all_results = {}

        for lab in base_labs:
            if lab.type == "Comment":
                data = pd.DataFrame.from_records(lab.observations)
            elif lab.type == "Single":
                data = pd.DataFrame([lab.data])
            else:
                data = pd.DataFrame.from_records(lab.data)

            if processor := self.processors.get(lab.name):
                processed_results = processor.process(data)
                category = self._get_lab_category(lab.name)

                for lab_name, df in processed_results.items():
                    if lab_name in [LabNames.DIABETES_STATUS, LabNames.HBA1C_TREND, LabNames.HBA1C]:
                        df['category'] = LabCategory.DIABETES
                    elif lab_name in [LabNames.CKD_STATUS, LabNames.EGFR_TREND]:
                        df['category'] = LabCategory.KIDNEY
                    else:
                        df['category'] = category

                all_results.update(processed_results)

        return self._combine_results(all_results)

    def _process_loinc_labs(self, labs: List[LoincLab]) -> pd.DataFrame:
        """Process labs in LOINC format with direct analysis"""
        if not labs:
            return pd.DataFrame(columns=['name', 'date', 'observationValue', 'category'])

        # Convert LOINC labs to DataFrame
        lab_records = []
        for lab in labs:
            lab_name, category = self.loinc_mapping.categorize_lab(lab.observationName)

            record = {
                'name': lab_name or lab.observationName,
                'date': lab.resultDate.date(),
                'observationValue': lab.observationValue,
                'category': category,
                'originalName': lab.observationName,
                'unit': lab.unit,
                'referenceRange': lab.referenceRange
            }
            lab_records.append(record)

        result_df = pd.DataFrame(lab_records)

        # Sort by date and keep latest 2 readings per test
        result_df = (result_df.sort_values('date', ascending=False)
                     .groupby('name')
                     .head(2)
                     .reset_index(drop=True))

        return result_df[['name', 'date', 'observationValue', 'category']]

    @staticmethod
    @pa.check_types()
    def _combine_results(results: Dict[LabNames, pd.DataFrame]) -> DataFrame[BaseLabSchema]:
        if not results:
            return pd.DataFrame(columns=['name', 'date', 'observationValue', 'category'])

        for lab_name, lab_df in results.items():
            lab_df['name'] = lab_name

        result_df = pd.concat(results.values(), ignore_index=True)[['name', 'date', 'observationValue', 'category']]
        # ensure a unified date format without datetime in a safe way
        result_df['date'] = result_df['date'].apply(lambda x: x.strftime('%Y-%m-%d') if isinstance(x, datetime) else x)
        # remove any duplicate rows
        result_df = result_df.drop_duplicates()
        return result_df
