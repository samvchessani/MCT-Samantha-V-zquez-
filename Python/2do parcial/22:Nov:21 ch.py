print("hi, estimado cliente welcome to the Fasti")

product1=(input("put the name of the first product:"))
price1=int(input("put the price of the first product:"))

product2=(input("put the name of the second product:"))
price2=int(input("put the price of the second product:"))

product3=(input("put the name of the third product:"))
price3=int(input("put the price of the third product:"))

product4=(input("put the name of the fourth product:"))
price4=int(input("put the price of the fourth product:"))

product5=(input("put the name of the fifth product:"))
price5=int(input("put the price of the fifth product:"))

print("Order #045 Sam helped you, Monday, November 22, 2021")

print("Product:", product1, "price:", price1)
print("Product:", product2, "price:", price2)
print("Product:", product3, "price:", price3)
print("Product:", product4, "price:", price4)
print("Product:", product5, "price:", price5)

subtotal= (price1+price2+price3+price4+price5)
print("Your subtotal is:", subtotal)

IVA=(subtotal*.16)
print("Your IVA is:", IVA)

total=(subtotal+IVA)
print("Your total is:", total)
print("Thanks for buy with us :D")