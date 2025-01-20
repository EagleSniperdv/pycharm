import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

# Load the dataset
file_path = "questionnaire_responses.csv"
df = pd.read_csv(file_path)

# Preview the dataset
print(df.head())

# Data Preprocessing
# Rename columns for simplicity
df.rename(columns=lambda x: x.strip().replace(" ", "_").lower(), inplace=True)

# Handle missing values if any
df.fillna(df.mean(), inplace=True)

# Convert categorical variables (like gender, age, etc.) to numeric
categorical_columns = ['gender', 'age', 'education_level', 'work_experience']
df = pd.get_dummies(df, columns=categorical_columns, drop_first=True)

# Dependent and independent variables for regression
variables = {
    "innovation": [
        "each_coop_bank_branch_has_an_automated_teller_machine_(atm)",
        "many_customers_prefer_to_withdraw_money_from_an_atm_as_opposed_to_counter_withdrawals",
        "many_customers_use_internet_banking",
        "the_branch_has_many_coop_bank_agents_(coop_kwa_jirani)"
    ],
    "product_development": [
        "the_bank_always_comes_up_with_new_products_into_the_market",
        "the_new_products_in_the_market_are_always_well_received_by_the_customers",
        "customers_are_fully_conversant_with_the_new_products_offered_by_the_bank"
    ],
    "corporate_banking": [
        "the_cooperative_bank_of_kenya_serves_both_retail_and_corporate_customers",
        "many_corporate_customers_prefer_coop_banks_to_other_competitors",
        "the_bank_provides_credit_facilities_to_many_corporate_customers"
    ],
    "capital_base": [
        "the_bank_has_a_large_capital_base_that_greatly_contributes_to_its_profitability",
        "the_bank_acquired_part_of_its_large_capital_base_from_an_initial_public_offer_(ipo)",
        "the_bank_keeps_part_of_its_net_profit_as_retained_earnings"
    ]
}

# Perform regression for each objective
results = {}
for key, features in variables.items():
    # Prepare data
    X = df[features]
    y = df['competitive_advantage_score']  # Example dependent variable
    
    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train model
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    # Predictions and evaluation
    y_pred = model.predict(X_test)
    r2 = r2_score(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    results[key] = {"R2_Score": r2, "MSE": mse}
    
    # Print summary
    print(f"Regression Analysis for {key.replace('_', ' ').capitalize()}:")
    print(f"R2 Score: {r2:.2f}")
    print(f"Mean Squared Error: {mse:.2f}\n")

# Visualization
# Correlation heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Matrix")
plt.show()

# Distribution of Competitive Advantage Scores
plt.figure(figsize=(8, 5))
sns.histplot(df['competitive_advantage_score'], kde=True, bins=20, color="blue")
plt.title("Distribution of Competitive Advantage Scores")
plt.xlabel("Competitive Advantage Score")
plt.ylabel("Frequency")
plt.show()

# Pairplot for Innovation
sns.pairplot(df[variables["innovation"] + ['competitive_advantage_score']])
plt.suptitle("Pairplot for Innovation Variables and Competitive Advantage", y=1.02)
plt.show()

# Bar plot for regression coefficients (example for one category)
coefficients = pd.DataFrame(model.coef_, index=X.columns, columns=["Coefficient"])
coefficients.sort_values(by="Coefficient", ascending=False).plot(kind="bar", figsize=(10, 6))
plt.title("Feature Importance for Innovation")
plt.ylabel("Coefficient Value")
plt.show()
