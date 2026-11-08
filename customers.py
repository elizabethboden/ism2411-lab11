# customers.py
# Author: Elizabeth Boden
# Module 11 Lab

# 1. I would use .get() when I am not sure if a key exists because it
# gives me the option of a default value instead of causing a KeyError. I
# would use [] when I know that the key exists and I want to access its value.

# 2. Exercise 8 reminds me of SUMIF in Excel because it adds numbers based 
# on categories. Python is more useful for large datasets because it can 
# automatically organize and calculate information much faster. 

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

# --- Exercise 5 ---
print("--- Exercise 5 ---")
tier_discounts = {"bronze": 0,
                  "silver": 0.05,
                  "gold": 0.1,
                  "platinum": 0.15}
purchase = 200
discount_rate = tier_discounts.get(customer["tier"], 0)
final_price = purchase * (1 - discount_rate)

print(f"Tier: {customer['tier']}")
print(f"Discount Rate: {discount_rate * 100:.2f}%")
print(f"Final Price: ${final_price:.2f}")

# --- Exercise 6 ---
print("--- Exercise 6 ---")
customers = [

    {"name": "Bob", "tier": "silver", "ytd_spend": 3200},
    {"name": "Carol", "tier": "gold", "ytd_spend": 8750},
    {"name": "David", "tier": "bronze", "ytd_spend": 450}
]

for record in customers: 
    rate = tier_discounts.get(record["tier"], 0)
    discount = 300 * rate
    print(f"{record['name']} ({record['tier']}): ${discount:.2f} discount on $300 purchase")

# --- Exercise 7 ---
print("--- Exercise 7 ---")
catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8},
}

for product, details in catalog.items():
    if details["stock"] < 20:
        print(f"LOW STOCK: {product} - only {details['stock']} left in stock!")

# --- Exercise 8 ---
print("--- Exercise 8 ---")
transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200},    
]
sales_by_region = {}
for sale in transactions:
    region = sale["region"]
    sales_by_region[region] = sales_by_region.get(region, 0) + sale["amount"]
print(sales_by_region)

for region in sorted(sales_by_region): 
    print(f"{region}: ${sales_by_region[region]}")


