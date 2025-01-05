# მომხმარებლისგან რიცხვების მიღება
num1 = float(input("შეიყვანეთ პირველი რიცხვი (num1): "))
num2 = float(input("შეიყვანეთ მეორე რიცხვი (num2): "))

# ლოგიკური ოპერატორები
print(f"{num1} > {num2}: {num1 > num2}")
print(f"{num1} < {num2}: {num1 < num2}")
print(f"{num1} >= {num2}: {num1 >= num2}")
print(f"{num1} <= {num2}: {num1 <= num2}")
print(f"{num1} != {num2}: {num1 != num2}")
print(f"{num1} == {num2}: {num1 == num2}")



# მომხმარებლისგან სიგანის (width) და სიმაღლის (height) მიღება
width = float(input("შეიყვანეთ მართკუთხედის სიგანე (width): "))
height = float(input("შეიყვანეთ მართკუთხედის სიმაღლე (height): "))

# პერიმეტრის გამოთვლა
perimeter = 2 * (width + height)


# შედეგის ჩვენება
print(f"მართკუთხედის პერიმეტრი არის: {perimeter}")


# მომხმარებლისგან სახელი (name) და რიცხვი (num) მიღება
name = input("შეიყვანეთ თქვენი სახელი: ")
num = int(input("შეიყვანეთ რიცხვი: "))

# name გამრავლება num-ზე
result = name * num

# შედეგის პრინტინგი
print(f"გამოყენებული სახელი {num} ჯერ: {result}")



# მომხმარებლისგან დაბადების წლის (birthyear) და მიმდინარე წლის (date) მიღება
birthyear = int(input("შეიყვანეთ თქვენი დაბადების წელი: "))
date = int(input("შეიყვანეთ მიმდინარე წელი: "))

# ასაკის გამოთვლა
age = date - birthyear

# შედეგის პრინტინგი
print(f"თქვენი ასაკია: {age} წელი")
