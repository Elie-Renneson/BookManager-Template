# run_test.py

import random
import time
import importlib.util
import sys

# Load the sorting function from the provided python file
script_path = sys.argv[1]
sort_func_name = sys.argv[2]
spec = importlib.util.spec_from_file_location("module.name", script_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
sort_function = getattr(module, sort_func_name)  # Get the function based on its name

from visualize import visualize_sorting, visualize_sorting_animation

def run_test():
    array_size = 50
    arr = [random.randint(1, 100) for _ in range(array_size)]

    start_time = time.time()
    sorted_arr = sort_function(arr)  # Call the sorting function from the imported script
    end_time = time.time()
    execution_time = end_time - start_time

    if execution_time < 0.75 * array_size:
        print('\033[92mExecution time for size', array_size, ':', execution_time, 'seconds')
    elif execution_time < 1.25 * array_size:
        print('\033[93mExecution time for size', array_size, ':', execution_time, 'seconds')
    else:
        print('\033[91mExecution time for size', array_size, ':', execution_time, 'seconds')

    # Generate graph using the sorting steps
    visualize_sorting(sorted_arr)

    # Generate animation using the sorting steps after the execution of the sorting process
    visualize_sorting_animation()

    sys.exit()  # Exit the program

run_test()
