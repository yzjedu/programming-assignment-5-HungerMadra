# Intro here
# Name: Anierobi Eziolise

#-------------------------------------------------------------------------------------

# Function that creates a 2D list filled with consecutive integers starting from 1.

def create_2d_list(rows, cols):
    return [[(i * cols) + j + 1 for j in range(cols)] for i in range(rows)]

# Function that returns the sum of the elements in a specified row of a 2D list.

def sum_of_row(matrix, row_index):
    return sum(matrix[row_index])

# Function that returns the maximum value in a specified column of a 2D list.

def max_in_column(matrix, col_index):
    return max(row[col_index] for row in matrix)

# Function that returns a 1D list containing all elements of the 2D list.

def flatten_matrix(matrix):
    return [element for row in matrix for element in row]

#------------------------------------------------------------------------------------

def main():

    # Task 1: Create a 2D list of 4x4 initialized with numbers from 1 to 16

    matrix = create_2d_list(4, 4)
    print("Original 2D List:")
    for row in matrix:
        print(row)

    # Task 2: Calculate the sum of the third row

    row_sum = sum_of_row(matrix, 2)
    print(f"Sum of the third row: {row_sum}")
    
    # Task 3: Find the maximum element in the last column

    col_max = max_in_column(matrix, 3)
    print(f"Maximum value in the last column: {col_max}")    

    # Task 4: Flatten the matrix into a 1D list
    
    flat_list = flatten_matrix(matrix)
    print(f"Flattened list: {flat_list}")

    #--------------------------------------------------------------------------------

    # Task 5: Perform list modifications

    #--------------------------------------------------------------------------------

    # Append an element to the list

    flat_list.append(99)    

    # Insert an element at a specific position

    flat_list.insert(2, 42)    

    # Sort the list

    flat_list.sort()    

    # Reverse the list

    flat_list.reverse()    

    # Find the minimum and maximum elements
    
    min_value = min(flat_list)
    max_value = max(flat_list)

    # Find the index of a specific element

    index_of_42 = flat_list.index(42)    

    # Print all results: 
    
    print(f"Modified list: {flat_list}")
    print(f"Minimum value: {min_value}")
    print(f"Maximum value: {max_value}")
    print(f"Index of 42: {index_of_42}")

    # Task 6: Decision making - Check if the minimum value in the modified list is greater than 0
    
    if min_value > 0:
        print("The minimum value in the modified list is greater than 0.")
    else:
        print("The minimum value in the modified list is not greater than 0.")

if __name__ == "__main__":
    main()