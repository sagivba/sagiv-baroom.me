import random
import time
import psutil
from memory_profiler import memory_usage
import copy
import numpy as np

# Define global parameters
X = 200  # Depth
Y = 200  # Rows
Z = 200  # Columns

# Initialize Process for memory measurements
process = psutil.Process()


def create_3d_list(x, y, z):
    """Create a 3D list (list of lists of lists) filled with random floating-point numbers."""
    return [[[random.random() for _ in range(z)] for _ in range(y)] for _ in range(x)]


def create_3d_numpy_array(x, y, z):
    """Create a 3D NumPy array filled with random floating-point numbers."""
    return np.random.random((x, y, z))


def copy_3d_list(lst):
    """Create a deep copy of a 3D list."""
    return copy.deepcopy(lst)


def copy_3d_numpy_array(arr):
    """Create a copy of a 3D NumPy array."""
    return arr.copy()


def calculate_stats_3d_list(lst):
    """Calculate mean, max, min, and standard deviation for a 3D list."""
    flat_list = [item for sublist2 in lst for sublist1 in sublist2 for item in sublist1]
    mean = sum(flat_list) / len(flat_list)
    max_val = max(flat_list)
    min_val = min(flat_list)
    std_dev = (sum((x - mean) ** 2 for x in flat_list) / len(flat_list)) ** 0.5
    return mean, max_val, min_val, std_dev


def calculate_stats_3d_numpy(arr):
    """Calculate mean, max, min, and standard deviation for a 3D NumPy array."""
    mean = arr.mean()
    max_val = arr.max()
    min_val = arr.min()
    std_dev = arr.std()
    return mean, max_val, min_val, std_dev


def measure_performance(func, *args, **kwargs):
    """
    Measure the performance of a function.

    Returns:
        A dictionary containing total time, CPU time, and memory usage.
    """
    # Measure memory before
    mem_before = process.memory_info().rss / (1024 ** 2)  # in MB

    # Measure time
    start_time = time.time()
    start_cpu = time.process_time()

    # Execute the function
    result = func(*args, **kwargs)

    # Measure time after
    end_cpu = time.process_time()
    end_time = time.time()

    # Measure memory after
    mem_after = process.memory_info().rss / (1024 ** 2)  # in MB

    # Calculate metrics
    total_time = end_time - start_time
    cpu_time = end_cpu - start_cpu
    memory_usage = mem_after - mem_before

    return {
        'result': result,
        'total_time': total_time,
        'cpu_time': cpu_time,
        'memory_usage': memory_usage
    }


def run_test_creation():
    """Test Case 1: Creation of Data Structures."""
    print("Running Test Case 1: Creation of Data Structures...")

    # 1.1 Create 3D List
    performance_list = measure_performance(create_3d_list, X, Y, Z)

    # 1.2 Create 3D NumPy Array
    performance_numpy = measure_performance(create_3d_numpy_array, X, Y, Z)

    return performance_list, performance_numpy


def run_test_copying(list_3d, numpy_3d):
    """Test Case 2: Copying Data Structures."""
    print("Running Test Case 2: Copying Data Structures...")

    # 2.1 Copy 3D List
    performance_list_copy = measure_performance(copy_3d_list, list_3d)

    # 2.2 Copy 3D NumPy Array
    performance_numpy_copy = measure_performance(copy_3d_numpy_array, numpy_3d)

    return performance_list_copy, performance_numpy_copy


def run_test_statistical_calculations(list_3d, numpy_3d):
    """Test Case 3: Statistical Calculations."""
    print("Running Test Case 3: Statistical Calculations...")

    # 3.1 Statistics for 3D List
    performance_stats_list = measure_performance(calculate_stats_3d_list, list_3d)

    # 3.2 Statistics for 3D NumPy Array
    performance_stats_numpy = measure_performance(calculate_stats_3d_numpy, numpy_3d)

    return performance_stats_list, performance_stats_numpy


