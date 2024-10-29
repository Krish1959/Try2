import numpy as np
import random

# Define the constant Lock Matrix within both encoder and decoder functions

'''
Unni's Algorithm to dynamically generate a Valid Key
'''


def decoder():
    # Get the lock matrix
    locked_key = np.array([
                        [
                            [85, 77, 77, 72],
                            [115, 106, 46, 112],
                            [115, 112, 107, 45],
                            [89, 109, 50, 79]
                        ],
                        [
                            [107, 104, 108, 102],
                            [77, 108, 102, 82],
                            [66, 78, 84, 116],
                            [102, 71, 66, 97]
                        ],
                        [
                            [84, 52, 66, 107],
                            [97, 108, 70, 73],
                            [71, 107, 79, 116],
                            [49, 66, 113, 83]
                        ],
                        [
                            [105, 119, 100, 103],
                            [75, 121, 72, 117],
                            [102, 78, 70, 108],
                            [65, 67, 65, 66]
                        ]
                    ])
    lock = [
            [
                [0, -1, -1, -1],
                [0, -1, 1, 0],
                [1, 1, 1, 0],
                [0, -1, 1, 1]
            ],
            [
                [1, -1, 1, -1],
                [1, 0, 1, 0],
                [1, 0, 0, -1],
                [1, -1, -1, -1]
            ],
            [
                [0, 1, 0, -1],
                [-1, 1, 0, -1],
                [0, -1, 1, 0],
                [0, -1, 1, 1]
            ],
            [
                [1, 1, 0, 1],
                [0, 0, 1, 1],
                [-1, 0, 1, -1],
                [-1, 0, 0, 1]
            ]
           ]
    
    # Subtract lock from sum_matrix to get the original ascii matrix
    new_matrix = locked_key - lock
    
    # Flatten new_matrix to get a 1D array
    ascii_array_flat = new_matrix.flatten()
    
    # Convert ASCII values back to characters
    source_key = ''.join([chr(int(val)) for val in ascii_array_flat])
    source_key = source_key[4:-4]
    return source_key

