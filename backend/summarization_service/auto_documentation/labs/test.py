import pandas as pd

from auto_documentation.labs.labs import BaseLab, SupportedBaseLabsNames, LoincLab
from auto_documentation.labs.process import LabProcessingService

example_json = [
    {
        "name": "CBC",
        "data": {
            "hgb": {
                "high": 15.9,
                "low": 11.1,
                "originalValue": "14.9",
                "value": 14.9,
                "date": "2022-04-12",
                "units": "g/dL",
                "producerId": None,
                "rangeType": "Float",
                "refRangeSource": "lab",
                "isNormal": True
            },
            "wbc": {
                "high": 10.8,
                "low": 3.4,
                "originalValue": "6.3",
                "value": 6.3,
                "date": "2022-04-12",
                "units": "x10e3/uL",
                "producerId": None,
                "rangeType": "Float",
                "refRangeSource": "lab",
                "isNormal": True
            },
            "plt": {
                "high": 450,
                "low": 150,
                "originalValue": "88",
                "value": 88,
                "date": "2022-04-12",
                "units": "x10e3/uL",
                "producerId": None,
                "rangeType": "Float",
                "refRangeSource": "lab",
                "isNormal": False
            }
        },
        "date": "2022-04-12",
        "type": "Collection",
        "child": {
            "name": "diff",
            "data": "normal",
            "observations": {},
            "observationsType": "Collection",
            "date": "2022-04-12",
            "type": "Comment",
            "isNewLine": False
        },
        "displayName": "CBC"
    },
    {
        "name": "Kidney function",
        "data": {
            "eGFR NAA": {
                "high": None,
                "low": 59,
                "originalValue": "52",
                "value": 52,
                "date": "2022-11-15",
                "units": "mL/min/1.73",
                "producerId": None,
                "rangeType": "Float",
                "refRangeSource": "lab",
                "isNormal": False,
                "source": "redox-event",
                "sourceDetails": None,
                "history": [
                    {
                        "date": "11/15/2022",
                        "observationValue": 52,
                        "originalValue": "52",
                        "observationNote": None,
                        "source": "redox-event",
                        "sourceDetails": None
                    },
                    {
                        "date": "10/28/2022",
                        "observationValue": 56,
                        "originalValue": "56",
                        "observationNote": None,
                        "source": "redox-event",
                        "sourceDetails": None
                    },
                    {
                        "date": "09/09/2022",
                        "observationValue": 63,
                        "originalValue": "63",
                        "observationNote": None,
                        "source": "HIE",
                        "sourceDetails": "{\"organization_name\": \"Main Street General\"}"
                    },
                    {
                        "date": "08/15/2022",
                        "observationValue": 67,
                        "originalValue": "67",
                        "observationNote": None,
                        "source": "HIE",
                        "sourceDetails": "{\"organization_name\": \"Sacred Heart Hospital\"}"
                    },
                    {
                        "date": "05/20/2022",
                        "observationValue": 54,
                        "originalValue": "54",
                        "observationNote": None,
                        "source": "HIE",
                        "sourceDetails": "{\"organization_name\": \"Main Street Clinic\"}"
                    },
                    {
                        "date": "04/29/2022",
                        "observationValue": 57,
                        "originalValue": "57",
                        "observationNote": None,
                        "source": "HIE",
                        "sourceDetails": "{\"organization_name\": \"Nephrology Consultants of Scranton \"}"
                    },
                    {
                        "date": "03/16/2022",
                        "observationValue": 55,
                        "originalValue": "55",
                        "observationNote": None,
                        "source": "redox-event",
                        "sourceDetails": None
                    },
                    {
                        "date": "01/12/2022",
                        "observationValue": 50,
                        "originalValue": "50",
                        "observationNote": None,
                        "source": "redox-event",
                        "sourceDetails": None
                    },
                    {
                        "date": "11/03/2021",
                        "observationValue": 61,
                        "originalValue": "61",
                        "observationNote": None,
                        "source": "redox-event",
                        "sourceDetails": None
                    },
                    {
                        "date": "09/23/2021",
                        "observationValue": 70,
                        "originalValue": "70",
                        "observationNote": None,
                        "source": "redox-event",
                        "sourceDetails": None
                    },
                    {
                        "date": "08/15/2021",
                        "observationValue": 88,
                        "originalValue": "88",
                        "observationNote": None,
                        "source": "redox-event",
                        "sourceDetails": None
                    },
                    {
                        "date": "05/29/2021",
                        "observationValue": 80,
                        "originalValue": "80",
                        "observationNote": None,
                        "source": "redox-event",
                        "sourceDetails": None
                    },
                    {
                        "date": "02/04/2021",
                        "observationValue": 74,
                        "originalValue": "74",
                        "observationNote": None,
                        "source": "HIE",
                        "sourceDetails": "{\"organization_name\": \"Main Street Clinic (Dr. Feller)\"}"
                    },
                    {
                        "date": "01/30/2021",
                        "observationValue": 80,
                        "originalValue": "80",
                        "observationNote": None,
                        "source": "redox-event",
                        "sourceDetails": None
                    },
                    {
                        "date": "11/1/2020",
                        "observationValue": 58,
                        "originalValue": "58",
                        "observationNote": None,
                        "source": "HIE",
                        "sourceDetails": "{\"organization_name\": \"Sacred Heart Hospital\"}"
                    },
                    {
                        "date": "10/30/2020",
                        "observationValue": 50,
                        "originalValue": "50",
                        "observationNote": None,
                        "source": "HIE",
                        "sourceDetails": "{\"organization_name\": \"MSacred Heart Hospital\"}"
                    },
                    {
                        "date": "10/29/2020",
                        "observationValue": 47,
                        "originalValue": "47",
                        "observationNote": None,
                        "source": "HIE",
                        "sourceDetails": "{\"organization_name\": \"Sacred Heart Hospital\"}"
                    },
                    {
                        "date": "10/28/2020",
                        "observationValue": 43,
                        "originalValue": "43",
                        "observationNote": None,
                        "source": "HIE",
                        "sourceDetails": "{\"organization_name\": \"Sacred Heart Hospital\"}"
                    },
                    {
                        "date": "08/24/2020",
                        "observationValue": 70,
                        "originalValue": "70",
                        "observationNote": None,
                        "source": "redox-event",
                        "sourceDetails": None
                    }
                ]
            },
            "creatinine": {
                "high": 1,
                "low": 0.57,
                "originalValue": "1.2",
                "value": 1.2,
                "date": "2022-03-16",
                "units": "mg/dL",
                "producerId": None,
                "rangeType": "Float",
                "refRangeSource": "lab",
                "isNormal": False
            },
            "bun": {
                "high": 27,
                "low": 8,
                "originalValue": "26",
                "value": 26,
                "date": "2022-03-16",
                "units": "mg/dL",
                "producerId": None,
                "rangeType": "Float",
                "refRangeSource": "lab",
                "isNormal": True
            }
        },
        "date": "2022-03-16",
        "type": "Collection",
        "displayName": "Kidney function"
    },
    {
        "name": "Electrolytes",
        "data": "normal",
        "observations": {
            "potassium": {
                "high": 5.2,
                "low": 3.5,
                "originalValue": "3.8",
                "value": 3.8,
                "date": "2022-03-16",
                "units": "mmol/L",
                "producerId": None,
                "rangeType": "Float",
                "refRangeSource": "lab",
                "history": [
                    {
                        "date": "2022-03-16",
                        "observationValue": 3.8,
                        "originalValue": "3.8",
                        "observationNote": None
                    },
                    {
                        "date": "2022-01-12",
                        "observationValue": 3.6,
                        "originalValue": "3.6",
                        "observationNote": None
                    }
                ],
                "isNormal": True
            },
            "sodium": {
                "high": 144,
                "low": 134,
                "originalValue": "142",
                "value": 142,
                "date": "2022-03-16",
                "units": "mmol/L",
                "producerId": None,
                "rangeType": "Float",
                "refRangeSource": "lab",
                "history": [
                    {
                        "date": "2022-03-16",
                        "observationValue": 142,
                        "originalValue": "142",
                        "observationNote": None
                    },
                    {
                        "date": "2022-01-12",
                        "observationValue": 140,
                        "originalValue": "140",
                        "observationNote": None
                    }
                ],
                "isNormal": True
            },
            "chloride": {
                "high": 106,
                "low": 96,
                "originalValue": "97",
                "value": 97,
                "date": "2022-03-16",
                "units": "mmol/L",
                "producerId": None,
                "rangeType": "Float",
                "refRangeSource": "lab",
                "history": [
                    {
                        "date": "2022-03-16",
                        "observationValue": 97,
                        "originalValue": "97",
                        "observationNote": None
                    },
                    {
                        "date": "2022-01-12",
                        "observationValue": 100,
                        "originalValue": "100",
                        "observationNote": None
                    }
                ],
                "isNormal": True
            }
        },
        "observationsType": "Collection",
        "date": "2022-03-16",
        "type": "Comment",
        "displayName": "Electrolytes"
    },
    {
        "name": "Glucose",
        "data": {
            "high": 99,
            "low": 65,
            "originalValue": "184",
            "value": 184,
            "date": "2022-03-16",
            "units": "mg/dL",
            "producerId": None,
            "rangeType": "Float",
            "refRangeSource": "lab",
            "isNormal": False
        },
        "date": "2022-03-16",
        "type": "Single",
        "displayName": "Glucose"
    },
    {
        "name": "HbA1c",
        "data": {
            "high": 5.7,
            "low": 3.8,
            "originalValue": "10.5",
            "value": 10.5,
            "date": "2022-08-20",
            "units": "%",
            "producerId": None,
            "rangeType": "Float",
            "refRangeSource": "static table",
            "isNormal": False,
            "source": "HIE",
            "sourceDetails": "{\"file_id\": \"b3c1b14d-fb9e-4374-a544-77098d13a6dd\",\"organization_name\": \"Main Street General\"}",
            "history": [
                {
                    "date": "08/20/2022",
                    "observationValue": 10.5,
                    "originalValue": "10.5",
                    "observationNote": None,
                    "source": "HIE",
                    "sourceDetails": "{\"file_id\": \"b3c1b14d-fb9e-4374-a544-77098d13a6dd\",\"organization_name\": \"Main Street General\"}"
                },
                {
                    "date": "05/29/2022",
                    "observationValue": 8.5,
                    "originalValue": "8.5",
                    "observationNote": None,
                    "source": "HIE",
                    "sourceDetails": "{\"organization_name\": \"Main Street General\"}"
                },
                {
                    "date": "02/05/2022",
                    "observationValue": 9.5,
                    "originalValue": "9.5",
                    "observationNote": None,
                    "source": "HIE",
                    "sourceDetails": "{\"organization_name\": \"Main Street General\"}"
                },
                {
                    "date": "01/01/2022",
                    "observationValue": 9.2,
                    "originalValue": "9.2",
                    "observationNote": None,
                    "source": "redox-event",
                    "sourceDetails": None
                },
                {
                    "date": "11/03/2021",
                    "observationValue": 8,
                    "originalValue": "8",
                    "observationNote": None,
                    "source": "redox-event",
                    "sourceDetails": None
                },
                {
                    "date": "08/15/2021",
                    "observationValue": 7.4,
                    "originalValue": "7.4",
                    "observationNote": None,
                    "source": "redox-event",
                    "sourceDetails": None
                },
                {
                    "date": "05/29/2021",
                    "observationValue": 6.4,
                    "originalValue": "6.4",
                    "observationNote": None,
                    "source": "HIE",
                    "sourceDetails": "{\"organization_name\": \"Main Street General\"}"
                },
                {
                    "date": "01/30/2021",
                    "observationValue": 6.3,
                    "originalValue": "6.3",
                    "observationNote": None,
                    "source": "redox-event",
                    "sourceDetails": None
                },
                {
                    "date": "10/1/2020",
                    "observationValue": 6.4,
                    "originalValue": "6.4",
                    "observationNote": None,
                    "source": "HIE",
                    "sourceDetails": "{\"organization_name\": \"Main Street General\"}"
                },
                {
                    "date": "08/24/2020",
                    "observationValue": 5.8,
                    "originalValue": "5.8",
                    "observationNote": None,
                    "source": "redox-event",
                    "sourceDetails": None
                },
                {
                    "date": "5/29/2020",
                    "observationValue": 5.9,
                    "originalValue": "5.9",
                    "observationNote": None,
                    "source": "redox-event",
                    "sourceDetails": None
                }
            ]
        },
        "date": "2022-01-12",
        "type": "Single",
        "displayName": "HbA1c"
    },
    {
        "name": "Liver function",
        "data": {
            "alt": {
                "high": 32,
                "low": 0,
                "originalValue": "21",
                "value": 21,
                "date": "2022-01-12",
                "units": "IU/L",
                "producerId": None,
                "rangeType": "Float",
                "refRangeSource": "lab",
                "isNormal": True
            },
            "alp": {
                "high": 121,
                "low": 44,
                "originalValue": "137",
                "value": 137,
                "date": "2022-01-12",
                "units": "IU/L",
                "producerId": None,
                "rangeType": "Float",
                "refRangeSource": "lab",
                "isNormal": False
            },
            "ast": {
                "high": 40,
                "low": 0,
                "originalValue": "25",
                "value": 25,
                "date": "2022-01-12",
                "units": "IU/L",
                "producerId": None,
                "rangeType": "Float",
                "refRangeSource": "lab",
                "isNormal": True
            },
            "bilirubin (tot)": {
                "high": 1.2,
                "low": 0,
                "originalValue": "0.5",
                "value": 0.5,
                "date": "2022-01-12",
                "units": "mg/dL",
                "producerId": None,
                "rangeType": "Float",
                "refRangeSource": "lab",
                "isNormal": True
            },
            "albumin": {
                "high": 4.7,
                "low": 3.7,
                "originalValue": "4,4",
                "value": None,
                "date": "2022-01-12",
                "units": None,
                "producerId": None,
                "rangeType": "Float",
                "refRangeSource": "lab",
                "isNormal": True
            }
        },
        "date": "2022-01-12",
        "type": "Collection",
        "displayName": "Liver function"
    },
    {
        "name": "Lipid profile",
        "data": {
            "tc": {
                "high": 199,
                "low": 100,
                "originalValue": "246",
                "value": 246,
                "date": "2021-03-17",
                "units": "mg/dL",
                "producerId": None,
                "rangeType": "Float",
                "refRangeSource": "lab",
                "isNormal": False
            },
            "tg": {
                "high": 149,
                "low": 0,
                "originalValue": "144",
                "value": 144,
                "date": "2021-03-17",
                "units": "mg/dL",
                "producerId": None,
                "rangeType": "Float",
                "refRangeSource": "lab",
                "isNormal": True
            },
            "ldl": {
                "high": 99,
                "low": 0,
                "originalValue": "155",
                "value": 155,
                "date": "2021-03-17",
                "units": "mg/dL",
                "producerId": None,
                "rangeType": "Float",
                "refRangeSource": "lab",
                "isNormal": False
            },
            "hdl": {
                "high": None,
                "low": 39,
                "originalValue": "65",
                "value": 65,
                "date": "2021-03-17",
                "units": "mg/dL",
                "producerId": None,
                "rangeType": "Float",
                "refRangeSource": "lab",
                "isNormal": True
            }
        },
        "date": "2021-03-17",
        "type": "Collection",
        "displayName": "Lipid profile"
    },
    {
        "name": "Thyroid",
        "data": {
            "ft4F": {
                "high": 1.8,
                "low": 0.8,
                "originalValue": "1.5",
                "value": 1.5,
                "date": "2022-01-12",
                "units": "NG/dL",
                "producerId": None,
                "rangeType": "Float",
                "refRangeSource": "lab",
                "isNormal": True
            }
        },
        "date": "2022-01-12",
        "type": "Collection",
        "displayName": "Thyroid"
    }
]

