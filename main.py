#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

bill = float(input("How much is the bill? $"))
ppl = int(input("How many people will be splitting?"))
tip = int(input("How much do you want to tip?"))

tip_percent = tip / 100 * bill
total_bill = tip_percent + bill
total_split = total_bill / ppl

final_amount = ("{:.2f}".format(total_split))

print(f"Each person will pay ${final_amount}.")

# total = float(tip) /100 + int(bill) / int(ppl)
# print(f"Each person should pay {total}.")