def run_test_multiply(list_3d, numpy_3d):
    def multiply_3d_lists(list1, list2):
        """Performs element-wise multiplication on two 3D lists."""
        return [
            [
                [a * b for a, b in zip(row1, row2)]
                for row1, row2 in zip(layer1, layer2)
            ]
            for layer1, layer2 in zip(list1, list2)
        ]
    def multiply_3d_numpy_arrays(arr1, arr2):
        """Perform element-wise addition on two 3D NumPy arrays."""
        return arr1 * arr2

    def add_3d_lists(lst1, lst2):
        """Perform element-wise addition on two 3D lists."""
        return [[[a + b for a, b in zip(row1, row2)] for row1, row2 in zip(layer1, layer2)]
                for layer1, layer2 in zip(lst1, lst2)]

    def add_3d_numpy_arrays(arr1, arr2):
        """Perform element-wise addition on two 3D NumPy arrays."""
        return arr1 + arr2

    def dot_3d_lists(list1, list2):
        """
        Performs a dot product on two 3D lists.
        Here, the dot product is defined as the sum of products along the last axis.
        """
        result = []
        for layer1, layer2 in zip(list1, list2):
            layer_result = []
            for row1, row2 in zip(layer1, layer2):
                dot = sum(a * b for a, b in zip(row1, row2))
                layer_result.append(dot)
            result.append(layer_result)
        return result
    """Test Case 4: multiply."""
    print("Running Test Case 4: multiply...")

    # Create a second 3D list and 3D NumPy array for addition
    list_3d_2 = create_3d_list(X, Y, Z)
    numpy_3d_2 = np.array(list_3d_2)

    # 4.1 Element-wise Addition for 3D Lists
    performance_multiply_lists = measure_performance(multiply_3d_lists, list_3d, list_3d_2)
    # 4.2 Element-wise Addition for 3D NumPy Arrays
    performance_multiply_numpy = measure_performance(multiply_3d_numpy_arrays, numpy_3d, numpy_3d_2)

    return performance_multiply_lists, performance_multiply_numpy


def run_test_dot(list_3d, numpy_3d):

    def add_3d_lists(lst1, lst2):
        """Perform element-wise addition on two 3D lists."""
        return [[[a + b for a, b in zip(row1, row2)] for row1, row2 in zip(layer1, layer2)]
                for layer1, layer2 in zip(lst1, lst2)]

    def add_3d_numpy_arrays(arr1, arr2):
        """Perform element-wise addition on two 3D NumPy arrays."""
        return arr1 + arr2

    def dot_3d_lists(list1, list2):
        """
        Performs a dot product on two 3D lists.
        Here, the dot product is defined as the sum of products along the last axis.
        """
        result = []
        for layer1, layer2 in zip(list1, list2):
            layer_result = []
            for row1, row2 in zip(layer1, layer2):
                dot = sum(a * b for a, b in zip(row1, row2))
                layer_result.append(dot)
            result.append(layer_result)
        return result
    def dot_3d_numpy(arr1, arr2):
        """Perform element-wise addition on two 3D NumPy arrays."""
        return arr1.dot(arr2)
    """Test Case 5: dot."""
    print("Running Test Case 5: dot operation")

    # Create a second 3D list and 3D NumPy array for addition
    list_3d_2 = create_3d_list(X, Y, Z)
    numpy_3d_2 = create_3d_numpy_array(X, Y, Z)

    # 5.1 dot
    try:
        performance_dot_lists = measure_performance(dot_3d_lists, list_3d, list_3d_2)
    except Exception as e:
        print(f"Error: dot_3d_lists: {e}")
        performance_dot_lists = 0.0

    # 5.2 Element-wise Addition for 3D NumPy Arrays
    try:
        performance_dot_numpy = measure_performance(dot_3d_numpy, numpy_3d, numpy_3d_2)
    except Exception as e:
        print(f"Error: dot_3d_numpy: {e}")
        performance_dot_numpy = 0.0
    return performance_dot_lists, performance_dot_numpy