all_labs = [
    {
        "code": "2093-3",
        "name": "Lipid Panel, Serum",
        "observationName": "Cholesterol, Total",
        "observationValue": "246",
        "referenceRange": "100-199 mg/dL",
        "unit": "mg/dL",
        "resultDate": "2021-03-17",
        "source": "redox-event",
        "method": "by_fallback",
        "originalResultCode": None
    },
    {
        "code": "2085-9",
        "name": "Lipid Panel, Serum",
        "observationName": "HDL Cholesterol",
        "observationValue": "65",
        "referenceRange": ">39 mg/dL",
        "unit": "mg/dL",
        "resultDate": "2021-03-17",
        "source": "redox-event",
        "method": "by dictionary",
        "originalResultCode": None
    },
    {
        "code": "2089-1",
        "name": "Lipid Panel, Serum",
        "observationName": "LDL Cholesterol",
        "observationValue": "155",
        "referenceRange": "0-99 mg/dL",
        "unit": "mg/dL",
        "resultDate": "2021-03-17",
        "source": "redox-event",
        "method": "by dictionary",
        "originalResultCode": None
    },
    {
        "code": "2571-8",
        "name": "Lipid Panel, Serum",
        "observationName": "Triglycerides",
        "observationValue": "144",
        "referenceRange": "0-149 mg/dL",
        "unit": "mg/dL",
        "resultDate": "2021-03-17",
        "source": "redox-event",
        "method": "by dictionary",
        "originalResultCode": None
    },
    {
        "code": "13458-5",
        "name": "Lipid Panel, Serum",
        "observationName": "VLDL Cholesterol",
        "observationValue": "26",
        "referenceRange": "5-40 mg/dL",
        "unit": "mg/dL",
        "resultDate": "2021-03-17",
        "source": "redox-event",
        "method": "by dictionary",
        "originalResultCode": None
    },
    {
        "code": "1751-7",
        "name": "BMP, Blood",
        "observationName": "Albumin",
        "observationValue": "4,4",
        "referenceRange": "3.7-4.7 g/dL",
        "unit": None,
        "resultDate": "2022-01-12",
        "source": "redox-event",
        "method": "by lab LOINC - fuzzy observation",
        "originalResultCode": None
    },
    {
        "code": "6768-6",
        "name": "BMP, Blood",
        "observationName": "Alkaline Phosphate",
        "observationValue": "137",
        "referenceRange": "44-121 IU/L",
        "unit": "IU/L",
        "resultDate": "2022-01-12",
        "source": "redox-event",
        "method": "by lab LOINC - fuzzy observation",
        "originalResultCode": None
    },
    {
        "code": "1742-6",
        "name": "BMP, Blood",
        "observationName": "Alt (Sgpt)",
        "observationValue": "21",
        "referenceRange": "0-32 IU/L",
        "unit": "IU/L",
        "resultDate": "2022-01-12",
        "source": "redox-event",
        "method": "by dictionary",
        "originalResultCode": None
    },
    {
        "code": "1920-8",
        "name": "BMP, Blood",
        "observationName": "Ast (Sgot)",
        "observationValue": "25",
        "referenceRange": "0-40 IU/L",
        "unit": "IU/L",
        "resultDate": "2022-01-12",
        "source": "redox-event",
        "method": "by dictionary",
        "originalResultCode": None
    },
    {
        "code": "1975-2",
        "name": "BMP, Blood",
        "observationName": "Bilirubin, Total",
        "observationValue": "0.5",
        "referenceRange": "0.0-1.2 mg/dL",
        "unit": "mg/dL",
        "resultDate": "2022-01-12",
        "source": "redox-event",
        "method": "by dictionary",
        "originalResultCode": None
    },
    {
        "code": "3094-0",
        "name": "BMP, Blood",
        "observationName": "Bun",
        "observationValue": "23",
        "referenceRange": "8-27 mg/dL",
        "unit": "mg/dL",
        "resultDate": "2022-01-12",
        "source": "redox-event",
        "method": "by dictionary",
        "originalResultCode": None
    },
    {
        "code": "3094-0",
        "name": "BMP, Blood",
        "observationName": "Bun",
        "observationValue": "26",
        "referenceRange": "8-27 mg/dL",
        "unit": "mg/dL",
        "resultDate": "2022-03-16",
        "source": "redox-event",
        "method": "by dictionary",
        "originalResultCode": None
    },
    {
        "code": "2075-0",
        "name": "BMP, Blood",
        "observationName": "Chloride",
        "observationValue": "100",
        "referenceRange": "96-106 mmol/L",
        "unit": "mmol/L",
        "resultDate": "2022-01-12",
        "source": "redox-event",
        "method": "by dictionary",
        "originalResultCode": None
    },
    {
        "code": "2075-0",
        "name": "BMP, Blood",
        "observationName": "Chloride",
        "observationValue": "97",
        "referenceRange": "96-106 mmol/L",
        "unit": "mmol/L",
        "resultDate": "2022-03-16",
        "source": "redox-event",
        "method": "by dictionary",
        "originalResultCode": None
    },
    {
        "code": "2160-0",
        "name": "BMP, Blood",
        "observationName": "Creatinine",
        "observationValue": "1.1",
        "referenceRange": "0.57-1.00 mg/dL",
        "unit": "mg/dL",
        "resultDate": "2022-01-12",
        "source": "redox-event",
        "method": "by dictionary",
        "originalResultCode": None
    },
    {
        "code": "2160-0",
        "name": "BMP, Blood",
        "observationName": "Creatinine",
        "observationValue": "1.2",
        "referenceRange": "0.57-1.00 mg/dL",
        "unit": "mg/dL",
        "resultDate": "2022-03-16",
        "source": "redox-event",
        "method": "by dictionary",
        "originalResultCode": None
    },
    {
        "code": "77147-7",
        "name": "BMP, Blood",
        "observationName": "Egfr Naa",
        "observationValue": "50",
        "referenceRange": ">59 mL/min/1.73",
        "unit": "mL/min/1.73",
        "resultDate": "2022-01-12",
        "source": "redox-event",
        "method": "by observation name only",
        "originalResultCode": None
    },
    {
        "code": "77147-7",
        "name": "BMP, Blood",
        "observationName": "Egfr Naa",
        "observationValue": "55",
        "referenceRange": ">59 mL/min/1.73",
        "unit": "mL/min/1.73",
        "resultDate": "2022-03-16",
        "source": "redox-event",
        "method": "by observation name only",
        "originalResultCode": None
    },
    {
        "code": "3024-7",
        "name": "BMP, Blood",
        "observationName": "Ft4",
        "observationValue": "1.5",
        "referenceRange": "0.8-1.8 NG/dL",
        "unit": "NG/dL",
        "resultDate": "2022-01-12",
        "source": "redox-event",
        "method": "by observation name only",
        "originalResultCode": None
    },
    {
        "code": "2345-7",
        "name": "BMP, Blood",
        "observationName": "Glucose",
        "observationValue": "155",
        "referenceRange": "65-99 mg/dL",
        "unit": "mg/dL",
        "resultDate": "2022-01-12",
        "source": "redox-event",
        "method": "by dictionary",
        "originalResultCode": None
    },
    {
        "code": "2345-7",
        "name": "BMP, Blood",
        "observationName": "Glucose",
        "observationValue": "184",
        "referenceRange": "65-99 mg/dL",
        "unit": "mg/dL",
        "resultDate": "2022-03-16",
        "source": "redox-event",
        "method": "by dictionary",
        "originalResultCode": None
    },
    {
        "code": "4548-4",
        "name": "BMP, Blood",
        "observationName": "Hba1C",
        "observationValue": "9.2",
        "referenceRange": None,
        "unit": "%",
        "resultDate": "2022-01-12",
        "source": "redox-event",
        "method": "by observation name only",
        "originalResultCode": None
    },
    {
        "code": "2823-3",
        "name": "BMP, Blood",
        "observationName": "Potassium",
        "observationValue": "3.6",
        "referenceRange": "3.5-5.2 mmol/L",
        "unit": "mmol/L",
        "resultDate": "2022-01-12",
        "source": "redox-event",
        "method": "by dictionary",
        "originalResultCode": None
    },
    {
        "code": "2823-3",
        "name": "BMP, Blood",
        "observationName": "Pottasium",
        "observationValue": "3.8",
        "referenceRange": "3.5-5.2 mmol/L",
        "unit": "mmol/L",
        "resultDate": "2022-03-16",
        "source": "redox-event",
        "method": "by lab LOINC - fuzzy observation",
        "originalResultCode": None
    },
    {
        "code": "2951-2",
        "name": "BMP, Blood",
        "observationName": "Sodium",
        "observationValue": "140",
        "referenceRange": "134-144 mmol/L",
        "unit": "mmol/L",
        "resultDate": "2022-01-12",
        "source": "redox-event",
        "method": "by dictionary",
        "originalResultCode": None
    },
    {
        "code": "2951-2",
        "name": "BMP, Blood",
        "observationName": "Sodium",
        "observationValue": "142",
        "referenceRange": "134-144 mmol/L",
        "unit": "mmol/L",
        "resultDate": "2022-03-16",
        "source": "redox-event",
        "method": "by dictionary",
        "originalResultCode": None
    },
    {
        "code": "nan",
        "name": "BMP, Blood",
        "observationName": "Tsh",
        "observationValue": "2,2",
        "referenceRange": "0.5-5 mIU/L",
        "unit": None,
        "resultDate": "2022-01-12",
        "source": "redox-event",
        "method": "",
        "originalResultCode": None
    },
    {
        "code": "nan",
        "name": "Cbc",
        "observationName": "Basphils (Absolute)",
        "observationValue": "0.1",
        "referenceRange": "0.0-0.2",
        "unit": None,
        "resultDate": "2022-04-12",
        "source": "redox-event",
        "method": "",
        "originalResultCode": None
    },
    {
        "code": "711-2",
        "name": "Cbc",
        "observationName": "Eosinophils (Absolute)",
        "observationValue": "0.3",
        "referenceRange": "0.0-0.4",
        "unit": None,
        "resultDate": "2022-04-12",
        "source": "redox-event",
        "method": "by dictionary",
        "originalResultCode": None
    },
    {
        "code": "718-7",
        "name": "Cbc",
        "observationName": "Hemoglobin",
        "observationValue": "14.9",
        "referenceRange": "11.1-15.9 g/dL",
        "unit": "g/dL",
        "resultDate": "2022-04-12",
        "source": "redox-event",
        "method": "by dictionary",
        "originalResultCode": None
    },
    {
        "code": "731-0",
        "name": "Cbc",
        "observationName": "Lymphocytes (Absolute)",
        "observationValue": "2.7",
        "referenceRange": "0.7-3.1",
        "unit": None,
        "resultDate": "2022-04-12",
        "source": "redox-event",
        "method": "by dictionary",
        "originalResultCode": None
    },
    {
        "code": "30428-7",
        "name": "Cbc",
        "observationName": "Mcv",
        "observationValue": "94",
        "referenceRange": "79-97 fL",
        "unit": "fL",
        "resultDate": "2022-04-12",
        "source": "redox-event",
        "method": "by dictionary",
        "originalResultCode": None
    },
    {
        "code": "742-7",
        "name": "Cbc",
        "observationName": "Monocytes (Absolute)",
        "observationValue": "0.6",
        "referenceRange": "01-0.9",
        "unit": None,
        "resultDate": "2022-04-12",
        "source": "redox-event",
        "method": "by_fallback",
        "originalResultCode": None
    },
    {
        "code": "751-8",
        "name": "Cbc",
        "observationName": "Neutrophils (Absolute)",
        "observationValue": "2.7",
        "referenceRange": "1.4-7.0",
        "unit": None,
        "resultDate": "2022-04-12",
        "source": "redox-event",
        "method": "by_fallback",
        "originalResultCode": None
    },
    {
        "code": "777-3",
        "name": "Cbc",
        "observationName": "Platelets",
        "observationValue": "88",
        "referenceRange": "150-450 x10e3/uL",
        "unit": "x10e3/uL",
        "resultDate": "2022-04-12",
        "source": "redox-event",
        "method": "by dictionary",
        "originalResultCode": None
    },
    {
        "code": "789-8",
        "name": "Cbc",
        "observationName": "Rbc",
        "observationValue": "4.73",
        "referenceRange": "3.77-5.28 x10e6/uL",
        "unit": "x10e6/uL",
        "resultDate": "2022-04-12",
        "source": "redox-event",
        "method": "by_fallback",
        "originalResultCode": None
    },
    {
        "code": "6690-2",
        "name": "Cbc",
        "observationName": "Wbc",
        "observationValue": "6.3",
        "referenceRange": "3.4-10.8 x10e3/uL",
        "unit": "x10e3/uL",
        "resultDate": "2022-04-12",
        "source": "redox-event",
        "method": "by_fallback",
        "originalResultCode": None
    }
]

base_labs = [BaseLab(**lab) for lab in example_json if SupportedBaseLabsNames.has_value(lab["name"])]
all_labs = [LoincLab(**lab) for lab in all_labs]
# Create service
lab_service = LabProcessingService()

# Process labs
results = lab_service.process_labs(base_labs, all_labs)

# Print formatted results line by line
for _, result in results.iterrows():
    print(f"Name: {result['name']} | Result: {result['observationValue']} | Date: {result['date']} | Category: {result['category']}")


