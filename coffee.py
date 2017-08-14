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

prime_numbers(11)
