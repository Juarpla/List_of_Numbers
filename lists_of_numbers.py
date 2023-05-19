"""
Core Requirements 😃
Work through these core requirements step-by-step to complete the program. Please don't skip ahead and do the whole thing at once, because others on your team may benefit from building the program up slowly.

Compute the sum, or total, of the numbers in the list.

Compute the average of the numbers in the list.

Find the maximum, or largest, number in the list.

Stretch Challenge 😎
Have the user enter both positive and negative numbers, then find the smallest positive number (the positive number that is closest to zero).

Sort the numbers in the list and display the new, sorted list. Hint: There are python libraries that can help you here, try searching the internet for them.

"""
list_number = []
finish = 1
number_total = 0
count_numbers = 0

#Enter numbers in a list
print("\nEnter a list of numbers, type 0 when finished.")
while finish != 0:
    number = int(input("Enter number: "))
    if number == 0:
        finish = 0
    else:
        list_number.append(number)

#Sum
for number_sum in list_number:
    number_total += number_sum
print(f"The sum is: {number_total}")

#The average
for count in list_number:
    count_numbers += 1
average = number_total/count_numbers
print(f"The average is: {average:,.4f}")

#smallest positive
new_list_number = []
for i in list_number:
    if i > 0:
        new_list_number.append(i)

small = 99999999
for j in new_list_number:
    if j < small:
        small = j
print(f"The smallest positive number is: {small}\n")

#Using sort
print("The sorted list is:")
for s_number in sorted(list_number):
    print(s_number)