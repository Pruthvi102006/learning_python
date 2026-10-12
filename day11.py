#Day 11 : functions
#Exercise 1
#Question 1: Declare a function add_two_numbers. It takes two parameters and it returns a sum.
def add_two_numbers(a,b):
    return a+b
print(add_two_numbers(3,7))

#Question 2: Area of a circle is calculated as follows: area = π * r ** 2. Write a function that calculates area_of_circle.
pi = 3.14
def area_of_circle(r):
    return pi * r * r
print(area_of_circle(5))

#Question 3: Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.
def add_all_nums(*args):
    total = 0
    for num in args:
        if isinstance(num, (int, float)):
            total += num
        else:
            return "All arguments must be numbers."
    return total
print(add_all_nums(1, 2, 3, 5)) # Example usage

#Question 4:Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit
def temperature_converter(c):
    return (c *9/5) + 32
print( temperature_converter(25))

#Question 5:Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
def season(month):
    if month in ['September', 'October', 'November']:
        return "Autumn"
    elif month in ['December', 'January', 'February']:
        return "Winter"
    elif month in ['March', 'April', 'May']:
        return "Spring"
    elif month in ['June', 'July', 'August']:
        return "Summer"
    else:
        return "Invalid month"
print(season('March')) # Example usage

#question 6:Write a function called calculate_slope which return the slope of a linear equation
def calculate_slope(x1, y1, x2 , y2):
    if x2 - x1 == 0:
        return "Slope is undefined (vertical line)."
    return (y2 - y1) / (x2 - x1)
                        
print(calculate_slope(1, 2, 3, 4)) # Example usage

#question 7:Write a function which can return any of the following: area of a rectangle, area of a triangle, area of a circle
#def area_of_shape(shape, *args):
 #   if shape ==