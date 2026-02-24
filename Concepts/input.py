# We use input() to take data from the user while the program is running.

user_name = input('Enter your name: ')
mark_one = int(input('Enter mark one: '))
mark_two = int(input('Enter mark two: '))
mark_three = int(input('Enter mark three: '))

total_mark = mark_one + mark_two + mark_three
average_mark = total_mark / 3

print('Hi',user_name,'!')
print('Your total mark is: ',total_mark)
print('The average mark is: ',average_mark)

# ------------------------------------------------------