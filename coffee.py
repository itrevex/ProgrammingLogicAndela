'''
Andela Making Coffee App 
'''
#Make my coffee

INGREDIENTS = ['coffee', 'hot water']
print('Started making coffee...')
print('Getting cup')
print('Adding {}'.format(' and '.join(INGREDIENTS)))
print('Stir the mix')
print('Finished making coffeee...')
MY_COFFEE = 'Tasty Coffee'
print("--Here's your {}, Enjoy!!-- Mr. {} \n".format(MY_COFFEE, 'Evans'))

def prime_numbers(upper_limit_n):
    """
    Function to return prime numbers from 0 to n
    """
    for i in range(0, upper_limit_n, 2):
        print(i)
    
    print(", ".join(""+str(i) for i in range(0, upper_limit_n, 2)))

    '''
    Big O notation analysis:
    Number of lines executed == 2
    memory points = n

    second print, lines 1
    memory points 1
    '''

def fibonacci_squence(total_number_of_values, first_value=0, second_value=1):
    """
    Generates fibonacci squence
    total_number_of_values represents the total number of values in squence
    first value is the start value of squence
    second value is the value after the start value
    """

    if total_number_of_values < 3:
        raise fibonacci_squence_exception()

    squence_values = [first_value, second_value]

    for counter in range(total_number_of_values-2):
        value_one = squence_values[counter]
        value_two = squence_values[counter+1]
        squence_values.append(sum_of_values(value_one, value_two))

    print(", ".join(str(number) for number in squence_values))

def sum_of_values(value_one, value_two):
    """
    returns sum of two values
    """
    return value_one + value_two

def fibonacci_squence_exception():
    """
    prints error message if total_number_of_values passed to 
    fibonacci squence function is less 3
    """
    print("Unsupported length of squence, total_number_of_values \n should b >= 3")

prime_numbers(11)
fibonacci_squence(20, 15, 15)
