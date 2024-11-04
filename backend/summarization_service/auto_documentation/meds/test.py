from auto_documentation.meds.meds import process_medications

meds_data = [
    {
        "name": "Bupropion Hcl 100 Mg Tablet",
        "dosage": "1",
        "frequency": "x 2/d",
        "appointmentDate": "2022-08-01 00:00:00",
        "medicationDate": "2022-08-01 00:00:00",
        "daysLeft": 72,
        "atcLevel2": [
            "N06"
        ],
        "atcLevel5": [
            "N06AX12"
        ],
        "displayInMedicationsList": True,
        "rxcui": [
            "993687"
        ]
    },
    {
        "name": "Voltaren Arthritis Pain 1 % Topical Gel",
        "dosage": "",
        "frequency": "PRN",
        "appointmentDate": "2022-08-01 00:00:00",
        "medicationDate": "2022-08-01 00:00:00",
        "daysLeft": None,
        "atcLevel2": [
            "M02",
            "M01",
            "S01"
        ],
        "atcLevel5": [
            "M02AA15",
            "M01AB05",
            "S01BC03"
        ],
        "displayInMedicationsList": True,
        "rxcui": [
            "855635"
        ]
    },
    {
        "name": "Meloxicam 15 Mg Tablet",
        "dosage": "1",
        "frequency": "x 2/d",
        "appointmentDate": "2022-08-01 00:00:00",
        "medicationDate": "2022-08-01 00:00:00",
        "daysLeft": 72,
        "atcLevel2": [
            "M01"
        ],
        "atcLevel5": [
            "M01AC06"
        ],
        "displayInMedicationsList": True,
        "rxcui": [
            "152695"
        ]
    },
    {
        "name": "Levothyroxine 125 Mcg Tablet",
        "dosage": "1",
        "frequency": "qd",
        "appointmentDate": "2022-11-01 00:00:00",
        "medicationDate": "2022-11-01 00:00:00",
        "daysLeft": 103,
        "atcLevel2": [
            "H03"
        ],
        "atcLevel5": [
            "H03AA01"
        ],
        "displayInMedicationsList": True,
        "rxcui": [
            "966224"
        ]
    },
    {
        "name": "Atorvastatin 10 Mg Tablet",
        "dosage": "1",
        "frequency": "qd",
        "appointmentDate": "2022-11-01 00:00:00",
        "medicationDate": "2022-11-01 00:00:00",
        "daysLeft": 103,
        "atcLevel2": [
            "C10"
        ],
        "atcLevel5": [
            "C10AA05"
        ],
        "displayInMedicationsList": True,
        "rxcui": [
            "617312"
        ]
    },
    {
        "name": "Losartan 100 Mg Tablet",
        "dosage": "1",
        "frequency": "qd",
        "appointmentDate": "2022-11-01 00:00:00",
        "medicationDate": "2022-11-01 00:00:00",
        "daysLeft": 103,
        "atcLevel2": [
            "C09"
        ],
        "atcLevel5": [
            "C09CA01"
        ],
        "displayInMedicationsList": True,
        "rxcui": [
            "979480"
        ]
    },
    {
        "name": "Omeprazole 40 Mg Capsule,Delayed Release",
        "dosage": "1",
        "frequency": "qd",
        "appointmentDate": "2022-11-01 00:00:00",
        "medicationDate": "2022-11-01 00:00:00",
        "daysLeft": 54,
        "atcLevel2": [
            "A02"
        ],
        "atcLevel5": [
            "A02BC01"
        ],
        "displayInMedicationsList": True,
        "rxcui": [
            "200329"
        ]
    },
    {
        "name": "Farxiga 10 Mg",
        "dosage": "1",
        "frequency": "qd",
        "appointmentDate": "2022-08-01 00:00:00",
        "medicationDate": "2022-08-01 00:00:00",
        "daysLeft": -35,
        "atcLevel2": [
            "A10"
        ],
        "atcLevel5": [
            "A10BK01"
        ],
        "displayInMedicationsList": True,
        "rxcui": [
            "1486977"
        ]
    }
]

print(process_medications(meds_data))
