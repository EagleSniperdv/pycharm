import csv
import random

# Define the options for each section
personal_info = {
    "Gender": ["Male", "Female"],
    "Age": ["18 to 25", "26 to 30", "31 to 35", "36 to 40", "Over 40"],
    "Education Level": ["O level/A level", "Diploma", "Degree", "Masters", "PHD", "Other"],
    "Work Experience": ["Below 2", "2 to 5", "6 to 10", "Over 10"]
}

responses = {
    "Product Development": ["The bank always comes up with new products into the market.",
                              "The new products in the market are always well received by the customers.",
                              "Customers are fully conversant with the new products offered by the bank.",
                              "The bank has a well worked out program for coming up with new products.",
                              "The bank has a team mandated with identifying market gaps and coming up with new innovative products to fill the gap.",
                              "The bank uses innovative methods in marketing its new products.",
                              "Many customers take on the bank’s new products after being adequately informed about them.",
                              "The bank makes more profits from the new products it introduces."],
    "Innovation": ["Each coop bank branch has an automated teller machine (ATM)",
                   "Many Customers prefer to withdraw money from an ATM as opposed to counter withdrawals",
                   "Many customers use internet banking",
                   "The branch has many Coop bank agents (Coop Kwa Jirani)",
                   "A suitable number of customers use agency banking to do their transactions",
                   "The bank employs adequate security measures to safeguard internet and agency banking",
                   "The bank has credit cards to help serve more customers"],
    "Corporate Banking": ["The Cooperative Bank of Kenya serves both retail and corporate customers.",
                          "Many corporate customers prefer coop banks to other competitors.",
                          "The bank provides credit facilities to many corporate customers.",
                          "The bank provides treasury and cash management services to corporate customers.",
                          "The bank supports business ventures by corporate customers.",
                          "Coop bank has invested in real estate management.",
                          "A suitable percentage of the bank's profit margins comes from corporate banking.",
                          "Corporate banking has led to a competitive advantage of the bank over other competitors."],
    "Capital Base": ["The bank has a large capital base that greatly contributes to its profitability.",
                     "The bank acquired part of its large capital base from an Initial Public Offer (IPO)",
                     "The bank keeps part of its net profit as retained earnings.",
                     "Shareholders are given dividends every financial year.",
                     "The bank sells bonds to improve its capital base.",
                     "The bank always ensures that its assets are more than its liabilities.",
                     "A large capital base improves the profitability of the bank.",
                     "A large capital base has led to the bank's competitive advantage in the industry."]
}

# Generate random responses for 1000 participants
data = []

for _ in range(1000):
    entry = {
        "Gender": random.choice(personal_info["Gender"]),
        "Age": random.choice(personal_info["Age"]),
        "Education Level": random.choice(personal_info["Education Level"]),
        "Work Experience": random.choice(personal_info["Work Experience"])
    }
    
    for section, questions in responses.items():
        for question in questions:
            entry[question] = random.randint(1, 5)

    data.append(entry)

# Write data to CSV file
output_file = "questionnaire_responses.csv"

with open(output_file, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=data[0].keys())
    writer.writeheader()
    writer.writerows(data)

print(f"Questionnaire responses for 1000 participants have been written to '{output_file}'.")
