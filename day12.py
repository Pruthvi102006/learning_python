#Day 12 - Modules
#exercise 1
#Question 1:Write a function which generates a six digit/character random_user_id.
import random
import string
from turtle import color
def random_user_id ():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=6))
print (random_user_id)

#Question 2:Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input(). One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.
def user_id_gen_by_user():
    num_chars = int(input("Enter the number of characters: "))
    num_ids = int(input("Enter the number of IDs to generate: "))

    characters = string.ascii_lowercase + string.digits

    for _ in range(num_ids):
        user_id = ''.join(random.choices(characters, k=num_chars))
        print(user_id)

user_id_gen_by_user()


#Question 3: Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).
def rgb_color_gen():
    r= random.randint(1,255)
    g= random.randint(1,255)
    b= random.randint(1,255)
    return f"rgb({r},{g},{b})"
print(random_user_id)

#Exercises: Level 2
#Question 4 :Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).

def list_of_hexa_colors(n):
    colors = []
    for i in range(n):
        color = '#' + ''.join(random.choices('0123456789abcdef', k=6))
        colors.append(color)
    return colors

print(list_of_hexa_colors(3))

#Question 5:Write a function generate_colors which can generate any number of hexa or rgb colors.
def generate_colors(color_type, n):
    colors = []
    if color_type == 'hexa':
        for i in range(n):
            color = '#' + ''.join(random.choices('0123456789abcdef', k=6))
            colors.append(color)
    elif color_type == 'rgb':
        for i in range(n):
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            colors.append(f"rgb({r},{g},{b})")
    else:
        return "Invalid color type. Please choose 'hexa' or 'rgb'."
    return colors

print(generate_colors('hexa', 3))


#Exercises: Level 3
#question 6: Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
def shuffle_list(lst):
    random.shuffle(lst)
    return lst
sample_list = [1, 2, 3, 4, 5]
shuffled_list = shuffle_list(sample_list) 
print(shuffled_list)

#Question 7: Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.
def unique_random_numbers():
    numbers = random.sample(range(10), 7)
    return numbers  
print(unique_random_numbers())
