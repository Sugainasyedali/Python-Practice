price = float(input("Enter the price"))
discount = int(input("Enter the dicount percentage"))
discountprice = (price*discount) /100

finalprice = price-discountprice
print(f"Discount Amount : ₹{discountprice}")
print(f"Final Price : ₹{finalprice}")