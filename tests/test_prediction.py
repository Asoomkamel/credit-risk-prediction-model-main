import pytest
from prediction_helper import predict, prepare_input, get_rating

def test_predict_valid_input():
    probability, credit_score, rating = predict(
        age=28,
        income=1200000,
        loan_amount=2560000,
        loan_tenure_months=36,
        avg_dpd_per_delinquency=20,
        delinquency_ratio=30,
        credit_utilization_ratio=30,
        num_open_accounts=2,
        residence_type='Owned',
        loan_purpose='Home',
        loan_type='Unsecured'
    )
    
    assert 0 <= probability <= 1
    assert 300 <= credit_score <= 900
    assert rating in ['Poor', 'Average', 'Good', 'Excellent']

def test_get_rating():
    assert get_rating(350) == 'Poor'
    assert get_rating(550) == 'Average'
    assert get_rating(700) == 'Good'
    assert get_rating(800) == 'Excellent'

def test_prepare_input_structure():
    df = prepare_input(
        age=28,
        income=1200000,
        loan_amount=2560000,
        loan_tenure_months=36,
        avg_dpd_per_delinquency=20,
        delinquency_ratio=30,
        credit_utilization_ratio=30,
        num_open_accounts=2,
        residence_type='Owned',
        loan_purpose='Home',
        loan_type='Unsecured'
    )
    
    assert df is not None
    assert len(df) == 1
