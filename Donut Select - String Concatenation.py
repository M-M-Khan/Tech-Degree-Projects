### assigning by score ###

# donut_condition = input("Enter donut condition:")
# donut_filling = input("Enter donut filling:")
# donut_price = input("Enter donut price:")


donut_condition, donut_filling, donut_price = input("Enter your comment:").split(", ")  ### valure are being stored with a comma if you don't define anything in the split but now it should be working fine since we defined a comma and a space inside sep? 
print(donut_condition)
print(donut_filling)
print(donut_price)
buy_score = 0

if donut_condition == "fresh":
    buy_score += 10
if donut_filling == "chocolate":
    buy_score += 5
if donut_price == "reasonable":
    buy_score += 7
print(buy_score)


## height function and try, except ### 
height = 0
height = int(input("enter your height = "))
if height <= 0:
    print("Enter height again")


def height () -> int:
    while True:
        try:
          return int(input("Please enter a number"))
             
        except ValueError:
            print("Input only accepts integer numbers.")

height()



to Concatenate a string and a list

First_Name = input("Enter your name")
Last_Name = ["Khan", "Niazi", "Butt"]

output = [First_Name + s for s in Last_Name]
print(output)

for i in Last_Name: 

    output = ["{} {}".format(First_Name, i)]

    #output = ["{}{}".format(First_Name, i) for i in Last_Name]
    print(output)
        

