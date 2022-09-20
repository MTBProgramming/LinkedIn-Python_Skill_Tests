########## DECLARE VARIABLES ##########

totalQuestions = 36
correctAnswers = 0
incorrectAnswers = []



########## Q37 ##########

number = '37'
correct = 'D'

question = input(
    number + ". Suppose a Game class inherits from two parent classes: BoardGame and LogicGame. Which statement is true about the methods of an object instantiated from the Game class?\n\n"
    "A. When instantiating an object, the object doesn't inherit any of the parent class's methods.\n"
    "B. When instantiating an object, the object will inherit the methods of whichever parent class has more methods.\n"
    "C. When instantiating an object, the programmer must specify which parent class to inherit methods from.\n"
    "D. An instance of the Game class will inherit whatever methods the BoardGame and LogicGame classes have.\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q38 ##########

number = '38'
correct = 'D'

question = input(
    number + ". What does calling namedtuple on a collection type return?\n\n"
    "A. a generic object class with iterable parameter fields\n"
    "B. a generic object class with non-iterable named fields\n"
    "C. a tuple subclass with non-iterable parameter fields\n"
    "D. a tuple subclass with iterable named fields\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q39 ##########

number = '39'
correct = 'C'

question = input(
    number + ". What symbol(s) do you use to assess equality between two elements?\n\n"
    "A. &&\n"
    "B. =\n"
    "C. ==\n"
    "D. ||\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q40 ##########

number = '40'
correct = 'A'

question = input(
    number + ". Review the code below. What is the correct syntax for changing the price to 1.5?\n"
        "   fruit_info = {\n"
        "     'fruit': 'apple',\n"
        "     'count': 2,\n"
        "     'price': 3.5\n"
        "   }\n\n"
    "A. fruit_info ['price'] = 1.5\n"
    "B. my_list [3.5] = 1.5\n"
    "C. 1.5 = fruit_info ['price]\n"
    "D. my_list['price'] == 1.5\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q41 ##########

number = '41'
correct = 'C'

question = input(
    number + ". What value would be returned by this check for equality?\n"
        "   5 != 6\n\n"
    "A. yes\n"
    "B. False\n"
    "C. True\n"
    "D. None\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q42 ##########

number = '42'
correct = 'C'

question = input(
    number + ". What does a class's __init__() method do?\n\n"
    "A. It makes classes aware of each other if more than one class is defined in a single code file.\n"
    "B. It is included to preserve backwards compatibility from Python 3 to Python 2, but no longer needs to be used in Python 3.\n"
    "C. It is a method that acts as a constructor and is called automatically whenever a new object is created from a class. It sets the initial state of a new object.\n"
    "D. It initializes any imports you may have included at the top of your file.\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q43 ##########

number = '43'
correct = 'C'

question = input(
    number + ". What is meant by the phrase 'space complexity'?\n\n"
    "A. How many microprocessors it would take to run your code in less than one second\n"
    "B. How many lines of code are in your code file\n"
    "C. The amount of space taken up in memory as a function of the input size\n"
    "D. How many copies of the code file could fit in 1 GB of memory\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q44 ##########

number = '44'
correct = 'A'

question = input(
    number + ". What is the correct syntax for creating a variable that is bound to a dictionary?\n\n"
    "A. fruit_info = {'fruit': 'apple', 'count': 2, 'price': 3.5}\n"
    "B. fruit_info =('fruit': 'apple', 'count': 2,'price': 3.5 ).dict()\n"
    "C. fruit_info = ['fruit': 'apple', 'count': 2,'price': 3.5 ].dict()\n"
    "D. fruit_info = to_dict('fruit': 'apple', 'count': 2, 'price': 3.5)\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q45 ##########

number = '45'
correct = 'C'

question = input(
    number + ". What is the proper way to write a list comprehension that represents all the keys in this dictionary?\n"
        "   fruits = {'Apples': 5, 'Oranges': 3, 'Bananas': 4}\n\n"
    "A. fruit_names = [x in fruits.keys() for x]\n"
    "B. fruit_names = for x in fruits.keys() *\n"
    "C. fruit_names = [x for x in fruits.keys()]\n"
    "D. fruit_names = x for x in fruits.keys()\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q46 ##########

number = '46'
correct = 'D'

question = input(
    number + ". What is the purpose of the self keyword when defining or calling methods on an instance of an object?\n\n"
    "A. self refers to the class that was inherited from to create the object using self.\n"
    "B. There is no real purpose for the self method. It's just legacy computer science jargon that Python keeps to stay consistent with other programming languages.\n"
    "C. self means that no other arguments are required to be passed into the method.\n"
    "D. self refers to the instance whose method was called.\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q47 ##########

number = '47'
correct = 'B'

question = input(
    number + ". What statement about the class methods is true?\n\n"
    "A. A class method is a regular function that belongs to a class, but it must return None.\n"
    "B. A class method can modify the state of the class, but they can't directly modify the state of an instance that inherits from that class.\n"
    "C. A class method is similar to a regular function, but a class method doesn't take any arguments.\n"
    "D. A class method hold all of the data for a particular class.\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q48 ##########

number = '48'
correct = 'D'

question = input(
    number + ". What does it mean for a function to have linear runtime?\n\n"
    "A. You did not use very many advanced computer programming concepts in your code.\n"
    "B. The difficulty level your code is written at is not that high.\n"
    "C. It will take your program less than half a second to run.\n"
    "D. The amount of time it takes the function to complete grows linearly as the input size increases.\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q49 ##########

number = '49'
correct = 'D'

question = input(
    number + ". What is the proper way to define a function?\n\n"
    "A. def getMaxNum(list_of_nums): # body of function goes here\n"
    "B. func get_max_num(list_of_nums): # body of function goes here\n"
    "C. func getMaxNum(list_of_nums): # body of function goes here\n"
    "D. def get_max_num(list_of_nums): # body of function goes here\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q50 ##########

number = '50'
correct = 'C'

question = input(
    number + ". According to the PEP 8 coding style guidelines, how should constant values be named in Python?\n\n"
    "A. in camel case without using underscores to separate words -- e.g. maxValue = 255\n"
    "B. in lowercase with underscores to separate words -- e.g. max_value = 255\n"
    "C. in all caps with underscores separating words -- e.g. MAX_VALUE = 255\n"
    "D. in mixed case without using underscores to separate words -- e.g. MaxValue = 255\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q51 ##########

number = '51'
correct = 'C'

question = input(
    number + ". Describe the functionality of a deque.\n\n"
    "A. A deque adds items to one side and remove items from the other side.\n"
    "B. A deque adds items to either or both sides, but only removes items from the top.\n"
    "C. A deque adds items at either or both ends, and remove items at either or both ends.\n"
    "D. A deque adds items only to the top, but remove from either or both sides.\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q52 ##########

number = '52'
correct = 'A'

question = input(
    number + ". What is the correct syntax for creating a variable that is bound to a set?\n\n"
    "A. my_set = {0, 'apple', 3.5}\n"
    "B. my_set = to_set(0, 'apple', 3.5)\n"
    "C. my_set = (0, 'apple', 3.5).to_set()\n"
    "D. my_set = (0, 'apple', 3.5).set()\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q53 ##########

number = '53'
correct = 'D'

question = input(
    number + ". What is the correct syntax for defining an __init__() method that takes no parameters?\n\n"
    "A. \n"
        "class __init__(self):\n"
        "    pass\n"
    "B. \n"
        "def __init__():\n"
        "    pass\n"
    "C. \n"
        "class __init__():\n"
        "    pass\n"
    "D. \n"
        "def __init__(self):\n"
        "    pass\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q54 ##########

number = '54'
correct = 'A'

question = input(
    number + ". Which of the following is TRUE About how numeric data would be organised in a binary Search tree?\n\n"
    "A. For any given Node in a binary Search Tree, the child node to the left is less than the value of the given node and the child node to its right is greater than the given node.\n"
    "B. Binary Search Tree cannot be used to organize and search through numeric data, given the complication that arise with very deep trees.\n"
    "C. The top node of the binary search tree would be an arbitrary number. All the nodes to the left of the top node need to be less than the top node's number, but they don't need to ordered in any particular way.\n"
    "D. The smallest numeric value would go in the top most node. The next highest number would go in its left child node, the the next highest number after that would go in its right child node. This pattern would continue until all numeric values were in their own node.\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q55 ##########

number = '55'
correct = 'C'

question = input(
    number + ". Why would you use a decorator?\n\n"
    "A. A decorator is similar to a class and should be used if you are doing functional programming instead of object oriented programming.\n"
    "B. A decorator is a visual indicator to someone reading your code that a portion of your code is critical and should not be changed.\n"
    "C. You use the decorator to alter the functionality of a function without having to modify the functions code.\n"
    "D. An import statement is preceded by a decorator, python knows to import the most recent version of whatever package or library is being imported.\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q56 ##########

number = '56'
correct = 'B'

question = input(
    number + ". When would you use a for loop?\n\n"
    "A. Only in some situations, as loops are used only for certain type of programming.\n"
    "B. When you need to check every element in an iterable of known length.\n"
    "C. When you want to minimize the use of strings in your code.\n"
    "D. When you want to run code in one file for a function in another file.\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q57 ##########

number = '57'
correct = 'D'

question = input(
    number + ". What is the most self-descriptive way to define a function that calculates sales tax on a purchase?\n\n"
    "A. \n"
        "def tax(my_float):\n"
        "    '''Calculates the sales tax of a purchase. Takes in a float representing the subtotal as an argument and returns a float representing the sales tax.'''\n"
        "    pass\n"
    "B. \n"
        "def tx(amt):\n"
        "    '''Gets the tax on an amount.'''\n"
    "C. \n"
        "def sales_tax(amount):\n"
        "    '''Calculates the sales tax of a purchase. Takes in a float representing the subtotal as an argument and returns a float representing the sales tax.'''\n"
    "D. \n"
        "def calculate_sales_tax(subtotal):\n"
        "    pass\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q58 ##########

number = '58'
correct = 'C'

question = input(
    number + ". What would happen if you did not alter the state of the element that an algorithm is operating on recursively?\n\n"
    "A. You do not have to alter the state of the element the algorithm is recursing on.\n"
    "B. You would eventually get a KeyError when the recursive portion of the code ran out of items to recurse on.\n"
    "C. You would get a RuntimeError: maximum recursion depth exceeded.\n"
    "D. The function using recursion would return None.\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q59 ##########

number = '59'
correct = 'C'

question = input(
    number + ". What is the runtime complexity of searching for an item in a binary search tree?\n\n"
    "A. The runtime for searching in a binary search tree is O(1) because each node acts as a key, similar to a dictionary.\n"
    "B. The runtime for searching in a binary search tree is O(n!) because every node must be compared to every other node.\n"
    "C. The runtime for searching in a binary search tree is generally O(h), where h is the height of the tree.\n"
    "D. The runtime for searching in a binary search tree is O(n) because every node in the tree must be visited.\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q60 ##########

number = '60'
correct = 'D'

question = input(
    number + ". Why would you use mixin?\n\n"
    "A. You use a mixin to force a function to accept an argument at runtime even if the argument wasn't included in the function's definition.\n"
    "B. You use a mixin to allow a decorator to accept keyword arguments.\n"
    "C. You use a mixin to make sure that a class's attributes and methods don't interfere with global variables and functions.\n"
    "D. If you have many classes that all need to have the same functionality, you'd use a mixin to define that functionality.\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q61 ##########

number = '61'
correct = 'B'

question = input(
    number + ". What is the runtime complexity of adding an item to a stack and removing an item from a stack?\n\n"
    "A. Add items to a stack in O(1) time and remove items from a stack on O(n) time.\n"
    "B. Add items to a stack in O(1) time and remove items from a stack in O(1) time.\n"
    "C. Add items to a stack in O(n) time and remove items from a stack on O(1) time.\n"
    "D. Add items to a stack in O(n) time and remove items from a stack on O(n) time.\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q62 ##########

number = '62'
correct = 'B'

question = input(
    number + ". Which statement accurately describes how items are added to and removed from a stack?\n\n"
    "A. a stacks adds items to one side and removes items from the other side.\n"
    "B. a stacks adds items to the top and removes items from the top.\n"
    "C. a stacks adds items to the top and removes items from anywhere in the stack.\n"
    "D. a stacks adds items to either end and removes items from either end.\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q63 ##########

number = '63'
correct = 'A'

question = input(
    number + ". What is a base case in a recursive function?\n\n"
    "A. A base case is the condition that allows the algorithm to stop recursing. It is usually a problem that is small enough to solve directly.\n"
    "B. The base case is summary of the overall problem that needs to be solved.\n"
    "C. The base case is passed in as an argument to a function whose body makes use of recursion.\n"
    "D. The base case is similar to a base class, in that it can be inherited by another object.\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q64 ##########

number = '64'
correct = 'D'

question = input(
    number + ". Why is it considered good practice to open a file from within a Python script by using the with keyword?\n\n"
    "A. The with keyword lets you choose which application to open the file in.\n"
    "B. The with keyword acts like a for loop, and lets you access each line in the file one by one.\n"
    "C. There is no benefit to using the with keyword for opening a file in Python.\n"
    "D. When you open a file using the with keyword in Python, Python will make sure the file gets closed, even if an exception or error is thrown.\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q65 ##########

number = '65'
correct = 'A'

question = input(
    number + ". Why would you use a virtual environment?\n\n"
    "A. Virtual environments create a 'bubble' around your project so that any libraries or packages you install within it don't affect your entire machine.\n"
    "B. Teams with remote employees use virtual environments so they can share code, do code reviews, and collaborate remotely.\n"
    "C. Virtual environments were common in Python 2 because they augmented missing features in the language. Virtual environments are not necessary in Python 3 due to advancements in the language.\n"
    "D. Virtual environments are tied to your GitHub or Bitbucket account, allowing you to access any of your repos virtually from any machine.\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q66 ##########

number = '66'
correct = 'A'

question = input(
    number + ". What is the correct way to run all the doctests in a given file from the command line?\n\n"
    "A. python3 -m doctest <_filename_>\n"
    "B. python3 <_filename_>\n"
    "C. python3 <_filename_> rundoctests\n"
    "D. python3 doctest\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q67 ##########

number = '67'
correct = 'D'

question = input(
    number + ". What is a lambda function ?\n\n"
    "A. any function that makes use of scientific or mathematical constants, often represented by Greek letters in academic writing\n"
    "B. a function that get executed when decorators are used\n"
    "C. any function whose definition is contained within five lines of code or fewer\n"
    "D. a small, anonymous function that can take any number of arguments but has only expression to evaluate\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q68 ##########

number = '68'
correct = 'B'

question = input(
    number + ". What is the primary difference between lists and tuples?\n\n"
    "A. You can access a specific element in a list by indexing to its position, but you cannot access a specific element in a tuple unless you iterate through the tuple\n"
    "B. Lists are mutable, meaning you can change the data that is inside them at any time. Tuples are immutable, meaning you cannot change the data that is inside them once you have created the tuple.\n"
    "C. Lists are immutable, meaning you cannot change the data that is inside them once you have created the list. Tuples are mutable, meaning you can change the data that is inside them at any time.\n"
    "D. Lists can hold several data types inside them at once, but tuples can only hold the same data type if multiple elements are present.\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q69 ##########

number = '69'
correct = 'B'

question = input(
    number + ". What does a generator return?\n\n"
    "A. None\n"
    "B. An iterable object\n"
    "C. A linked list data structure from a non-empty list\n"
    "D. All the keys of the given dictionary\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q70 ##########

number = '70'
correct = 'B'

question = input(
    number + ". What is the difference between class attributes and instance attributes?\n\n"
    "A. Instance attributes can be changed, but class attributes cannot be changed\n"
    "B. Class attributes are shared by all instances of the class. Instance attributes may be unique to just that instance\n"
    "C. There is no difference between class attributes and instance attributes\n"
    "D. Class attributes belong just to the class, not to instance of that class. Instance attributes are shared among all instances of a class\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q71 ##########

number = '71'
correct = 'B'

question = input(
    number + ". What is the correct syntax of creating an instance method?\n\n"
    "A. \n"
        "def get_next_card():\n"
        "  # method body goes here\n"
    "B. \n"
        "def get_next_card(self):\n"
        "  # method body goes here\n"
    "C. \n"
        "def self.get_next_card():\n"
        "  # method body goes here\n"
    "D. \n"
        "def self.get_next_card(self):\n"
        "  # method body goes here\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q72 ##########

number = '72'
correct = 'A'

question = input(
    number + ". What is the correct way to call a function?\n\n"
    "A. get_max_num([57, 99, 31, 18])\n"
    "B. call.(get_max_num)\n"
    "C. def get_max_num([57, 99, 31, 18])\n"
    "D. call.get_max_num([57, 99, 31, 18])\n\n"
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