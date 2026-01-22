cust_no = input("Enter Customer Number: ")
cust_name = input("Enter Customer Name: ")
item_desc = input("Enter Item Description: ")

price = float(input("Enter Price of Item: "))
quantity = int(input("Enter Quantity Purchased: "))

total = price * quantity

print("TOTAL SALES AMOUNT")
print("------------------")
print("Customer Number    :", cust_no)
print("Customer Name      :", cust_name)
print("Item Description   :", item_desc)
print("Total Sales Amount :", total)
