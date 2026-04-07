import os

MODEL_PATH = os.getenv('MODEL_PATH', 'artifacts/model_data.joblib')

DEFAULT_FEATURE_VALUES = {
    'number_of_dependants': 1,
    'years_at_current_address': 1,
    'zipcode': 1,
    'sanction_amount': 1,
    'processing_fee': 1,
    'gst': 1,
    'net_disbursement': 1,
    'principal_outstanding': 1,
    'bank_balance_at_application': 1,
    'number_of_closed_accounts': 1,
    'enquiry_count': 1
}

CREDIT_SCORE_CONFIG = {
    'base_score': 300,
    'scale_length': 600
}

CREDIT_RATING_THRESHOLDS = {
    'poor': (300, 500),
    'average': (500, 650),
    'good': (650, 750),
    'excellent': (750, 901)
}

RESIDENCE_TYPES = ['Owned', 'Rented', 'Mortgage']
LOAN_PURPOSES = ['Education', 'Home', 'Auto', 'Personal']
LOAN_TYPES = ['Unsecured', 'Secured']

AGE_MIN = 18
AGE_MAX = 100
INCOME_MIN = 0
LOAN_AMOUNT_MIN = 0
LOAN_TENURE_MIN = 0
AVG_DPD_MIN = 0
DELINQUENCY_RATIO_MIN = 0
DELINQUENCY_RATIO_MAX = 100
CREDIT_UTILIZATION_RATIO_MIN = 0
CREDIT_UTILIZATION_RATIO_MAX = 100
NUM_OPEN_ACCOUNTS_MIN = 1
NUM_OPEN_ACCOUNTS_MAX = 4
