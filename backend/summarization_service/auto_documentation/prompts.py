# Prompts
BATCH_LABS_ASSIGNMENT_PROMPT = """
You are a medical assistant tasked with identifying relevant lab results for multiple medical conditions.
For each condition, identify which lab results are relevant for assessing that condition.
Only include labs that are truly relevant for each specific condition - do not include labs just because they might be generally useful.
If no labs are relevant for a condition, return "none" for that condition.

Conditions:
{conditions}

Available Labs:
{labs}

For each condition index, output all relevant lab indices.

Be strict about relevance - only include labs that are directly related to assessing or monitoring the specific condition.
"""

BATCH_MEDS_ASSIGNMENT_PROMPT = """
You are a medical assistant tasked with identifying relevant medications for multiple medical conditions.
For each condition, identify which medications are typically used to treat that condition.
Only include medications that are commonly used for each specific condition - do not include medications just because they might be generally useful.
If no medications are relevant for a condition, return "none" for that condition.

Conditions:
{conditions}

Available Medications:
{medications}

For each condition index, output all relevant medication indices.

Be strict about relevance - only include medications that are directly related to treating the specific condition.
Consider both medication names and ATC codes (level2 and level5) in your assessment.
"""

CONDITION_ASSESSMENT_PROMPT = """
You are a medical assistant creating a brief condition assessment based on available evidence.
Create a concise assessment for the specific condition using ONLY the provided information.
Do not make assumptions or add information not present in the provided data.

Condition: {condition}
ICD Code: {icd_code}

Evidence:
{evidences}

Relevant Labs:
{relevant_labs}

Relevant Medications:
{relevant_meds}

Family History:
{family_history}

Social History:
{social_history}

Create a single paragraph assessment (2-3 sentences maximum) that summarizes the current state of this condition based solely on the provided information.
Focus only on objective findings and documented evidence.
Do not repeat condition name or code.
State findings dates (month and year) when available.
State medication dosages and frequencies when available.
If insufficient information is available return "Insufficient information to assess this condition."
"""
