# Week Three Assignment
  
# Question  1  
    
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        total_price = price - discount_amount
        return total_price
    else:
        return price

# Question 2
price = float(input("Enter the item price: "))
discount_percent = float(input("Enter the discount percentage: "))
total_price = calculate_discount(price, discount_percent)
print("The discounted total price is: ", total_price)

