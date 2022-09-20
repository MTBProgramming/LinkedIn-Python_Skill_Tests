########## DECLARE VARIABLES ##########

totalQuestions = 36
correctAnswers = 0
incorrectAnswers = []



########## Q109 ##########

number = '109'
correct = 'D'

question = input(
    number + ". What will be the value of x after running this code?\n"
        "   x = {1,2,3,4,5}\n"
        "   x.add(5)\n"
        "   x.add(6)\n\n"
    "A. {1, 2, 3, 4, 5, 5, 6}\n"
    "B. {5, 6, 1, 2, 3, 4, 5, 6}\n"
    "C. {6, 1, 2, 3, 4, 5}\n"
    "D. {1, 2, 3, 4, 5, 6}\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q110 ##########

number = '110'
correct = 'D'

question = input(
    number + ". How would you access and store all of the keys in this dictionary at once?\n"
        "   fruit_info = {\n"
        "       'fruit': 'apple',\n"
        "       'count': 2,\n"
        "       'price': 3.5\n"
        "   }\n\n"
    "A. my_keys = fruit_info.to_keys()\n"
    "B. my_keys = fruit_info.all_keys()\n"
    "C. my_keys = fruit_info.keys\n"
    "D. my_keys = fruit_info.keys()\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q111 ##########

number = '111'
correct = 'C'

question = input(
    number + ". What is wrong with this function definition?\n"
        "   def be_friendly(greet = 'How are you!', name):\n"
        "       pass\n\n"
    "A. name is a reserved word.\n"
    "B. Underscores are not allowed in function names.\n"
    "C. A non-default argument follows a default argument.\n"
    "D. There is nothing wrong with this function definition.\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q112 ##########

number = '112'
correct = 'A'

question = input(
    number + ". Given that NumPy is imported as np, which choice will return True?\n\n"
    "A. \n"
        "a = np.zeros([3,4])\n"
        "b = a.copy()\n"
        "np.array_equal(a,b)\n"
    "B. \n"
        "a = np.empty([3,4])\n"
        "b = np.empty([3,4])\n"
        "np.array_equal(a,b)\n"
    "C. \n"
        "a = np.zeros([3,4])\n"
        "b = np.zeros([4,3])\n"
        "np.array_equal(a,b)\n"
    "D. \n"
        "a = np.array([1, np.nan])\n"
        "np.array_equal(a,a)\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q113 ##########

number = '113'
correct = 'B'

question = input(
    number + ". How do you add a comment to existing Python script?\n\n"
    "A. // This is a comment\n"
    "B. # This is a comment\n"
    "C. -- This is a comment\n"
    "D. /* This is a comment *\\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q114 ##########

number = '114'
correct = 'D'

question = input(
    number + ". In this code fragment, what will the values of c and d be equivalent to?\n"
        "   import numpy as np\n"
        "   a = np.array([1,2,3])\n"
        "   b = np.array([4,5,6])\n"
        "   c = a*b\n"
        "   d = np.dot(a,b)\n\n"
    "A. \n"
        "c = [ a[1] * b[1], a[2] * b[2], a[3] * b[3] ]\n"
        "d = sum(c)\n"
    "B. \n"
        "c = a[0] * b[0], a[1] * b[1], a[2] * b[2]\n"
        "\n"
        "d = [ a[0] * b[0], a[1] * b[1], a[2] * b[2] ]\n"
    "C. \n"
        "c = [ a[0] * b[0], a[1] * b[1], a[2] * b[2] ]\n"
        "\n"
        "d = sum(a) + sum(b)\n"
    "D. \n"
        "c = [ a[0] * b[0], a[1] * b[1], a[2] * b[2] ]\n"
        "\n"
        "d = sum(c)\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q115 ##########

number = '115'
correct = 'A'

question = input(
    number + ". What two functions within the NumPy library could you use to solve a system of linear equations?\n\n"
    "A. linalg.eig() and .matmul()\n"
    "B. linalg.inv() and .dot()\n"
    "C. linalg.det() and .dot()\n"
    "D. linalg.inv() and .eye()\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q116 ##########

number = '116'
correct = 'B'

question = input(
    number + ". What is the correct syntax for creating a variable that is bound to a list?\n\n"
    "A. my_list = (2, 'apple', 3.5)\n"
    "B. my_list = [2, 'apple', 3.5]\n"
    "C. my_list = [2, 'apple', 3.5].to_list()\n"
    "D. my_list = to_list(2, 'apple', 3.5)\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q117 ##########

number = '117'
correct = 'D'

question = input(
    number + ". This code provides the _ of the list of numbers.\n"
        "   num_list = [21, 13, 19, 3, 11, 5, 18]\n"
        "   num_list.sort()\n"
        "   num_list[len(num_list) // 2]\n\n"
    "A. mode\n"
    "B. average\n"
    "C. mean\n"
    "D. median\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q118 ##########

number = '118'
correct = 'D'

question = input(
    number + ". What are the two main data structures in the Pandas library?\n\n"
    "A. Arrays and DataFrames\n"
    "B. Series and Matrixes\n"
    "C. Matrixes and DataFrames\n"
    "D. Series and DataFrames\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q119 ##########

number = '119'
correct = 'D'

question = input(
    number + ". Suppose you have a variale named vector of type np.array with 10,000 elements. How can you turn vector into a variable named matrix with dimensions 100x100?\n\n"
    "A. matrix = (vector.shape = (100,100))\n"
    "B. matrix = vector.to_matrix(100,100)\n"
    "C. matrix = matrix(vector,100,100)\n"
    "D. matrix = vector.reshape(100, 100)\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q120 ##########

number = '120'
correct = 'D'

question = input(
    number + ". Which choice is an immutable data type?\n\n"
    "A. dictionnary\n"
    "B. list\n"
    "C. set\n"
    "D. string\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q121 ##########

number = '121'
correct = 'C'

question = input(
    number + ". What is the output of this code?\n"
        "   def myFunction(country = 'France'):\n"
        "       print('Hello, I am from', country)\n"
        "\n"
        "   myFunction('Spain')\n"
        "   myFunction("")\n"
        "   myFunction()\n\n"
    "A. \n"
        "Hello, I am from Spain\n"
        "Hello, I am from\n"
        "Hello, I am from\n"
    "B. \n"
        "Hello, I am from France\n"
        "Hello, I am from France\n"
        "Hello, I am from France\n"
    "C. \n"
        "Hello, I am from Spain\n"
        "Hello, I am from\n"
        "Hello, I am from France\n"
    "D. \n"
        "Hello, I am from Spain\n"
        "Hello, I am from France\n"
        "Hello, I am from France\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q122 ##########

number = '122'
correct = 'D'

question = input(
    number + ". Choose the option below for which instance of the class cannot be created\n\n"
    "A. Anonymous Class\n"
    "B. Parent Class\n"
    "C. Nested Class\n"
    "D. Abstract Class\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q123 ##########

number = '123'
correct = 'A'

question = input(
    number + ". Using Pandas, we load a data set from Kaggle, as structured in the image below. Which command will return the total number of survivors?\n\n"
    "A. sum(titanic['Survived'])\n"
    "B. [x for x in titanic['Survived'] if x == 1]\n"
    "C. len(titanic[''Survived''])\n"
    "D. sum(titanic['Survived']==0)\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q124 ##########

number = '124'
correct = 'B'

question = input(
    number + ". How would you create a list of tuples matching these lists of characters and actors?\n"
        "   characters = ['Iron Man', 'Spider Man', 'Captain America']\n"
        "   actors = ['Downey', 'Holland', 'Evans']\n\n"
    "A. \n"
        "[(x,y)] for x in characters for y in actors]\n"
    "B. \n"
        "zip(characters, actors)\n"
    "C. \n"
        "d = {}\n"
        "\n"
        "for x in range(1, len(characters)):\n"
        "    d[x] = actors[x]\n"
    "D. \n"
        "{x:y for x in characters for y in actors}\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q125 ##########

number = '125'
correct = 'B'

question = input(
    number + ". What will this statement return?\n"
        "   {x : x*x for x in range(1,100)}\n\n"
    "A. a dictionary with x as a key, and x squared as its value; from 1 to 100\n"
    "B. a dictionary with x as a key, and x squared as its value; from 1 to 99\n"
    "C. a set of tuples, consisting of (x, x squared); from 1 to 99\n"
    "D. a list with all numbers squared from 1 to 99\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q126 ##########

number = '126'
correct = 'B'

question = input(
    number + ". Jaccard Similarity is a formula that tells you how similar two sets are. It is defined as the cardinality of the intersection divided by the cardinality of the union. Which choice is an accurate implementation in Python?\n\n"
    "A. def jaccard(a, b): return len (a | b) / len (a & b)\n"
    "B. def jaccard(a, b): return len (a & b) / len (a | b)\n"
    "C. def jaccard(a, b): return len (a && b) / len (a || b)\n"
    "D. def jaccard(a, b): return a.intersection(b) / a.union(b)\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q127 ##########

number = '127'
correct = 'D'

question = input(
    number + ". Which choice is not a native numerical type in Python?\n\n"
    "A. Long\n"
    "B. Int\n"
    "C. Float\n"
    "D. Double\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q128 ##########

number = '128'
correct = 'B'

question = input(
    number + ". What will be the output of this code?\n"
        "   [1,2,3] * 3\n\n"
    "A. [3,2,3]\n"
    "B. [1, 2, 3, 1, 2, 3, 1, 2, 3]\n"
    "C. You will get a type error.\n"
    "D. [3,6,9]\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q129 ##########

number = '129'
correct = 'B'

question = input(
    number + ". Given a list defined as numbers = [1,2,3,4], what is the value of numbers[-2]?\n\n"
    "A. 1\n"
    "B. 2\n"
    "C. 3\n"
    "D. An IndexError exception is thrown.\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q130 ##########

number = '130'
correct = 'A'

question = input(
    number + ". Which statement about strings in Python is true?\n\n"
    "A. Strings can be enclosed by double quotes ('') or single quotes (').\n"
    "B. Strings can only be enclosed in single quotes (').\n"
    "C. Single character strings must be enclosed in single quotes ('), and the rest must be enclosed in double quotes ('').\n"
    "D. Strings can only be enclosed in double quotes ('').\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q131 ##########

number = '131'
correct = 'D'

question = input(
    number + ". What is the correct syntax for defining an init() method that takes no parameters?\n\n"
    "A. definit(self): pass\n"
    "B. classinit(self): pass\n"
    "C. classinit(): pass\n"
    "D. definit(): pass\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q132 ##########

number = '132'
correct = 'C'

question = input(
    number + ". Suppose you need to use the sin function from the math library. What is the correct syntax for importing only that function?\n\n"
    "A. using math.sin\n"
    "B. import math.sin\n"
    "C. from math import sin\n"
    "D. import sin from math\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q133 ##########

number = '133'
correct = 'B'

question = input(
    number + ". What do you get if you apply numpy.sum() to a list that contains only Boolean values?\n\n"
    "A. 0\n"
    "B. the count of all True values\n"
    "C. a type error\n"
    "D. None\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q134 ##########

number = '134'
correct = 'B'

question = input(
    number + ". What will this code print?\n"
        "   print ('foo' if (256).bit_length() > 8 else 'bar')\n\n"
    "A. True\n"
    "B. foo\n"
    "C. You will get an error message because constant integer values are not classes.\n"
    "D. bar\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q135 ##########

number = '135'
correct = 'D'

question = input(
    number + ". If you do not explicitly return a value from a function, what happens?\n\n"
    "A. If the return keyword is absent, the function will return True.\n"
    "B. The function will enter an infinite loop because it will not know when to stop executing its code.\n"
    "C. The function will return a RuntimeError if you do not return a value.\n"
    "D. If the return keyword is absent the function will return None.\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q136 ##########

number = '136'
correct = 'A'

question = input(
    number + ". it is often the case that the pandas library is used for _ data and NumPy for _ data.\n\n"
    "A. string; numerical\n"
    "B. unstructured; structured\n"
    "C. numerical; tabular\n"
    "D. tabular; numerical\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q137 ##########

number = '137'
correct = 'B'

question = input(
    number + ". What do you need to do to install additional packages into Python?\n\n"
    "A. Use a C compiler like gcc or clang.\n"
    "B. Use a package manager like pip or conda.\n"
    "C. Use an IDE like Notepad++ or Idle.\n"
    "D. Use a package manager like NPM or NuGet.\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q138 ##########

number = '138'
correct = 'B'

question = input(
    number + ". The image below was created using Matplotlib. It is a distribution plot of a list of integers filled with numbers using the function _ and plotted with _.\n\n"
    "A. random.uniform(0,50);plt.hist\n"
    "B. random.gauss(50,20);plt.hist\n"
    "C. random();plt.scatter\n"
    "D. random.triangular(0,50);plt.bar\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q139 ##########

number = '139'
correct = 'A'

question = input(
    number + ". In this code fragment, what will be the values of a and b?\n"
        "   import numpy as np\n"
        "   \n"
        "   a = np.arange(100)\n"
        "   b = a[50:60:2]\n\n"
    "A. a: all integers from 0 to 99 (inclusive) b: all even integers from 50 to 58 (inclusive)\n"
    "B. a: all integers from 0 to 100 (inclusive) b: all even integers from 50 to 60 (inclusive)\n"
    "C. a: all integers from 0 to 99 (inclusive) b: all even integers from 50 to 60 (inclusive)\n"
    "D. a: all integers from 0 to 99 (inclusive) b: all odd integers from 49 to 59 (inclusive)\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q140 ##########

number = '140'
correct = 'B'

question = input(
    number + ". When using NumPy in Python, how do you check the dimensionality (number and length of dimensions) of an object called my_object?\n\n"
    "A. my_object.get_shape()\n"
    "B. my_object.shape\n"
    "C. my_object.dim()\n"
    "D. len(my_object)\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q141 ##########

number = '141'
correct = 'A'

question = input(
    number + ". Assume you have a non-empty list named mylist and you want to search for a specific value. The minimum number of comparison will be __ and the maximum number of comparison will be _?\n\n"
    "A. len(mylist); len(mylist)\n"
    "B. 1; len(mylist)\n"
    "C. 2; len(mylist)\n"
    "D. 0; len(mylist)\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q142 ##########

number = '142'
correct = 'C'

question = input(
    number + ". If a function does not have a return statement, what does it really return?\n\n"
    "A. 0\n"
    "B. True\n"
    "C. None\n"
    "D. False\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q143 ##########

number = '143'
correct = 'A'

question = input(
    number + ". What is a common use of python's sys library?\n\n"
    "A. to capture command-line arguments given at a file's runtime\n"
    "B. to take a snapshot of all the packages and libraries in your virtual environment\n"
    "C. to connect various systems, such as connecting a web front end, an API service, a database, and a mobile app\n"
    "D. to scan the health of your Python ecosystem while inside a virtual environment\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q144 ##########

number = '144'
correct = 'D'

question = input(
    number + ". Suppose you want to double-check if two matrices can be multipled using NumPy for debugging purposes. How would you complete this code fragment by filling in the blanks with the appropiate variables?\n"
        "   def can_matrices_be_multiplied (matrix1, matrix2):\n"
        "       rowsMat1, columnsMat1 = matrix1.shape\n"
        "       rowsMat2, columnsMat2 = matrix2.shape\n"
        "\n"
        "       if _____ == ______ :\n"
        "           print('The matrices can be multipled!')\n"
        "           return True\n"
        "       else:\n"
        "           return False\n\n"
    "A. columnsMat1; rowsMat1;\n"
    "B. columnsMat1; rowsMat2;\n"
    "C. columnsMat1; columnsMat2;\n"
    "D. columnsMat2; rowsMat1;\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## PRINT RESULTS ##########

print("Total Questions: " + str(totalQuestions))
print("Correct Answers: " + str(correctAnswers))
print("Final Grade: " + str((100 / totalQuestions) * correctAnswers) + "%")

for i in range(len(incorrectAnswers)):

    print("\n" + incorrectAnswers[i])