from auto_documentation.diagnosis.diagnosis import create_evidence_table, create_diagnoses_table
import json
example_json = [
    [
        {
            "showInInsights": True,
            "showInCart": False,
            "icdCode": "J449",
            "icdDescription": "Chronic obstructive pulmonary disease, unspecified",
            "hccs": {
                "rx": [
                    {
                        "group": 229,
                        "weight": 0.186
                    }
                ],
                "v24": [
                    {
                        "group": 111,
                        "weight": 0.335
                    }
                ],
                "v28": [
                    {
                        "group": 280,
                        "weight": 0.319
                    }
                ]
            },
            "snomedDescription": "Chronic obstructive lung disease",
            "snomedCode": "13645005",
            "reasons": {
                "consults": [
                    {
                        "id": "b3c1b14d-fb9e-4374-a544-77098d13a6dd",
                        "encounterDate": "08/20/2022",
                        "fileDate": "2024-01-20",
                        "fileId": "b3c1b14d-fb9e-4374-a544-77098d13a6dd",
                        "fileLabel": "2024-01-20 Hospital discharge summary",
                        "fileLoinc": "34797-1",
                        "fileLoincName": "HIE - Hospital discharge summary",
                        "fileName": "Athena/7/7637/7637_20_08_2022_HOSPITAL_DISCHARGE_SUMMARY (HOSPITALDISCHARGE).html.pdf",
                        "hccWeight": 0.335,
                        "icd10CodeLine": 10,
                        "icd10CodeLineContent": "J44.9 Chronic Obstructive Pulmonary Disease (COPD)",
                        "icdCodes": "J44.9",
                        "index": 8,
                        "lineContentOccurrenceInDoc": 1,
                        "secondaryName": "Hospital",
                        "snomedCode": "13645005",
                        "snomedName": "Chronic obstructive lung disease"
                    }
                ],
                "inferred": [],
                "plGap": [],
                "rafGap": [
                    {
                        "data": {
                            "encounterType": "consult",
                            "modificationDate": "2023-09-14 00:00:00",
                            "providerName": "Chip Ach"
                        },
                        "icdCode": [
                            "J449"
                        ],
                        "icdData": [
                            {
                                "code": "J449",
                                "description": "Chronic obstructive pulmonary disease, unspecified",
                                "hccGroup": "111",
                                "hccWeight": 0.335
                            }
                        ],
                        "snomedCode": "13645005",
                        "type": "PreviousYears"
                    },
                    {
                        "data": {
                            "encounterType": "ops test",
                            "modificationDate": "2023-09-02 00:00:00",
                            "providerName": "Macc Test"
                        },
                        "icdCode": [
                            "J449"
                        ],
                        "icdData": [
                            {
                                "code": "J449",
                                "description": "Chronic obstructive pulmonary disease, unspecified",
                                "hccGroup": "111",
                                "hccWeight": 0.335
                            }
                        ],
                        "snomedCode": "13645005",
                        "type": "PreviousYears"
                    }
                ]
            },
            "diagnosisSources": [
                {
                    "sourceName": "Encounter (Chip Ach)",
                    "type": "raf_gap",
                    "date": "09/14/2023",
                    "data": [
                        {
                            "title": "Encounter",
                            "date": "09/14/2023",
                            "rows": [
                                {
                                    "key": "Provider name",
                                    "value": "Chip Ach"
                                }
                            ]
                        }
                    ]
                },
                {
                    "sourceName": "HIE - Hospital discharge summary",
                    "type": "consults",
                    "date": "01/20/2024",
                    "document": {
                        "name": "HIE - Hospital discharge summary",
                        "id": "b3c1b14d-fb9e-4374-a544-77098d13a6dd",
                        "date": "01/20/2024",
                        "searchTerm": "J44.9 Chronic Obstructive Pulmonary Disease (COPD)",
                        "searchTermOccurrence": 1
                    },
                    "data": [
                        {
                            "title": "Consult note",
                            "date": "01/20/2024",
                            "rows": [
                                {
                                    "key": "Document name",
                                    "value": "HIE - Hospital discharge summary"
                                },
                                {
                                    "key": "Document date",
                                    "value": "01/20/2024"
                                }
                            ]
                        }
                    ]
                }
            ],
            "suggestionDateTime": "2023-09-14 00:00:00",
            "isPrimary": True,
            "billable": True,
            "billableDescendants": [],
            "isOptionalIcd": False,
            "isChosenOptionalIcd": False,
            "diagnosisOptionalIcds": [],
            "confidenceLabel": "Recapture",
            "isBillableSubDx": False,
            "dxId": "J449",
            "dxDescription": "Chronic obstructive pulmonary disease, unspecified",
            "addedInPostVisit": False,
            "statusUpdatedAt": None,
            "statusUpdatedBy": None,
            "statusUpdatedByName": None,
            "actionUsername": "",
            "addressedGroup": "NewHCCGroup",
            "companionAddressedGroup": None,
            "status": None,
            "type": "recommendation",
            "isValid": True,
            "lastCoderStatus": None,
            "lastCoderStatusUpdatedAt": None,
            "lastCoderStatusUpdatedBy": None,
            "lastCoderStatusUpdatedByName": None,
            "lastProviderStatus": "ignored_provider",
            "lastProviderStatusUpdatedAt": "2024-10-07T14:18:45.729Z",
            "lastProviderStatusUpdatedBy": "961e602d-cda0-4797-918d-6decaeccee2a",
            "lastProviderStatusUpdatedByName": "Demo Navina",
            "coderStatus": None,
            "coderStatusUpdatedAt": None,
            "coderStatusUpdatedBy": None,
            "isCoderStatusFromCurrentSid": False,
            "providerStatus": None,
            "providerStatusUpdatedAt": None,
            "providerStatusUpdatedBy": None,
            "isProviderStatusFromCurrentSid": False,
            "statusUpdatedTimestamp": 0,
            "statusAddedTimestamp": 0,
            "companionOrder": 0,
            "companionDxs": None,
            "primaryDx": None,
            "isNavinaCoupledSuggestion": False,
            "isCoupledSuggestion": False,
            "companionId": None,
            "isSyncedFromEmr": False,
            "actionsHistory": [],
            "invalidOverride": False,
            "overrideFilter": None,
            "sourceData": {
                "type": "recommendation",
                "extra": {
                    "consults": [
                        {
                            "id": "b3c1b14d-fb9e-4374-a544-77098d13a6dd",
                            "encounterDate": "08/20/2022",
                            "fileDate": "2024-01-20",
                            "fileId": "b3c1b14d-fb9e-4374-a544-77098d13a6dd",
                            "fileLabel": "2024-01-20 Hospital discharge summary",
                            "fileLoinc": "34797-1",
                            "fileLoincName": "HIE - Hospital discharge summary",
                            "fileName": "Athena/7/7637/7637_20_08_2022_HOSPITAL_DISCHARGE_SUMMARY (HOSPITALDISCHARGE).html.pdf",
                            "hccWeight": 0.335,
                            "icd10CodeLine": 10,
                            "icd10CodeLineContent": "J44.9 Chronic Obstructive Pulmonary Disease (COPD)",
                            "icdCodes": "J44.9",
                            "index": 8,
                            "lineContentOccurrenceInDoc": 1,
                            "secondaryName": "Hospital",
                            "snomedCode": "13645005",
                            "snomedName": "Chronic obstructive lung disease"
                        }
                    ],
                    "inferred": [],
                    "plGap": [],
                    "rafGap": [
                        {
                            "data": {
                                "encounterType": "consult",
                                "modificationDate": "2023-09-14 00:00:00",
                                "providerName": "Chip Ach"
                            },
                            "icdCode": [
                                "J449"
                            ],
                            "icdData": [
                                {
                                    "code": "J449",
                                    "description": "Chronic obstructive pulmonary disease, unspecified",
                                    "hccGroup": "111",
                                    "hccWeight": 0.335
                                }
                            ],
                            "snomedCode": "13645005",
                            "type": "PreviousYears"
                        },
                        {
                            "data": {
                                "encounterType": "ops test",
                                "modificationDate": "2023-09-02 00:00:00",
                                "providerName": "Macc Test"
                            },
                            "icdCode": [
                                "J449"
                            ],
                            "icdData": [
                                {
                                    "code": "J449",
                                    "description": "Chronic obstructive pulmonary disease, unspecified",
                                    "hccGroup": "111",
                                    "hccWeight": 0.335
                                }
                            ],
                            "snomedCode": "13645005",
                            "type": "PreviousYears"
                        }
                    ]
                },
                "diagnosisSources": [
                    {
                        "sourceName": "Encounter (Chip Ach)",
                        "type": "raf_gap",
                        "date": "09/14/2023",
                        "data": [
                            {
                                "title": "Encounter",
                                "date": "09/14/2023",
                                "rows": [
                                    {
                                        "key": "Provider name",
                                        "value": "Chip Ach"
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "sourceName": "HIE - Hospital discharge summary",
                        "type": "consults",
                        "date": "01/20/2024",
                        "document": {
                            "name": "HIE - Hospital discharge summary",
                            "id": "b3c1b14d-fb9e-4374-a544-77098d13a6dd",
                            "date": "01/20/2024",
                            "searchTerm": "J44.9 Chronic Obstructive Pulmonary Disease (COPD)",
                            "searchTermOccurrence": 1
                        },
                        "data": [
                            {
                                "title": "Consult note",
                                "date": "01/20/2024",
                                "rows": [
                                    {
                                        "key": "Document name",
                                        "value": "HIE - Hospital discharge summary"
                                    },
                                    {
                                        "key": "Document date",
                                        "value": "01/20/2024"
                                    }
                                ]
                            }
                        ]
                    }
                ]
            },
            "numberOfSources": 2,
            "dataFromAction": False,
            "diagnosisAction": {
                "reason": "NO_REASON",
                "status": "Untouched",
                "detailedStatus": "ignored_provider",
                "note": {
                    "display": True
                },
                "performed": {
                    "byId": "961e602d-cda0-4797-918d-6decaeccee2a",
                    "byUserName": "Demo Navina",
                    "atIsoDatetime": "2024-10-07T14:18:45.729Z"
                }
            },
            "isHint": True,
            "captionInfo": "ignored_coder",
            "suggestionId": "J449",
            "lowerRelevancyReason": None,
            "hccGroup": 111,
            "hccWeight": 0.335,
            "sid": "dd119322-bcb1-42be-8064-1f4b99076de8",
            "nid": "fcba6f0f-c8cf-4efc-b597-32277cd5255e",
            "navinaProviderId": 12875,
            "view": "provider",
            "dataSourceId": 7,
            "portraitCreatedAt": "2024-03-05 10:52:44",
            "dateOfService": "2024-10-13T02:00:00.000Z"
        }
    ],
    [
        {
            "showInInsights": False,
            "showInCart": False,
            "icdCode": "N1830",
            "icdDescription": "Chronic kidney disease, stage 3 unspecified",
            "hccs": {
                "rx": [],
                "v24": [
                    {
                        "group": 138,
                        "weight": 0.069
                    }
                ],
                "v28": [
                    {
                        "group": 329,
                        "weight": 0.127
                    }
                ]
            },
            "snomedDescription": "Chronic kidney disease stage 3 (disorder)",
            "snomedCode": "433144002",
            "reasons": {
                "consults": [],
                "inferred": [],
                "plGap": [],
                "rafGap": [
                    {
                        "data": {
                            "encounterType": "ops test",
                            "modificationDate": "2023-09-02 00:00:00",
                            "providerName": "Macc Test"
                        },
                        "icdCode": [
                            "N1830"
                        ],
                        "icdData": [
                            {
                                "code": "N1830",
                                "description": "Chronic kidney disease, stage 3 unspecified",
                                "hccGroup": "138",
                                "hccWeight": 0.069
                            }
                        ],
                        "snomedCode": "433144002",
                        "type": "PreviousYears"
                    }
                ]
            },
            "diagnosisSources": [
                {
                    "sourceName": "Encounter (Macc Test)",
                    "type": "raf_gap",
                    "date": "09/02/2023",
                    "data": [
                        {
                            "title": "Encounter",
                            "date": "09/02/2023",
                            "rows": [
                                {
                                    "key": "Provider name",
                                    "value": "Macc Test"
                                }
                            ]
                        }
                    ]
                }
            ],
            "suggestionDateTime": "2023-09-02 00:00:00",
            "isPrimary": True,
            "billable": True,
            "billableDescendants": [],
            "isOptionalIcd": False,
            "isChosenOptionalIcd": False,
            "diagnosisOptionalIcds": [],
            "confidenceLabel": "",
            "isBillableSubDx": False,
            "dxId": "N1830",
            "dxDescription": "Chronic kidney disease, stage 3 unspecified",
            "addedInPostVisit": False,
            "statusUpdatedAt": None,
            "statusUpdatedBy": None,
            "statusUpdatedByName": None,
            "actionUsername": "",
            "addressedGroup": "NewHCCGroup",
            "companionAddressedGroup": None,
            "status": None,
            "type": "recommendation",
            "isValid": False,
            "lastCoderStatus": "ignored_coder",
            "lastCoderStatusUpdatedAt": "2024-07-25T09:10:29.246Z",
            "lastCoderStatusUpdatedBy": "0df79952-bceb-4701-992a-604489760156",
            "lastCoderStatusUpdatedByName": "Aviv Coder",
            "lastProviderStatus": "ignored_provider",
            "lastProviderStatusUpdatedAt": "2024-10-20T17:26:39.949Z",
            "lastProviderStatusUpdatedBy": "7ac6a86c-4800-4955-8a89-d4c86df01eea",
            "lastProviderStatusUpdatedByName": "Shiran Hazon",
            "coderStatus": None,
            "coderStatusUpdatedAt": None,
            "coderStatusUpdatedBy": None,
            "isCoderStatusFromCurrentSid": False,
            "providerStatus": None,
            "providerStatusUpdatedAt": None,
            "providerStatusUpdatedBy": None,
            "isProviderStatusFromCurrentSid": False,
            "statusUpdatedTimestamp": 0,
            "statusAddedTimestamp": 0,
            "companionOrder": 0,
            "companionDxs": [],
            "primaryDx": None,
            "isNavinaCoupledSuggestion": False,
            "isCoupledSuggestion": False,
            "companionId": None,
            "noteData": None,
            "isSyncedFromEmr": False,
            "actionsHistory": [
                {
                    "actionByInferredRule": "2108108452",
                    "actionName": "False_negate",
                    "actionTo": [
                        "N1830"
                    ]
                },
                {
                    "actionByInferredRule": "2123806305",
                    "actionName": "False_negate",
                    "actionTo": [
                        "N1830"
                    ]
                },
                {
                    "actionByInferredRule": "2123806537",
                    "actionName": "False_negate",
                    "actionTo": [
                        "N1830"
                    ]
                }
            ],
            "invalidOverride": False,
            "overrideFilter": None,
            "sourceData": {
                "type": "recommendation",
                "extra": {
                    "consults": [],
                    "inferred": [],
                    "plGap": [],
                    "rafGap": [
                        {
                            "data": {
                                "encounterType": "ops test",
                                "modificationDate": "2023-09-02 00:00:00",
                                "providerName": "Macc Test"
                            },
                            "icdCode": [
                                "N1830"
                            ],
                            "icdData": [
                                {
                                    "code": "N1830",
                                    "description": "Chronic kidney disease, stage 3 unspecified",
                                    "hccGroup": "138",
                                    "hccWeight": 0.069
                                }
                            ],
                            "snomedCode": "433144002",
                            "type": "PreviousYears"
                        }
                    ]
                },
                "diagnosisSources": [
                    {
                        "sourceName": "Encounter (Macc Test)",
                        "type": "raf_gap",
                        "date": "09/02/2023",
                        "data": [
                            {
                                "title": "Encounter",
                                "date": "09/02/2023",
                                "rows": [
                                    {
                                        "key": "Provider name",
                                        "value": "Macc Test"
                                    }
                                ]
                            }
                        ]
                    }
                ]
            },
            "numberOfSources": 1,
            "dataFromAction": False,
            "diagnosisAction": {
                "reason": "NO_REASON",
                "status": "Untouched",
                "detailedStatus": "ignored_provider",
                "note": {
                    "display": True
                },
                "performed": {
                    "byId": "7ac6a86c-4800-4955-8a89-d4c86df01eea",
                    "byUserName": "Shiran Hazon",
                    "atIsoDatetime": "2024-10-20T17:26:39.949Z"
                }
            },
            "isHint": False,
            "captionInfo": "ignored_coder",
            "suggestionId": "N1830",
            "lowerRelevancyReason": None,
            "hccGroup": 138,
            "hccWeight": 0.069,
            "sid": "dd119322-bcb1-42be-8064-1f4b99076de8",
            "nid": "fcba6f0f-c8cf-4efc-b597-32277cd5255e",
            "navinaProviderId": 12875,
            "view": "provider",
            "dataSourceId": 7,
            "portraitCreatedAt": "2024-03-05 10:52:44",
            "dateOfService": "2024-10-13T02:00:00.000Z"
        }
    ],
    [
        {
            "showInInsights": True,
            "showInCart": False,
            "icdCode": "L97519",
            "icdDescription": "Non-pressure chronic ulcer of other part of right foot with unspecified severity",
            "hccs": {
                "rx": [
                    {
                        "group": 311,
                        "weight": 0.137
                    }
                ],
                "v24": [
                    {
                        "group": 161,
                        "weight": 0.515
                    }
                ],
                "v28": [
                    {
                        "group": 383,
                        "weight": 0.646
                    }
                ]
            },
            "snomedDescription": "",
            "snomedCode": "830072004",
            "reasons": {
                "consults": [],
                "inferred": [],
                "plGap": [],
                "rafGap": [
                    {
                        "data": {
                            "encounterType": "consult",
                            "modificationDate": "2023-09-14 00:00:00",
                            "providerName": "Chip Ach"
                        },
                        "icdCode": [
                            "L97519"
                        ],
                        "icdData": [
                            {
                                "code": "L97519",
                                "description": "Non-pressure chronic ulcer of other part of right foot with unspecified severity",
                                "hccGroup": "161",
                                "hccWeight": 0.515
                            }
                        ],
                        "snomedCode": "830072004",
                        "type": "PreviousYears"
                    }
                ]
            },
            "diagnosisSources": [
                {
                    "sourceName": "Encounter (Chip Ach)",
                    "type": "raf_gap",
                    "date": "09/14/2023",
                    "data": [
                        {
                            "title": "Encounter",
                            "date": "09/14/2023",
                            "rows": [
                                {
                                    "key": "Provider name",
                                    "value": "Chip Ach"
                                }
                            ]
                        }
                    ]
                }
            ],
            "suggestionDateTime": "2023-09-14 00:00:00",
            "isPrimary": True,
            "billable": True,
            "billableDescendants": [],
            "isOptionalIcd": False,
            "isChosenOptionalIcd": False,
            "diagnosisOptionalIcds": [],
            "confidenceLabel": "Recapture",
            "isBillableSubDx": False,
            "dxId": "L97519",
            "dxDescription": "Non-pressure chronic ulcer of other part of right foot with unspecified severity",
            "addedInPostVisit": False,
            "statusUpdatedAt": None,
            "statusUpdatedBy": None,
            "statusUpdatedByName": None,
            "actionUsername": "",
            "addressedGroup": "NewHCCGroup",
            "companionAddressedGroup": None,
            "status": None,
            "type": "recommendation",
            "isValid": True,
            "lastCoderStatus": None,
            "lastCoderStatusUpdatedAt": None,
            "lastCoderStatusUpdatedBy": None,
            "lastCoderStatusUpdatedByName": None,
            "lastProviderStatus": "pushed_provider",
            "lastProviderStatusUpdatedAt": "2024-09-08T10:18:14.349Z",
            "lastProviderStatusUpdatedBy": "961e602d-cda0-4797-918d-6decaeccee2a",
            "lastProviderStatusUpdatedByName": "Demo Navina",
            "coderStatus": None,
            "coderStatusUpdatedAt": None,
            "coderStatusUpdatedBy": None,
            "isCoderStatusFromCurrentSid": False,
            "providerStatus": None,
            "providerStatusUpdatedAt": None,
            "providerStatusUpdatedBy": None,
            "isProviderStatusFromCurrentSid": False,
            "statusUpdatedTimestamp": 0,
            "statusAddedTimestamp": 0,
            "companionOrder": 0,
            "companionDxs": None,
            "primaryDx": None,
            "isNavinaCoupledSuggestion": False,
            "isCoupledSuggestion": False,
            "companionId": None,
            "isSyncedFromEmr": False,
            "actionsHistory": [],
            "invalidOverride": False,
            "overrideFilter": None,
            "sourceData": {
                "type": "recommendation",
                "extra": {
                    "consults": [],
                    "inferred": [],
                    "plGap": [],
                    "rafGap": [
                        {
                            "data": {
                                "encounterType": "consult",
                                "modificationDate": "2023-09-14 00:00:00",
                                "providerName": "Chip Ach"
                            },
                            "icdCode": [
                                "L97519"
                            ],
                            "icdData": [
                                {
                                    "code": "L97519",
                                    "description": "Non-pressure chronic ulcer of other part of right foot with unspecified severity",
                                    "hccGroup": "161",
                                    "hccWeight": 0.515
                                }
                            ],
                            "snomedCode": "830072004",
                            "type": "PreviousYears"
                        }
                    ]
                },
                "diagnosisSources": [
                    {
                        "sourceName": "Encounter (Chip Ach)",
                        "type": "raf_gap",
                        "date": "09/14/2023",
                        "data": [
                            {
                                "title": "Encounter",
                                "date": "09/14/2023",
                                "rows": [
                                    {
                                        "key": "Provider name",
                                        "value": "Chip Ach"
                                    }
                                ]
                            }
                        ]
                    }
                ]
            },
            "numberOfSources": 1,
            "dataFromAction": False,
            "diagnosisAction": {
                "reason": "NO_REASON",
                "status": "Accepted",
                "detailedStatus": "pushed_provider",
                "note": {
                    "display": True
                },
                "performed": {
                    "byId": "961e602d-cda0-4797-918d-6decaeccee2a",
                    "byUserName": "Demo Navina",
                    "atIsoDatetime": "2024-09-08T10:18:14.349Z"
                }
            },
            "isHint": True,
            "captionInfo": "ignored_coder",
            "suggestionId": "L97519",
            "lowerRelevancyReason": None,
            "hccGroup": 161,
            "hccWeight": 0.515,
            "sid": "dd119322-bcb1-42be-8064-1f4b99076de8",
            "nid": "fcba6f0f-c8cf-4efc-b597-32277cd5255e",
            "navinaProviderId": 12875,
            "view": "provider",
            "dataSourceId": 7,
            "portraitCreatedAt": "2024-03-05 10:52:44",
            "dateOfService": "2024-10-13T02:00:00.000Z"
        }
    ],
    [
        {
            "showInInsights": True,
            "showInCart": False,
            "icdCode": "G35",
            "icdDescription": "Multiple sclerosis",
            "hccs": {
                "rx": [
                    {
                        "group": 159,
                        "weight": 1.486
                    }
                ],
                "v24": [
                    {
                        "group": 77,
                        "weight": 0.423
                    }
                ],
                "v28": [
                    {
                        "group": 198,
                        "weight": 0.647
                    }
                ]
            },
            "snomedDescription": "Multiple sclerosis",
            "snomedCode": "24700007",
            "reasons": {
                "consults": [
                    {
                        "id": "ab4cb4f9-cb47-4ef2-99c6-ea45441071a4",
                        "encounterDate": "06/04/2021",
                        "fileDate": "2023-06-04",
                        "fileId": "ab4cb4f9-cb47-4ef2-99c6-ea45441071a4",
                        "fileLabel": "06/04/2021_neurologist consult note_142581",
                        "fileLoinc": "34797-1",
                        "fileLoincName": "neurologist consult note",
                        "fileName": "Athena/7/7637/7637_06_04_2021_neurologist_consult_note_142581 (CLINICALDOCUMENT-CLINICALDOCUMENT_CONSULTNOTE).pdf",
                        "hccWeight": 0.423,
                        "icd10CodeLine": 68,
                        "icd10CodeLineContent": "G35",
                        "icdCodes": "G35",
                        "index": 8,
                        "lineContentOccurrenceInDoc": 1,
                        "secondaryName": "Neurology",
                        "snomedCode": "24700007",
                        "snomedName": "Multiple sclerosis"
                    }
                ],
                "inferred": [],
                "plGap": [],
                "rafGap": []
            },
            "diagnosisSources": [
                {
                    "sourceName": "neurologist consult note",
                    "type": "consults",
                    "date": "06/04/2023",
                    "document": {
                        "name": "neurologist consult note",
                        "id": "ab4cb4f9-cb47-4ef2-99c6-ea45441071a4",
                        "date": "06/04/2023",
                        "searchTerm": "G35",
                        "searchTermOccurrence": 1
                    },
                    "data": [
                        {
                            "title": "Consult note",
                            "date": "06/04/2023",
                            "rows": [
                                {
                                    "key": "Document name",
                                    "value": "neurologist consult note"
                                },
                                {
                                    "key": "Document date",
                                    "value": "06/04/2023"
                                }
                            ]
                        }
                    ]
                }
            ],
            "suggestionDateTime": "2023-06-04 00:00:00",
            "isPrimary": True,
            "billable": True,
            "billableDescendants": [],
            "isOptionalIcd": False,
            "isChosenOptionalIcd": False,
            "diagnosisOptionalIcds": [],
            "confidenceLabel": "Recapture",
            "isBillableSubDx": False,
            "dxId": "G35",
            "dxDescription": "Multiple sclerosis",
            "addedInPostVisit": False,
            "statusUpdatedAt": None,
            "statusUpdatedBy": None,
            "statusUpdatedByName": None,
            "actionUsername": "",
            "addressedGroup": "NewHCCGroup",
            "companionAddressedGroup": None,
            "status": None,
            "type": "recommendation",
            "isValid": True,
            "lastCoderStatus": "ignored_coder",
            "lastCoderStatusUpdatedAt": "2024-08-20T22:34:06.912Z",
            "lastCoderStatusUpdatedBy": "0df79952-bceb-4701-992a-604489760156",
            "lastCoderStatusUpdatedByName": "Aviv Coder",
            "lastProviderStatus": "ignored_provider",
            "lastProviderStatusUpdatedAt": "2024-09-19T10:04:11.222Z",
            "lastProviderStatusUpdatedBy": "e14c61af-8c1b-4ca8-a0d8-446184cfa820",
            "lastProviderStatusUpdatedByName": "Bat-El Ziony",
            "coderStatus": None,
            "coderStatusUpdatedAt": None,
            "coderStatusUpdatedBy": None,
            "isCoderStatusFromCurrentSid": False,
            "providerStatus": None,
            "providerStatusUpdatedAt": None,
            "providerStatusUpdatedBy": None,
            "isProviderStatusFromCurrentSid": False,
            "statusUpdatedTimestamp": 0,
            "statusAddedTimestamp": 0,
            "companionOrder": 0,
            "companionDxs": None,
            "primaryDx": None,
            "isNavinaCoupledSuggestion": False,
            "isCoupledSuggestion": False,
            "companionId": None,
            "noteData": {
                "text": "",
                "authorName": "dave.madlom@navina.ai",
                "authorType": None,
                "noteDate": "2024-04-25T14:38:58.511Z",
                "shouldPush": False,
                "addedInPostVisit": False
            },
            "isSyncedFromEmr": False,
            "actionsHistory": [],
            "invalidOverride": False,
            "overrideFilter": None,
            "sourceData": {
                "type": "recommendation",
                "extra": {
                    "consults": [
                        {
                            "id": "ab4cb4f9-cb47-4ef2-99c6-ea45441071a4",
                            "encounterDate": "06/04/2021",
                            "fileDate": "2023-06-04",
                            "fileId": "ab4cb4f9-cb47-4ef2-99c6-ea45441071a4",
                            "fileLabel": "06/04/2021_neurologist consult note_142581",
                            "fileLoinc": "34797-1",
                            "fileLoincName": "neurologist consult note",
                            "fileName": "Athena/7/7637/7637_06_04_2021_neurologist_consult_note_142581 (CLINICALDOCUMENT-CLINICALDOCUMENT_CONSULTNOTE).pdf",
                            "hccWeight": 0.423,
                            "icd10CodeLine": 68,
                            "icd10CodeLineContent": "G35",
                            "icdCodes": "G35",
                            "index": 8,
                            "lineContentOccurrenceInDoc": 1,
                            "secondaryName": "Neurology",
                            "snomedCode": "24700007",
                            "snomedName": "Multiple sclerosis"
                        }
                    ],
                    "inferred": [],
                    "plGap": [],
                    "rafGap": []
                },
                "diagnosisSources": [
                    {
                        "sourceName": "neurologist consult note",
                        "type": "consults",
                        "date": "06/04/2023",
                        "document": {
                            "name": "neurologist consult note",
                            "id": "ab4cb4f9-cb47-4ef2-99c6-ea45441071a4",
                            "date": "06/04/2023",
                            "searchTerm": "G35",
                            "searchTermOccurrence": 1
                        },
                        "data": [
                            {
                                "title": "Consult note",
                                "date": "06/04/2023",
                                "rows": [
                                    {
                                        "key": "Document name",
                                        "value": "neurologist consult note"
                                    },
                                    {
                                        "key": "Document date",
                                        "value": "06/04/2023"
                                    }
                                ]
                            }
                        ]
                    }
                ]
            },
            "numberOfSources": 1,
            "dataFromAction": False,
            "diagnosisAction": {
                "reason": "NO_REASON",
                "status": "Untouched",
                "detailedStatus": "ignored_provider",
                "note": {
                    "display": True
                },
                "performed": {
                    "byId": "e14c61af-8c1b-4ca8-a0d8-446184cfa820",
                    "byUserName": "Bat-El Ziony",
                    "atIsoDatetime": "2024-09-19T10:04:11.222Z"
                }
            },
            "isHint": True,
            "captionInfo": "ignored_coder",
            "suggestionId": "G35",
            "lowerRelevancyReason": None,
            "hccGroup": 77,
            "hccWeight": 0.423,
            "sid": "dd119322-bcb1-42be-8064-1f4b99076de8",
            "nid": "fcba6f0f-c8cf-4efc-b597-32277cd5255e",
            "navinaProviderId": 12875,
            "view": "provider",
            "dataSourceId": 7,
            "portraitCreatedAt": "2024-03-05 10:52:44",
            "dateOfService": "2024-10-13T02:00:00.000Z"
        }
    ],
    [
        {
            "showInInsights": True,
            "showInCart": False,
            "icdCode": "E6601",
            "icdDescription": "Morbid (severe) obesity due to excess calories",
            "hccs": {
                "rx": [],
                "v24": [
                    {
                        "group": 22,
                        "weight": 0.25
                    }
                ],
                "v28": [
                    {
                        "group": 48,
                        "weight": 0.186
                    }
                ]
            },
            "snomedDescription": "Morbid obesity",
            "snomedCode": "238136002",
            "reasons": {
                "consults": [],
                "inferred": [
                    {
                        "icdCode": "E6601",
                        "icdDescription": "Morbid (severe) obesity due to excess calories",
                        "operators": [
                            {
                                "data": [
                                    {
                                        "bmi": 42.3,
                                        "date": "2024-03-17",
                                        "measurementDate": "03/2022",
                                        "rawDate": "2024-03-17",
                                        "value": 42.3
                                    }
                                ],
                                "date": "2024-03-17",
                                "name": "BMI",
                                "result": True
                            },
                            {
                                "data": [
                                    {
                                        "bmi": 42.3,
                                        "date": "2024-03-17",
                                        "measurementDate": "03/2022",
                                        "rawDate": "2024-03-17",
                                        "value": 42.3
                                    }
                                ],
                                "date": "2024-03-17",
                                "name": "BMI",
                                "result": True
                            }
                        ],
                        "plInclusion": None,
                        "ruleId": "2108108627",
                        "ruleName": "Body mass index [BMI]40.0-44.9, adult (based ICD)",
                        "snomedCode": "238136002",
                        "snomedDescription": "Morbid obesity"
                    }
                ],
                "plGap": [],
                "rafGap": []
            },
            "diagnosisSources": [
                {
                    "sourceName": "BMI = 42.3",
                    "type": "inferred",
                    "data": [
                        {
                            "title": "Suspected finding",
                            "rows": [
                                {
                                    "key": "03/17/2024",
                                    "value": "BMI = 42.3",
                                    "subtype": "Others"
                                }
                            ]
                        }
                    ],
                    "date": "03/17/2024",
                    "extraData": [
                        {
                            "key": "subSourceName",
                            "value": "BMI = 42.3"
                        }
                    ]
                }
            ],
            "suggestionDateTime": "2024-03-17 00:00:00",
            "isPrimary": True,
            "billable": True,
            "billableDescendants": [],
            "isOptionalIcd": False,
            "isChosenOptionalIcd": False,
            "diagnosisOptionalIcds": [],
            "confidenceLabel": "Suspect",
            "isBillableSubDx": False,
            "dxId": "E6601",
            "dxDescription": "Morbid (severe) obesity due to excess calories",
            "addedInPostVisit": False,
            "statusUpdatedAt": None,
            "statusUpdatedBy": None,
            "statusUpdatedByName": None,
            "actionUsername": "",
            "addressedGroup": "NewHCCGroup",
            "companionAddressedGroup": "NewHCCGroup",
            "status": None,
            "type": "recommendation",
            "isValid": True,
            "lastCoderStatus": "ignored_coder",
            "lastCoderStatusUpdatedAt": "2024-09-04T21:54:37.367Z",
            "lastCoderStatusUpdatedBy": "315738d5-1274-43e6-b9e0-e39d5af749e5",
            "lastCoderStatusUpdatedByName": "waymon barnette",
            "lastProviderStatus": "ignored_provider",
            "lastProviderStatusUpdatedAt": "2024-10-10T15:58:43.131Z",
            "lastProviderStatusUpdatedBy": "961e602d-cda0-4797-918d-6decaeccee2a",
            "lastProviderStatusUpdatedByName": "Demo Navina",
            "coderStatus": None,
            "coderStatusUpdatedAt": None,
            "coderStatusUpdatedBy": None,
            "isCoderStatusFromCurrentSid": False,
            "providerStatus": None,
            "providerStatusUpdatedAt": None,
            "providerStatusUpdatedBy": None,
            "isProviderStatusFromCurrentSid": False,
            "statusUpdatedTimestamp": 0,
            "statusAddedTimestamp": 0,
            "companionOrder": 1,
            "companionDxs": [
                "Z6841"
            ],
            "primaryDx": None,
            "isNavinaCoupledSuggestion": True,
            "isCoupledSuggestion": True,
            "companionId": "RIiq-R-vfkx",
            "noteData": {
                "text": "test",
                "authorName": "Demo Navina",
                "authorType": "Admin",
                "noteDate": "2024-09-24T06:47:08.700Z",
                "shouldPush": False,
                "addedInPostVisit": False
            },
            "isSyncedFromEmr": False,
            "actionsHistory": [],
            "invalidOverride": False,
            "overrideFilter": None,
            "sourceData": {
                "type": "recommendation",
                "extra": {
                    "consults": [],
                    "inferred": [
                        {
                            "icdCode": "E6601",
                            "icdDescription": "Morbid (severe) obesity due to excess calories",
                            "operators": [
                                {
                                    "data": [
                                        {
                                            "bmi": 42.3,
                                            "date": "2024-03-17",
                                            "measurementDate": "03/2022",
                                            "rawDate": "2024-03-17",
                                            "value": 42.3
                                        }
                                    ],
                                    "date": "2024-03-17",
                                    "name": "BMI",
                                    "result": True
                                },
                                {
                                    "data": [
                                        {
                                            "bmi": 42.3,
                                            "date": "2024-03-17",
                                            "measurementDate": "03/2022",
                                            "rawDate": "2024-03-17",
                                            "value": 42.3
                                        }
                                    ],
                                    "date": "2024-03-17",
                                    "name": "BMI",
                                    "result": True
                                }
                            ],
                            "plInclusion": None,
                            "ruleId": "2108108627",
                            "ruleName": "Body mass index [BMI]40.0-44.9, adult (based ICD)",
                            "snomedCode": "238136002",
                            "snomedDescription": "Morbid obesity"
                        }
                    ],
                    "plGap": [],
                    "rafGap": []
                },
                "diagnosisSources": [
                    {
                        "sourceName": "BMI = 42.3",
                        "type": "inferred",
                        "data": [
                            {
                                "title": "Suspected finding",
                                "rows": [
                                    {
                                        "key": "03/17/2024",
                                        "value": "BMI = 42.3",
                                        "subtype": "Others"
                                    }
                                ]
                            }
                        ],
                        "date": "03/17/2024",
                        "extraData": [
                            {
                                "key": "subSourceName",
                                "value": "BMI = 42.3"
                            }
                        ]
                    }
                ]
            },
            "numberOfSources": 1,
            "dataFromAction": False,
            "diagnosisAction": {
                "reason": "NO_REASON",
                "status": "Untouched",
                "detailedStatus": "ignored_provider",
                "note": {
                    "display": True
                },
                "performed": {
                    "byId": "961e602d-cda0-4797-918d-6decaeccee2a",
                    "byUserName": "Demo Navina",
                    "atIsoDatetime": "2024-10-10T15:58:43.131Z"
                }
            },
            "isHint": True,
            "captionInfo": "ignored_coder",
            "suggestionId": "Z6841",
            "lowerRelevancyReason": None,
            "hccGroup": 22,
            "hccWeight": 0.25,
            "sid": "dd119322-bcb1-42be-8064-1f4b99076de8",
            "nid": "fcba6f0f-c8cf-4efc-b597-32277cd5255e",
            "navinaProviderId": 12875,
            "view": "provider",
            "dataSourceId": 7,
            "portraitCreatedAt": "2024-03-05 10:52:44",
            "dateOfService": "2024-10-13T02:00:00.000Z"
        },
        {
            "showInInsights": True,
            "showInCart": False,
            "icdCode": "Z6841",
            "icdDescription": "Body mass index [BMI] 40.0-44.9, adult",
            "hccs": {
                "rx": [],
                "v24": [
                    {
                        "group": 22,
                        "weight": 0.25
                    }
                ],
                "v28": [
                    {
                        "group": 48,
                        "weight": 0.186
                    }
                ]
            },
            "snomedDescription": "Body mass index 40+ - severely obese (finding)",
            "snomedCode": "408512008",
            "reasons": {
                "consults": [],
                "inferred": [
                    {
                        "icdCode": "Z6841",
                        "icdDescription": "Body mass index [BMI] 40.0-44.9, adult",
                        "operators": [
                            {
                                "data": [
                                    {
                                        "bmi": 42.3,
                                        "date": "2024-03-17",
                                        "measurementDate": "03/2022",
                                        "rawDate": "2024-03-17",
                                        "value": 42.3
                                    }
                                ],
                                "date": "2024-03-17",
                                "name": "BMI",
                                "result": True
                            },
                            {
                                "data": [
                                    {
                                        "bmi": 42.3,
                                        "date": "2024-03-17",
                                        "measurementDate": "03/2022",
                                        "rawDate": "2024-03-17",
                                        "value": 42.3
                                    }
                                ],
                                "date": "2024-03-17",
                                "name": "BMI",
                                "result": True
                            }
                        ],
                        "plInclusion": None,
                        "ruleId": "2108108627",
                        "ruleName": "Body mass index [BMI]40.0-44.9, adult (based ICD)",
                        "snomedDescription": "Body mass index 40+ - severely obese (finding)"
                    }
                ],
                "plGap": [],
                "rafGap": []
            },
            "diagnosisSources": [
                {
                    "sourceName": "BMI = 42.3",
                    "type": "inferred",
                    "data": [
                        {
                            "title": "Suspected finding",
                            "rows": [
                                {
                                    "key": "03/17/2024",
                                    "value": "BMI = 42.3",
                                    "subtype": "Others"
                                }
                            ]
                        }
                    ],
                    "date": "03/17/2024",
                    "extraData": [
                        {
                            "key": "subSourceName",
                            "value": "BMI = 42.3"
                        }
                    ]
                }
            ],
            "suggestionDateTime": "2024-03-17 00:00:00",
            "isPrimary": False,
            "billable": True,
            "billableDescendants": [],
            "isOptionalIcd": False,
            "isChosenOptionalIcd": False,
            "diagnosisOptionalIcds": [],
            "confidenceLabel": "Suspect",
            "isBillableSubDx": False,
            "dxId": "Z6841",
            "dxDescription": "Body mass index [BMI] 40.0-44.9, adult",
            "addedInPostVisit": False,
            "statusUpdatedAt": None,
            "statusUpdatedBy": None,
            "statusUpdatedByName": None,
            "actionUsername": "",
            "addressedGroup": "NewHCCGroup",
            "companionAddressedGroup": "NewHCCGroup",
            "status": None,
            "type": "recommendation",
            "isValid": True,
            "lastCoderStatus": "ignored_coder",
            "lastCoderStatusUpdatedAt": "2024-09-04T21:54:37.922Z",
            "lastCoderStatusUpdatedBy": "315738d5-1274-43e6-b9e0-e39d5af749e5",
            "lastCoderStatusUpdatedByName": "waymon barnette",
            "lastProviderStatus": "ignored_provider",
            "lastProviderStatusUpdatedAt": "2024-10-10T15:58:44.768Z",
            "lastProviderStatusUpdatedBy": "961e602d-cda0-4797-918d-6decaeccee2a",
            "lastProviderStatusUpdatedByName": "Demo Navina",
            "coderStatus": None,
            "coderStatusUpdatedAt": None,
            "coderStatusUpdatedBy": None,
            "isCoderStatusFromCurrentSid": False,
            "providerStatus": None,
            "providerStatusUpdatedAt": None,
            "providerStatusUpdatedBy": None,
            "isProviderStatusFromCurrentSid": False,
            "statusUpdatedTimestamp": 0,
            "statusAddedTimestamp": 0,
            "companionOrder": 2,
            "companionDxs": [],
            "primaryDx": "E6601",
            "isNavinaCoupledSuggestion": True,
            "isCoupledSuggestion": True,
            "companionId": "RIiq-R-vfkx",
            "noteData": {
                "text": "",
                "authorName": "ronen.gordon.provider@navina.ai",
                "authorType": "Provider",
                "noteDate": "2024-06-25T08:10:27.617Z",
                "shouldPush": False,
                "addedInPostVisit": False
            },
            "isSyncedFromEmr": False,
            "actionsHistory": [],
            "invalidOverride": False,
            "overrideFilter": None,
            "sourceData": {
                "type": "recommendation",
                "extra": {
                    "consults": [],
                    "inferred": [
                        {
                            "icdCode": "Z6841",
                            "icdDescription": "Body mass index [BMI] 40.0-44.9, adult",
                            "operators": [
                                {
                                    "data": [
                                        {
                                            "bmi": 42.3,
                                            "date": "2024-03-17",
                                            "measurementDate": "03/2022",
                                            "rawDate": "2024-03-17",
                                            "value": 42.3
                                        }
                                    ],
                                    "date": "2024-03-17",
                                    "name": "BMI",
                                    "result": True
                                },
                                {
                                    "data": [
                                        {
                                            "bmi": 42.3,
                                            "date": "2024-03-17",
                                            "measurementDate": "03/2022",
                                            "rawDate": "2024-03-17",
                                            "value": 42.3
                                        }
                                    ],
                                    "date": "2024-03-17",
                                    "name": "BMI",
                                    "result": True
                                }
                            ],
                            "plInclusion": None,
                            "ruleId": "2108108627",
                            "ruleName": "Body mass index [BMI]40.0-44.9, adult (based ICD)",
                            "snomedDescription": "Body mass index 40+ - severely obese (finding)"
                        }
                    ],
                    "plGap": [],
                    "rafGap": []
                },
                "diagnosisSources": [
                    {
                        "sourceName": "BMI = 42.3",
                        "type": "inferred",
                        "data": [
                            {
                                "title": "Suspected finding",
                                "rows": [
                                    {
                                        "key": "03/17/2024",
                                        "value": "BMI = 42.3",
                                        "subtype": "Others"
                                    }
                                ]
                            }
                        ],
                        "date": "03/17/2024",
                        "extraData": [
                            {
                                "key": "subSourceName",
                                "value": "BMI = 42.3"
                            }
                        ]
                    }
                ]
            },
            "numberOfSources": 1,
            "dataFromAction": False,
            "diagnosisAction": {
                "reason": "NO_REASON",
                "status": "Untouched",
                "detailedStatus": "ignored_provider",
                "note": {
                    "display": True
                },
                "performed": {
                    "byId": "961e602d-cda0-4797-918d-6decaeccee2a",
                    "byUserName": "Demo Navina",
                    "atIsoDatetime": "2024-10-10T15:58:44.768Z"
                }
            },
            "isHint": True,
            "captionInfo": "ignored_coder",
            "suggestionId": "E6601",
            "lowerRelevancyReason": None,
            "hccGroup": 22,
            "hccWeight": 0.25,
            "sid": "dd119322-bcb1-42be-8064-1f4b99076de8",
            "nid": "fcba6f0f-c8cf-4efc-b597-32277cd5255e",
            "navinaProviderId": 12875,
            "view": "provider",
            "dataSourceId": 7,
            "portraitCreatedAt": "2024-03-05 10:52:44",
            "dateOfService": "2024-10-13T02:00:00.000Z"
        }
    ],
    [
        {
            "showInInsights": True,
            "showInCart": False,
            "icdCode": "E1122",
            "icdDescription": "Type 2 diabetes mellitus with diabetic chronic kidney disease",
            "hccs": {
                "rx": [
                    {
                        "group": 30,
                        "weight": 0.586
                    }
                ],
                "v24": [
                    {
                        "group": 18,
                        "weight": 0.302
                    }
                ],
                "v28": [
                    {
                        "group": 37,
                        "weight": 0.166
                    }
                ]
            },
            "snomedDescription": "Disorder of kidney due to diabetes mellitus (disorder)",
            "snomedCode": "771000119108",
            "reasons": {
                "consults": [
                    {
                        "id": "65b4715a-f648-4d5f-a758-bac5a9a62836",
                        "encounterDate": "05/14/2021",
                        "fileDate": "2023-05-12",
                        "fileId": "65b4715a-f648-4d5f-a758-bac5a9a62836",
                        "fileLabel": "05/14/2021_nephrologist consult note_142578",
                        "fileLoinc": "34795-5",
                        "fileLoincName": "nephrologist consult note",
                        "fileName": "Athena/7/7637/7637_05_14_2021_nephrologist_consult_note_142578 (CLINICALDOCUMENT-CLINICALDOCUMENT_CONSULTNOTE).pdf",
                        "hccWeight": 0.302,
                        "icd10CodeLine": 13,
                        "icd10CodeLineContent": "4. Type Il DM w/diabetic CKD - E11.22",
                        "icdCodes": "E1122",
                        "index": 26,
                        "lineContentOccurrenceInDoc": 1,
                        "secondaryName": "Nephrology",
                        "snomedCode": "771000119108",
                        "snomedName": "Type 2 diabetes mellitus with diabetic chronic kidney disease"
                    }
                ],
                "inferred": [
                    {
                        "icdCode": "E1122",
                        "icdDescription": "Type 2 diabetes mellitus with diabetic chronic kidney disease",
                        "operators": [
                            {
                                "data": [
                                    {
                                        "date": "2024-2-15",
                                        "operator": "<",
                                        "value": 52
                                    }
                                ],
                                "date": "2024-2-15",
                                "name": "eGFR",
                                "result": True
                            },
                            {
                                "data": [
                                    {
                                        "date": "2024-05-28",
                                        "operator": ">=",
                                        "value": 56
                                    }
                                ],
                                "date": "2024-05-28",
                                "name": "eGFR",
                                "result": True
                            }
                        ],
                        "plInclusion": None,
                        "ruleId": "2162214139",
                        "ruleName": "Type II DM with CKD 3a",
                        "snomedCode": "771000119108",
                        "snomedDescription": "Disorder of kidney due to diabetes mellitus (disorder)"
                    }
                ],
                "plGap": [],
                "rafGap": []
            },
            "diagnosisSources": [
                {
                    "sourceName": "eGFR = 56",
                    "type": "inferred",
                    "data": [
                        {
                            "title": "Suspected finding",
                            "rows": [
                                {
                                    "key": "05/28/2024",
                                    "value": "eGFR = 56",
                                    "subtype": "Others"
                                },
                                {
                                    "key": "02/15/2024",
                                    "value": "eGFR = 52",
                                    "subtype": "Others"
                                }
                            ]
                        }
                    ],
                    "date": "05/28/2024",
                    "extraData": [
                        {
                            "key": "subSourceName",
                            "value": "eGFR = 56"
                        }
                    ]
                },
                {
                    "sourceName": "nephrologist consult note",
                    "type": "consults",
                    "date": "05/12/2023",
                    "document": {
                        "name": "nephrologist consult note",
                        "id": "65b4715a-f648-4d5f-a758-bac5a9a62836",
                        "date": "05/12/2023",
                        "searchTerm": "4. Type Il DM w/diabetic CKD - E11.22",
                        "searchTermOccurrence": 1
                    },
                    "data": [
                        {
                            "title": "Consult note",
                            "date": "05/12/2023",
                            "rows": [
                                {
                                    "key": "Document name",
                                    "value": "nephrologist consult note"
                                },
                                {
                                    "key": "Document date",
                                    "value": "05/12/2023"
                                }
                            ]
                        }
                    ]
                }
            ],
            "suggestionDateTime": "2024-03-16 00:00:00",
            "isPrimary": True,
            "billable": True,
            "billableDescendants": [],
            "isOptionalIcd": False,
            "isChosenOptionalIcd": False,
            "diagnosisOptionalIcds": [],
            "confidenceLabel": "Suspect",
            "isBillableSubDx": False,
            "dxId": "E1122",
            "dxDescription": "Type 2 diabetes mellitus with diabetic chronic kidney disease",
            "addedInPostVisit": False,
            "statusUpdatedAt": "2024-08-28T17:26:35.997Z",
            "statusUpdatedBy": "0355859c-63db-4b02-b3b9-1d7a0200efb0",
            "statusUpdatedByName": "Jordan crumpler",
            "actionUsername": "Jordan crumpler",
            "addressedGroup": "NewHCCGroup",
            "companionAddressedGroup": "NewHCCGroup",
            "status": "accepted_coder",
            "type": "recommendation",
            "isValid": True,
            "lastCoderStatus": "accepted_coder",
            "lastCoderStatusUpdatedAt": "2024-08-28T17:26:35.997Z",
            "lastCoderStatusUpdatedBy": "0355859c-63db-4b02-b3b9-1d7a0200efb0",
            "lastCoderStatusUpdatedByName": "Jordan crumpler",
            "lastProviderStatus": "ignored_provider",
            "lastProviderStatusUpdatedAt": "2024-10-10T15:58:39.949Z",
            "lastProviderStatusUpdatedBy": "961e602d-cda0-4797-918d-6decaeccee2a",
            "lastProviderStatusUpdatedByName": "Demo Navina",
            "coderStatus": "accepted_coder",
            "coderStatusUpdatedAt": "2024-08-28T17:26:35.997Z",
            "coderStatusUpdatedBy": "0355859c-63db-4b02-b3b9-1d7a0200efb0",
            "isCoderStatusFromCurrentSid": False,
            "providerStatus": None,
            "providerStatusUpdatedAt": None,
            "providerStatusUpdatedBy": None,
            "isProviderStatusFromCurrentSid": False,
            "statusUpdatedTimestamp": 1724865988,
            "statusAddedTimestamp": 1724865988,
            "companionOrder": 1,
            "companionDxs": [
                "N1831"
            ],
            "primaryDx": None,
            "isNavinaCoupledSuggestion": True,
            "isCoupledSuggestion": True,
            "companionId": "XjX9elO3EIw",
            "noteData": {
                "text": "",
                "authorName": "Demo Navina",
                "authorType": "Admin",
                "noteDate": "2024-10-07T10:26:07.172Z",
                "shouldPush": False,
                "addedInPostVisit": False
            },
            "isSyncedFromEmr": False,
            "actionsHistory": [
                {
                    "actionBy": [
                        "E1122",
                        "N1831"
                    ],
                    "actionName": "didnt_invalidated_conflicting_dx_because_recent_date",
                    "actionTo": [
                        "E119"
                    ]
                }
            ],
            "invalidOverride": False,
            "overrideFilter": None,
            "sourceData": {
                "type": "recommendation",
                "extra": {
                    "consults": [
                        {
                            "id": "65b4715a-f648-4d5f-a758-bac5a9a62836",
                            "encounterDate": "05/14/2021",
                            "fileDate": "2023-05-12",
                            "fileId": "65b4715a-f648-4d5f-a758-bac5a9a62836",
                            "fileLabel": "05/14/2021_nephrologist consult note_142578",
                            "fileLoinc": "34795-5",
                            "fileLoincName": "nephrologist consult note",
                            "fileName": "Athena/7/7637/7637_05_14_2021_nephrologist_consult_note_142578 (CLINICALDOCUMENT-CLINICALDOCUMENT_CONSULTNOTE).pdf",
                            "hccWeight": 0.302,
                            "icd10CodeLine": 13,
                            "icd10CodeLineContent": "4. Type Il DM w/diabetic CKD - E11.22",
                            "icdCodes": "E1122",
                            "index": 26,
                            "lineContentOccurrenceInDoc": 1,
                            "secondaryName": "Nephrology",
                            "snomedCode": "771000119108",
                            "snomedName": "Type 2 diabetes mellitus with diabetic chronic kidney disease"
                        }
                    ],
                    "inferred": [
                        {
                            "icdCode": "E1122",
                            "icdDescription": "Type 2 diabetes mellitus with diabetic chronic kidney disease",
                            "operators": [
                                {
                                    "data": [
                                        {
                                            "date": "2024-2-15",
                                            "operator": "<",
                                            "value": 52
                                        }
                                    ],
                                    "date": "2024-2-15",
                                    "name": "eGFR",
                                    "result": True
                                },
                                {
                                    "data": [
                                        {
                                            "date": "2024-05-28",
                                            "operator": ">=",
                                            "value": 56
                                        }
                                    ],
                                    "date": "2024-05-28",
                                    "name": "eGFR",
                                    "result": True
                                }
                            ],
                            "plInclusion": None,
                            "ruleId": "2162214139",
                            "ruleName": "Type II DM with CKD 3a",
                            "snomedCode": "771000119108",
                            "snomedDescription": "Disorder of kidney due to diabetes mellitus (disorder)"
                        }
                    ],
                    "plGap": [],
                    "rafGap": []
                },
                "diagnosisSources": [
                    {
                        "sourceName": "eGFR = 56",
                        "type": "inferred",
                        "data": [
                            {
                                "title": "Suspected finding",
                                "rows": [
                                    {
                                        "key": "05/28/2024",
                                        "value": "eGFR = 56",
                                        "subtype": "Others"
                                    },
                                    {
                                        "key": "02/15/2024",
                                        "value": "eGFR = 52",
                                        "subtype": "Others"
                                    }
                                ]
                            }
                        ],
                        "date": "05/28/2024",
                        "extraData": [
                            {
                                "key": "subSourceName",
                                "value": "eGFR = 56"
                            }
                        ]
                    },
                    {
                        "sourceName": "nephrologist consult note",
                        "type": "consults",
                        "date": "05/12/2023",
                        "document": {
                            "name": "nephrologist consult note",
                            "id": "65b4715a-f648-4d5f-a758-bac5a9a62836",
                            "date": "05/12/2023",
                            "searchTerm": "4. Type Il DM w/diabetic CKD - E11.22",
                            "searchTermOccurrence": 1
                        },
                        "data": [
                            {
                                "title": "Consult note",
                                "date": "05/12/2023",
                                "rows": [
                                    {
                                        "key": "Document name",
                                        "value": "nephrologist consult note"
                                    },
                                    {
                                        "key": "Document date",
                                        "value": "05/12/2023"
                                    }
                                ]
                            }
                        ]
                    }
                ]
            },
            "numberOfSources": 2,
            "dataFromAction": False,
            "diagnosisAction": {
                "reason": "NO_REASON",
                "status": "Untouched",
                "detailedStatus": "ignored_provider",
                "note": {
                    "display": True
                },
                "performed": {
                    "byId": "961e602d-cda0-4797-918d-6decaeccee2a",
                    "byUserName": "Demo Navina",
                    "atIsoDatetime": "2024-10-10T15:58:39.949Z"
                }
            },
            "isHint": True,
            "isFromRescheduledAppointment": False,
            "suggestionId": "N1831",
            "lowerRelevancyReason": None,
            "hccGroup": 18,
            "hccWeight": 0.302,
            "sid": "dd119322-bcb1-42be-8064-1f4b99076de8",
            "nid": "fcba6f0f-c8cf-4efc-b597-32277cd5255e",
            "navinaProviderId": 12875,
            "view": "provider",
            "dataSourceId": 7,
            "portraitCreatedAt": "2024-03-05 10:52:44",
            "dateOfService": "2024-10-13T02:00:00.000Z"
        },
        {
            "showInInsights": True,
            "showInCart": False,
            "icdCode": "N1831",
            "icdDescription": "Chronic kidney disease, stage 3a",
            "hccs": {
                "rx": [],
                "v24": [
                    {
                        "group": 138,
                        "weight": 0.069
                    }
                ],
                "v28": [
                    {
                        "group": 329,
                        "weight": 0.127
                    }
                ]
            },
            "snomedDescription": "Chronic kidney disease stage 3A",
            "snomedCode": "700378005",
            "reasons": {
                "consults": [],
                "inferred": [
                    {
                        "icdCode": "N1831",
                        "icdDescription": "Chronic kidney disease, stage 3a",
                        "operators": [
                            {
                                "data": [
                                    {
                                        "date": "2024-2-15",
                                        "operator": "<",
                                        "value": 52
                                    }
                                ],
                                "date": "2024-2-15",
                                "name": "eGFR",
                                "result": True
                            },
                            {
                                "data": [
                                    {
                                        "date": "2024-05-28",
                                        "operator": ">=",
                                        "value": 56
                                    }
                                ],
                                "date": "2024-05-28",
                                "name": "eGFR",
                                "result": True
                            }
                        ],
                        "plInclusion": None,
                        "ruleId": "2162214139",
                        "ruleName": "Type II DM with CKD 3a",
                        "snomedDescription": "Chronic kidney disease stage 3A"
                    }
                ],
                "plGap": [],
                "rafGap": [
                    {
                        "data": {
                            "encounterType": "consult",
                            "modificationDate": "2023-11-04 00:00:00",
                            "providerName": "Database Test"
                        },
                        "icdCode": [
                            "N1831"
                        ],
                        "icdData": [
                            {
                                "code": "N1831",
                                "description": "Chronic kidney disease, stage 3a",
                                "hccGroup": "138",
                                "hccWeight": 0.069
                            }
                        ],
                        "snomedCode": "700378005",
                        "type": "PreviousYears"
                    },
                    {
                        "data": {
                            "encounterType": "consult",
                            "modificationDate": "2023-11-04 00:00:00",
                            "providerName": "Chip Ach"
                        },
                        "icdCode": [
                            "N1831"
                        ],
                        "icdData": [
                            {
                                "code": "N1831",
                                "description": "Chronic kidney disease, stage 3a",
                                "hccGroup": "138",
                                "hccWeight": 0.069
                            }
                        ],
                        "snomedCode": "700378005",
                        "type": "PreviousYears"
                    }
                ]
            },
            "diagnosisSources": [
                {
                    "sourceName": "Encounter (Database Test)",
                    "type": "raf_gap",
                    "date": "11/04/2023",
                    "data": [
                        {
                            "title": "Encounter",
                            "date": "11/04/2023",
                            "rows": [
                                {
                                    "key": "Provider name",
                                    "value": "Database Test"
                                }
                            ]
                        }
                    ]
                },
                {
                    "sourceName": "eGFR = 56",
                    "type": "inferred",
                    "data": [
                        {
                            "title": "Suspected finding",
                            "rows": [
                                {
                                    "key": "05/28/2024",
                                    "value": "eGFR = 56",
                                    "subtype": "Others"
                                },
                                {
                                    "key": "02/15/2024",
                                    "value": "eGFR = 52",
                                    "subtype": "Others"
                                }
                            ]
                        }
                    ],
                    "date": "05/28/2024",
                    "extraData": [
                        {
                            "key": "subSourceName",
                            "value": "eGFR = 56"
                        }
                    ]
                }
            ],
            "suggestionDateTime": "2024-03-16 00:00:00",
            "isPrimary": False,
            "billable": True,
            "billableDescendants": [],
            "isOptionalIcd": False,
            "isChosenOptionalIcd": False,
            "diagnosisOptionalIcds": [],
            "confidenceLabel": "Suspect",
            "isBillableSubDx": False,
            "dxId": "N1831",
            "dxDescription": "Chronic kidney disease, stage 3a",
            "addedInPostVisit": False,
            "statusUpdatedAt": "2024-08-28T17:26:35.997Z",
            "statusUpdatedBy": "0355859c-63db-4b02-b3b9-1d7a0200efb0",
            "statusUpdatedByName": "Jordan crumpler",
            "actionUsername": "Jordan crumpler",
            "addressedGroup": "NewHCCGroup",
            "companionAddressedGroup": "NewHCCGroup",
            "status": "accepted_coder",
            "type": "recommendation",
            "isValid": True,
            "lastCoderStatus": "accepted_coder",
            "lastCoderStatusUpdatedAt": "2024-08-28T17:26:35.997Z",
            "lastCoderStatusUpdatedBy": "0355859c-63db-4b02-b3b9-1d7a0200efb0",
            "lastCoderStatusUpdatedByName": "Jordan crumpler",
            "lastProviderStatus": "ignored_provider",
            "lastProviderStatusUpdatedAt": "2024-10-10T15:58:40.312Z",
            "lastProviderStatusUpdatedBy": "961e602d-cda0-4797-918d-6decaeccee2a",
            "lastProviderStatusUpdatedByName": "Demo Navina",
            "coderStatus": "accepted_coder",
            "coderStatusUpdatedAt": "2024-08-28T17:26:35.997Z",
            "coderStatusUpdatedBy": "0355859c-63db-4b02-b3b9-1d7a0200efb0",
            "isCoderStatusFromCurrentSid": False,
            "providerStatus": None,
            "providerStatusUpdatedAt": None,
            "providerStatusUpdatedBy": None,
            "isProviderStatusFromCurrentSid": False,
            "statusUpdatedTimestamp": 1724865988,
            "statusAddedTimestamp": 1724865988,
            "companionOrder": 2,
            "companionDxs": [],
            "primaryDx": "E1122",
            "isNavinaCoupledSuggestion": True,
            "isCoupledSuggestion": True,
            "companionId": "XjX9elO3EIw",
            "noteData": {
                "text": "",
                "authorName": "dave.madlom@navina.ai",
                "authorType": None,
                "noteDate": "2024-05-15T17:37:45.815Z",
                "shouldPush": False,
                "addedInPostVisit": False
            },
            "isSyncedFromEmr": False,
            "actionsHistory": [
                {
                    "actionBy": [
                        "E1122",
                        "N1831"
                    ],
                    "actionName": "didnt_invalidated_conflicting_dx_because_recent_date",
                    "actionTo": [
                        "E119"
                    ]
                }
            ],
            "invalidOverride": False,
            "overrideFilter": None,
            "sourceData": {
                "type": "recommendation",
                "extra": {
                    "consults": [],
                    "inferred": [
                        {
                            "icdCode": "N1831",
                            "icdDescription": "Chronic kidney disease, stage 3a",
                            "operators": [
                                {
                                    "data": [
                                        {
                                            "date": "2024-2-15",
                                            "operator": "<",
                                            "value": 52
                                        }
                                    ],
                                    "date": "2024-2-15",
                                    "name": "eGFR",
                                    "result": True
                                },
                                {
                                    "data": [
                                        {
                                            "date": "2024-05-28",
                                            "operator": ">=",
                                            "value": 56
                                        }
                                    ],
                                    "date": "2024-05-28",
                                    "name": "eGFR",
                                    "result": True
                                }
                            ],
                            "plInclusion": None,
                            "ruleId": "2162214139",
                            "ruleName": "Type II DM with CKD 3a",
                            "snomedDescription": "Chronic kidney disease stage 3A"
                        }
                    ],
                    "plGap": [],
                    "rafGap": [
                        {
                            "data": {
                                "encounterType": "consult",
                                "modificationDate": "2023-11-04 00:00:00",
                                "providerName": "Database Test"
                            },
                            "icdCode": [
                                "N1831"
                            ],
                            "icdData": [
                                {
                                    "code": "N1831",
                                    "description": "Chronic kidney disease, stage 3a",
                                    "hccGroup": "138",
                                    "hccWeight": 0.069
                                }
                            ],
                            "snomedCode": "700378005",
                            "type": "PreviousYears"
                        },
                        {
                            "data": {
                                "encounterType": "consult",
                                "modificationDate": "2023-11-04 00:00:00",
                                "providerName": "Chip Ach"
                            },
                            "icdCode": [
                                "N1831"
                            ],
                            "icdData": [
                                {
                                    "code": "N1831",
                                    "description": "Chronic kidney disease, stage 3a",
                                    "hccGroup": "138",
                                    "hccWeight": 0.069
                                }
                            ],
                            "snomedCode": "700378005",
                            "type": "PreviousYears"
                        }
                    ]
                },
                "diagnosisSources": [
                    {
                        "sourceName": "Encounter (Database Test)",
                        "type": "raf_gap",
                        "date": "11/04/2023",
                        "data": [
                            {
                                "title": "Encounter",
                                "date": "11/04/2023",
                                "rows": [
                                    {
                                        "key": "Provider name",
                                        "value": "Database Test"
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "sourceName": "eGFR = 56",
                        "type": "inferred",
                        "data": [
                            {
                                "title": "Suspected finding",
                                "rows": [
                                    {
                                        "key": "05/28/2024",
                                        "value": "eGFR = 56",
                                        "subtype": "Others"
                                    },
                                    {
                                        "key": "02/15/2024",
                                        "value": "eGFR = 52",
                                        "subtype": "Others"
                                    }
                                ]
                            }
                        ],
                        "date": "05/28/2024",
                        "extraData": [
                            {
                                "key": "subSourceName",
                                "value": "eGFR = 56"
                            }
                        ]
                    }
                ]
            },
            "numberOfSources": 2,
            "dataFromAction": False,
            "diagnosisAction": {
                "reason": "NO_REASON",
                "status": "Untouched",
                "detailedStatus": "ignored_provider",
                "note": {
                    "display": True
                },
                "performed": {
                    "byId": "961e602d-cda0-4797-918d-6decaeccee2a",
                    "byUserName": "Demo Navina",
                    "atIsoDatetime": "2024-10-10T15:58:40.312Z"
                }
            },
            "isHint": True,
            "isFromRescheduledAppointment": False,
            "suggestionId": "E1122",
            "lowerRelevancyReason": None,
            "hccGroup": 138,
            "hccWeight": 0.069,
            "sid": "dd119322-bcb1-42be-8064-1f4b99076de8",
            "nid": "fcba6f0f-c8cf-4efc-b597-32277cd5255e",
            "navinaProviderId": 12875,
            "view": "provider",
            "dataSourceId": 7,
            "portraitCreatedAt": "2024-03-05 10:52:44",
            "dateOfService": "2024-10-13T02:00:00.000Z"
        }
    ],
    [
        {
            "showInInsights": False,
            "showInCart": False,
            "icdCode": "E1022",
            "icdDescription": "Type 1 diabetes mellitus with diabetic chronic kidney disease",
            "hccs": {
                "rx": [
                    {
                        "group": 30,
                        "weight": 0.586
                    }
                ],
                "v24": [
                    {
                        "group": 18,
                        "weight": 0.302
                    }
                ],
                "v28": [
                    {
                        "group": 37,
                        "weight": 0.166
                    }
                ]
            },
            "snomedDescription": "Renal disorder due to type 1 diabetes mellitus",
            "snomedCode": "421893009",
            "reasons": {
                "agilon": [],
                "claimCms": [],
                "consults": [],
                "inferred": [
                    {
                        "icdCode": "E1022",
                        "icdDescription": "Type 1 diabetes mellitus with diabetic chronic kidney disease",
                        "operators": [
                            {
                                "data": [
                                    {
                                        "date": "2024-05-28",
                                        "operator": "<",
                                        "value": 56
                                    }
                                ],
                                "date": "2024-05-28",
                                "name": "eGFR",
                                "result": True
                            },
                            {
                                "data": [
                                    {
                                        "date": "2024-05-28",
                                        "operator": ">=",
                                        "value": 56
                                    }
                                ],
                                "date": "2024-05-28",
                                "name": "eGFR",
                                "result": True
                            },
                            {
                                "data": [
                                    {
                                        "date": "2024-05-28",
                                        "operator": "<",
                                        "value": 56
                                    },
                                    {
                                        "date": "2024-02-15",
                                        "operator": "<",
                                        "value": 52
                                    }
                                ],
                                "date": "2024-05-28",
                                "name": "eGFR",
                                "result": True
                            }
                        ],
                        "plInclusion": None,
                        "ruleId": "2206091971",
                        "ruleName": "Type I DM with CKD 3a",
                        "snomedCode": "421893009",
                        "snomedDescription": "Renal disorder due to type 1 diabetes mellitus"
                    }
                ],
                "plGap": [],
                "rafGap": []
            },
            "diagnosisSources": [
                {
                    "sourceName": "eGFR = 56",
                    "type": "inferred",
                    "data": [
                        {
                            "title": "Suspected finding",
                            "rows": [
                                {
                                    "key": "05/28/2024",
                                    "value": "eGFR = 56",
                                    "subtype": "Others"
                                },
                                {
                                    "key": "02/15/2024",
                                    "value": "eGFR = 52",
                                    "subtype": "Others"
                                }
                            ]
                        }
                    ],
                    "date": "05/28/2024",
                    "extraData": [
                        {
                            "key": "subSourceName",
                            "value": "eGFR = 56"
                        }
                    ]
                }
            ],
            "suggestionDateTime": "2024-05-28 00:00:00",
            "isPrimary": True,
            "billable": True,
            "billableDescendants": [],
            "isOptionalIcd": False,
            "isChosenOptionalIcd": False,
            "diagnosisOptionalIcds": [],
            "confidenceLabel": "",
            "isBillableSubDx": False,
            "dxId": "E1022",
            "dxDescription": "Type 1 diabetes mellitus with diabetic chronic kidney disease",
            "addedInPostVisit": False,
            "statusUpdatedAt": None,
            "statusUpdatedBy": None,
            "statusUpdatedByName": None,
            "actionUsername": "",
            "addressedGroup": "NewHCCGroup",
            "companionAddressedGroup": None,
            "status": None,
            "type": "recommendation",
            "isValid": False,
            "lastCoderStatus": None,
            "lastCoderStatusUpdatedAt": None,
            "lastCoderStatusUpdatedBy": None,
            "lastCoderStatusUpdatedByName": None,
            "lastProviderStatus": None,
            "lastProviderStatusUpdatedAt": None,
            "lastProviderStatusUpdatedBy": None,
            "lastProviderStatusUpdatedByName": None,
            "coderStatus": None,
            "coderStatusUpdatedAt": None,
            "coderStatusUpdatedBy": None,
            "isCoderStatusFromCurrentSid": False,
            "providerStatus": None,
            "providerStatusUpdatedAt": None,
            "providerStatusUpdatedBy": None,
            "isProviderStatusFromCurrentSid": False,
            "statusUpdatedTimestamp": 0,
            "statusAddedTimestamp": 0,
            "companionOrder": 0,
            "companionDxs": [],
            "primaryDx": None,
            "isNavinaCoupledSuggestion": False,
            "isCoupledSuggestion": False,
            "companionId": "og2G7QMhOjT",
            "noteData": None,
            "isSyncedFromEmr": False,
            "actionsHistory": [
                {
                    "actionBy": "2206091971",
                    "actionName": "inclusion_chart=False",
                    "actionTo": [
                        "E1022",
                        "N1831"
                    ]
                }
            ],
            "invalidOverride": False,
            "overrideFilter": None,
            "sourceData": {
                "type": "recommendation",
                "extra": {
                    "agilon": [],
                    "claimCms": [],
                    "consults": [],
                    "inferred": [
                        {
                            "icdCode": "E1022",
                            "icdDescription": "Type 1 diabetes mellitus with diabetic chronic kidney disease",
                            "operators": [
                                {
                                    "data": [
                                        {
                                            "date": "2024-05-28",
                                            "operator": "<",
                                            "value": 56
                                        }
                                    ],
                                    "date": "2024-05-28",
                                    "name": "eGFR",
                                    "result": True
                                },
                                {
                                    "data": [
                                        {
                                            "date": "2024-05-28",
                                            "operator": ">=",
                                            "value": 56
                                        }
                                    ],
                                    "date": "2024-05-28",
                                    "name": "eGFR",
                                    "result": True
                                },
                                {
                                    "data": [
                                        {
                                            "date": "2024-05-28",
                                            "operator": "<",
                                            "value": 56
                                        },
                                        {
                                            "date": "2024-02-15",
                                            "operator": "<",
                                            "value": 52
                                        }
                                    ],
                                    "date": "2024-05-28",
                                    "name": "eGFR",
                                    "result": True
                                }
                            ],
                            "plInclusion": None,
                            "ruleId": "2206091971",
                            "ruleName": "Type I DM with CKD 3a",
                            "snomedCode": "421893009",
                            "snomedDescription": "Renal disorder due to type 1 diabetes mellitus"
                        }
                    ],
                    "plGap": [],
                    "rafGap": []
                },
                "diagnosisSources": [
                    {
                        "sourceName": "eGFR = 56",
                        "type": "inferred",
                        "data": [
                            {
                                "title": "Suspected finding",
                                "rows": [
                                    {
                                        "key": "05/28/2024",
                                        "value": "eGFR = 56",
                                        "subtype": "Others"
                                    },
                                    {
                                        "key": "02/15/2024",
                                        "value": "eGFR = 52",
                                        "subtype": "Others"
                                    }
                                ]
                            }
                        ],
                        "date": "05/28/2024",
                        "extraData": [
                            {
                                "key": "subSourceName",
                                "value": "eGFR = 56"
                            }
                        ]
                    }
                ]
            },
            "numberOfSources": 1,
            "dataFromAction": False,
            "diagnosisAction": "NO_ACTION",
            "isHint": False,
            "captionInfo": "ignored_coder",
            "suggestionId": "E1022",
            "lowerRelevancyReason": None,
            "hccGroup": 18,
            "hccWeight": 0.302,
            "sid": "dd119322-bcb1-42be-8064-1f4b99076de8",
            "nid": "fcba6f0f-c8cf-4efc-b597-32277cd5255e",
            "navinaProviderId": 12875,
            "view": "provider",
            "dataSourceId": 7,
            "portraitCreatedAt": "2024-03-05 10:52:44",
            "dateOfService": "2024-10-13T02:00:00.000Z"
        }
    ],
    [
        {
            "showInInsights": False,
            "showInCart": False,
            "icdCode": "N1831",
            "icdDescription": "Chronic kidney disease, stage 3a",
            "hccs": {
                "rx": [],
                "v24": [
                    {
                        "group": 138,
                        "weight": 0.069
                    }
                ],
                "v28": [
                    {
                        "group": 329,
                        "weight": 0.127
                    }
                ]
            },
            "snomedDescription": "Chronic kidney disease stage 3A (disorder)",
            "snomedCode": "700378005",
            "reasons": {
                "agilon": [],
                "claimCms": [],
                "consults": [],
                "inferred": [
                    {
                        "icdCode": "N1831",
                        "icdDescription": "Chronic kidney disease, stage 3a",
                        "operators": [
                            {
                                "data": [
                                    {
                                        "date": "2024-05-28",
                                        "operator": "<",
                                        "value": 56
                                    }
                                ],
                                "date": "2024-05-28",
                                "name": "eGFR",
                                "result": True
                            },
                            {
                                "data": [
                                    {
                                        "date": "2024-05-28",
                                        "operator": ">=",
                                        "value": 56
                                    }
                                ],
                                "date": "2024-05-28",
                                "name": "eGFR",
                                "result": True
                            },
                            {
                                "data": [
                                    {
                                        "date": "2024-05-28",
                                        "operator": "<",
                                        "value": 56
                                    },
                                    {
                                        "date": "2024-02-15",
                                        "operator": "<",
                                        "value": 52
                                    }
                                ],
                                "date": "2024-05-28",
                                "name": "eGFR",
                                "result": True
                            }
                        ],
                        "plInclusion": None,
                        "ruleId": "2206091971",
                        "ruleName": "Type I DM with CKD 3a",
                        "snomedDescription": "Chronic kidney disease stage 3A (disorder)"
                    }
                ],
                "plGap": [],
                "rafGap": []
            },
            "diagnosisSources": [
                {
                    "sourceName": "eGFR = 56",
                    "type": "inferred",
                    "data": [
                        {
                            "title": "Suspected finding",
                            "rows": [
                                {
                                    "key": "05/28/2024",
                                    "value": "eGFR = 56",
                                    "subtype": "Others"
                                },
                                {
                                    "key": "02/15/2024",
                                    "value": "eGFR = 52",
                                    "subtype": "Others"
                                }
                            ]
                        }
                    ],
                    "date": "05/28/2024",
                    "extraData": [
                        {
                            "key": "subSourceName",
                            "value": "eGFR = 56"
                        }
                    ]
                }
            ],
            "suggestionDateTime": "2024-05-28 00:00:00",
            "isPrimary": False,
            "billable": True,
            "billableDescendants": [],
            "isOptionalIcd": False,
            "isChosenOptionalIcd": False,
            "diagnosisOptionalIcds": [],
            "confidenceLabel": "",
            "isBillableSubDx": False,
            "dxId": "N1831",
            "dxDescription": "Chronic kidney disease, stage 3a",
            "addedInPostVisit": False,
            "statusUpdatedAt": "2024-08-28T17:26:35.997Z",
            "statusUpdatedBy": "0355859c-63db-4b02-b3b9-1d7a0200efb0",
            "statusUpdatedByName": "Jordan crumpler",
            "actionUsername": "Jordan crumpler",
            "addressedGroup": "NewHCCGroup",
            "companionAddressedGroup": None,
            "status": "accepted_coder",
            "type": "recommendation",
            "isValid": False,
            "lastCoderStatus": "accepted_coder",
            "lastCoderStatusUpdatedAt": "2024-08-28T17:26:35.997Z",
            "lastCoderStatusUpdatedBy": "0355859c-63db-4b02-b3b9-1d7a0200efb0",
            "lastCoderStatusUpdatedByName": "Jordan crumpler",
            "lastProviderStatus": "ignored_provider",
            "lastProviderStatusUpdatedAt": "2024-10-10T15:58:40.312Z",
            "lastProviderStatusUpdatedBy": "961e602d-cda0-4797-918d-6decaeccee2a",
            "lastProviderStatusUpdatedByName": "Demo Navina",
            "coderStatus": "accepted_coder",
            "coderStatusUpdatedAt": "2024-08-28T17:26:35.997Z",
            "coderStatusUpdatedBy": "0355859c-63db-4b02-b3b9-1d7a0200efb0",
            "isCoderStatusFromCurrentSid": False,
            "providerStatus": None,
            "providerStatusUpdatedAt": None,
            "providerStatusUpdatedBy": None,
            "isProviderStatusFromCurrentSid": False,
            "statusUpdatedTimestamp": 1724865988,
            "statusAddedTimestamp": 1724865988,
            "companionOrder": 0,
            "companionDxs": [],
            "primaryDx": None,
            "isNavinaCoupledSuggestion": False,
            "isCoupledSuggestion": False,
            "companionId": "og2G7QMhOjT",
            "noteData": {
                "text": "",
                "authorId": "8d79e112-ac58-4334-9454-dbfa3c01d758",
                "authorName": "dave.madlom@navina.ai",
                "authorType": None,
                "shouldPush": False,
                "noteDate": "2024-05-15T17:37:45.815Z",
                "addedInPostVisit": False
            },
            "isSyncedFromEmr": False,
            "actionsHistory": [
                {
                    "actionBy": "2206091971",
                    "actionName": "inclusion_chart=False",
                    "actionTo": [
                        "E1022",
                        "N1831"
                    ]
                }
            ],
            "invalidOverride": False,
            "overrideFilter": None,
            "sourceData": {
                "type": "recommendation",
                "extra": {
                    "agilon": [],
                    "claimCms": [],
                    "consults": [],
                    "inferred": [
                        {
                            "icdCode": "N1831",
                            "icdDescription": "Chronic kidney disease, stage 3a",
                            "operators": [
                                {
                                    "data": [
                                        {
                                            "date": "2024-05-28",
                                            "operator": "<",
                                            "value": 56
                                        }
                                    ],
                                    "date": "2024-05-28",
                                    "name": "eGFR",
                                    "result": True
                                },
                                {
                                    "data": [
                                        {
                                            "date": "2024-05-28",
                                            "operator": ">=",
                                            "value": 56
                                        }
                                    ],
                                    "date": "2024-05-28",
                                    "name": "eGFR",
                                    "result": True
                                },
                                {
                                    "data": [
                                        {
                                            "date": "2024-05-28",
                                            "operator": "<",
                                            "value": 56
                                        },
                                        {
                                            "date": "2024-02-15",
                                            "operator": "<",
                                            "value": 52
                                        }
                                    ],
                                    "date": "2024-05-28",
                                    "name": "eGFR",
                                    "result": True
                                }
                            ],
                            "plInclusion": None,
                            "ruleId": "2206091971",
                            "ruleName": "Type I DM with CKD 3a",
                            "snomedDescription": "Chronic kidney disease stage 3A (disorder)"
                        }
                    ],
                    "plGap": [],
                    "rafGap": []
                },
                "diagnosisSources": [
                    {
                        "sourceName": "eGFR = 56",
                        "type": "inferred",
                        "data": [
                            {
                                "title": "Suspected finding",
                                "rows": [
                                    {
                                        "key": "05/28/2024",
                                        "value": "eGFR = 56",
                                        "subtype": "Others"
                                    },
                                    {
                                        "key": "02/15/2024",
                                        "value": "eGFR = 52",
                                        "subtype": "Others"
                                    }
                                ]
                            }
                        ],
                        "date": "05/28/2024",
                        "extraData": [
                            {
                                "key": "subSourceName",
                                "value": "eGFR = 56"
                            }
                        ]
                    }
                ]
            },
            "numberOfSources": 1,
            "dataFromAction": False,
            "diagnosisAction": {
                "reason": "NO_REASON",
                "status": "Untouched",
                "detailedStatus": "ignored_provider",
                "note": {
                    "display": True
                },
                "performed": {
                    "byId": "961e602d-cda0-4797-918d-6decaeccee2a",
                    "byUserName": "Demo Navina",
                    "atIsoDatetime": "2024-10-10T15:58:40.312Z"
                }
            },
            "isHint": False,
            "isFromRescheduledAppointment": False,
            "suggestionId": "N1831",
            "lowerRelevancyReason": None,
            "hccGroup": 138,
            "hccWeight": 0.069,
            "sid": "dd119322-bcb1-42be-8064-1f4b99076de8",
            "nid": "fcba6f0f-c8cf-4efc-b597-32277cd5255e",
            "navinaProviderId": 12875,
            "view": "provider",
            "dataSourceId": 7,
            "portraitCreatedAt": "2024-03-05 10:52:44",
            "dateOfService": "2024-10-13T02:00:00.000Z",
            "notShownInInsightsReason": "another dx with the same ICD is shown in insights"
        }
    ],
    [
        {
            "showInInsights": False,
            "showInCart": False,
            "icdCode": "N183",
            "icdDescription": "Chronic kidney disease, stage 3 (moderate)",
            "hccs": {
                "rx": [],
                "v24": [
                    {
                        "group": 138,
                        "weight": 0.069
                    }
                ],
                "v28": []
            },
            "snomedDescription": "Chronic kidney disease stage 3 (disorder)",
            "snomedCode": "433144002",
            "reasons": {
                "agilon": [],
                "claimCms": [
                    {
                        "allClaimCpts": [],
                        "allClaimDxs": [
                            {
                                "icdCode": "N183",
                                "icdDescription": "Chronic kidney disease, stage 3 (moderate)"
                            }
                        ],
                        "endDate": "2022-09-29",
                        "icdCode": "N183",
                        "icdData": [
                            {
                                "code": "N183",
                                "description": "Chronic kidney disease, stage 3 (moderate)",
                                "hccGroup": "138",
                                "hccWeight": 0.069
                            }
                        ],
                        "icdDescription": "Chronic kidney disease, stage 3 (moderate)",
                        "navinaClaimId": "carrier-28170135076_BCDA_23458925",
                        "providerFirstName": "MATTHEW",
                        "providerLastName": "MCGUIRE",
                        "providerNpi": "1407102007",
                        "s3FilePath": "2/ExplanationOfBenefit_fa7930ad-0d97-412d-9ad5-0d666c56d2e2.ndjson",
                        "serviceAddress": "Cleveland, Cuyahoga County, OH, US",
                        "snomedCode": "433144002",
                        "snomedDescription": "Chronic kidney disease stage 3 (disorder)",
                        "startDate": "2022-09-29"
                    }
                ],
                "consults": [],
                "inferred": [],
                "plGap": [],
                "rafGap": [
                    {
                        "data": {
                            "encounterType": "estpt",
                            "modificationDate": "2023-07-15 00:00:00",
                            "providerName": "ROBERT L HILL"
                        },
                        "icdCode": [
                            "N183"
                        ],
                        "icdData": [
                            {
                                "code": "N183",
                                "description": "Chronic kidney disease, stage 3 (moderate)",
                                "hccGroup": "138",
                                "hccWeight": 0.069
                            }
                        ],
                        "snomedCode": "433144002",
                        "type": "PreviousYears"
                    },
                    {
                        "data": {
                            "encounterType": "estpt",
                            "modificationDate": "2023-03-24 00:00:00",
                            "providerName": "ROBERT L HILL"
                        },
                        "icdCode": [
                            "N183"
                        ],
                        "icdData": [
                            {
                                "code": "N183",
                                "description": "Chronic kidney disease, stage 3 (moderate)",
                                "hccGroup": "138",
                                "hccWeight": 0.069
                            }
                        ],
                        "snomedCode": "433144002",
                        "type": "PreviousYears"
                    },
                    {
                        "data": {
                            "encounterType": "estpt",
                            "modificationDate": "2022-11-10 00:00:00",
                            "providerName": "ROBERT L HILL"
                        },
                        "icdCode": [
                            "N183"
                        ],
                        "icdData": [
                            {
                                "code": "N183",
                                "description": "Chronic kidney disease, stage 3 (moderate)",
                                "hccGroup": "138",
                                "hccWeight": 0.069
                            }
                        ],
                        "snomedCode": "433144002",
                        "type": "PreviousYears"
                    },
                    {
                        "data": {
                            "encounterType": "estpt",
                            "modificationDate": "2022-09-16 00:00:00",
                            "providerName": "ROBERT L HILL"
                        },
                        "icdCode": [
                            "N183"
                        ],
                        "icdData": [
                            {
                                "code": "N183",
                                "description": "Chronic kidney disease, stage 3 (moderate)",
                                "hccGroup": "138",
                                "hccWeight": 0.069
                            }
                        ],
                        "snomedCode": "433144002",
                        "type": "PreviousYears"
                    },
                    {
                        "data": {
                            "encounterType": "estpt",
                            "modificationDate": "2022-08-11 00:00:00",
                            "providerName": "ROBERT L HILL"
                        },
                        "icdCode": [
                            "N183"
                        ],
                        "icdData": [
                            {
                                "code": "N183",
                                "description": "Chronic kidney disease, stage 3 (moderate)",
                                "hccGroup": "138",
                                "hccWeight": 0.069
                            }
                        ],
                        "snomedCode": "433144002",
                        "type": "PreviousYears"
                    },
                    {
                        "data": {
                            "encounterType": "telephone",
                            "modificationDate": "2022-05-18 00:00:00",
                            "providerName": "ROBERT L HILL"
                        },
                        "icdCode": [
                            "N183"
                        ],
                        "icdData": [
                            {
                                "code": "N183",
                                "description": "Chronic kidney disease, stage 3 (moderate)",
                                "hccGroup": "138",
                                "hccWeight": 0.069
                            }
                        ],
                        "snomedCode": "433144002",
                        "type": "PreviousYears"
                    },
                    {
                        "data": {
                            "encounterType": "estpt",
                            "modificationDate": "2022-02-18 00:00:00",
                            "providerName": "ROBERT L HILL"
                        },
                        "icdCode": [
                            "N183"
                        ],
                        "icdData": [
                            {
                                "code": "N183",
                                "description": "Chronic kidney disease, stage 3 (moderate)",
                                "hccGroup": "138",
                                "hccWeight": 0.069
                            }
                        ],
                        "snomedCode": "433144002",
                        "type": "PreviousYears"
                    },
                    {
                        "data": {
                            "encounterType": "estpt",
                            "modificationDate": "2021-11-12 00:00:00",
                            "providerName": "ROBERT L HILL"
                        },
                        "icdCode": [
                            "N183"
                        ],
                        "icdData": [
                            {
                                "code": "N183",
                                "description": "Chronic kidney disease, stage 3 (moderate)",
                                "hccGroup": "138",
                                "hccWeight": 0.069
                            }
                        ],
                        "snomedCode": "433144002",
                        "type": "PreviousYears"
                    },
                    {
                        "data": {
                            "encounterType": "mawv",
                            "modificationDate": "2021-11-12 00:00:00",
                            "providerName": "YUERONG BAYER"
                        },
                        "icdCode": [
                            "N183"
                        ],
                        "icdData": [
                            {
                                "code": "N183",
                                "description": "Chronic kidney disease, stage 3 (moderate)",
                                "hccGroup": "138",
                                "hccWeight": 0.069
                            }
                        ],
                        "snomedCode": "433144002",
                        "type": "PreviousYears"
                    },
                    {
                        "data": {
                            "encounterType": "estpt",
                            "modificationDate": "2021-08-20 00:00:00",
                            "providerName": "ROBERT L HILL"
                        },
                        "icdCode": [
                            "N183"
                        ],
                        "icdData": [
                            {
                                "code": "N183",
                                "description": "Chronic kidney disease, stage 3 (moderate)",
                                "hccGroup": "138",
                                "hccWeight": 0.069
                            }
                        ],
                        "snomedCode": "433144002",
                        "type": "PreviousYears"
                    },
                    {
                        "data": {
                            "encounterType": "hfu",
                            "modificationDate": "2021-07-29 00:00:00",
                            "providerName": "ROBERT L HILL"
                        },
                        "icdCode": [
                            "N183"
                        ],
                        "icdData": [
                            {
                                "code": "N183",
                                "description": "Chronic kidney disease, stage 3 (moderate)",
                                "hccGroup": "138",
                                "hccWeight": 0.069
                            }
                        ],
                        "snomedCode": "433144002",
                        "type": "PreviousYears"
                    },
                    {
                        "data": {
                            "encounterType": "estpt",
                            "modificationDate": "2021-05-29 00:00:00",
                            "providerName": "ROBERT L HILL"
                        },
                        "icdCode": [
                            "N183"
                        ],
                        "icdData": [
                            {
                                "code": "N183",
                                "description": "Chronic kidney disease, stage 3 (moderate)",
                                "hccGroup": "138",
                                "hccWeight": 0.069
                            }
                        ],
                        "snomedCode": "433144002",
                        "type": "PreviousYears"
                    },
                    {
                        "data": {
                            "encounterType": "estpt",
                            "modificationDate": "2021-05-06 00:00:00",
                            "providerName": "ROBERT L HILL"
                        },
                        "icdCode": [
                            "N183"
                        ],
                        "icdData": [
                            {
                                "code": "N183",
                                "description": "Chronic kidney disease, stage 3 (moderate)",
                                "hccGroup": "138",
                                "hccWeight": 0.069
                            }
                        ],
                        "snomedCode": "433144002",
                        "type": "PreviousYears"
                    },
                    {
                        "data": {
                            "encounterType": "estpt",
                            "modificationDate": "2021-02-05 00:00:00",
                            "providerName": "ROBERT L HILL"
                        },
                        "icdCode": [
                            "N183"
                        ],
                        "icdData": [
                            {
                                "code": "N183",
                                "description": "Chronic kidney disease, stage 3 (moderate)",
                                "hccGroup": "138",
                                "hccWeight": 0.069
                            }
                        ],
                        "snomedCode": "433144002",
                        "type": "PreviousYears"
                    }
                ]
            },
            "diagnosisSources": [
                {
                    "sourceName": "Encounter (ROBERT L HILL)",
                    "type": "raf_gap",
                    "date": "07/15/2023",
                    "data": [
                        {
                            "title": "Encounter",
                            "date": "07/15/2023",
                            "rows": [
                                {
                                    "key": "Provider name",
                                    "value": "ROBERT L HILL"
                                }
                            ]
                        }
                    ]
                }
            ],
            "suggestionDateTime": "2023-07-15 00:00:00",
            "isPrimary": True,
            "billable": False,
            "billableDescendants": [
                {
                    "icdCode": "N1830",
                    "icdDescription": "Chronic kidney disease, stage 3 unspecified",
                    "hccs": {
                        "rx": [],
                        "v24": [
                            {
                                "group": 138,
                                "weight": 0.069
                            }
                        ],
                        "v28": [
                            {
                                "group": 329,
                                "weight": 0.127
                            }
                        ]
                    },
                    "hccGroup": 138,
                    "hccWeight": 0.069,
                    "billable": True
                },
                {
                    "icdCode": "N1831",
                    "icdDescription": "Chronic kidney disease, stage 3a",
                    "hccs": {
                        "rx": [],
                        "v24": [
                            {
                                "group": 138,
                                "weight": 0.069
                            }
                        ],
                        "v28": [
                            {
                                "group": 329,
                                "weight": 0.127
                            }
                        ]
                    },
                    "hccGroup": 138,
                    "hccWeight": 0.069,
                    "billable": True
                },
                {
                    "icdCode": "N1832",
                    "icdDescription": "Chronic kidney disease, stage 3b",
                    "hccs": {
                        "rx": [],
                        "v24": [
                            {
                                "group": 138,
                                "weight": 0.069
                            }
                        ],
                        "v28": [
                            {
                                "group": 328,
                                "weight": 0.127
                            }
                        ]
                    },
                    "hccGroup": 138,
                    "hccWeight": 0.069,
                    "billable": True
                }
            ],
            "isOptionalIcd": False,
            "isChosenOptionalIcd": False,
            "diagnosisOptionalIcds": [],
            "confidenceLabel": "Recapture",
            "isBillableSubDx": False,
            "dxId": "N183",
            "dxDescription": "Chronic kidney disease, stage 3 (moderate)",
            "addedInPostVisit": False,
            "statusUpdatedAt": "2024-09-01T12:02:17.497Z",
            "statusUpdatedBy": "8f86df48-7903-44f5-9686-eaa7e8637274",
            "statusUpdatedByName": "Rachel Coder",
            "actionUsername": "Rachel Coder",
            "addressedGroup": "NewHCCGroup",
            "companionAddressedGroup": None,
            "status": "accepted_coder",
            "type": "recommendation",
            "isValid": False,
            "lastCoderStatus": "accepted_coder",
            "lastCoderStatusUpdatedAt": "2024-09-01T12:02:17.497Z",
            "lastCoderStatusUpdatedBy": "8f86df48-7903-44f5-9686-eaa7e8637274",
            "lastCoderStatusUpdatedByName": "Rachel Coder",
            "lastProviderStatus": "ignored_provider",
            "lastProviderStatusUpdatedAt": "2024-09-19T10:05:37.882Z",
            "lastProviderStatusUpdatedBy": "e14c61af-8c1b-4ca8-a0d8-446184cfa820",
            "lastProviderStatusUpdatedByName": "Bat-El Ziony",
            "coderStatus": "accepted_coder",
            "coderStatusUpdatedAt": "2024-09-01T12:02:17.497Z",
            "coderStatusUpdatedBy": "8f86df48-7903-44f5-9686-eaa7e8637274",
            "isCoderStatusFromCurrentSid": False,
            "providerStatus": None,
            "providerStatusUpdatedAt": None,
            "providerStatusUpdatedBy": None,
            "isProviderStatusFromCurrentSid": False,
            "statusUpdatedTimestamp": 1725192127,
            "statusAddedTimestamp": 1725192127,
            "companionOrder": 0,
            "companionDxs": [],
            "primaryDx": None,
            "isNavinaCoupledSuggestion": False,
            "isCoupledSuggestion": False,
            "companionId": None,
            "noteData": None,
            "isSyncedFromEmr": False,
            "actionsHistory": [
                {
                    "actionByInferredRule": "2108108452",
                    "actionName": "False_negate",
                    "actionTo": [
                        "N183"
                    ]
                },
                {
                    "actionByInferredRule": "2123806305",
                    "actionName": "False_negate",
                    "actionTo": [
                        "N183"
                    ]
                },
                {
                    "actionByInferredRule": "2123806537",
                    "actionName": "False_negate",
                    "actionTo": [
                        "N183"
                    ]
                }
            ],
            "invalidOverride": False,
            "overrideFilter": None,
            "sourceData": {
                "type": "recommendation",
                "extra": {
                    "agilon": [],
                    "claimCms": [
                        {
                            "allClaimCpts": [],
                            "allClaimDxs": [
                                {
                                    "icdCode": "N183",
                                    "icdDescription": "Chronic kidney disease, stage 3 (moderate)"
                                }
                            ],
                            "endDate": "2022-09-29",
                            "icdCode": "N183",
                            "icdData": [
                                {
                                    "code": "N183",
                                    "description": "Chronic kidney disease, stage 3 (moderate)",
                                    "hccGroup": "138",
                                    "hccWeight": 0.069
                                }
                            ],
                            "icdDescription": "Chronic kidney disease, stage 3 (moderate)",
                            "navinaClaimId": "carrier-28170135076_BCDA_23458925",
                            "providerFirstName": "MATTHEW",
                            "providerLastName": "MCGUIRE",
                            "providerNpi": "1407102007",
                            "s3FilePath": "2/ExplanationOfBenefit_fa7930ad-0d97-412d-9ad5-0d666c56d2e2.ndjson",
                            "serviceAddress": "Cleveland, Cuyahoga County, OH, US",
                            "snomedCode": "433144002",
                            "snomedDescription": "Chronic kidney disease stage 3 (disorder)",
                            "startDate": "2022-09-29"
                        }
                    ],
                    "consults": [],
                    "inferred": [],
                    "plGap": [],
                    "rafGap": [
                        {
                            "data": {
                                "encounterType": "estpt",
                                "modificationDate": "2023-07-15 00:00:00",
                                "providerName": "ROBERT L HILL"
                            },
                            "icdCode": [
                                "N183"
                            ],
                            "icdData": [
                                {
                                    "code": "N183",
                                    "description": "Chronic kidney disease, stage 3 (moderate)",
                                    "hccGroup": "138",
                                    "hccWeight": 0.069
                                }
                            ],
                            "snomedCode": "433144002",
                            "type": "PreviousYears"
                        },
                        {
                            "data": {
                                "encounterType": "estpt",
                                "modificationDate": "2023-03-24 00:00:00",
                                "providerName": "ROBERT L HILL"
                            },
                            "icdCode": [
                                "N183"
                            ],
                            "icdData": [
                                {
                                    "code": "N183",
                                    "description": "Chronic kidney disease, stage 3 (moderate)",
                                    "hccGroup": "138",
                                    "hccWeight": 0.069
                                }
                            ],
                            "snomedCode": "433144002",
                            "type": "PreviousYears"
                        },
                        {
                            "data": {
                                "encounterType": "estpt",
                                "modificationDate": "2022-11-10 00:00:00",
                                "providerName": "ROBERT L HILL"
                            },
                            "icdCode": [
                                "N183"
                            ],
                            "icdData": [
                                {
                                    "code": "N183",
                                    "description": "Chronic kidney disease, stage 3 (moderate)",
                                    "hccGroup": "138",
                                    "hccWeight": 0.069
                                }
                            ],
                            "snomedCode": "433144002",
                            "type": "PreviousYears"
                        },
                        {
                            "data": {
                                "encounterType": "estpt",
                                "modificationDate": "2022-09-16 00:00:00",
                                "providerName": "ROBERT L HILL"
                            },
                            "icdCode": [
                                "N183"
                            ],
                            "icdData": [
                                {
                                    "code": "N183",
                                    "description": "Chronic kidney disease, stage 3 (moderate)",
                                    "hccGroup": "138",
                                    "hccWeight": 0.069
                                }
                            ],
                            "snomedCode": "433144002",
                            "type": "PreviousYears"
                        },
                        {
                            "data": {
                                "encounterType": "estpt",
                                "modificationDate": "2022-08-11 00:00:00",
                                "providerName": "ROBERT L HILL"
                            },
                            "icdCode": [
                                "N183"
                            ],
                            "icdData": [
                                {
                                    "code": "N183",
                                    "description": "Chronic kidney disease, stage 3 (moderate)",
                                    "hccGroup": "138",
                                    "hccWeight": 0.069
                                }
                            ],
                            "snomedCode": "433144002",
                            "type": "PreviousYears"
                        },
                        {
                            "data": {
                                "encounterType": "telephone",
                                "modificationDate": "2022-05-18 00:00:00",
                                "providerName": "ROBERT L HILL"
                            },
                            "icdCode": [
                                "N183"
                            ],
                            "icdData": [
                                {
                                    "code": "N183",
                                    "description": "Chronic kidney disease, stage 3 (moderate)",
                                    "hccGroup": "138",
                                    "hccWeight": 0.069
                                }
                            ],
                            "snomedCode": "433144002",
                            "type": "PreviousYears"
                        },
                        {
                            "data": {
                                "encounterType": "estpt",
                                "modificationDate": "2022-02-18 00:00:00",
                                "providerName": "ROBERT L HILL"
                            },
                            "icdCode": [
                                "N183"
                            ],
                            "icdData": [
                                {
                                    "code": "N183",
                                    "description": "Chronic kidney disease, stage 3 (moderate)",
                                    "hccGroup": "138",
                                    "hccWeight": 0.069
                                }
                            ],
                            "snomedCode": "433144002",
                            "type": "PreviousYears"
                        },
                        {
                            "data": {
                                "encounterType": "estpt",
                                "modificationDate": "2021-11-12 00:00:00",
                                "providerName": "ROBERT L HILL"
                            },
                            "icdCode": [
                                "N183"
                            ],
                            "icdData": [
                                {
                                    "code": "N183",
                                    "description": "Chronic kidney disease, stage 3 (moderate)",
                                    "hccGroup": "138",
                                    "hccWeight": 0.069
                                }
                            ],
                            "snomedCode": "433144002",
                            "type": "PreviousYears"
                        },
                        {
                            "data": {
                                "encounterType": "mawv",
                                "modificationDate": "2021-11-12 00:00:00",
                                "providerName": "YUERONG BAYER"
                            },
                            "icdCode": [
                                "N183"
                            ],
                            "icdData": [
                                {
                                    "code": "N183",
                                    "description": "Chronic kidney disease, stage 3 (moderate)",
                                    "hccGroup": "138",
                                    "hccWeight": 0.069
                                }
                            ],
                            "snomedCode": "433144002",
                            "type": "PreviousYears"
                        },
                        {
                            "data": {
                                "encounterType": "estpt",
                                "modificationDate": "2021-08-20 00:00:00",
                                "providerName": "ROBERT L HILL"
                            },
                            "icdCode": [
                                "N183"
                            ],
                            "icdData": [
                                {
                                    "code": "N183",
                                    "description": "Chronic kidney disease, stage 3 (moderate)",
                                    "hccGroup": "138",
                                    "hccWeight": 0.069
                                }
                            ],
                            "snomedCode": "433144002",
                            "type": "PreviousYears"
                        },
                        {
                            "data": {
                                "encounterType": "hfu",
                                "modificationDate": "2021-07-29 00:00:00",
                                "providerName": "ROBERT L HILL"
                            },
                            "icdCode": [
                                "N183"
                            ],
                            "icdData": [
                                {
                                    "code": "N183",
                                    "description": "Chronic kidney disease, stage 3 (moderate)",
                                    "hccGroup": "138",
                                    "hccWeight": 0.069
                                }
                            ],
                            "snomedCode": "433144002",
                            "type": "PreviousYears"
                        },
                        {
                            "data": {
                                "encounterType": "estpt",
                                "modificationDate": "2021-05-29 00:00:00",
                                "providerName": "ROBERT L HILL"
                            },
                            "icdCode": [
                                "N183"
                            ],
                            "icdData": [
                                {
                                    "code": "N183",
                                    "description": "Chronic kidney disease, stage 3 (moderate)",
                                    "hccGroup": "138",
                                    "hccWeight": 0.069
                                }
                            ],
                            "snomedCode": "433144002",
                            "type": "PreviousYears"
                        },
                        {
                            "data": {
                                "encounterType": "estpt",
                                "modificationDate": "2021-05-06 00:00:00",
                                "providerName": "ROBERT L HILL"
                            },
                            "icdCode": [
                                "N183"
                            ],
                            "icdData": [
                                {
                                    "code": "N183",
                                    "description": "Chronic kidney disease, stage 3 (moderate)",
                                    "hccGroup": "138",
                                    "hccWeight": 0.069
                                }
                            ],
                            "snomedCode": "433144002",
                            "type": "PreviousYears"
                        },
                        {
                            "data": {
                                "encounterType": "estpt",
                                "modificationDate": "2021-02-05 00:00:00",
                                "providerName": "ROBERT L HILL"
                            },
                            "icdCode": [
                                "N183"
                            ],
                            "icdData": [
                                {
                                    "code": "N183",
                                    "description": "Chronic kidney disease, stage 3 (moderate)",
                                    "hccGroup": "138",
                                    "hccWeight": 0.069
                                }
                            ],
                            "snomedCode": "433144002",
                            "type": "PreviousYears"
                        }
                    ]
                },
                "diagnosisSources": [
                    {
                        "sourceName": "Encounter (ROBERT L HILL)",
                        "type": "raf_gap",
                        "date": "07/15/2023",
                        "data": [
                            {
                                "title": "Encounter",
                                "date": "07/15/2023",
                                "rows": [
                                    {
                                        "key": "Provider name",
                                        "value": "ROBERT L HILL"
                                    }
                                ]
                            }
                        ]
                    }
                ]
            },
            "numberOfSources": 1,
            "dataFromAction": False,
            "diagnosisAction": {
                "reason": "NO_REASON",
                "status": "Untouched",
                "detailedStatus": "ignored_provider",
                "note": {
                    "display": True
                },
                "performed": {
                    "byId": "e14c61af-8c1b-4ca8-a0d8-446184cfa820",
                    "byUserName": "Bat-El Ziony",
                    "atIsoDatetime": "2024-09-19T10:05:37.882Z"
                }
            },
            "isHint": False,
            "isFromRescheduledAppointment": False,
            "suggestionId": "N183",
            "lowerRelevancyReason": None,
            "hccGroup": 138,
            "hccWeight": 0.069,
            "sid": "dd119322-bcb1-42be-8064-1f4b99076de8",
            "nid": "fcba6f0f-c8cf-4efc-b597-32277cd5255e",
            "navinaProviderId": 12875,
            "view": "provider",
            "dataSourceId": 7,
            "portraitCreatedAt": "2024-03-05 10:52:44",
            "dateOfService": "2024-10-13T02:00:00.000Z"
        }
    ],
    [
        {
            "showInInsights": True,
            "showInCart": False,
            "icdCode": "D696",
            "icdDescription": "Thrombocytopenia, unspecified",
            "hccs": {
                "rx": [],
                "v24": [
                    {
                        "group": 48,
                        "weight": 0.192
                    }
                ],
                "v28": []
            },
            "snomedDescription": "Thrombocytopenia, unspecified",
            "snomedCode": "302215000",
            "reasons": {
                "agilon": [],
                "claimCms": [
                    {
                        "allClaimCpts": [],
                        "allClaimDxs": [
                            {
                                "icdCode": "D696",
                                "icdDescription": "Thrombocytopenia, unspecified"
                            },
                            {
                                "icdCode": "R509",
                                "icdDescription": "Fever, unspecified"
                            },
                            {
                                "icdCode": "R531",
                                "icdDescription": "Weakness"
                            },
                            {
                                "icdCode": "R5383",
                                "icdDescription": "Other fatigue"
                            }
                        ],
                        "endDate": "2024-06-13",
                        "icdCode": "D696",
                        "icdData": [
                            {
                                "code": "D696",
                                "description": "Thrombocytopenia, unspecified",
                                "hccGroup": "52",
                                "hccWeight": 0.346
                            }
                        ],
                        "icdDescription": "Thrombocytopenia, unspecified",
                        "navinaClaimId": "carrier-27909862498_BCDA_23458925",
                        "providerFirstName": "YOUNG",
                        "providerLastName": "HONG",
                        "providerNpi": "1790783132",
                        "s3FilePath": "2/ExplanationOfBenefit_fa7930ad-0d97-412d-9ad5-0d666c56d2e2.ndjson",
                        "serviceAddress": "Sandusky, Erie County, OH, US",
                        "snomedCode": "278849000",
                        "snomedDescription": "Cerebral atrophy",
                        "startDate": "2024-06-13"
                    }
                ],
                "consults": [],
                "inferred": [
                    {
                        "diagnosisOptionalIcds": [],
                        "dropdownIcd10": [],
                        "dropdownTitle": None,
                        "icdCode": "D696",
                        "icdDescription": "Thrombocytopenia, unspecified",
                        "operators": [
                            {
                                "data": [
                                    {
                                        "date": "2024-05-16",
                                        "operator": ">=",
                                        "source": "PLT",
                                        "value": 92
                                    }
                                ],
                                "date": "2024-05-16",
                                "name": "PLT",
                                "result": True
                            },
                            {
                                "data": [
                                    {
                                        "date": "2023-12-20",
                                        "operator": ">=",
                                        "source": "PLT",
                                        "value": 88
                                    }
                                ],
                                "date": "2023-12-20",
                                "name": "PLT",
                                "result": True
                            }
                        ],
                        "plInclusion": None,
                        "ruleId": "3942167759",
                        "ruleName": "Major depressive disorder, single episode, severe",
                        "snomedCode": "302215000",
                        "snomedDescription": "Thrombocytopenia, unspecified"
                    }
                ],
                "plGap": [],
                "rafGap": []
            },
            "diagnosisSources": [
                {
                    "sourceName": "PLT = 92",
                    "type": "inferred",
                    "data": [
                        {
                            "title": "Suspected finding",
                            "rows": [
                                {
                                    "key": "05/16/2024",
                                    "value": "PLT = 92",
                                    "label": "PLT",
                                    "subtype": "Others"
                                },
                                {
                                    "key": "12/20/2023",
                                    "value": "PLT = 88",
                                    "label": "PLT",
                                    "subtype": "Others"
                                }
                            ]
                        }
                    ],
                    "date": "05/16/2024",
                    "extraData": [
                        {
                            "key": "subSourceName",
                            "value": "PLT = 92"
                        }
                    ]
                },
                {
                    "sourceName": "Claims CMS",
                    "type": "claim_cms",
                    "date": "06/13/2024",
                    "data": [
                        {
                            "title": "Claims CMS",
                            "date": "06/13/2024",
                            "rows": [
                                {
                                    "key": "Provider name",
                                    "value": "YOUNG HONG"
                                },
                                {
                                    "key": "Facility",
                                    "value": "Sandusky, Erie County, OH, US"
                                },
                                {
                                    "key": "Diagnoses in claim",
                                    "value": "D696: Thrombocytopenia, unspecified\nR509: Fever, unspecified\nR531: Weakness\nR5383: Other fatigue"
                                }
                            ]
                        },
                        {
                            "title": "Diagnoses in claim",
                            "rows": [
                                {
                                    "key": "Thrombocytopenia, unspecified",
                                    "value": "D696"
                                },
                                {
                                    "key": "Fever, unspecified",
                                    "value": "R509"
                                },
                                {
                                    "key": "Weakness",
                                    "value": "R531"
                                },
                                {
                                    "key": "Other fatigue",
                                    "value": "R5383"
                                }
                            ]
                        }
                    ],
                    "extraData": [
                        {
                            "key": "claimType",
                            "value": "BCDA"
                        }
                    ]
                }
            ],
            "suggestionDateTime": "2024-06-13 00:00:00",
            "isPrimary": True,
            "billable": True,
            "billableDescendants": [],
            "isOptionalIcd": False,
            "isChosenOptionalIcd": False,
            "diagnosisOptionalIcds": [],
            "confidenceLabel": "Suspect",
            "isBillableSubDx": False,
            "dxId": "D696",
            "dxDescription": "Thrombocytopenia, unspecified",
            "addedInPostVisit": False,
            "statusUpdatedAt": None,
            "statusUpdatedBy": None,
            "statusUpdatedByName": None,
            "actionUsername": "",
            "addressedGroup": "NewHCCGroup",
            "companionAddressedGroup": None,
            "status": None,
            "type": "recommendation",
            "isValid": True,
            "lastCoderStatus": "added_coder",
            "lastCoderStatusUpdatedAt": "2024-08-20T08:49:28.181Z",
            "lastCoderStatusUpdatedBy": "eab73223-6f80-41e9-a250-4ad9ec2d03b7",
            "lastCoderStatusUpdatedByName": "sivan.sagi@navina.ai",
            "lastProviderStatus": "ignored_provider",
            "lastProviderStatusUpdatedAt": "2024-10-08T09:14:05.269Z",
            "lastProviderStatusUpdatedBy": "961e602d-cda0-4797-918d-6decaeccee2a",
            "lastProviderStatusUpdatedByName": "Demo Navina",
            "coderStatus": None,
            "coderStatusUpdatedAt": None,
            "coderStatusUpdatedBy": None,
            "isCoderStatusFromCurrentSid": False,
            "providerStatus": None,
            "providerStatusUpdatedAt": None,
            "providerStatusUpdatedBy": None,
            "isProviderStatusFromCurrentSid": False,
            "statusUpdatedTimestamp": 0,
            "statusAddedTimestamp": 0,
            "companionOrder": 0,
            "companionDxs": None,
            "primaryDx": None,
            "isNavinaCoupledSuggestion": False,
            "isCoupledSuggestion": False,
            "companionId": None,
            "isSyncedFromEmr": False,
            "actionsHistory": [],
            "invalidOverride": False,
            "overrideFilter": None,
            "sourceData": {
                "type": "recommendation",
                "extra": {
                    "agilon": [],
                    "claimCms": [
                        {
                            "allClaimCpts": [],
                            "allClaimDxs": [
                                {
                                    "icdCode": "D696",
                                    "icdDescription": "Thrombocytopenia, unspecified"
                                },
                                {
                                    "icdCode": "R509",
                                    "icdDescription": "Fever, unspecified"
                                },
                                {
                                    "icdCode": "R531",
                                    "icdDescription": "Weakness"
                                },
                                {
                                    "icdCode": "R5383",
                                    "icdDescription": "Other fatigue"
                                }
                            ],
                            "endDate": "2024-06-13",
                            "icdCode": "D696",
                            "icdData": [
                                {
                                    "code": "D696",
                                    "description": "Thrombocytopenia, unspecified",
                                    "hccGroup": "52",
                                    "hccWeight": 0.346
                                }
                            ],
                            "icdDescription": "Thrombocytopenia, unspecified",
                            "navinaClaimId": "carrier-27909862498_BCDA_23458925",
                            "providerFirstName": "YOUNG",
                            "providerLastName": "HONG",
                            "providerNpi": "1790783132",
                            "s3FilePath": "2/ExplanationOfBenefit_fa7930ad-0d97-412d-9ad5-0d666c56d2e2.ndjson",
                            "serviceAddress": "Sandusky, Erie County, OH, US",
                            "snomedCode": "278849000",
                            "snomedDescription": "Cerebral atrophy",
                            "startDate": "2024-06-13"
                        }
                    ],
                    "consults": [],
                    "inferred": [
                        {
                            "diagnosisOptionalIcds": [],
                            "dropdownIcd10": [],
                            "dropdownTitle": None,
                            "icdCode": "D696",
                            "icdDescription": "Thrombocytopenia, unspecified",
                            "operators": [
                                {
                                    "data": [
                                        {
                                            "date": "2024-05-16",
                                            "operator": ">=",
                                            "source": "PLT",
                                            "value": 92
                                        }
                                    ],
                                    "date": "2024-05-16",
                                    "name": "PLT",
                                    "result": True
                                },
                                {
                                    "data": [
                                        {
                                            "date": "2023-12-20",
                                            "operator": ">=",
                                            "source": "PLT",
                                            "value": 88
                                        }
                                    ],
                                    "date": "2023-12-20",
                                    "name": "PLT",
                                    "result": True
                                }
                            ],
                            "plInclusion": None,
                            "ruleId": "3942167759",
                            "ruleName": "Major depressive disorder, single episode, severe",
                            "snomedCode": "302215000",
                            "snomedDescription": "Thrombocytopenia, unspecified"
                        }
                    ],
                    "plGap": [],
                    "rafGap": []
                },
                "diagnosisSources": [
                    {
                        "sourceName": "PLT = 92",
                        "type": "inferred",
                        "data": [
                            {
                                "title": "Suspected finding",
                                "rows": [
                                    {
                                        "key": "05/16/2024",
                                        "value": "PLT = 92",
                                        "label": "PLT",
                                        "subtype": "Others"
                                    },
                                    {
                                        "key": "12/20/2023",
                                        "value": "PLT = 88",
                                        "label": "PLT",
                                        "subtype": "Others"
                                    }
                                ]
                            }
                        ],
                        "date": "05/16/2024",
                        "extraData": [
                            {
                                "key": "subSourceName",
                                "value": "PLT = 92"
                            }
                        ]
                    },
                    {
                        "sourceName": "Claims CMS",
                        "type": "claim_cms",
                        "date": "06/13/2024",
                        "data": [
                            {
                                "title": "Claims CMS",
                                "date": "06/13/2024",
                                "rows": [
                                    {
                                        "key": "Provider name",
                                        "value": "YOUNG HONG"
                                    },
                                    {
                                        "key": "Facility",
                                        "value": "Sandusky, Erie County, OH, US"
                                    },
                                    {
                                        "key": "Diagnoses in claim",
                                        "value": "D696: Thrombocytopenia, unspecified\nR509: Fever, unspecified\nR531: Weakness\nR5383: Other fatigue"
                                    }
                                ]
                            },
                            {
                                "title": "Diagnoses in claim",
                                "rows": [
                                    {
                                        "key": "Thrombocytopenia, unspecified",
                                        "value": "D696"
                                    },
                                    {
                                        "key": "Fever, unspecified",
                                        "value": "R509"
                                    },
                                    {
                                        "key": "Weakness",
                                        "value": "R531"
                                    },
                                    {
                                        "key": "Other fatigue",
                                        "value": "R5383"
                                    }
                                ]
                            }
                        ],
                        "extraData": [
                            {
                                "key": "claimType",
                                "value": "BCDA"
                            }
                        ]
                    }
                ]
            },
            "numberOfSources": 2,
            "dataFromAction": False,
            "diagnosisAction": {
                "reason": "NO_REASON",
                "status": "Untouched",
                "detailedStatus": "ignored_provider",
                "note": {
                    "display": True
                },
                "performed": {
                    "byId": "961e602d-cda0-4797-918d-6decaeccee2a",
                    "byUserName": "Demo Navina",
                    "atIsoDatetime": "2024-10-08T09:14:05.269Z"
                }
            },
            "isHint": True,
            "captionInfo": "ignored_coder",
            "suggestionId": "D696",
            "lowerRelevancyReason": None,
            "hccGroup": 48,
            "hccWeight": 0.192,
            "sid": "dd119322-bcb1-42be-8064-1f4b99076de8",
            "nid": "fcba6f0f-c8cf-4efc-b597-32277cd5255e",
            "navinaProviderId": 12875,
            "view": "provider",
            "dataSourceId": 7,
            "portraitCreatedAt": "2024-03-05 10:52:44",
            "dateOfService": "2024-10-13T02:00:00.000Z"
        }
    ],
    [
        {
            "showInInsights": True,
            "showInCart": False,
            "icdCode": "F320",
            "icdDescription": "Major depressive disorder, single episode, mild",
            "hccs": {
                "rx": [
                    {
                        "group": 132,
                        "weight": 0.023
                    }
                ],
                "v24": [
                    {
                        "group": 59,
                        "weight": 0.309
                    }
                ],
                "v28": []
            },
            "snomedDescription": "Mild major depression, single episode",
            "snomedCode": "79298009",
            "reasons": {
                "agilon": [
                    {
                        "claimId": 23649217,
                        "date": "2023-04-30",
                        "icdCode": "F320",
                        "icdData": [
                            {
                                "code": "F320",
                                "description": "Major depressive disorder, single episode, mild",
                                "hccGroup": "59",
                                "hccWeight": 0.309
                            }
                        ],
                        "icdDescription": "Major depressive disorder, single episode, mild",
                        "id": "c0f0be51-353a-4b79-8407-ccececd4b446",
                        "lastModified": None,
                        "memo": None,
                        "msoName": "MSO Data",
                        "providerFirstName": "Laurier",
                        "providerLastName": "Vocal",
                        "snomedCode": "79298009",
                        "snomedDescription": "Mild major depression, single episode",
                        "suggestionType": "Chronic"
                    }
                ],
                "claimCms": [],
                "consults": [],
                "inferred": [],
                "plGap": [],
                "rafGap": []
            },
            "diagnosisSources": [
                {
                    "sourceName": "MSO Data chronic diagnosis",
                    "type": "agilon",
                    "date": "04/30/2023",
                    "data": [
                        {
                            "title": "MSO Data chronic diagnosis",
                            "date": "04/30/2023",
                            "rows": [
                                {
                                    "key": "Attached memo",
                                    "value": "N/A"
                                },
                                {
                                    "key": "Provider name",
                                    "value": "Laurier Vocal"
                                }
                            ]
                        }
                    ],
                    "extraData": [
                        {
                            "key": "claimType",
                            "value": "AgilonChronic"
                        }
                    ]
                }
            ],
            "suggestionDateTime": "2023-04-30 00:00:00",
            "isPrimary": True,
            "billable": True,
            "billableDescendants": [],
            "isOptionalIcd": False,
            "isChosenOptionalIcd": False,
            "diagnosisOptionalIcds": [],
            "confidenceLabel": "Recapture",
            "isBillableSubDx": False,
            "dxId": "F320",
            "dxDescription": "Major depressive disorder, single episode, mild",
            "addedInPostVisit": False,
            "statusUpdatedAt": None,
            "statusUpdatedBy": None,
            "statusUpdatedByName": None,
            "actionUsername": "",
            "addressedGroup": "NewHCCGroup",
            "companionAddressedGroup": None,
            "status": None,
            "type": "recommendation",
            "isValid": True,
            "lastCoderStatus": None,
            "lastCoderStatusUpdatedAt": None,
            "lastCoderStatusUpdatedBy": None,
            "lastCoderStatusUpdatedByName": None,
            "lastProviderStatus": "pushed_provider",
            "lastProviderStatusUpdatedAt": "2024-09-08T10:18:14.359Z",
            "lastProviderStatusUpdatedBy": "961e602d-cda0-4797-918d-6decaeccee2a",
            "lastProviderStatusUpdatedByName": "Demo Navina",
            "coderStatus": None,
            "coderStatusUpdatedAt": None,
            "coderStatusUpdatedBy": None,
            "isCoderStatusFromCurrentSid": False,
            "providerStatus": None,
            "providerStatusUpdatedAt": None,
            "providerStatusUpdatedBy": None,
            "isProviderStatusFromCurrentSid": False,
            "statusUpdatedTimestamp": 0,
            "statusAddedTimestamp": 0,
            "companionOrder": 0,
            "companionDxs": None,
            "primaryDx": None,
            "isNavinaCoupledSuggestion": False,
            "isCoupledSuggestion": False,
            "companionId": None,
            "noteData": {
                "text": "",
                "authorName": "ronen.gordon.provider@navina.ai",
                "authorType": "Provider",
                "noteDate": "2023-12-06T12:00:55.240Z",
                "shouldPush": False,
                "addedInPostVisit": False
            },
            "isSyncedFromEmr": False,
            "actionsHistory": [],
            "invalidOverride": False,
            "overrideFilter": None,
            "sourceData": {
                "type": "recommendation",
                "extra": {
                    "agilon": [
                        {
                            "claimId": 23649217,
                            "date": "2023-04-30",
                            "icdCode": "F320",
                            "icdData": [
                                {
                                    "code": "F320",
                                    "description": "Major depressive disorder, single episode, mild",
                                    "hccGroup": "59",
                                    "hccWeight": 0.309
                                }
                            ],
                            "icdDescription": "Major depressive disorder, single episode, mild",
                            "id": "c0f0be51-353a-4b79-8407-ccececd4b446",
                            "lastModified": None,
                            "memo": None,
                            "msoName": "MSO Data",
                            "providerFirstName": "Laurier",
                            "providerLastName": "Vocal",
                            "snomedCode": "79298009",
                            "snomedDescription": "Mild major depression, single episode",
                            "suggestionType": "Chronic"
                        }
                    ],
                    "claimCms": [],
                    "consults": [],
                    "inferred": [],
                    "plGap": [],
                    "rafGap": []
                },
                "diagnosisSources": [
                    {
                        "sourceName": "MSO Data chronic diagnosis",
                        "type": "agilon",
                        "date": "04/30/2023",
                        "data": [
                            {
                                "title": "MSO Data chronic diagnosis",
                                "date": "04/30/2023",
                                "rows": [
                                    {
                                        "key": "Attached memo",
                                        "value": "N/A"
                                    },
                                    {
                                        "key": "Provider name",
                                        "value": "Laurier Vocal"
                                    }
                                ]
                            }
                        ],
                        "extraData": [
                            {
                                "key": "claimType",
                                "value": "AgilonChronic"
                            }
                        ]
                    }
                ]
            },
            "numberOfSources": 1,
            "dataFromAction": False,
            "diagnosisAction": {
                "reason": "NO_REASON",
                "status": "Accepted",
                "detailedStatus": "pushed_provider",
                "note": {
                    "display": True
                },
                "performed": {
                    "byId": "961e602d-cda0-4797-918d-6decaeccee2a",
                    "byUserName": "Demo Navina",
                    "atIsoDatetime": "2024-09-08T10:18:14.359Z"
                }
            },
            "isHint": True,
            "captionInfo": "ignored_coder",
            "notShownInInsightsReason": "",
            "suggestionId": "F320",
            "lowerRelevancyReason": None,
            "hccGroup": 59,
            "hccWeight": 0.309,
            "sid": "dd119322-bcb1-42be-8064-1f4b99076de8",
            "nid": "fcba6f0f-c8cf-4efc-b597-32277cd5255e",
            "navinaProviderId": 12875,
            "view": "provider",
            "dataSourceId": 7,
            "portraitCreatedAt": "2024-03-05 10:52:44",
            "dateOfService": "2024-10-13T02:00:00.000Z"
        }
    ],
    [
        {
            "showInInsights": True,
            "showInCart": False,
            "icdCode": "M064",
            "icdDescription": "Inflammatory polyarthropathy",
            "hccs": {
                "rx": [
                    {
                        "group": 83,
                        "weight": 0.205
                    }
                ],
                "v24": [
                    {
                        "group": 40,
                        "weight": 0.421
                    }
                ],
                "v28": [
                    {
                        "group": 94,
                        "weight": 0.268
                    }
                ]
            },
            "snomedDescription": "Inflammatory polyarthropathy (disorder)",
            "snomedCode": "417373000",
            "reasons": {
                "agilon": [
                    {
                        "claimId": 225091,
                        "date": "2024-03-08",
                        "icdCode": "M064",
                        "icdData": [
                            {
                                "code": "M064",
                                "description": "Inflammatory polyarthropathy",
                                "hccGroup": "40",
                                "hccWeight": 0.421
                            }
                        ],
                        "icdDescription": "Inflammatory polyarthropathy",
                        "id": "9dbace9a-37fc-41fe-a892-0bb003383fc1",
                        "lastModified": "2024-03-08",
                        "memo": "Patient noted to have Inflammatory Polyneuropathy on Rheumatology note 4/19/23.",
                        "msoName": "MSO Data",
                        "providerFirstName": None,
                        "providerLastName": "Unknown PCP - Austin",
                        "snomedCode": "417373000",
                        "snomedDescription": "Inflammatory polyarthropathy (disorder)",
                        "suggestionType": "Suspect"
                    }
                ],
                "claimCms": [],
                "consults": [],
                "inferred": [],
                "plGap": [],
                "rafGap": []
            },
            "diagnosisSources": [
                {
                    "sourceName": "MSO Data suspect diagnosis",
                    "type": "agilon",
                    "date": "03/08/2024",
                    "data": [
                        {
                            "title": "MSO Data suspect diagnosis",
                            "date": "03/08/2024",
                            "rows": [
                                {
                                    "key": "Attached memo",
                                    "value": "Patient noted to have Inflammatory Polyneuropathy on Rheumatology note 4/19/23."
                                },
                                {
                                    "key": "Provider name",
                                    "value": "N/A"
                                }
                            ]
                        }
                    ],
                    "extraData": [
                        {
                            "key": "claimType",
                            "value": "AgilonSuspect"
                        }
                    ]
                }
            ],
            "suggestionDateTime": "2024-03-08 00:00:00",
            "isPrimary": True,
            "billable": True,
            "billableDescendants": [],
            "isOptionalIcd": False,
            "isChosenOptionalIcd": False,
            "diagnosisOptionalIcds": [],
            "confidenceLabel": "Suspect",
            "isBillableSubDx": False,
            "dxId": "M064",
            "dxDescription": "Inflammatory polyarthropathy",
            "addedInPostVisit": False,
            "statusUpdatedAt": None,
            "statusUpdatedBy": None,
            "statusUpdatedByName": None,
            "actionUsername": "",
            "addressedGroup": "NewHCCGroup",
            "companionAddressedGroup": None,
            "status": None,
            "type": "recommendation",
            "isValid": True,
            "lastCoderStatus": "added_coder",
            "lastCoderStatusUpdatedAt": "2024-08-20T08:49:24.131Z",
            "lastCoderStatusUpdatedBy": "eab73223-6f80-41e9-a250-4ad9ec2d03b7",
            "lastCoderStatusUpdatedByName": "sivan.sagi@navina.ai",
            "lastProviderStatus": "ignored_provider",
            "lastProviderStatusUpdatedAt": "2024-10-10T15:58:49.087Z",
            "lastProviderStatusUpdatedBy": "961e602d-cda0-4797-918d-6decaeccee2a",
            "lastProviderStatusUpdatedByName": "Demo Navina",
            "coderStatus": None,
            "coderStatusUpdatedAt": None,
            "coderStatusUpdatedBy": None,
            "isCoderStatusFromCurrentSid": False,
            "providerStatus": None,
            "providerStatusUpdatedAt": None,
            "providerStatusUpdatedBy": None,
            "isProviderStatusFromCurrentSid": False,
            "statusUpdatedTimestamp": 0,
            "statusAddedTimestamp": 0,
            "companionOrder": 0,
            "companionDxs": None,
            "primaryDx": None,
            "isNavinaCoupledSuggestion": False,
            "isCoupledSuggestion": False,
            "companionId": None,
            "noteData": {
                "text": "",
                "authorName": "Aviv Provider",
                "authorType": "Admin",
                "noteDate": "2024-08-07T11:49:33.992Z",
                "shouldPush": False,
                "addedInPostVisit": False
            },
            "isSyncedFromEmr": False,
            "actionsHistory": [],
            "invalidOverride": False,
            "overrideFilter": None,
            "sourceData": {
                "type": "recommendation",
                "extra": {
                    "agilon": [
                        {
                            "claimId": 225091,
                            "date": "2024-03-08",
                            "icdCode": "M064",
                            "icdData": [
                                {
                                    "code": "M064",
                                    "description": "Inflammatory polyarthropathy",
                                    "hccGroup": "40",
                                    "hccWeight": 0.421
                                }
                            ],
                            "icdDescription": "Inflammatory polyarthropathy",
                            "id": "9dbace9a-37fc-41fe-a892-0bb003383fc1",
                            "lastModified": "2024-03-08",
                            "memo": "Patient noted to have Inflammatory Polyneuropathy on Rheumatology note 4/19/23.",
                            "msoName": "MSO Data",
                            "providerFirstName": None,
                            "providerLastName": "Unknown PCP - Austin",
                            "snomedCode": "417373000",
                            "snomedDescription": "Inflammatory polyarthropathy (disorder)",
                            "suggestionType": "Suspect"
                        }
                    ],
                    "claimCms": [],
                    "consults": [],
                    "inferred": [],
                    "plGap": [],
                    "rafGap": []
                },
                "diagnosisSources": [
                    {
                        "sourceName": "MSO Data suspect diagnosis",
                        "type": "agilon",
                        "date": "03/08/2024",
                        "data": [
                            {
                                "title": "MSO Data suspect diagnosis",
                                "date": "03/08/2024",
                                "rows": [
                                    {
                                        "key": "Attached memo",
                                        "value": "Patient noted to have Inflammatory Polyneuropathy on Rheumatology note 4/19/23."
                                    },
                                    {
                                        "key": "Provider name",
                                        "value": "N/A"
                                    }
                                ]
                            }
                        ],
                        "extraData": [
                            {
                                "key": "claimType",
                                "value": "AgilonSuspect"
                            }
                        ]
                    }
                ]
            },
            "numberOfSources": 1,
            "dataFromAction": False,
            "diagnosisAction": {
                "reason": "NO_REASON",
                "status": "Untouched",
                "detailedStatus": "ignored_provider",
                "note": {
                    "display": True
                },
                "performed": {
                    "byId": "961e602d-cda0-4797-918d-6decaeccee2a",
                    "byUserName": "Demo Navina",
                    "atIsoDatetime": "2024-10-10T15:58:49.087Z"
                }
            },
            "isHint": True,
            "captionInfo": "ignored_coder",
            "notShownInInsightsReason": "",
            "suggestionId": "M064",
            "lowerRelevancyReason": None,
            "hccGroup": 40,
            "hccWeight": 0.421,
            "sid": "dd119322-bcb1-42be-8064-1f4b99076de8",
            "nid": "fcba6f0f-c8cf-4efc-b597-32277cd5255e",
            "navinaProviderId": 12875,
            "view": "provider",
            "dataSourceId": 7,
            "portraitCreatedAt": "2024-03-05 10:52:44",
            "dateOfService": "2024-10-13T02:00:00.000Z"
        }
    ],
    [
        {
            "showInInsights": True,
            "showInCart": False,
            "icdCode": "Emphysema",
            "icdDescription": "Emphysema",
            "hccs": {
                "v24": [
                    {
                        "group": 111,
                        "weight": 0.335
                    }
                ],
                "v28": [
                    {
                        "group": 280,
                        "weight": 0.319
                    }
                ],
                "rx": [
                    {
                        "group": 229,
                        "weight": 0.186
                    }
                ]
            },
            "snomedDescription": None,
            "snomedCode": None,
            "reasons": {
                "agilon": [],
                "claimCms": [],
                "consults": [],
                "imagingInferred": [
                    {
                        "id": "212f54e2-7d39-458b-9a34-b5ec61fb75cf",
                        "encounterDate": "04/04/2020",
                        "fileDate": "2023-04-04",
                        "fileId": "1abdf3bd-6976-43a4-84ee-95b0c57d552f",
                        "fileLabel": "ct_w-contrast",
                        "fileLoinc": "87279-6",
                        "fileLoincName": "ct_w-contrast",
                        "fileName": "Athena/7/7637/7637_10_20_2022_inferred_imaging_demo.pdf",
                        "hccWeight": 0.331,
                        "icd10CodeLineContent": "emphysematous changes",
                        "index": 22,
                        "lineContentOccurrenceInDoc": 2,
                        "matchWindow": "IMPRESSION: Overall little change since previous examination. Cystic emphysematous changes No definite spiculated mass",
                        "secondaryName": "chest imaging",
                        "snomedCode": None,
                        "snomedName": None
                    }
                ],
                "inferred": [],
                "plGap": [],
                "rafGap": []
            },
            "diagnosisSources": [
                {
                    "sourceName": "Imaging",
                    "type": "imaging_inferred",
                    "date": "04/04/2023",
                    "document": {
                        "name": "ct_w-contrast",
                        "id": "1abdf3bd-6976-43a4-84ee-95b0c57d552f",
                        "date": "04/04/2023",
                        "searchTerm": "emphysematous changes",
                        "searchTermOccurrence": 1
                    },
                    "data": [
                        {
                            "title": "Imaging",
                            "date": "04/04/2023",
                            "rows": [
                                {
                                    "key": "Excerpt",
                                    "value": "...IMPRESSION: Overall little change since previous examination. Cystic **emphysematous changes** No definite spiculated mass...",
                                    "contentType": "text/markdown"
                                },
                                {
                                    "key": "Document name",
                                    "value": "ct_w-contrast"
                                },
                                {
                                    "key": "Document date",
                                    "value": "04/04/2023"
                                }
                            ]
                        }
                    ]
                }
            ],
            "suggestionDateTime": "2023-04-04 00:00:00",
            "isPrimary": True,
            "billable": True,
            "billableDescendants": [],
            "isOptionalIcd": True,
            "isChosenOptionalIcd": False,
            "diagnosisOptionalIcds": [
                {
                    "icdCode": "J431",
                    "icdDescription": "Panlobular emphysema",
                    "hccs": {
                        "rx": [
                            {
                                "group": 229,
                                "weight": 0.186
                            }
                        ],
                        "v24": [
                            {
                                "group": 111,
                                "weight": 0.335
                            }
                        ],
                        "v28": [
                            {
                                "group": 280,
                                "weight": 0.319
                            }
                        ]
                    },
                    "hccGroup": 111,
                    "hccWeight": 0.335,
                    "addressedGroup": "NewHCCGroup"
                },
                {
                    "icdCode": "J432",
                    "icdDescription": "Centrilobular emphysema",
                    "hccs": {
                        "rx": [
                            {
                                "group": 229,
                                "weight": 0.186
                            }
                        ],
                        "v24": [
                            {
                                "group": 111,
                                "weight": 0.335
                            }
                        ],
                        "v28": [
                            {
                                "group": 280,
                                "weight": 0.319
                            }
                        ]
                    },
                    "hccGroup": 111,
                    "hccWeight": 0.335,
                    "addressedGroup": "NewHCCGroup"
                },
                {
                    "icdCode": "J439",
                    "icdDescription": "Emphysema, unspecified",
                    "hccs": {
                        "rx": [
                            {
                                "group": 229,
                                "weight": 0.186
                            }
                        ],
                        "v24": [
                            {
                                "group": 111,
                                "weight": 0.335
                            }
                        ],
                        "v28": [
                            {
                                "group": 280,
                                "weight": 0.319
                            }
                        ]
                    },
                    "hccGroup": 111,
                    "hccWeight": 0.335,
                    "addressedGroup": "NewHCCGroup"
                }
            ],
            "confidenceLabel": "Suspect",
            "isBillableSubDx": False,
            "dxId": "Emphysema",
            "dxDescription": "Emphysema",
            "addedInPostVisit": False,
            "statusUpdatedAt": None,
            "statusUpdatedBy": None,
            "statusUpdatedByName": None,
            "actionUsername": "",
            "addressedGroup": "NewHCCGroup",
            "companionAddressedGroup": None,
            "status": None,
            "type": "recommendation",
            "isValid": True,
            "lastCoderStatus": None,
            "lastCoderStatusUpdatedAt": None,
            "lastCoderStatusUpdatedBy": None,
            "lastCoderStatusUpdatedByName": None,
            "lastProviderStatus": "pushed_provider",
            "lastProviderStatusUpdatedAt": "2024-09-10T07:27:06.168Z",
            "lastProviderStatusUpdatedBy": "961e602d-cda0-4797-918d-6decaeccee2a",
            "lastProviderStatusUpdatedByName": "Demo Navina",
            "coderStatus": None,
            "coderStatusUpdatedAt": None,
            "coderStatusUpdatedBy": None,
            "isCoderStatusFromCurrentSid": False,
            "providerStatus": None,
            "providerStatusUpdatedAt": None,
            "providerStatusUpdatedBy": None,
            "isProviderStatusFromCurrentSid": False,
            "statusUpdatedTimestamp": 0,
            "statusAddedTimestamp": 0,
            "companionOrder": 0,
            "companionDxs": None,
            "primaryDx": None,
            "isNavinaCoupledSuggestion": False,
            "isCoupledSuggestion": False,
            "companionId": None,
            "noteData": {
                "text": "",
                "authorName": "Aviv Provider",
                "authorType": "Admin",
                "noteDate": "2024-08-07T11:55:08.589Z",
                "shouldPush": False,
                "addedInPostVisit": False
            },
            "isSyncedFromEmr": False,
            "actionsHistory": [],
            "invalidOverride": False,
            "overrideFilter": None,
            "sourceData": {
                "type": "recommendation",
                "extra": {
                    "agilon": [],
                    "claimCms": [],
                    "consults": [],
                    "imagingInferred": [
                        {
                            "id": "212f54e2-7d39-458b-9a34-b5ec61fb75cf",
                            "encounterDate": "04/04/2020",
                            "fileDate": "2023-04-04",
                            "fileId": "1abdf3bd-6976-43a4-84ee-95b0c57d552f",
                            "fileLabel": "ct_w-contrast",
                            "fileLoinc": "87279-6",
                            "fileLoincName": "ct_w-contrast",
                            "fileName": "Athena/7/7637/7637_10_20_2022_inferred_imaging_demo.pdf",
                            "hccWeight": 0.331,
                            "icd10CodeLineContent": "emphysematous changes",
                            "index": 22,
                            "lineContentOccurrenceInDoc": 2,
                            "matchWindow": "IMPRESSION: Overall little change since previous examination. Cystic emphysematous changes No definite spiculated mass",
                            "secondaryName": "chest imaging",
                            "snomedCode": None,
                            "snomedName": None
                        }
                    ],
                    "inferred": [],
                    "plGap": [],
                    "rafGap": []
                },
                "diagnosisSources": [
                    {
                        "sourceName": "Imaging",
                        "type": "imaging_inferred",
                        "date": "04/04/2023",
                        "document": {
                            "name": "ct_w-contrast",
                            "id": "1abdf3bd-6976-43a4-84ee-95b0c57d552f",
                            "date": "04/04/2023",
                            "searchTerm": "emphysematous changes",
                            "searchTermOccurrence": 1
                        },
                        "data": [
                            {
                                "title": "Imaging",
                                "date": "04/04/2023",
                                "rows": [
                                    {
                                        "key": "Excerpt",
                                        "value": "...IMPRESSION: Overall little change since previous examination. Cystic **emphysematous changes** No definite spiculated mass...",
                                        "contentType": "text/markdown"
                                    },
                                    {
                                        "key": "Document name",
                                        "value": "ct_w-contrast"
                                    },
                                    {
                                        "key": "Document date",
                                        "value": "04/04/2023"
                                    }
                                ]
                            }
                        ]
                    }
                ]
            },
            "numberOfSources": 1,
            "dataFromAction": False,
            "diagnosisAction": {
                "reason": "NO_REASON",
                "status": "Accepted",
                "detailedStatus": "pushed_provider",
                "note": {
                    "display": True
                },
                "performed": {
                    "byId": "961e602d-cda0-4797-918d-6decaeccee2a",
                    "byUserName": "Demo Navina",
                    "atIsoDatetime": "2024-09-10T07:27:06.168Z"
                }
            },
            "isHint": True,
            "captionInfo": "ignored_coder",
            "suggestionId": "Emphysema",
            "lowerRelevancyReason": None,
            "hccGroup": 111,
            "hccWeight": 0.335,
            "sid": "dd119322-bcb1-42be-8064-1f4b99076de8",
            "nid": "fcba6f0f-c8cf-4efc-b597-32277cd5255e",
            "navinaProviderId": 12875,
            "view": "provider",
            "dataSourceId": 7,
            "portraitCreatedAt": "2024-03-05 10:52:44",
            "dateOfService": "2024-10-13T02:00:00.000Z"
        }
    ],
    [
        {
            "showInInsights": True,
            "showInCart": False,
            "icdCode": "F322",
            "icdDescription": "Major depressive disorder, single episode, severe without psychotic features",
            "hccs": {
                "rx": [
                    {
                        "group": 132,
                        "weight": 0.023
                    }
                ],
                "v24": [
                    {
                        "group": 59,
                        "weight": 0.309
                    }
                ],
                "v28": [
                    {
                        "group": 155,
                        "weight": 0.299
                    }
                ]
            },
            "snomedDescription": "Severe major depression, single episode, without psychotic features",
            "snomedCode": "76441001",
            "reasons": {
                "agilon": [],
                "claimCms": [],
                "consults": [],
                "hieEncounters": [],
                "imagingInferred": [],
                "inferred": [
                    {
                        "diagnosisOptionalIcds": [],
                        "dropdownIcd10": [],
                        "dropdownTitle": None,
                        "icdCode": "F322",
                        "icdDescription": "Major depressive disorder, single episode, severe without psychotic features",
                        "operators": [
                            {
                                "data": [
                                    {
                                        "date": "2024-04-22",
                                        "operator": ">=",
                                        "source": "PHQ",
                                        "value": 19
                                    }
                                ],
                                "date": "2024-04-22",
                                "name": "PHQ",
                                "result": True
                            },
                            {
                                "data": [
                                    {
                                        "date": "2024-04-22",
                                        "operator": "<",
                                        "source": "PHQ",
                                        "value": 19
                                    }
                                ],
                                "date": "2024-04-22",
                                "name": "PHQ",
                                "result": True
                            }
                        ],
                        "plInclusion": None,
                        "ruleId": "3942167759",
                        "ruleName": "Major depressive disorder, single episode, severe",
                        "snomedCode": "76441001",
                        "snomedDescription": "Severe major depression, single episode, without psychotic features",
                        "validityOutput": "Suspected condition"
                    }
                ],
                "plGap": [],
                "rafGap": []
            },
            "diagnosisSources": [
                {
                    "sourceName": "PHQ",
                    "type": "inferred",
                    "data": [
                        {
                            "title": "Suspected finding",
                            "rows": [
                                {
                                    "key": "04/22/2024",
                                    "value": "PHQ = 19",
                                    "label": "PHQ",
                                    "subtype": "PHQ"
                                }
                            ]
                        }
                    ],
                    "date": "04/22/2024",
                    "extraData": [
                        {
                            "key": "subSourceName",
                            "value": "PHQ"
                        }
                    ]
                }
            ],
            "suggestionDateTime": "2024-04-22 00:00:00",
            "isPrimary": True,
            "billable": True,
            "billableDescendants": [],
            "isOptionalIcd": False,
            "isChosenOptionalIcd": False,
            "diagnosisOptionalIcds": [],
            "confidenceLabel": "Suspect",
            "isBillableSubDx": False,
            "dxId": "F322",
            "dxDescription": "Major depressive disorder, single episode, severe without psychotic features",
            "addedInPostVisit": False,
            "statusUpdatedAt": None,
            "statusUpdatedBy": None,
            "statusUpdatedByName": None,
            "actionUsername": "",
            "addressedGroup": "NewHCCGroup",
            "companionAddressedGroup": None,
            "status": None,
            "type": "recommendation",
            "isValid": True,
            "lastCoderStatus": "ignored_coder",
            "lastCoderStatusUpdatedAt": "2024-08-20T22:34:55.009Z",
            "lastCoderStatusUpdatedBy": "0df79952-bceb-4701-992a-604489760156",
            "lastCoderStatusUpdatedByName": "Aviv Coder",
            "lastProviderStatus": "ignored_provider",
            "lastProviderStatusUpdatedAt": "2024-10-07T10:25:48.394Z",
            "lastProviderStatusUpdatedBy": "961e602d-cda0-4797-918d-6decaeccee2a",
            "lastProviderStatusUpdatedByName": "Demo Navina",
            "coderStatus": None,
            "coderStatusUpdatedAt": None,
            "coderStatusUpdatedBy": None,
            "isCoderStatusFromCurrentSid": False,
            "providerStatus": None,
            "providerStatusUpdatedAt": None,
            "providerStatusUpdatedBy": None,
            "isProviderStatusFromCurrentSid": False,
            "statusUpdatedTimestamp": 0,
            "statusAddedTimestamp": 0,
            "companionOrder": 0,
            "companionDxs": None,
            "primaryDx": None,
            "isNavinaCoupledSuggestion": False,
            "isCoupledSuggestion": False,
            "companionId": None,
            "noteData": {
                "text": "",
                "authorName": "dave.madlom@navina.ai",
                "authorType": None,
                "noteDate": "2024-05-02T14:50:32.369Z",
                "shouldPush": False,
                "addedInPostVisit": False
            },
            "isSyncedFromEmr": False,
            "actionsHistory": [],
            "invalidOverride": False,
            "overrideFilter": None,
            "sourceData": {
                "type": "recommendation",
                "extra": {
                    "agilon": [],
                    "claimCms": [],
                    "consults": [],
                    "hieEncounters": [],
                    "imagingInferred": [],
                    "inferred": [
                        {
                            "diagnosisOptionalIcds": [],
                            "dropdownIcd10": [],
                            "dropdownTitle": None,
                            "icdCode": "F322",
                            "icdDescription": "Major depressive disorder, single episode, severe without psychotic features",
                            "operators": [
                                {
                                    "data": [
                                        {
                                            "date": "2024-04-22",
                                            "operator": ">=",
                                            "source": "PHQ",
                                            "value": 19
                                        }
                                    ],
                                    "date": "2024-04-22",
                                    "name": "PHQ",
                                    "result": True
                                },
                                {
                                    "data": [
                                        {
                                            "date": "2024-04-22",
                                            "operator": "<",
                                            "source": "PHQ",
                                            "value": 19
                                        }
                                    ],
                                    "date": "2024-04-22",
                                    "name": "PHQ",
                                    "result": True
                                }
                            ],
                            "plInclusion": None,
                            "ruleId": "3942167759",
                            "ruleName": "Major depressive disorder, single episode, severe",
                            "snomedCode": "76441001",
                            "snomedDescription": "Severe major depression, single episode, without psychotic features",
                            "validityOutput": "Suspected condition"
                        }
                    ],
                    "plGap": [],
                    "rafGap": []
                },
                "diagnosisSources": [
                    {
                        "sourceName": "PHQ",
                        "type": "inferred",
                        "data": [
                            {
                                "title": "Suspected finding",
                                "rows": [
                                    {
                                        "key": "04/22/2024",
                                        "value": "PHQ = 19",
                                        "label": "PHQ",
                                        "subtype": "PHQ"
                                    }
                                ]
                            }
                        ],
                        "date": "04/22/2024",
                        "extraData": [
                            {
                                "key": "subSourceName",
                                "value": "PHQ"
                            }
                        ]
                    }
                ]
            },
            "numberOfSources": 1,
            "dataFromAction": False,
            "diagnosisAction": {
                "reason": "NO_REASON",
                "status": "Untouched",
                "detailedStatus": "ignored_provider",
                "note": {
                    "display": True
                },
                "performed": {
                    "byId": "961e602d-cda0-4797-918d-6decaeccee2a",
                    "byUserName": "Demo Navina",
                    "atIsoDatetime": "2024-10-07T10:25:48.394Z"
                }
            },
            "isHint": True,
            "captionInfo": "ignored_coder",
            "suggestionId": "F322",
            "lowerRelevancyReason": None,
            "hccGroup": 59,
            "hccWeight": 0.309,
            "sid": "dd119322-bcb1-42be-8064-1f4b99076de8",
            "nid": "fcba6f0f-c8cf-4efc-b597-32277cd5255e",
            "navinaProviderId": 12875,
            "view": "provider",
            "dataSourceId": 7,
            "portraitCreatedAt": "2024-03-05 10:52:44",
            "dateOfService": "2024-10-13T02:00:00.000Z"
        }
    ],
    [
        {
            "showInInsights": False,
            "showInCart": False,
            "icdCode": "heart_failure",
            "icdDescription": "Heart failure",
            "hccs": {
                "v24": [
                    {
                        "group": "85",
                        "weight": 0.331
                    }
                ],
                "v28": [
                    {
                        "group": "226",
                        "weight": 0.36
                    }
                ]
            },
            "snomedDescription": None,
            "snomedCode": None,
            "reasons": {
                "agilon": [],
                "claimCms": [],
                "consults": [],
                "hieEncounters": [],
                "inferred": [],
                "imagingInferred": [
                    {
                        "diagnosisOptionalIcds": [
                            {
                                "hccGroup": "85",
                                "hccWeight": 0.331,
                                "icdCode": "I509",
                                "icdDescription": "Heart failure, unspecified",
                                "snomedCode": "84114007"
                            },
                            {
                                "hccGroup": "85",
                                "hccWeight": 0.331,
                                "icdCode": "I5022",
                                "icdDescription": "Chronic systolic (congestive) heart failure",
                                "snomedCode": "88805009"
                            },
                            {
                                "hccGroup": "85",
                                "hccWeight": 0.331,
                                "icdCode": "I5032",
                                "icdDescription": "Chronic diastolic (congestive) heart failure",
                                "snomedCode": "42343007"
                            },
                            {
                                "hccGroup": "85",
                                "hccWeight": 0.331,
                                "icdCode": "I5042",
                                "icdDescription": "Chronic combined systolic (congestive) and diastolic (congestive) heart failure",
                                "snomedCode": "42343007"
                            }
                        ],
                        "icdCode": "heart_failure",
                        "icdDescription": "Heart failure",
                        "icd10CodeLineContent": "ejection fraction of 45%",
                        "lineContentOccurrenceInDoc": 1,
                        "matchWindow": "Mild decrease in systolic function with an ejection fraction of 45%",
                        "snomedCode": None,
                        "snomedDescription": None,
                        "fileId": "624a2a38-b450-404b-a568-4be8251a670e",
                        "fileDate": "2024-06-02",
                        "fileLoincName": "scan_060223"
                    }
                ],
                "plGap": [],
                "rafGap": []
            },
            "diagnosisSources": [
                {
                    "sourceName": "Imaging",
                    "type": "imaging_inferred",
                    "date": "06/02/2024",
                    "document": {
                        "name": "scan_060223",
                        "id": "624a2a38-b450-404b-a568-4be8251a670e",
                        "date": "06/02/2024",
                        "searchTerm": "ejection fraction of 45%",
                        "searchTermOccurrence": 1
                    },
                    "data": [
                        {
                            "title": "Imaging",
                            "date": "06/02/2024",
                            "rows": [
                                {
                                    "key": "Excerpt",
                                    "value": "...Mild decrease in systolic function with an **ejection fraction of 45%**...",
                                    "contentType": "text/markdown"
                                },
                                {
                                    "key": "Document name",
                                    "value": "scan_060223"
                                },
                                {
                                    "key": "Document date",
                                    "value": "06/02/2024"
                                }
                            ]
                        }
                    ]
                }
            ],
            "suggestionDateTime": "2024-06-02 00:00:00",
            "isPrimary": True,
            "billable": True,
            "billableDescendants": [],
            "isOptionalIcd": True,
            "isChosenOptionalIcd": False,
            "diagnosisOptionalIcds": [
                {
                    "icdCode": "I509",
                    "icdDescription": "Heart failure, unspecified",
                    "hccs": {
                        "rx": [
                            {
                                "group": 186,
                                "weight": 0.183
                            }
                        ],
                        "v24": [
                            {
                                "group": 85,
                                "weight": 0.331
                            }
                        ],
                        "v28": [
                            {
                                "group": 226,
                                "weight": 0.36
                            }
                        ]
                    },
                    "hccGroup": 85,
                    "hccWeight": 0.331,
                    "snomedCode": "84114007",
                    "addressedGroup": "RejectedByProvider"
                },
                {
                    "icdCode": "I5022",
                    "icdDescription": "Chronic systolic (congestive) heart failure",
                    "hccs": {
                        "rx": [
                            {
                                "group": 186,
                                "weight": 0.183
                            }
                        ],
                        "v24": [
                            {
                                "group": 85,
                                "weight": 0.331
                            }
                        ],
                        "v28": [
                            {
                                "group": 226,
                                "weight": 0.36
                            }
                        ]
                    },
                    "hccGroup": 85,
                    "hccWeight": 0.331,
                    "snomedCode": "88805009",
                    "addressedGroup": "RejectedByProvider"
                },
                {
                    "icdCode": "I5032",
                    "icdDescription": "Chronic diastolic (congestive) heart failure",
                    "hccs": {
                        "rx": [
                            {
                                "group": 186,
                                "weight": 0.183
                            }
                        ],
                        "v24": [
                            {
                                "group": 85,
                                "weight": 0.331
                            }
                        ],
                        "v28": [
                            {
                                "group": 226,
                                "weight": 0.36
                            }
                        ]
                    },
                    "hccGroup": 85,
                    "hccWeight": 0.331,
                    "snomedCode": "42343007",
                    "addressedGroup": "RejectedByProvider"
                },
                {
                    "icdCode": "I5042",
                    "icdDescription": "Chronic combined systolic (congestive) and diastolic (congestive) heart failure",
                    "hccs": {
                        "rx": [
                            {
                                "group": 186,
                                "weight": 0.183
                            }
                        ],
                        "v24": [
                            {
                                "group": 85,
                                "weight": 0.331
                            }
                        ],
                        "v28": [
                            {
                                "group": 226,
                                "weight": 0.36
                            }
                        ]
                    },
                    "hccGroup": 85,
                    "hccWeight": 0.331,
                    "snomedCode": "42343007",
                    "addressedGroup": "RejectedByProvider"
                }
            ],
            "confidenceLabel": "Suspect",
            "isBillableSubDx": False,
            "dxId": "heart_failure",
            "dxDescription": "Heart failure",
            "addedInPostVisit": False,
            "statusUpdatedAt": "2024-07-22T18:20:47.730Z",
            "statusUpdatedBy": "961e602d-cda0-4797-918d-6decaeccee2a",
            "statusUpdatedByName": "Demo Navina",
            "actionUsername": "Demo Navina",
            "addressedGroup": "RejectedByProvider",
            "companionAddressedGroup": None,
            "status": "previously_rejected_provider",
            "type": "recommendation",
            "isValid": True,
            "lastCoderStatus": None,
            "lastCoderStatusUpdatedAt": None,
            "lastCoderStatusUpdatedBy": None,
            "lastCoderStatusUpdatedByName": None,
            "lastProviderStatus": "rejected_provider",
            "lastProviderStatusUpdatedAt": "2024-07-22T18:20:47.730Z",
            "lastProviderStatusUpdatedBy": "961e602d-cda0-4797-918d-6decaeccee2a",
            "lastProviderStatusUpdatedByName": "Demo Navina",
            "coderStatus": None,
            "coderStatusUpdatedAt": None,
            "coderStatusUpdatedBy": None,
            "isCoderStatusFromCurrentSid": False,
            "providerStatus": None,
            "providerStatusUpdatedAt": None,
            "providerStatusUpdatedBy": None,
            "isProviderStatusFromCurrentSid": False,
            "statusUpdatedTimestamp": 1721672447,
            "statusAddedTimestamp": 1721672435,
            "companionOrder": 0,
            "companionDxs": [],
            "primaryDx": None,
            "isNavinaCoupledSuggestion": False,
            "isCoupledSuggestion": False,
            "companionId": None,
            "noteData": {
                "text": "",
                "authorId": "961e602d-cda0-4797-918d-6decaeccee2a",
                "authorName": "Demo Navina",
                "authorType": "Admin",
                "shouldPush": False,
                "noteDate": "2024-07-03T12:09:37.518Z",
                "addedInPostVisit": False
            },
            "isSyncedFromEmr": False,
            "actionsHistory": [],
            "invalidOverride": False,
            "overrideFilter": None,
            "sourceData": {
                "type": "recommendation",
                "extra": {
                    "agilon": [],
                    "claimCms": [],
                    "consults": [],
                    "hieEncounters": [],
                    "inferred": [],
                    "imagingInferred": [
                        {
                            "diagnosisOptionalIcds": [
                                {
                                    "hccGroup": "85",
                                    "hccWeight": 0.331,
                                    "icdCode": "I509",
                                    "icdDescription": "Heart failure, unspecified",
                                    "snomedCode": "84114007"
                                },
                                {
                                    "hccGroup": "85",
                                    "hccWeight": 0.331,
                                    "icdCode": "I5022",
                                    "icdDescription": "Chronic systolic (congestive) heart failure",
                                    "snomedCode": "88805009"
                                },
                                {
                                    "hccGroup": "85",
                                    "hccWeight": 0.331,
                                    "icdCode": "I5032",
                                    "icdDescription": "Chronic diastolic (congestive) heart failure",
                                    "snomedCode": "42343007"
                                },
                                {
                                    "hccGroup": "85",
                                    "hccWeight": 0.331,
                                    "icdCode": "I5042",
                                    "icdDescription": "Chronic combined systolic (congestive) and diastolic (congestive) heart failure",
                                    "snomedCode": "42343007"
                                }
                            ],
                            "icdCode": "heart_failure",
                            "icdDescription": "Heart failure",
                            "icd10CodeLineContent": "ejection fraction of 45%",
                            "lineContentOccurrenceInDoc": 1,
                            "matchWindow": "Mild decrease in systolic function with an ejection fraction of 45%",
                            "snomedCode": None,
                            "snomedDescription": None,
                            "fileId": "624a2a38-b450-404b-a568-4be8251a670e",
                            "fileDate": "2024-06-02",
                            "fileLoincName": "scan_060223"
                        }
                    ],
                    "plGap": [],
                    "rafGap": []
                },
                "diagnosisSources": [
                    {
                        "sourceName": "Imaging",
                        "type": "imaging_inferred",
                        "date": "06/02/2024",
                        "document": {
                            "name": "scan_060223",
                            "id": "624a2a38-b450-404b-a568-4be8251a670e",
                            "date": "06/02/2024",
                            "searchTerm": "ejection fraction of 45%",
                            "searchTermOccurrence": 1
                        },
                        "data": [
                            {
                                "title": "Imaging",
                                "date": "06/02/2024",
                                "rows": [
                                    {
                                        "key": "Excerpt",
                                        "value": "...Mild decrease in systolic function with an **ejection fraction of 45%**...",
                                        "contentType": "text/markdown"
                                    },
                                    {
                                        "key": "Document name",
                                        "value": "scan_060223"
                                    },
                                    {
                                        "key": "Document date",
                                        "value": "06/02/2024"
                                    }
                                ]
                            }
                        ]
                    }
                ]
            },
            "numberOfSources": 1,
            "dataFromAction": False,
            "diagnosisAction": {
                "reason": {
                    "id": 1,
                    "freeText": None,
                    "title": "Condition resolved",
                    "description": "This is no longer an active problem (including remission)"
                },
                "status": "Rejected",
                "detailedStatus": "previously_rejected_provider",
                "note": {
                    "display": False
                },
                "performed": {
                    "byId": "961e602d-cda0-4797-918d-6decaeccee2a",
                    "byUserName": "Demo Navina",
                    "atIsoDatetime": "2024-07-22T18:20:47.730Z"
                }
            },
            "isHint": False,
            "isFromRescheduledAppointment": False,
            "captionInfo": "ignored_coder",
            "notShownInInsightsReason": "RejectedByProvider not shown for provider user",
            "suggestionId": "heart_failure",
            "lowerRelevancyReason": None,
            "hccGroup": 85,
            "hccWeight": 0.331,
            "sid": "dd119322-bcb1-42be-8064-1f4b99076de8",
            "nid": "fcba6f0f-c8cf-4efc-b597-32277cd5255e",
            "navinaProviderId": 12875,
            "view": "provider",
            "dataSourceId": 7,
            "portraitCreatedAt": "2024-03-05 10:52:44",
            "dateOfService": "2024-10-13T02:00:00.000Z"
        }
    ],
    [
        {
            "icdCode": "C3412",
            "icdDescription": "Malignant neoplasm of upper lobe, left bronchus or lung",
            "hccs": {
                "rx": [
                    {
                        "group": 20,
                        "weight": 0.517
                    }
                ],
                "v24": [
                    {
                        "group": 9,
                        "weight": 1.024
                    }
                ],
                "v28": [
                    {
                        "group": 20,
                        "weight": 1.136
                    }
                ]
            },
            "snomedDescription": "Malignant neoplasm of upper lobe, left bronchus or lung",
            "snomedCode": None,
            "sourceData": {
                "type": "manual",
                "extra": {
                    "inserterType": "coder"
                },
                "sourceRole": "coder"
            },
            "reasons": {},
            "diagnosisSources": [],
            "suggestionDateTime": "2024-10-13T14:39:01.376Z",
            "dxId": "C3412",
            "dxDescription": "Malignant neoplasm of upper lobe, left bronchus or lung",
            "addedInPostVisit": False,
            "statusUpdatedAt": "2024-10-13T20:36:20",
            "statusUpdatedBy": "614981e1-4b44-469a-97bb-144d16ec132e",
            "statusUpdatedByName": "Aviv Provider",
            "actionUsername": "Aviv Coder",
            "statusAddedTimestamp": 1728830341,
            "statusUpdatedTimestamp": 1728851780,
            "showInInsights": True,
            "showInCart": False,
            "addressedGroup": "ReAddressed",
            "status": "ignored_provider",
            "billable": True,
            "billableDescendants": [],
            "diagnosisOptionalIcds": [],
            "isBillableSubDx": False,
            "isChosenOptionalIcd": False,
            "isOptionalIcd": False,
            "confidenceLabel": "",
            "numberOfSources": 1,
            "type": "manual",
            "isValid": True,
            "lastCoderStatus": "accepted_coder",
            "lastCoderStatusUpdatedAt": "2024-10-13T14:39:07.095Z",
            "lastCoderStatusUpdatedBy": "0df79952-bceb-4701-992a-604489760156",
            "lastCoderStatusUpdatedByName": "Aviv Coder",
            "lastProviderStatus": "ignored_provider",
            "lastProviderStatusUpdatedAt": "2024-10-13T20:36:20.636Z",
            "lastProviderStatusUpdatedBy": "614981e1-4b44-469a-97bb-144d16ec132e",
            "lastProviderStatusUpdatedByName": "Aviv Provider",
            "coderStatus": "accepted_coder",
            "coderStatusUpdatedAt": "2024-10-13T14:39:07.095Z",
            "coderStatusUpdatedBy": "0df79952-bceb-4701-992a-604489760156",
            "isCoderStatusFromCurrentSid": True,
            "providerStatus": "ignored_provider",
            "providerStatusUpdatedAt": "2024-10-13T20:36:20.636Z",
            "providerStatusUpdatedBy": "614981e1-4b44-469a-97bb-144d16ec132e",
            "isProviderStatusFromCurrentSid": True,
            "noteData": {
                "text": "test",
                "authorName": "Aviv Coder",
                "authorType": None,
                "noteDate": "2024-10-09T11:37:14.516Z",
                "shouldPush": True,
                "addedInPostVisit": False
            },
            "isSyncedFromEmr": False,
            "companionOrder": 0,
            "isCoupledSuggestion": False,
            "isPrimary": True,
            "companionAddressedGroup": None,
            "isNavinaCoupledSuggestion": False,
            "companionId": None,
            "actionsHistory": [],
            "invalidOverride": False,
            "overrideFilter": None,
            "diagnosisAction": {
                "reason": "NO_REASON",
                "status": "Untouched",
                "detailedStatus": "ignored_provider",
                "note": {
                    "display": False
                },
                "performed": {
                    "byId": "614981e1-4b44-469a-97bb-144d16ec132e",
                    "byUserName": "Aviv Provider",
                    "atIsoDatetime": "2024-10-13T20:36:20.636Z"
                }
            },
            "isHint": True,
            "suggestionId": "C3412",
            "lowerRelevancyReason": None,
            "hccGroup": 9,
            "hccWeight": 1.024,
            "sid": "dd119322-bcb1-42be-8064-1f4b99076de8",
            "nid": "fcba6f0f-c8cf-4efc-b597-32277cd5255e",
            "navinaProviderId": 12875,
            "view": "provider",
            "dataSourceId": 7,
            "portraitCreatedAt": "2024-03-05 10:52:44",
            "dateOfService": "2024-10-13T02:00:00.000Z"
        }
    ],
    [
        {
            "icdCode": "I739",
            "icdDescription": "Peripheral vascular disease, unspecified",
            "hccs": {
                "rx": [],
                "v24": [
                    {
                        "group": 108,
                        "weight": 0.288
                    }
                ],
                "v28": []
            },
            "snomedDescription": "Peripheral vascular disease, unspecified",
            "snomedCode": None,
            "sourceData": {
                "type": "manual",
                "extra": {
                    "inserterType": "coder"
                },
                "sourceRole": "coder"
            },
            "reasons": {},
            "diagnosisSources": [],
            "suggestionDateTime": "2024-09-10T18:09:38.475Z",
            "dxId": "I739",
            "dxDescription": "Peripheral vascular disease, unspecified",
            "addedInPostVisit": False,
            "statusUpdatedAt": "2024-09-10T18:19:43",
            "statusUpdatedBy": "ed875045-6769-4e41-85ff-4dab7f271386",
            "statusUpdatedByName": "jordan.crumpler@navina.ai",
            "actionUsername": "Jordan crumpler",
            "statusAddedTimestamp": 1725991778,
            "statusUpdatedTimestamp": 1725992382,
            "showInInsights": True,
            "showInCart": False,
            "addressedGroup": "NewHCCGroup",
            "status": "ignored_coder",
            "billable": True,
            "billableDescendants": [],
            "diagnosisOptionalIcds": [],
            "isBillableSubDx": False,
            "isChosenOptionalIcd": False,
            "isOptionalIcd": False,
            "confidenceLabel": "",
            "numberOfSources": 1,
            "type": "manual",
            "isValid": True,
            "lastCoderStatus": "accepted_coder",
            "lastCoderStatusUpdatedAt": "2024-09-10T18:10:04.221Z",
            "lastCoderStatusUpdatedBy": "0355859c-63db-4b02-b3b9-1d7a0200efb0",
            "lastCoderStatusUpdatedByName": "Jordan crumpler",
            "lastProviderStatus": "ignored_provider",
            "lastProviderStatusUpdatedAt": "2024-09-10T18:19:43.390Z",
            "lastProviderStatusUpdatedBy": "ed875045-6769-4e41-85ff-4dab7f271386",
            "lastProviderStatusUpdatedByName": "jordan.crumpler@navina.ai",
            "coderStatus": None,
            "coderStatusUpdatedAt": None,
            "coderStatusUpdatedBy": None,
            "isCoderStatusFromCurrentSid": False,
            "providerStatus": None,
            "providerStatusUpdatedAt": None,
            "providerStatusUpdatedBy": None,
            "isProviderStatusFromCurrentSid": False,
            "noteData": {
                "text": "Test test",
                "authorName": "Jordan crumpler",
                "authorType": "Coder",
                "noteDate": "2024-09-10T18:09:38.475Z",
                "shouldPush": True,
                "addedInPostVisit": False
            },
            "isSyncedFromEmr": False,
            "companionOrder": 0,
            "isCoupledSuggestion": False,
            "isPrimary": True,
            "companionAddressedGroup": None,
            "isNavinaCoupledSuggestion": False,
            "companionId": None,
            "actionsHistory": [],
            "invalidOverride": False,
            "overrideFilter": None,
            "isManualFromPreviousAppointments": True,
            "diagnosisAction": {
                "reason": "NO_REASON",
                "status": "Untouched",
                "detailedStatus": "ignored_provider",
                "note": {
                    "display": False
                },
                "performed": {
                    "byId": "ed875045-6769-4e41-85ff-4dab7f271386",
                    "byUserName": "jordan.crumpler@navina.ai",
                    "atIsoDatetime": "2024-09-10T18:19:43.390Z"
                }
            },
            "isHint": True,
            "isFromRescheduledAppointment": False,
            "suggestionId": "I739",
            "lowerRelevancyReason": None,
            "hccGroup": 108,
            "hccWeight": 0.288,
            "sid": "dd119322-bcb1-42be-8064-1f4b99076de8",
            "nid": "fcba6f0f-c8cf-4efc-b597-32277cd5255e",
            "navinaProviderId": 12875,
            "view": "provider",
            "dataSourceId": 7,
            "portraitCreatedAt": "2024-03-05 10:52:44",
            "dateOfService": "2024-10-13T02:00:00.000Z"
        }
    ]
]

print(create_evidence_table([dx for dsx in example_json for dx in dsx]))
print(create_diagnoses_table([dx for dsx in example_json for dx in dsx]))
