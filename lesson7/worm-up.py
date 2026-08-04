# def greet(name,message="こんにちは"):
#     print(f"{message},{name}さん")

# greet("太郎","おはよう")

# greet(message="こんにちは",name="花子")

# greet("次郎")

# def calculate(a,b):
#     sum_result=a+b
#     diff_result=a-b
#     return sum_result,diff_result
# sum_val,diff_val=calculate(10,5)
# print(sum_val)
# print(diff_val)

def calculate_average(a,b):
    return (a+b)/2
def product_info(product_name,price):
    print(f"{product_name}の価格は{price}円です")

print(calculate_average(10,5))
product_info("お菓子",30)