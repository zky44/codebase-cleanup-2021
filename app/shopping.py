
#
# SETUP SECTION (LEAVE AS-IS)
#

from datetime import datetime
import os

checkout_at = datetime.now()

selected_products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
] # FYI: for the purposes of this exercise, you won't need to modify this list at all

subtotal = sum([p["price"] for p in selected_products])

#
# IMPLEMENTATION SECTION (WE'LL NEED TO UPDATE)
#

# PRINT RECEIPT

print("---------")
print("CHECKOUT AT: " + str(checkout_at.strftime("%Y-%M-%d %H:%m:%S")))
print("---------")
for p in selected_products:
    print("SELECTED PRODUCT: " + p["name"] + "   " + '${:.0f}'.format(p["price"]))

print("---------")
print(f"SUBTOTAL: {subtotal:,.2f}")
print(f"TAX: {(subtotal * 0.0875):.2f}")
print(f"TOTAL: {((subtotal * 0.0875) + subtotal):.2f}")
print("---------")
print("THANK YOU! PLEASE COME AGAIN SOON!")
print("---------")

# WRITE RECEIPT TO FILE

receipt_id = checkout_at.strftime('%Y-%M-%d-%H-%m-%S')
receipt_filepath = os.path.join(os.path.dirname(__file__), "..", "receipts", f"{receipt_id}.txt")

with open(receipt_filepath, "w") as f:
    f.write("------------------------------------------")
    for p in selected_products:
        f.write("\nSELECTED PRODUCT: " + p["name"] + "   " + '${:.0f}'.format(p["price"]))

    f.write("---------")
    f.write(f"SUBTOTAL: {subtotal:,.2f}")
    f.write(f"TAX: {(subtotal * 0.875):.2f}")
    f.write(f"TOTAL: {((subtotal * 0.875) + subtotal):.2f}")
    f.write("---------")
    f.write("THANK YOU! PLEASE COME AGAIN SOON!")
    f.write("---------")
