# 1
# def calculate_product(num1,num2):
#     return num1*num2

# print(calculate_product(5,10))

# 2
# def my_favorite_char(name,char):
#     print(f"名前:{name},好きなキャラ:{char}")

# my_favorite_char("陽琉","?")

# 3
# def calculate_discounted_total(price,quantity):
#     total=price*quantity
#     if quantity>=5:
#         total*=0.9
#     return int(total)

# print(calculate_discounted_total(100,100))

# 4
def calculation_point(amount:int):
    if amount<1000:
        point=amount*0.01
    elif amount<5000:
        point=amount*0.03
    else:
        point=amount*0.05
    return int(point)

print(calculation_point(5000))
