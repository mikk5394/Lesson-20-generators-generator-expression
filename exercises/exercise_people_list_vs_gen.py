import random
import time

names = ['John', 'Corey', 'Adam', 'Steve', 'Rick', 'Thomas']
majors = ['Math', 'Engineering', 'CompSci', 'Arts', 'Business']

# Decorator
def timer(func):
    print('im in decorator')
    def wrapper(*args, **kwargs):
        start = time.time()
        
        value = func(*args, **kwargs)
    
        end = time.time()
        print('The scripts execusion time was', format(end - start, '.6f'), 'seconds')
        print('========')

        return value
    return wrapper



@timer
def people_list(num_people):
    result = []
    for i in range(num_people):
        person = {
                    'id': i,
                    'name': random.choice(names),
                    'major': random.choice(majors)
                }
        result.append(person)
    return result
@timer
def people_generator(num_people):
    for i in range(num_people):
        person = {
                    'id': i,
                    'name': random.choice(names),
                    'major': random.choice(majors)
                }
        yield person

# t1 = time.time
people = people_list(1000000)
# t2 = time.time

#start = time.time()
people = people_generator(1000000)
#end = time.time()

#print('Took {} Seconds'.format(end-start))