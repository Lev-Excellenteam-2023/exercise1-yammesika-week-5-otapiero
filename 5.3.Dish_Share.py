
# define a generator that return the perfect numbers from 1 to infinity
def perfect_numbers():
    # define a function that get a number and check if the sum of the divisors of the number is equal to the number
    # if the sum is equal to the number return True else return False
    def is_perfect(num):
        # create a list of the divisors of the number
        divisors = [i for i in range(1, int(num / 2) + 1) if num % i == 0]
        # check if the sum of the divisors is equal to the number
        if sum(divisors) == num:
            return True
        else:
            return False
    # create a variable for the number
    num = 1
    # create an infinite loop
    while True:
        # check if the number is perfect
        if is_perfect(num):
            # return the number
            yield num
        # increment the number
        num += 1
for num in perfect_numbers():
    print(num)