import numpy as np
import time

print("=" * 60)
print("           NUMPY DATA EXPLORER")
print("=" * 60)

# 1. Array Creation
data = np.array([10, 20, 30, 40, 50])

print("\n1. ARRAY CREATION")
print("Original Array:", data)

# 2. Indexing
print("\n2. INDEXING")
print("First Element:", data[0])
print("Last Element:", data[-1])

# 3. Slicing
print("\n3. SLICING")
print("First Three Elements:", data[:3])
print("Elements from Index 2:", data[2:])

# 4. Mathematical Operations
print("\n4. MATHEMATICAL OPERATIONS")
print("Addition:", data + 5)
print("Subtraction:", data - 5)
print("Multiplication:", data * 2)
print("Division:", data / 2)

# 5. Statistical Operations
print("\n5. STATISTICAL OPERATIONS")
print("Sum:", np.sum(data))
print("Mean:", np.mean(data))
print("Median:", np.median(data))
print("Minimum:", np.min(data))
print("Maximum:", np.max(data))
print("Standard Deviation:", np.std(data))

# 6. Axis-wise Operations
matrix = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print("\n6. AXIS-WISE OPERATIONS")
print("Matrix:")
print(matrix)
print("Column-wise Sum:", np.sum(matrix, axis=0))
print("Row-wise Sum:", np.sum(matrix, axis=1))

# 7. Reshaping
print("\n7. RESHAPING")

numbers = np.arange(1, 13)
reshaped = numbers.reshape(3, 4)

print("Original:", numbers)
print("Reshaped to 3x4:")
print(reshaped)

# 8. Broadcasting
print("\n8. BROADCASTING")

bonus = np.array([1, 2, 3, 4])
scores = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80]
])

print("Original Scores:")
print(scores)

print("After Broadcasting:")
print(scores + bonus)

# 9. Save and Load NumPy Array
print("\n9. SAVE / LOAD")

np.save("data.npy", data)

loaded_data = np.load("data.npy")

print("Saved Array:", data)
print("Loaded Array:", loaded_data)

# 10. NumPy vs Python List Performance
print("\n10. PERFORMANCE COMPARISON")

size = 1_000_000

python_list = list(range(size))
numpy_array = np.arange(size)

start = time.time()
python_result = [x * 2 for x in python_list]
python_time = time.time() - start

start = time.time()
numpy_result = numpy_array * 2
numpy_time = time.time() - start

print("Python List Time:", python_time, "seconds")
print("NumPy Array Time:", numpy_time, "seconds")

if numpy_time < python_time:
    print("Result: NumPy is faster for this operation.")
else:
    print("Result: Python list was faster for this operation.")

print("\n" + "=" * 60)
print("          PROJECT COMPLETED SUCCESSFULLY")
print("=" * 60)