def generate_markdown_summary(results):

    md =[]
    headers =  "| **Test Case**      | **Operation**            | **3D List**         | **3D NumPy Array**   |"
    line_sep = "|--------------------|--------------------------|---------------------|----------------------|"

    md.append(headers)
    md.append(line_sep)
    md.append(f"| **1. Creation**    | Create random            |                     |                      |")
    md.append(f"|       **Time:**    |  `[{X:5} x{Y:5} x{Z:5}]` |{results['creation_list']['total_time'  ]:^21.4f}|{results['creation_numpy']['total_time'  ]:^22.4f}|")
    md.append(f"|       *CPU Time:** |                          |{results['creation_list']['cpu_time'    ]:^21.4f}|{results['creation_numpy']['cpu_time'    ]:^22.4f}|")
    md.append(f"|       *Memory:**   |                          |{results['creation_list']['memory_usage']:^21.4f}|{results['creation_numpy']['memory_usage']:^22.4f}|")
    md.append(line_sep)
    md.append(f"| **2. Copying**     | Deep copy                |                     |                      |")
    md.append(f"|       **Time:**    |                          |{results['copying_list_copy']['total_time'  ]:^21.4f}|{results['copying_list_copy']['total_time'  ]:^22.4f}|")
    md.append(f"|       *CPU Time:** |                          |{results['copying_list_copy']['cpu_time'    ]:^21.4f}|{results['copying_list_copy']['cpu_time'    ]:^22.4f}|")
    md.append(f"|       *Memory:**   |                          |{results['copying_list_copy']['memory_usage']:^21.4f}|{results['copying_list_copy']['memory_usage']:^22.4f}|")
    md.append(line_sep)
    md.append(f"| **3. Stat Calc**   | Calculate:               |                     |                      |")
    md.append(f"|       **Time:**    |    Mean, Max, Min        |{results['stats_list'       ]['total_time'  ]:^21.4f}|{results['stats_list']['total_time'  ]:^22.4f}|")
    md.append(f"|       *CPU Time:** |    and Std Dev           |{results['stats_list'       ]['cpu_time'    ]:^21.4f}|{results['stats_list']['cpu_time'    ]:^22.4f}|")
    md.append(f"|       *Memory:**   |                          |{results['stats_list'       ]['memory_usage']:^21.4f}|{results['stats_list']['memory_usage']:^22.4f}|")
    md.append(line_sep)
    md.append(f"| **4. muliplty**    | np.multiply vs list      |                     |                      |")
    md.append(f"|       **Time:**    |                          |{results['multiply_list']['total_time'  ]:^21.4f}|{results['multiply_list']['total_time'  ]:^22.4f}|")
    md.append(f"|       *CPU Time:** |                          |{results['multiply_list']['cpu_time'    ]:^21.4f}|{results['multiply_list']['cpu_time'    ]:^22.4f}|")
    md.append(f"|       *Memory:**   |                          |{results['multiply_list']['memory_usage']:^21.4f}|{results['multiply_list']['memory_usage']:^22.4f}|")
    md.append(line_sep)
    md.append(f"| **5. dot**         | np.dot vs list           |                     |                      |")
    md.append(f"|       **Time:**    |                          |{results['dot_list']['total_time'  ]:^21.4f}|{results['dot_list']['total_time'  ]:^22.4f}|")
    md.append(f"|       *CPU Time:** |                          |{results['dot_list']['cpu_time'    ]:^21.4f}|{results['dot_list']['cpu_time'    ]:^22.4f}|")
    md.append(f"|       *Memory:**   |                          |{results['dot_list']['memory_usage']:^21.4f}|{results['dot_list']['memory_usage']:^22.4f}|")
    md.append(line_sep)

    return "\n".join(md)


def main():
    """Main function to run all tests and generate the comprehensive summary."""
    print("## NumPy vs 3D List of Lists Performance Comparison ##\n")

    # Initialize a dictionary to store all results
    results = {}

    # Test Case 1: Creation
    creation_list, creation_numpy = run_test_creation()
    results['creation_list'] = creation_list
    results['creation_numpy'] = creation_numpy
    print("End run_test_creation")

    # we create the same values
    a_list,a_numpy= creation_list['result'],  np.array(creation_list['result'])

    # Test Case 2: Copying
    copying_list_copy, copying_numpy_copy = run_test_copying( a_list,a_numpy)
    results['copying_list_copy'] = copying_list_copy
    results['copying_numpy_copy'] = copying_numpy_copy
    print("End run_test_copying")

    # Test Case 3: Statistical Calculations
    stats_list, stats_numpy = run_test_statistical_calculations( a_list,a_numpy)
    results['stats_list'] = stats_list
    results['stats_numpy'] = stats_numpy

    # Test Case 5: multiply
    multiply_lists, multiply_numpy = run_test_multiply( a_list,a_numpy)
    results['multiply_list'] = multiply_lists
    results['multiply_numpy'] = multiply_numpy
    print("End run_test_multiply")

    # Test Case 6: dot
    dot_lists, dot_numpy = run_test_dot( a_list,a_numpy)
    results['dot_list'] = dot_lists
    results['dot_numpy'] = dot_numpy
    print("End run_test_dot")
    # Generate the Markdown summary
    markdown_summary = generate_markdown_summary(results)

    # Print the summary
    print(markdown_summary)

    # Save the summary to a Markdown file
    with open("comprehensive_summary.md", "w") as md_file:
        md_file.write(markdown_summary)

    print("\n**Comprehensive Summary has been saved to `comprehensive_summary.md`**")


if __name__ == "__main__":
    main()
