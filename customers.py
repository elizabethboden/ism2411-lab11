# customers.py
# Author: Elizabeth Boden
# Module 11 Lab

# --- Exercise 1: One Customer ---
print("--- Exercise 1: One Customer ---")

customer = { 
    "name": "Alice",
    "email": "alice@example.com",
    "tier": "gold",
    "ytd_spend": 12400
}

print("Name:", customer["name"])
print("Email:", customer["email"])
print("Tier:", customer["tier"])
print("YTD Spend:", customer["ytd_spend"])

print(customer)

# --- Exercise 2: Update and add ---
print("--- Exercise 2: Update and add ---")
customer["phone"] = "815-555-0412"

print(customer)
customer["tier"] = "platinum"

print(customer)
del customer["email"]

print(customer)

print(customer.get("email", "Email not found"))

# --- Exercise 3 ---
print("--- Exercise 3 ---")

print(customer.get("email", "no email on file"))

try: 
    print(customer["email"])
except KeyError as error:
    print(f"KeyError Caught: {error}")

# --- Exercise 4 ---
print("--- Exercise 4 ---")
for key, value in customer.items():
    print(f"{key} : {value}")

for item in customer: 
    print(item)

