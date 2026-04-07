import joblib
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import logging
from config import MODEL_PATH, DEFAULT_FEATURE_VALUES, CREDIT_SCORE_CONFIG, CREDIT_RATING_THRESHOLDS

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

_model = None
_scaler = None
_features = None
_cols_to_scale = None

def load_model():
    global _model, _scaler, _features, _cols_to_scale
    
    if _model is not None:
        return _model, _scaler, _features, _cols_to_scale
    
    try:
        model_data = joblib.load(MODEL_PATH)
        _model = model_data['model']
        _scaler = model_data['scaler']
        _features = model_data['features']
        _cols_to_scale = model_data['cols_to_scale']
        logger.info("Model loaded successfully")
        return _model, _scaler, _features, _cols_to_scale
    except FileNotFoundError:
        logger.error(f"Model file not found at {MODEL_PATH}")
        raise
    except KeyError as e:
        logger.error(f"Missing key in model data: {e}")
        raise
    except Exception as e:
        logger.error(f"Error loading model: {e}")
        raise

def prepare_input(age, income, loan_amount, loan_tenure_months, avg_dpd_per_delinquency,
                  delinquency_ratio, credit_utilization_ratio, num_open_accounts, residence_type,
                  loan_purpose, loan_type):
    
    model, scaler, features, cols_to_scale = load_model()
    
    input_data = {
        'age': age,
        'loan_tenure_months': loan_tenure_months,
        'number_of_open_accounts': num_open_accounts,
        'credit_utilization_ratio': credit_utilization_ratio,
        'loan_to_income': loan_amount / income if income > 0 else 0,
        'delinquency_ratio': delinquency_ratio,
        'avg_dpd_per_delinquency': avg_dpd_per_delinquency,
        'residence_type_Owned': 1 if residence_type == 'Owned' else 0,
        'residence_type_Rented': 1 if residence_type == 'Rented' else 0,
        'loan_purpose_Education': 1 if loan_purpose == 'Education' else 0,
        'loan_purpose_Home': 1 if loan_purpose == 'Home' else 0,
        'loan_purpose_Personal': 1 if loan_purpose == 'Personal' else 0,
        'loan_type_Unsecured': 1 if loan_type == 'Unsecured' else 0,
    }
    
    input_data.update(DEFAULT_FEATURE_VALUES)
    
    df = pd.DataFrame([input_data])
    df[cols_to_scale] = scaler.transform(df[cols_to_scale])
    df = df[features]
    
    return df

def predict(age, income, loan_amount, loan_tenure_months, avg_dpd_per_delinquency,
            delinquency_ratio, credit_utilization_ratio, num_open_accounts,
            residence_type, loan_purpose, loan_type):
    
    input_df = prepare_input(age, income, loan_amount, loan_tenure_months, avg_dpd_per_delinquency,
                             delinquency_ratio, credit_utilization_ratio, num_open_accounts, residence_type,
                             loan_purpose, loan_type)
    
    probability, credit_score, rating = calculate_credit_score(input_df)
    
    return probability, credit_score, rating

def calculate_credit_score(input_df):
    model, _, _, _ = load_model()
    
    base_score = CREDIT_SCORE_CONFIG['base_score']
    scale_length = CREDIT_SCORE_CONFIG['scale_length']
    
    x = np.dot(input_df.values, model.coef_.T) + model.intercept_
    default_probability = 1 / (1 + np.exp(-x))
    non_default_probability = 1 - default_probability
    credit_score = base_score + non_default_probability.flatten() * scale_length
    
    rating = get_rating(credit_score[0])
    
    return default_probability.flatten()[0], int(credit_score[0]), rating

def get_rating(score):
    for rating_name, (min_score, max_score) in CREDIT_RATING_THRESHOLDS.items():
        if min_score <= score < max_score:
            return rating_name.capitalize()
    return 'Undefined'
