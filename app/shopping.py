import os
from datetime import datetime
from pandas import read_csv


def format_usd(my_price):
    """

    Formats a number as USD with dollar sign and two decimals (and also thousands separator)

    Params my_price is a number (int or float) that we want to format the

    Examples: format_usd(10)

    """

    return f"${my_price:,.2f}"


def lookup_product(product_id, all_products):
    """
    Params :

    product_id (str) like "8"

    all_products (list of dict) each dict should have "id", "name", "department", "aisle", and "price" attributes

    """
    matching_products = [p for p in all_products if str(p["id"]) == str(product_id)]
    if any(matching_products):
        return matching_products[0]
    else:
        return None


# PREVENT ALL THE APP CODE FROM BEING IMPORTED
# BUT STILL BE ABLE TO RUN IT FROM THE COMMAND LINE LIKE THIS...

if __name__ == "__main__":

    # READ INVENTORY OF PRODUCTS

    products_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "products.csv")
    products_df = read_csv(products_filepath)
    products = products_df.to_dict("records")
    
    #CAPTURE PRODUCT SELECTIONS

    selected_products = []
    while True:
        selected_id = input("Please select a product identifier: ")
        if selected_id.upper() == "DONE":
            break
    else:
        matching_product = lookup_product(selected_id, products)
        if matching_product:
            selected_products.append(matching_product)
        else:
            print("OOPS, Couldn't find that product. Please try again.")
    
    checkout_at = datetime.now()

    subtotal = sum([float(p["price"]) for p in selected_products])

    # PRINT RECEIPT

    print("---------")
    print("CHECKOUT AT: " + str(checkout_at.strftime("%Y-%M-%d %H:%m:%S")))
    print("---------")
    for p in selected_products:
        print("SELECTED PRODUCT: " + p["name"] + "   " + format_usd(p["price"]))
        
    print("---------")
    print(f"SUBTOTAL: {format_usd(subtotal)}")
    print(f"TAX: {format_usd(subtotal * 0.0875)}")
    print(f"TOTAL: {format_usd(subtotal * 0.0875 + subtotal)}")
    print("---------")
    print("THANK YOU! PLEASE COME AGAIN SOON!")
    print("---------")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # WRITE RECEIPT TO FILE
    
    receipt_id = checkout_at.strftime('%Y-%M-%d-%H-%m-%S')
    receipt_filepath = os.path.join(os.path.dirname(__file__), "..", "receipts", f"{receipt_id}.txt")
    
    with open(receipt_filepath, "w") as receipt_file:
        receipt_file.write("------------------------------------------")
        for p in selected_products:
            receipt_file.write("\nSELECTED PRODUCT: " + p["name"] + "   " + '${:.0f}'.format(p["price"]))
    
        receipt_file.write("\n---------")
        receipt_file.write(f"\nSUBTOTAL: {subtotal}")
        receipt_file.write(f"\nTAX: {subtotal * 0.875}")
        receipt_file.write(f"\nTOTAL: {((subtotal * 0.875) + subtotal)}")
        receipt_file.write("\n---------")
        receipt_file.write("\nTHANK YOU! PLEASE COME AGAIN SOON!")
        receipt_file.write("\n---------")
