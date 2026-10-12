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


#Question 5:Change the following list to a list of dictionaries:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
countries_dict =[{'country': country[0], 'city': country[1]} for sublist in countries for country in sublist]
print(countries_dict)


#question 6:Change the following list of lists to a list of concatenated strings:
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
concatenated_names=[' '.join(name) for sublist in names for name in sublist]
print (concatenated_names)


#question 7 :Write a lambda function which can solve a slope or y-intercept of linear functions.
slope = lambda x1, y1, x2, y2 : (y2 -y1)/(x2 - x1)
y_intercept = lambda x, y, m : y - m * x
print(slope(1, 2, 3, 4)) # Example usage for slope
print(y_intercept(1, 2, 1)) # Example usage for y-intercept
