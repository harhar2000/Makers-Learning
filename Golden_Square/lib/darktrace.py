# @ Decorater is a function that takes another function as it's only argument to return a modified version 
#                                                                                                   function   

# Add decorator that prints how long it takes for the function to print "hello!"

from time import time, sleep

def timer(func):
    def measure_time():
        start_time = time()
        func()
        end_time = time()
        time_difference = end_time - start_time
        print(f"Time taken: {time_difference:.6f} seconds")
    return measure_time


@timer
def hello():
    sleep(1)
    print("Hello!")

@timer
def goodbye():
    sleep(0.05)
    print("Goodbye!")


hello()
goodbye()
