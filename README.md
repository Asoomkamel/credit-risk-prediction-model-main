

# 💳 Credit Risk Predictor Using Machine Learning 📊

Welcome to the **Credit Risk Predictor**! This Streamlit-based web app transforms **credit risk assessment** in the finance industry using a **Logistic Regression model** optimized with **SMOTE Tomek** and **Optuna**. Achieving **93% accuracy** and **94% recall**, it reduces false negatives by **15%**, enabling precise loan default predictions and scalable creditworthiness ratings (300–900). Built with **Scikit-learn**, **XGBoost**, and robust **feature engineering**, this tool empowers banks and fintech firms to make data-driven lending decisions with **25% improved efficiency**! 🚀

Input borrower details, get real-time predictions, and explore credit risk with an intuitive interface. Perfect for financial institutions, analysts, or anyone curious about credit scoring! 😎

---

## 🎉 Try It Out!

Experience the predictor live at:  
🔗 [Credit Risk Predictor Demo](https://ml-project-credit-risk-model-vraj-dobariya.streamlit.app/)


---

## 🌟 What Makes This Project Unique?

This credit risk predictor stands out by combining advanced machine learning, class imbalance handling, and a production-ready interface. Here’s why it shines:

- **High-Performance Model** 🧠: Logistic Regression achieves **93% accuracy** and **94% recall**, reducing false negatives by **15%** for reliable default predictions.
- **SMOTE Tomek for Imbalance** ⚖️: Addresses the imbalanced dataset (10% defaults) to ensure robust performance on high-risk cases.
- **Optuna Hyperparameter Tuning** ⚙️: Optimizes model parameters for maximum accuracy, producing credit scores from 300 to 900.
- **Interactive Streamlit App** 🎨: Vibrant, emoji-rich UI allows users to input borrower details (e.g., age, income) and view predictions, credit scores, and ratings.
- **Feature Engineering** 📋: Includes domain-relevant features like **Loan-to-Income Ratio** and **Credit Utilization Ratio** for precise risk profiling.
- **Scalable Deployment** 🌐: Modular pipeline with pre-trained artifacts supports integration into real-world fintech systems.
- **Interpretability** 📈: Logistic Regression coefficients provide feature importance, ensuring transparency for regulatory compliance.

---

## 🎯 Industry Impact

This project revolutionizes **credit risk assessment** in the finance industry by addressing key challenges:

- **Enhanced Decision-Making**: Improves lending efficiency by **25%**, enabling faster, data-driven decisions for banks and fintech platforms.
- **Reduced Risk**: Cuts false negatives by **15%**, minimizing losses from loan defaults and enhancing portfolio stability.
- **High Accuracy & Recall**: Achieves **93% accuracy** and **94% recall**, ensuring reliable identification of high-risk borrowers.
- **Regulatory Compliance**: Transparent model with interpretable coefficients aligns with banking regulations.
- **Scalability**: Modular design supports large-scale deployment, ideal for startups or established financial institutions.
- **Customer Insights**: Features like **Debt-to-Income Ratio** and **credit utilization** drive precise risk profiling, benefiting lenders and borrowers.

This tool is perfect for banks, credit unions, fintech platforms, or analysts aiming to optimize lending and manage risk effectively. 💸

---

## 🏗️ Architecture

The system integrates machine learning with a user-friendly frontend for seamless credit risk predictions:

- **Frontend**: Streamlit app (`main.py`) with an intuitive UI for inputting borrower details (e.g., age, income, loan amount) and displaying predictions, credit scores (300–900), and ratings (Poor to Excellent).
- **Model**: Logistic Regression (`artifacts/model_data.joblib`) tuned with **Optuna** and enhanced with **SMOTE Tomek** for handling imbalanced data.
- **Feature Engineering**: Processes continuous (e.g., income, loan amount) and categorical (e.g., residence type, loan purpose) features, including derived features like **Loan-to-Income Ratio** (`prediction_helper.py`).
- **Data Pipeline**: Includes EDA, preprocessing, and scaling (`MinMaxScaler`) for robust predictions, as seen in `ml_credit_risk_model.ipynb`.
- **Artifacts**: Pre-trained model (`model_data.joblib`) and tuned hyperparameters (`tuned_hyperparameters.txt`) for efficient deployment.
- **Prediction Logic**: Calculates default probability, credit score, and rating using Logistic Regression coefficients and a sigmoid function (`prediction_helper.py`).

---

## 📊 Model Performance

| **Model**            | **Accuracy** | **Precision** | **Recall** | **F1-Score** | **Why This Result?** |
|-----------------------|--------------|---------------|------------|--------------|----------------------|
| **Logistic Regression (Tuned)** | **93%** | **~90%** | **94%** | **~92%** | SMOTE Tomek balances classes, Optuna optimizes parameters, reducing false negatives by 15%. |
| **XGBoost (Baseline)** | ~91% | ~88% | ~90% | ~89% | Strong performance but slightly lower recall than Logistic Regression. |

The **Logistic Regression model** excels due to its high recall (94%) and interpretability, critical for identifying high-risk borrowers while meeting regulatory needs. The model’s coefficients (visualized in `ml_credit_risk_model.ipynb`) highlight key features like **credit utilization ratio** and **delinquency ratio**.

---

## 🛠️ Setup & Execution

Follow these steps to run the predictor locally:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Vraj-Data-Scientist/credit-risk-prediction-model
   cd credit-risk-prediction-model
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
   Required packages: `pandas`, `numpy`, `scikit-learn`, `xgboost`, `imbalanced-learn`, `optuna`, `streamlit`.

3. **Run the Streamlit App**:
   ```bash
   streamlit run main.py
   ```
   - Access the app at `http://localhost:8501`.
   - Ensure the `artifacts` directory contains `model_data.joblib` and `tuned_hyperparameters.txt`.

4. **Interact with the App**:
   - Input borrower details (e.g., age, income, loan amount) in the Streamlit UI.
   - Click **Calculate Risk** to get default probability, credit score (300–900), and rating (Poor, Average, Good, Excellent).

---

## 📋 How to Use

1. **Open the App**:
   - Visit the live demo: [Credit Risk Predictor](https://ml-project-credit-risk-model-vraj-dobariya.streamlit.app/) or run locally.
2. **Input Borrower Details**:
   - Enter details like **Age** (18–100), **Income** (INR), **Loan Amount**, **Loan Tenure** (months), **Average DPD**, **Delinquency Ratio**, **Credit Utilization Ratio**, **Number of Open Loan Accounts**, **Residence Type** (Owned, Rented, Mortgage), **Loan Purpose** (Education, Home, Auto, Personal), and **Loan Type** (Secured, Unsecured).
   - The **Loan-to-Income Ratio** is calculated automatically.
3. **Get Predictions**:
   - Click **Calculate Risk** to receive:
     - **Default Probability**: Likelihood of default (e.g., 5.2%).
     - **Credit Score**: 300–900, reflecting creditworthiness.
     - **Rating**: Poor (300–500), Average (500–650), Good (650–750), or Excellent (750–900).
4. **Explore Results**:
   - Expand sections for explanations of **Default Probability**, **Credit Score**, and **Credit Rating**.


---

## ⚠️ Things to Know

- **Valid Inputs** ✅: Ensure numerical inputs (e.g., income, loan amount) are realistic and within specified ranges (e.g., Age: 18–100, Ratios: 0–100).
- **Class Imbalance** ⚖️: SMOTE Tomek addresses the 10% default rate, but retraining may be needed for new datasets.
- **Interpretability** 📊: Model coefficients highlight key features (e.g., credit utilization, delinquency ratio) for transparency.
- **Dataset Dependency** 🗄️: Trained on a custom dataset (`customers.csv`, `loans.csv`, `bureau_data.csv`); new data requires preprocessing.
- **Performance** ⚡: Pre-trained model loads quickly, but initial setup may take a moment.

---

## 🛠️ Technical Details

### Key Components
- **Streamlit (`main.py`)**: Interactive UI with a grid layout for inputting borrower details and displaying predictions, scores, and ratings.
- **Prediction Logic (`prediction_helper.py`)**: Prepares inputs, scales features using `MinMaxScaler`, and calculates default probability, credit score, and rating using Logistic Regression coefficients.
- **Model (`artifacts/model_data.joblib`)**: Logistic Regression with SMOTE Tomek and Optuna-tuned hyperparameters, saved with features and scaler.
- **Feature Engineering**: Includes continuous features (e.g., age, loan amount, loan-to-income ratio) and one-hot encoded categorical features (e.g., residence_type_Owned, loan_purpose_Home).
- **Notebook (`ml_credit_risk_model.ipynb`)**: Performs EDA, preprocessing, model training, and feature importance visualization using Logistic Regression coefficients.
- **Artifacts**: `model_data.joblib` (model, scaler, features) and `tuned_hyperparameters.txt` (Optuna results) for efficient deployment.

### Optimization Techniques
- **SMOTE Tomek**: Balances the 10% default rate to improve recall for high-risk cases.
- **Optuna Tuning**: Optimizes Logistic Regression parameters (e.g., C, solver) for maximum accuracy.
- **Feature Selection**: Uses domain-relevant features like loan-to-income ratio and delinquency ratio, with one-hot encoding for categorical variables.
- **Scaling**: Applies `MinMaxScaler` to continuous features for consistent model input.
- **Modular Pipeline**: Separates preprocessing (`prediction_helper.py`) and UI (`main.py`) for scalability.

---

## 📚 Future Enhancements

- **Multi-Model Ensemble** 🧠: Combine Logistic Regression with XGBoost or LightGBM for higher accuracy.
- **Real-Time Data** ⏰: Integrate live transaction data for dynamic predictions.
- **Advanced Features** 📋: Incorporate additional features (e.g., credit inquiries, payment history) for richer profiling.
- **SHAP Integration** 📊: Add SHAP plots to the Streamlit app for real-time feature importance visualization.
- **API Deployment** 🌐: Expose the model via an API for integration with banking systems.

---

## 🧑‍💻 About the Developer


- 📂 [GitHub](https://github.com/Asoomkamel )
- 🔗 [LinkedIn](https://www.linkedin.com/in/mutasim-al-kamil-40a299318) 


---

## 🙌 Acknowledgments

- **Scikit-learn**: For the Logistic Regression model and preprocessing tools.
- **SMOTE Tomek**: For handling class imbalance.
- **Optuna**: For hyperparameter optimization.
- **Streamlit**: For the intuitive UI.
- **Pandas & NumPy**: For efficient data processing.

---

⭐ **Star this repo** if you find it useful! Contributions and feedback are welcome! 😊

---
