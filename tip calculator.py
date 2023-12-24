print('welcome to the tip calculator!')
bill = float(input("what is the total bill? $"))
tip = int(input('what % of tip you would like to pay? '))
final_tip = tip/100 * bill
final_bill = final_tip + bill
people = int(input('how many people would split the bill? '))
per_person = final_bill/people
final_amount = format(per_person, ".2f")
print(f"Each person would pay: ${final_amount}")