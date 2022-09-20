########## DECLARE VARIABLES ##########

totalQuestions = 36
correctAnswers = 0
incorrectAnswers = []



########## Q1 ##########

number = '1'
correct = 'D'

question = input(
    number + ". What is an abstract class?\n\n"
    "A. An abstract class is the name for any class from which you can instantiate an object.\n"
    "B. Abstract classes must be redefined any time an object is instantiated from them.\n"
    "C. Abstract classes must inherit from concrete classes.\n"
    "D. An abstract class exists only so that other 'concrete' classes can inherit from the abstract class.\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q2 ##########

number = '2'
correct = 'B'

question = input(
    number + ". What happens when you use the build-in function any() on a list?\n\n"
    "A. The any() function will randomly return any item from the list.\n"
    "B. The any() function returns True if any item in the list evaluates to True. Otherwise, it returns False.\n"
    "C. The any() function takes as arguments the list to check inside, and the item to check for. If 'any' of the items in the list match the item to check for, the function returns True.\n"
    "D. The any() function takes as arguments the list to check inside, and the item to check for. If 'any' of the items in the list match the item\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q3 ##########

number = '3'
correct = 'A'

question = input(
    number + ". What data structure does a binary tree degenerate to if it isn't balanced properly?\n\n"
    "A. linked list\n"
    "B. queue\n"
    "C. set\n"
    "D. OrderedDict\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q4 ##########

number = '4'
correct = 'C'

question = input(
    number + ". What statement about static methods is true?\n\n"
    "A. Static methods are called static because they always return None.\n"
    "B. Static methods can be bound to either a class or an instance of a class.\n"
    "C. Static methods serve mostly as utility methods or helper methods, since they can't access or modify a class's state.\n"
    "D. Static methods can access and modify the state of a class or an instance of a class.\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q5 ##########

number = '5'
correct = 'B'

question = input(
    number + ". What are attributes?\n\n"
    "A. Attributes are long-form version of an if/else statement, used when testing for equality between objects.\n"
    "B. Attributes are a way to hold data or describe a state for a class or an instance of a class.\n"
    "C. Attributes are strings that describe characteristics of a class.\n"
    "D. Function arguments are called 'attributes' in the context of class methods and instance methods.\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q6 ##########

number = '6'
correct = 'B'

question = input(
    number + ". What is the term to describe this code?\n"
        "   count, fruit, price = (2, 'apple', 3.5)\n\n"
    "A. tuple assignment\n"
    "B. tuple unpacking\n"
    "C. tuple matching\n"
    "D. tuple duplication\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q7 ##########

number = '7'
correct = 'D'

question = input(
    number + ". What built-in list method would you use to remove items from a list?\n\n"
    "A. .delete() method\n"
    "B. pop(my_list)\n"
    "C. del(my_list)\n"
    "D. .pop() method\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q8 ##########

number = '8'
correct = 'A'

question = input(
    number + ". What is one of the most common use of Python's sys library?\n\n"
    "A. to capture command-line arguments given at a file's runtime\n"
    "B. to connect various systems, such as connecting a web front end, an API service, a database, and a mobile app\n"
    "C. to take a snapshot of all the packages and libraries in your virtual environment\n"
    "D. to scan the health of your Python ecosystem while inside a virtual environment\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q9 ##########

number = '9'
correct = 'D'

question = input(
    number + ". What is the runtime of accessing a value in a dictionary by using its key?\n\n"
    "A. O(n), also called linear time.\n"
    "B. O(log n), also called logarithmic time.\n"
    "C. O(n^2), also called quadratic time.\n"
    "D. O(1), also called constant time.\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q10 ##########

number = '10'
correct = 'A'

question = input(
    number + ". What is the correct syntax for defining a class called Game, if it inherits from a parent class called LogicGame?\n\n"
    "A. class Game(LogicGame): pass\n"
    "B. def Game(LogicGame): pass\n"
    "C. def Game.LogicGame(): pass\n"
    "D. class Game.LogicGame(): pass\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q11 ##########

number = '11'
correct = 'B'

question = input(
    number + ". What is the correct way to write a doctest?\n\n"
     """A.
     def sum(a, b):
     '''
     sum(4, 3)
     7
 
     sum(-4, 5)
     1
     '''
     return a + b\n"""
     """B.
     def sum(a, b):
     '''
     >>> sum(4, 3)
     7
 
     >>> sum(-4, 5)
     1
     '''
     return a + b\n"""
     """C.
     def sum(a, b):
     '''
     # >>> sum(4, 3)
     # 7
 
     # >>> sum(-4, 5)
     # 1
     '''
     return a + b\n"""
     """D. 
     def sum(a, b):
     ###
     >>> sum(4, 3)
     7
 
     >>> sum(-4, 5)
     1
     ###
     return a + b\n\n"""
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q12 ##########

number = '12'
correct = 'B'

question = input(
    number + ". What built-in Python data type is commonly used to represent a stack?\n\n"
    "A. set\n"
    "B. list\n"
    "C. None\n"
    "D. dictionary\n"
    "E. You can only build a stack from scratch.\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q13 ##########

number = '13'
correct = 'D'

question = input(
    number + ". What would this expression return?\n"
        "   college_years = ['Freshman', 'Sophomore', 'Junior', 'Senior']\n"
        "   return list(enumerate(college_years, 2019))\n\n"
    "A. [('Freshman', 2019), ('Sophomore', 2020), ('Junior', 2021), ('Senior', 2022)]\n"
    "B. [(2019, 2020, 2021, 2022), ('Freshman', 'Sophomore', 'Junior', 'Senior')]\n"
    "C. [('Freshman', 'Sophomore', 'Junior', 'Senior'), (2019, 2020, 2021, 2022)]\n"
    "D. [(2019, 'Freshman'), (2020, 'Sophomore'), (2021, 'Junior'), (2022, 'Senior')]\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q14 ##########

number = '14'
correct = 'C'

question = input(
    number + ". What is the purpose of the 'self' keyword when defining or calling instance methods?\n\n"
    "A. self means that no other arguments are required to be passed into the method.\n"
    "B. There is no real purpose for the self method; it's just historic computer science jargon that Python keeps to stay consistent with other programming languages.\n"
    "C. self refers to the instance whose method was called.\n"
    "D. self refers to the class that was inherited from to create the object using self.\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q15 ##########

number = '15'
correct = 'D'

question = input(
    number + ". Which of these is NOT a characteristic of namedtuples?\n\n"
    "A. You can assign a name to each of the namedtuple members and refer to them that way, similarly to how you would access keys in dictionary.\n"
    "B. Each member of a namedtuple object can be indexed to directly, just like in a regular tuple.\n"
    "C. namedtuples are just as memory efficient as regular tuples.\n"
    "D. No import is needed to use namedtuples because they are available in the standard library.\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q16 ##########

number = '16'
correct = 'A'

question = input(
    number + ". What is an instance method?\n\n"
    "A. Instance methods can modify the state of an instance or the state of its parent class.\n"
    "B. Instance methods hold data related to the instance.\n"
    "C. An instance method is any class method that doesn't take any arguments.\n"
    "D. An instance method is a regular function that belongs to a class, but it must return None.\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q17 ##########

number = '17'
correct = 'D'

question = input(
    number + ". Which statement does NOT describe the object-oriented programming concept of encapsulation?\n\n"
    "A. It protects the data from outside interference.\n"
    "B. A parent class is encapsulated and no data from the parent class passes on to the child class.\n"
    "C. It keeps data and the methods that can manipulate that data in one place.\n"
    "D. It only allows the data to be changed by methods.\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q18 ##########

number = '18'
correct = 'C'

question = input(
    number + ". What is the purpose of an if/else statement?\n\n"
    "A. It tells the computer which chunk of code to run if the instructions you coded are incorrect.\n"
    "B. It runs one chunk of code if all the imports were successful, and another chunk of code if the imports were not successful.\n"
    "C. It executes one chunk of code if a condition is true, but a different chunk of code if the condition is false.\n"
    "D. It tells the computer which chunk of code to run if the is enough memory to handle it, and which chunk of code to run if there is not enough memory to handle it.\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q19 ##########

number = '19'
correct = 'D'

question = input(
    number + ". What built-in Python data type is best suited for implementing a queue?\n\n"
    "A. dictionary\n"
    "B. set\n"
    "C. None. You can only build a queue from scratch.\n"
    "D. list\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q20 ##########

number = '20'
correct = 'C'

question = input(
    number + ". What is the correct syntax for instantiating a new object of the type Game?\n\n"
    "A. my_game = class.Game()\n"
    "B. my_game = class(Game)\n"
    "C. my_game = Game()\n"
    "D. my_game = Game.create()\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q21 ##########

number = '21'
correct = 'B'

question = input(
    number + ". What does the built-in map() function do?\n\n"
    "A. It creates a path from multiple values in an iterable to a single value.\n"
    "B. It applies a function to each item in an iterable and returns the value of that function.\n"
    "C. It converts a complex value type into simpler value types.\n"
    "D. It creates a mapping between two different elements of different iterables.\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q22 ##########

number = '22'
correct = 'B'

question = input(
    number + ". If you don't explicitly return a value from a function, what happens?\n\n"
    "A. The function will return a RuntimeError if you don't return a value.\n"
    "B. If the return keyword is absent, the function will return None.\n"
    "C. If the return keyword is absent, the function will return True.\n"
    "D. The function will enter an infinite loop because it won't know when to stop executing its code.\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q23 ##########

number = '23'
correct = 'B'

question = input(
    number + ". What is the purpose of the pass statement in Python?\n\n"
    "A. It is used to skip the yield statement of a generator and return a value of None.\n"
    "B. It is a null operation used mainly as a placeholder in functions, classes, etc.\n"
    "C. It is used to pass control from one statement block to another.\n"
    "D. It is used to skip the rest of a while or for loop and return to the start of the loop.\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q24 ##########

number = '24'
correct = 'A'

question = input(
    number + ". What is the term used to describe items that may be passed into a function?\n\n"
    "A. arguments\n"
    "B. paradigms\n"
    "C. attributes\n"
    "D. decorators\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q25 ##########

number = '25'
correct = 'B'

question = input(
    number + ". Which collection type is used to associate values with unique keys?\n\n"
    "A. slot\n"
    "B. dictionary\n"
    "C. queue\n"
    "D. sorted list\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q26 ##########

number = '26'
correct = 'C'

question = input(
    number + ". When does a for loop stop iterating?\n\n"
    "A. when it encounters an infinite loop\n"
    "B. when it encounters an if/else statement that contains a break keyword\n"
    "C. when it has assessed each item in the iterable it is working on or a break keyword is encountered\n"
    "D. when the runtime for the loop exceeds O(n^2)\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q27 ##########

number = '27'
correct = 'A'

question = input(
    number + ". Assuming the node is in a singly linked list, what is the runtime complexity of searching for a specific node within a singly linked list?\n\n"
    "A. The runtime is O(n) because in the worst case, the node you are searching for is the last node, and every node in the linked list must be visited.\n"
    "B. The runtime is O(nk), with n representing the number of nodes and k representing the amount of time it takes to access each node in memory.\n"
    "C. The runtime cannot be determined unless you know how many nodes are in the singly linked list.\n"
    "D. The runtime is O(1) because you can index directly to a node in a singly linked list.\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q28 ##########

number = '28'
correct = 'B'

question = input(
    number + ". Given the following three list, how would you create a new list that matches the desired output printed below?\n"
        "   fruits = ['Apples', 'Oranges', 'Bananas']\n"
        "   quantities = [5, 3, 4]\n"
        "   prices = [1.50, 2.25, 0.89]\n"
        "\n"
        "   #Desired output\n"
        "   [('Apples', 5, 1.50),\n"
        "   ('Oranges', 3, 2.25),\n"
        "   ('Bananas', 4, 0.89)]\n\n"
    "A. \n"
        "output = []\n"
        "\n"
        "fruit_tuple_0 = (first[0], quantities[0], price[0])\n"
        "output.append(fruit_tuple)\n"
        "\n"
        "fruit_tuple_1 = (first[1], quantities[1], price[1])\n"
        "output.append(fruit_tuple)\n"
        "\n"
        "fruit_tuple_2 = (first[2], quantities[2], price[2])\n"
        "output.append(fruit_tuple)\n"
        "\n"
        "return output\n"
    "B. \n"
        "i = 0\n"
        "output = []\n"
        "for fruit in fruits:\n"
        "    temp_qty = quantities[i]\n"
        "    temp_price = prices[i]\n"
        "    output.append((fruit, temp_qty, temp_price))\n"
        "    i += 1\n"
        "return output\n"
    "C. \n"
        "groceries = zip(fruits, quantities, prices)\n"
        "return groceries\n"
        "\n"
        ">>> [\n"
        "('Apples', 5, 1.50),\n"
        "('Oranges', 3, 2.25),\n"
        "('Bananas', 4, 0.89)\n"
        "]\n"
    "D. \n"
        "i = 0\n"
        "output = []\n"
        "for fruit in fruits:\n"
        "    for qty in quantities:\n"
        "        for price in prices:\n"
        "            output.append((fruit, qty, price))\n"
        "    i += 1\n"
        "return output\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q29 ##########

number = '29'
correct = 'D'

question = input(
    number + ". What happens when you use the built-in function all() on a list?\n\n"
    "A. The all() function returns a Boolean value that answers the question 'Are all the items in this list the same?'\n"
    "B. The all() function returns True if all the items in the list can be converted to strings. Otherwise, it returns False.\n"
    "C. The all() function will return all the values in the list.\n"
    "D. The all() function returns True if all items in the list evaluate to True. Otherwise, it returns False.\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q30 ##########

number = '30'
correct = 'A'

question = input(
    number + ". What is the correct syntax for calling an instance method on a class named Game?\n\n"
    "A. \n"
        ">>> dice = Game()\n"
        ">>> dice.roll()\n"
    "B. \n"
        ">>> dice = Game(self)\n"
        ">>> dice.roll(self)\n"
    "C. \n"
        ">>> dice = Game()\n"
        ">>> dice.roll(self)\n"
    "D. \n"
        ">>> dice = Game(self)\n"
        ">>> dice.roll()\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q31 ##########

number = '31'
correct = 'D'

question = input(
    number + ". What is the algorithmic paradigm of quick sort?\n\n"
    "A. backtracking\n"
    "B. dynamic programming\n"
    "C. decrease and conquer\n"
    "D. divide and conquer\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q32 ##########

number = '32'
correct = 'A'

question = input(
    number + ". What is runtime complexity of the list's built-in .append() method?\n\n"
    "A. O(1), also called constant time\n"
    "B. O(log n), also called logarithmic time\n"
    "C. O(n^2), also called quadratic time\n"
    "D. O(n), also called linear time\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q33 ##########

number = '33'
correct = 'D'

question = input(
    number + ". What is key difference between a set and a list?\n\n"
    "A. A set is an ordered collection unique items. A list is an unordered collection of non-unique items.\n"
    "B. Elements can be retrieved from a list but they cannot be retrieved from a set.\n"
    "C. A set is an ordered collection of non-unique items. A list is an unordered collection of unique items.\n"
    "D. A set is an unordered collection unique items. A list is an ordered collection of non-unique items.\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q34 ##########

number = '34'
correct = 'B'

question = input(
    number + ". What is the definition of abstraction as applied to object-oriented Python?\n\n"
    "A. Abstraction means that a different style of code can be used, since many details are already known to the program behind the scenes.\n"
    "B. Abstraction means the implementation is hidden from the user, and only the relevant data or information is shown.\n"
    "C. Abstraction means that the data and the functionality of a class are combined into one entity.\n"
    "D. Abstraction means that a class can inherit from more than one parent class.\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q35 ##########

number = '35'
correct = 'A'

question = input(
    number + ". What does this function print?\n"
        "   def print_alpha_nums(abc_list, num_list):\n"
        "       for char in abc_list:\n"
        "           for num in num_list:\n"
        "               print(char, num)\n"
        "       return\n\n"
        "\n"
        "   print_alpha_nums(['a', 'b', 'c'], [1, 2, 3])\n\n"
    "A. \n"
        "a 1\n"
        "a 2\n"
        "a 3\n"
        "b 1\n"
        "b 2\n"
        "b 3\n"
        "c 1\n"
        "c 2\n"
        "c 3\n"
    "B. \n"
        "['a', 'b', 'c'], [1, 2, 3]\n"
    "C. \n"
        "aaa\n"
        "bbb\n"
        "ccc\n"
        "111\n"
        "222\n"
        "333\n"
    "D. \n"
        "a 1 2 3\n"
        "b 1 2 3\n"
        "c 1 2 3\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q36 ##########

number = '36'
correct = 'C'

question = input(
    number + ". Pick correct representation of doctest for function in Python.\n\n"
    "A. \n"
        "def sum(a, b):\n"
        "    # a = 1\n"
        "    # b = 2\n"
        "    # sum(a, b) = 3\n"
        "\n"
        "    return a + b\n"
    "B. \n"
        "def sum(a, b):\n"
        "    '''\n"
        "    a = 1\n"
        "    b = 2\n"
        "    sum(a, b) = 3\n"
        "    '''\n"
        "\n"
        "    return a + b\n"
    "C. \n"
        "def sum(a, b):\n"
        "    '''\n"
        "    >>> a = 1\n"
        "    >>> b = 2\n"
        "    >>> sum(a, b)\n"
        "    3\n"
        "    '''\n"
        "\n"
        "    return a + b\n"
    "D. \n"
        "def sum(a, b):\n"
        "    '''\n"
        "    a = 1\n"
        "    b = 2\n"
        "    sum(a, b) = 3\n"
        "    '''\n"
        "    return a + b\n\n"
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