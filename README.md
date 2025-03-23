
#  Advanced Linear Algebra




## Description

The project implements matrix operations:
- **Determinant Calculation**
- **Minor Matrices**
- **Cofactor Matrices**
- **AdjugateMatrices**
- **Inverse Matrices**
- **Matrix Definiteness Classification with numpy.linalg.eig**





## Files and function description
| Function | Description 
--- | --- 
|determinant | Calculates the determinant of a matrix
|minor| Calculates the minor matrix
|cofactor| Calculates the cofactor matrix|
|adjugate| Calculates the adjugate matrix|
|inverse| Calculates the inverse matrix|
|definitness| Determines if the matrix is positive definite/ semi-definite, negative definite/semi-definite or indefinite based on eigenvalues extracted by numpy.linalg.eig

## Features Implemented

Computing matrix **determinant** recursively  
Generating **minor and cofactor matrices**  
Computing **adjugate and inverse** of a matrix  
Determination of **matrix definiteness** using eigenvalues
## Challenges Faced
Optimizing determinant computation using recursion.
## Usage

Determinant calculation:

    determinant = __import__('0-determinant').determinant

    mat0 = [[]]
    mat1 = [[5]]
    mat2 = [[1, 2], [3, 4]]
    mat3 = [[1, 1], [1, 1]]
    mat4 = [[5, 7, 9], [3, 1, 8], [6, 2, 4]]
    mat5 = []
    mat6 = [[1, 2, 3], [4, 5, 6]]

    print(determinant(mat0))
    print(determinant(mat1))
    print(determinant(mat2))
    print(determinant(mat3))
    print(determinant(mat4))
    try:
        determinant(mat5)
    except Exception as e:
        print(e)
    try:
        determinant(mat6)
    except Exception as e:
        print(e)

Output:

<img width="178" alt="readme_code_snippet_1" src="https://github.com/user-attachments/assets/a1699311-e672-4090-a636-a7bb7dde483d" />

Inverse matrix:

    inverse = __import__('4-inverse').inverse

    mat1 = [[5]]
    mat2 = [[1, 2], [3, 4]]
    mat3 = [[1, 1], [1, 1]]
    mat4 = [[5, 7, 9], [3, 1, 8], [6, 2, 4]]
    mat5 = []
    mat6 = [[1, 2, 3], [4, 5, 6]]

    print(inverse(mat1))
    print(inverse(mat2))
    print(inverse(mat3))
    print(inverse(mat4))
    try:
        inverse(mat5)
    except Exception as e:
        print(e)
    try:
        inverse(mat6)
    except Exception as e:
        print(e)

Output:

<img width="305" alt="raedme_code_snippet_2" src="https://github.com/user-attachments/assets/aba684b7-2cf3-4caa-95c2-f168ea0ecff4" />


Definiteness determination:

    definiteness = __import__('5-definiteness').definiteness
    import numpy as np

    mat1 = np.array([[5, 1], [1, 1]])
    mat2 = np.array([[2, 4], [4, 8]])
    mat3 = np.array([[-1, 1], [1, -1]])
    mat4 = np.array([[-2, 4], [4, -9]])
    mat5 = np.array([[1, 2], [2, 1]])
    mat6 = np.array([])
    mat7 = np.array([[1, 2, 3], [4, 5, 6]])
    mat8 = [[1, 2], [1, 2]]

    print(definiteness(mat1))
    print(definiteness(mat2))
    print(definiteness(mat3))
    print(definiteness(mat4))
    print(definiteness(mat5))
    print(definiteness(mat6))
    print(definiteness(mat7))
    try:
        definiteness(mat8)
    except Exception as e:
        print(e)

Output:

<img width="179" alt="readme_code_snippet_4" src="https://github.com/user-attachments/assets/dbac20fd-c9b7-467f-8cc9-85e8a3aa0024" />







## Authors

Leila Louajri

Studying Machine Learning & AI at Holberton School Toulouse. I'm a PharmD candidate with a passion for biotechnology, machine learning, and data science. My goal is to merge machine learning techniques with biotechnology applications.

[LinkedIn](https://www.linkedin.com/in/leila-louajri-4750aa211/)
