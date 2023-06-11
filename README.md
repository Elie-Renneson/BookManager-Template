# BookSorter

BookSorter is a Python program that visualizes different sorting algorithms using a stacked bar chart representation, making the bars resemble stacked books. It provides a visual demonstration of how the sorting algorithms work and how they rearrange the elements in an array.

## Installation

1. Clone the repository:
```https://github.com/Elie-Renneson/BookManager-Template```

2. Navigate to the `booksorter` directory:
```cd booksorter```

3. Install the required dependencies:
```pip install -r requirements.txt```


## Usage

To run the sorting algorithm and visualize the sorting process, use the following command:

```python3 run_test.py <path_to_sort_script> <sort_function_name>```

- `<path_to_sort_script>`: The path to the Python file containing the sorting function implementation.
- `<sort_function_name>`: The name of the sorting function to be executed.

For example, to run the Quick Sort algorithm, you can use the following command:

```python3 run_test.py ../quick_sort/quick_sort.py quick_sort```



Make sure to replace `<path_to_sort_script>` with the actual path to your sorting script and `<sort_function_name>` with the name of the sorting function within the script.

The program will generate a graph representing the initial state of the array and an animation showing the sorting process. Additionally, the execution time for the sorting process will be displayed.

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
You can use this README template as a starting point and customize it based on your specific needs and the features of your BookSorter project.