def calculate_discount(price, customer_type):
    if customer_type == "Regular":
        discount = price * 0.05
        print("Regular Customer: 5% discount applied")
    elif customer_type == "Premium":
        discount = price * 0.15
        print("Premium Customer: 15% discount applied")
    elif customer_type == "Employee":
        discount = price * 0.25
        print("Employee Customer: 25% discount applied")
    else:
        discount = 0
        print("No discount applied: Invalid customer type")

    final_price = price - discount
    return final_price


price = float(input("Enter product price: "))
customer_type = input("Enter customer type (Regular / Premium / Employee): ")

result = calculate_discount(price, customer_type)
print("Final Price after Discount:", result)