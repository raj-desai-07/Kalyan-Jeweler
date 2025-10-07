name = input("Enter Your Name : ")
gdr = input("Enter Your Gender : ")
print(type(gdr))
age = int(input("Enter Your Age : "))

pro = input("Enter Product name : ")
gram = int(input("Enter Product in Gram : "))
current = 11190

print("----------------------------------------")
totalGoldRate = gram * current
print(f"Total Gold Rate is : {totalGoldRate}")

print("Making Charges (1 Grame) : 845")
totalMackingCharhe = gram * 845

print("---------------------------------------------")
total = totalGoldRate + totalMackingCharhe

print(f"Total Price is : {total}")
print("---------------------------------------------")


if gdr == 'male':
    if age >= 65:
        if total > 210000 and total < 310000:
            print("Discount is 20%")
            discount = totalGoldRate * 20 / 100
            final = total - discount
            print(f"Final Price to Pay : {total} - {discount} = {final}")
        elif total > 310000 and total < 510000:
            print("Discount is 30%")
            discount = totalGoldRate * 30 / 100
            final = total - discount
            print(f"Final Price to Pay : {total} - {discount} = {final}")
        else:
            print("Discount is 35%")
            discount = totalGoldRate * 35 / 100
            final = total - discount
            print(f"Final Price to Pay : {total} - {discount} = {final}")
    else:
        if total > 210000 and total < 310000:
            print("Discount is 10%")
            discount = totalGoldRate * 10 / 100
            final = total - discount
            print(f"Final Price to Pay : {total} - {discount} = {final}")
        elif total > 310000 and total < 510000:
            print("Discount is 20%")
            discount = totalGoldRate * 20 / 100
            final = total - discount
            print(f"Final Price to Pay : {total} - {discount} = {final}")
        else:
            print("Discount is 25%")
            discount = totalGoldRate * 25 / 100
            final = total - discount
            print(f"Final Price to Pay : {total} - {discount} = {final}")
elif gdr == 'female':
    if age >= 65:
        if total > 210000 and total < 310000:
            print("Discount is 25%")
            discount = totalGoldRate * 25 / 100
            final = total - discount
            print(f"Final Price to Pay : {total} - {discount} = {final}")
        elif total > 310000 and total < 510000:
            print("Discount is 35%")
            discount = totalGoldRate * 35 / 100
            final = total - discount
            print(f"Final Price to Pay : {total} - {discount} = {final}")
        else:
            print("Discount is 40%")
            discount = totalGoldRate * 40 / 100
            final = total - discount
            print(f"Final Price to Pay : {total} - {discount} = {final}")
    else:
        if total > 210000 and total < 310000:
            print("Discount is 15%")
            discount = totalGoldRate * 15 / 100
            final = total - discount
            print(f"Final Price to Pay : {total} - {discount} = {final}")
        elif total > 310000 and total < 510000:
            print("Discount is 25%")
            discount = totalGoldRate * 25 / 100
            final = total - discount
            print(f"Final Price to Pay : {total} - {discount} = {final}")
        else:
            print("Discount is 30%")
            discount = totalGoldRate * 30 / 100
            final = total - discount
            print(f"Final Price to Pay : {total} - {discount} = {final}")
else:
    print("Invalid Gender!!")