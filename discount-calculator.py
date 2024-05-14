price = float(input("Enter your product price: "))
discount_percentage = int(input("Enter your discount percentage (0-100: )"))

if discount_percentage >= 0 and discount_percentage <= 100:
    discount_amount = price * (discount_percentage / 100)
    final_price = price - discount_amount
    print("Final price Width ", discount_percentage, " % discount: ", final_price)
else:
    print("Invalid discount percentage. Please a value between 0 and 100 ")