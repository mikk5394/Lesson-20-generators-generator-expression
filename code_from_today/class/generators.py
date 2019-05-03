

# generator
def my_generator_num(nums):
    for i in nums:
        yield i*i

# normal function
def my_generator_numbers(nums):
    result = []
    for i in nums:
        result.append(i*i)
    return result

my_num = my_generator_numbers([1, 2, 3, 4])

my_list_comp = [i*i for i in [1, 2, 3, 4]] # list comprehension
my_gen_exp = (i*i for i in [1, 2, 3, 4]) # generator expression



print(my_gen_exp)