#List comprehension
#exercise 1
# Question 1: filter only negaative & zero in the list using list comprehension num =[-4, -3, -2, -1, 0, 1, 2, 4, 6]
num = [-4, -3, -2, -1, 0, 1, 2, 4, 6]
negative_zero=[num for num in num if num<=0]
print (negative_zero)


#question 2:flatten the list of list using list comprehension a one dimensional list
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list =[number for row in list_of_lists for number in row]
print(flattened_list)


#Question 3: Using list comprehension create the following list of tuples:
tuples_list = [(i, 1, i**2) for i in range(11)]
print(tuples_list)


#Question 4: Flatten the following list to a new list:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flattened_countries = [country for sublist in countries for country in sublist]
print(flattened_countries)

