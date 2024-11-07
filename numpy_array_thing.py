import numpy as np

def numpyArrayThingy():
    # Part 1: Create the array with specific conditions
    print("Part 1: Creating a 2D NumPy array with specific conditions............ ; - ; \n")

    # Set random seed for reproducibility , Not sure if its allowed, works both ways. uncomment if want to test
    # np.random.seed(0)



    # Generate initial array with random integers between 10 and 100
    arr = np.random.randint(10, 101, size=(20, 5))
    print("Initial array:\n", arr)

    # Ensure the sum of each row is even
    for i in range(arr.shape[0]):
        row_sum = arr[i].sum()
        if row_sum % 2 != 0:
            # Sum is odd, adjust one element in the row
            # Find an element to adjust
            for j in range(arr.shape[1]):
                if arr[i, j] < 100:
                    arr[i, j] += 1  # Increase by 1
                    break
                elif arr[i, j] > 10:
                    arr[i, j] -= 1  # Decrease by 1
                    break

    # Verify that the sum of each row is even
    row_sums = arr.sum(axis=1)
    assert np.all(row_sums % 2 == 0), "Not all row sums are even."

    # Ensure the total sum is a multiple of 5
    total_sum = arr.sum()
    remainder = total_sum % 5
    if remainder != 0:
        # Adjust the last element to make the total sum a multiple of 5
        adjustment = (5 - remainder)
        if arr[-1, -1] + adjustment <= 100:
            arr[-1, -1] += adjustment
        elif arr[-1, -1] - remainder >= 10:
            arr[-1, -1] -= remainder
        else:
            # Find another element to adjust
            for i in range(arr.shape[0]):
                for j in range(arr.shape[1]):
                    if arr[i, j] + adjustment <= 100:
                        arr[i, j] += adjustment
                        break
                    elif arr[i, j] - remainder >= 10:
                        arr[i, j] -= remainder
                        break

    # Verify that the total sum is a multiple of 5
    total_sum = arr.sum()
    assert total_sum % 5 == 0, "Total sum is not a multiple of 5."

    print("\nAdjusted array:\n", arr)
    print("\nSum of each row:", row_sums)
    print("Total sum of array:", total_sum)
    print("Total sum modulo 5:", total_sum % 5)

    # Part 2: Array indexing and loops
    print("\nPart 2: Extracting and replacing elements...\n")

    # Extract and print all elements divisible by both 3 and 5
    divisible_by_15 = arr[(arr % 15 == 0)]
    print("Elements divisible by both 3 and 5 (i.e., divisible by 15):")
    print(divisible_by_15)

    # Calculate the mean of the entire array
    mean_value = arr.mean()
    print("\nMean of the array:", mean_value)

    # Replace elements greater than 75 with the mean
    arr_replaced = arr.copy()
    arr_replaced[arr_replaced > 75] = int(mean_value)

    print("\nArray after replacing elements greater than 75 with the mean:")
    print(arr_replaced)

    # Part 3: Statistical operations
    print("\nPart 3: Performing statistical operations...\n")

    # Calculate the mean and standard deviation of all values in the array
    overall_mean = arr.mean()
    overall_std = arr.std()
    print(f"Mean of all values: {overall_mean}")
    print(f"Standard deviation of all values: {overall_std}")

    # Find the median value of the array
    median_value = np.median(arr)
    print(f"Median value of the array: {median_value}")

    # Compute the variance for each column
    column_variances = arr.var(axis=0)
    print(f"Variance for each column:\n{column_variances}")

# Call the function to execute the code
# Very similar to a rubix cube cypher I've done before, But that was in c
numpyArrayThingy()
