# Introduction to NumPy Arrays

NumPy is one of Python's most powerful and popular libraries for mathematical and scientific data manipulation. 
In this guide, we will explore the basics of NumPy arrays, their creation, properties, and common operations.

## 1. What is a NumPy Array?
- A **NumPy Array** is a data structure **similar** to a Python list but optimized for numerical data and matrices.
- It is more memory-efficient and faster for computation than regular Python lists.
- Enables mathematical operations directly on whole arrays without loops.

## 2. Creating Basic Arrays
```python
import numpy as np

array_1d = np.array([1, 2, 3, 4, 5])           # Creating a 1D array
array_2d = np.array([[1, 2, 3], [4, 5, 6]])    # Creating a 2D array (matrix)
float_array = np.array([1, 2, 3], dtype=float) # Array with a specific data type
```

## 3. Creating Arrays with Built-in Functions
```python
zeros = np.zeros((3, 3))  # Matrix of zeros with size 3x3
ones = np.ones((2, 4))    # Matrix of ones with size 2x4
empty_array = np.empty((2, 3))  # Array with size 2x3
sequence = np.arange(0, 10, 2)  # [0, 2, 4, 6, 8]
```

- **Array with evenly spaced values:**
```python
linspace = np.linspace(0, 1, 5)  # [0. , 0.25, 0.5 , 0.75, 1. ]
```

## 4. Key Properties of Arrays
- **Shape:** Dimensions of the array.
- **Data type (dtype):** Type of values stored in the array.
- **Number of dimensions (ndim):**
```python
array = np.array([[1, 2, 3], [4, 5, 6]])
print(array.shape)  # (2, 3)
print(array.ndim)   # 2
print(array.dtype)  # int64
```

## 5. Operations on Arrays
- **Mathematical operations:**
```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a + b)  # [5, 7, 9]   ~~~ a.plus(b)
print(a * b)  # [4, 10, 18] ~~~ a.multiply(b)
print(a ** 2) # [1, 4, 9]   
```

- **Transpose of a matrix:**
```
[[1, 2], ===>[[1, 3],
 [3, 4]] ===> [2, 4]]

```
```python
matrix = np.array([[1, 2], [3, 4]])
print(matrix.T)  # [[1, 3], [2, 4]]
```


## 6. Slicing and Indexing
- Slicing works similarly to Python lists:
```python
array = np.array([10, 20, 30, 40, 50])
print(array[1:4])  # [20, 30, 40]
```

- **Conditional indexing:**
```python
array = np.array([1, 2, 3, 4, 5])
print(array[array > 3])  # [4, 5]
print(array[(array > 2) & (array < 5)]) # [3, 4]
```

## 7. Multi-dimensional Arrays
- Complex indexing:
```python
#           indexes 0  1  2        
matrix = np.array([[1, 2, 3],   # index 0 
                   [4, 5, 6]])  # index 1
print(matrix[1, 2])  # Value: 6
```

- Multi-dimensional slicing:
```python
print(matrix[:, 1])  # Second column
print(matrix[1, :])  # Second row
```

---

## 8. Advanced Usage
- **Statistical operations:**
```python
data = np.array([10, 20, 30, 40])
print(data.mean())   # Mean ==>  25
print(data.sum())    # Sum  ==> 100
print(data.std())    # Standard deviation ==>11.180339887498949

# works the same on matrix
matrix = np.array([[10, 20], [30, 40]])
print(matrix.mean())   # Mean ==>  25
print(matrix.sum())    # Sum  ==> 100
print(matrix.std())    # Standard deviation ==>11.180339887498949
```

- **Matrix computations:**
```python
matrix = np.array([[1, 2],   #  [1  2    X [3
                   [3, 4]])  #   3  4]      4]
vector = np.array([5, 6])    #
result = matrix.dot(vector)  # Matrix-vector multiplication
```

