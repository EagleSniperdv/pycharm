import csv
import random

# Define the options for each section
personal_info = {
    "Gender": ["Male", "Female"],
    "Age": ["18 to 25", "26 to 30", "31 to 35", "36 to 40", "Over 40"],
    "Education Level": ["O level/A level", "Diploma", "Degree", "Masters", "PHD", "Other"],
    "Work Experience": ["Below 2", "2 to 5", "6 to 10", "Over 10"]
}

# Improved responses structure: Adjusting the responses to reflect more realistic and varied inputs
responses = {
    "Product Development": [
        "The bank always comes up with new products into the market.",
        "The new products in the market are always well received by the customers.",
        "Customers are fully conversant with the new products offered by the bank.",
        "The bank has a well worked out program for coming up with new products.",
        "The bank has a team mandated with identifying market gaps and coming up with new innovative products to fill the gap.",
        "The bank uses innovative methods in marketing its new products.",
        "Many customers take on the bank’s new products after being adequately informed about them.",
        "The bank makes more profits from the new products it introduces."
    ],
    "Innovation": [
        "Each coop bank branch has an automated teller machine (ATM)",
        "Many customers prefer to withdraw money from an ATM as opposed to counter withdrawals",
        "Many customers use internet banking",
        "The branch has many Coop bank agents (Coop Kwa Jirani)",
        "A suitable number of customers use agency banking to do their transactions",
        "The bank employs adequate security measures to safeguard internet and agency banking",
        "The bank has credit cards to help serve more customers"
    ],
    "Corporate Banking": [
        "The Cooperative Bank of Kenya serves both retail and corporate customers.",
        "Many corporate customers prefer coop banks to other competitors.",
        "The bank provides credit facilities to many corporate customers.",
        "The bank provides treasury and cash management services to corporate customers.",
        "The bank supports business ventures by corporate customers.",
        "Coop bank has invested in real estate management.",
        "A suitable percentage of the bank's profit margins comes from corporate banking.",
        "Corporate banking has led to a competitive advantage of the bank over other competitors."
    ],
    "Capital Base": [
        "The bank has a large capital base that greatly contributes to its profitability.",
        "The bank acquired part of its large capital base from an Initial Public Offer (IPO)",
        "The bank keeps part of its net profit as retained earnings.",
        "Shareholders are given dividends every financial year.",
        "The bank sells bonds to improve its capital base.",
        "The bank always ensures that its assets are more than its liabilities.",
        "A large capital base improves the profitability of the bank.",
        "A large capital base has led to the bank's competitive advantage in the industry."
    ]
}

# Generate random responses for 1000 participants, ensuring a more balanced and realistic data distribution
data = []

# Generate a balance in demographic characteristics
for _ in range(1000):
    entry = {
        "Gender": random.choice(personal_info["Gender"]),
        "Age": random.choice(personal_info["Age"]),
        "Education Level": random.choice(personal_info["Education Level"]),
        "Work Experience": random.choice(personal_info["Work Experience"])
    }
    
    # Generate more realistic responses by using a weighted choice, making some responses more likely than others
    for section, questions in responses.items():
        for question in questions:
            # Simulate responses with a more realistic distribution, avoiding pure randomness
            # For example, customers may be more likely to give middle-range scores (3-4) for questions
            response = random.choices([1, 2, 3, 4, 5], weights=[5, 15, 40, 30, 10], k=1)[0]
            entry[question] = response

    data.append(entry)

# Write data to CSV file with an appropriate structure
output_file = "improved_questionnaire_responses.csv"

with open(output_file, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=data[0].keys())
    writer.writeheader()
    writer.writerows(data)

print(f"Improved questionnaire responses for 1000 participants have been written to '{output_file}'.")
