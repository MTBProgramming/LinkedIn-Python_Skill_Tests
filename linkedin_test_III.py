########## DECLARE VARIABLES ##########

totalQuestions = 36
correctAnswers = 0
incorrectAnswers = []



########## Q73 ##########

number = '73'
correct = 'B'

question = input(
    number + ". How is comment created?\n\n"
    "A. -- This is a comment\n"
    "B. # This is a comment\n"
    "C. /_ This is a comment _\n"
    "D. // This is a comment\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q74 ##########

number = '74'
correct = 'B'

question = input(
    number + ". What is the correct syntax for replacing the string apple in the list with the string orange?\n"
        "my_list = ['kiwi', 'apple', 'banana']\n\n"
    "A. orange = my_list[1]\n"
    "B. my_list[1] = 'orange'\n"
    "C. my_list['orange'] = 1\n"
    "D. my_list[1] == orange\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q75 ##########

number = '75'
correct = 'C'

question = input(
    number + ". What will happen if you use a while loop and forget to include logic that eventually causes the while loop to stop?\n\n"
    "A. Nothing will happen; your computer knows when to stop running the code in the while loop.\n"
    "B. You will get a KeyError.\n"
    "C. Your code will get stuck in an infinite loop.\n"
    "D. You will get a WhileLoopError.\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q76 ##########

number = '76'
correct = 'A'

question = input(
    number + ". Describe the functionality of a queue?\n\n"
    "A. A queue adds items to either end and removes items from either end.\n"
    "B. A queue adds items to the top and removes items from the top.\n"
    "C. A queue adds items to the top, and removes items from anywhere in, a list.\n"
    "D. A queue adds items to the top and removes items from anywhere in the queue.\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q77 ##########

number = '77'
correct = 'A'

question = input(
    number + ". Which choice is the most syntactically correct example of the conditional branching?\n\n"
    "A. \n"
        "num_people = 5\n"
        "\n"
        "if num_people > 10:\n"
        "    print('There is a lot of people in the pool.')\n"
        "elif num_people > 4:\n"
        "    print('There are some people in the pool.')\n"
        "else:\n"
        "    print('There is no one in the pool.')\n"
    "B. \n"
        "num_people = 5\n"
        "\n"
        "if num_people > 10:\n"
        "    print('There is a lot of people in the pool.')\n"
        "if num_people > 4:\n"
        "    print('There are some people in the pool.')\n"
        "else:\n"
        "    print('There is no one in the pool.')\n"
    "C. \n"
        "num_people = 5\n"
        "\n"
        "if num_people > 10;\n"
        "    print('There is a lot of people in the pool.')\n"
        "elif num_people > 4;\n"
        "    print('There are some people in the pool.')\n"
        "else;\n"
        "    print('There is no one in the pool.')\n"
    "D. \n"
        "if num_people > 10;\n"
        "    print('There is a lot of people in the pool.')\n"
        "if num_people > 4;\n"
        "    print('There are some people in the pool.')\n"
        "else;\n"
        "    print('There is no one in the pool.')\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q78 ##########

number = '78'
correct = 'C'

question = input(
    number + ". How does defaultdict work?\n\n"
    "A. defaultdict will automatically create a dictionary for you that has keys which are the integers 0-10.\n"
    "B. defaultdict forces a dictionary to only accept keys that are of the types specified when you created the defaultdict (such as strings or integers).\n"
    "C. If you try to read from a defaultdict with a nonexistent key, a new default key-value pair will be created for you instead of throwing a KeyError.\n"
    "D. defaultdict stores a copy of a dictionary in memory that you can default to if the original gets unintentionally modified.\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q79 ##########

number = '79'
correct = 'B'

question = input(
    number + ". What is the correct syntax for adding a key called variety to the fruit_info dictionary that has a value of Red Delicious?\n\n"
    "A. fruit_info['variety'] == 'Red Delicious'\n"
    "B. fruit_info['variety'] = 'Red Delicious'\n"
    "C. red_delicious = fruit_info['variety']\n"
    "D. red_delicious == fruit_info['variety']\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q80 ##########

number = '80'
correct = 'C'

question = input(
    number + ". When would you use a while loop?\n\n"
    "A. when you want to minimize the use of strings in your code\n"
    "B. when you want to run code in one file while code in another file is also running\n"
    "C. when you want some code to continue running as long as some condition is true\n"
    "D. when you need to run two or more chunks of code at once within the same file\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q81 ##########

number = '81'
correct = 'C'

question = input(
    number + ". What is the correct syntax for defining an __init__() method that sets instance-specific attributes upon creation of a new class instance?\n\n"
    "A. \n"
        "def __init__(self, attr1, attr2):\n"
        "    attr1 = attr1\n"
        "    attr2 = attr2\n"
    "B. \n"
        "def __init__(attr1, attr2):\n"
        "    attr1 = attr1\n"
        "    attr2 = attr2\n"
    "C. \n"
        "def __init__(self, attr1, attr2):\n"
        "    self.attr1 = attr1\n"
        "    self.attr2 = attr2\n"
    "D. \n"
        "def __init__(attr1, attr2):\n"
        "    self.attr1 = attr1\n"
        "    self.attr2 = attr2\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q82 ##########

number = '82'
correct = 'D'

question = input(
    number + ". What would this recursive function print if it is called with no parameters?\n"
        "   def count_recursive(n=1):\n"
        "       if n > 3:\n"
        "           return\n"
        "       print(n)\n"
        "   \n"
        "       count_recursive(n + 1)\n\n"
    "A. \n"
        "1\n"
        "1\n"
        "2\n"
        "2\n"
        "3\n"
        "3\n"
    "B. \n"
        "3\n"
        "2\n"
        "1\n"
    "C. \n"
        "3\n"
        "3\n"
        "2\n"
        "2\n"
        "1\n"
        "1\n"
    "D. \n"
        "1\n"
        "2\n"
        "3\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q83 ##########

number = '83'
correct = 'C'

question = input(
    number + ". In Python, when using sets, you use _ to calculate the intersection between two sets and _ to calculate the union.\n\n"
    "A. Intersect; union\n"
    "B. |; &\n"
    "C. &; |\n"
    "D. &&; ||\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q84 ##########

number = '84'
correct = 'D'

question = input(
    number + ". What will this code fragment return?\n"
        "   import numpy as np\n"
        "   np.ones([1,2,3,4,5])\n\n"
    "A. It returns a 5x5 matric; each row will have the values 1,2,3,4,5.\n"
    "B. It returns an array with the values 1,2,3,4,5\n"
    "C. It returns five different square matrices filled with ones. The first is 1x1, the second 2x2, and so on to 5x5\n"
    "D. It returns a 5-dimensional array of size 1x2x3x4x5 filled with 1s.\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q85 ##########

number = '85'
correct = 'C'

question = input(
    number + ". You encounter a FileNotFoundException while using just the filename in the open function. What might be the easiest solution?\n\n"
    "A. Make sure the file is on the system PATH\n"
    "B. Create a symbolic link to allow better access to the file\n"
    "C. Copy the file to the same directory as where the script is running from\n"
    "D. Add the path to the file to the PYTHONPATH environment variable\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q86 ##########

number = '86'
correct = 'A'

question = input(
    number + ". what will this command return?\n"
        "   {x for x in range(100) if x%3 == 0}\n\n"
    "A. a set of all the multiples of 3 less then 100\n"
    "B. a set of all the number from 0 to 100 multiplied by 3\n"
    "C. a list of all the multiples of 3 less then 100\n"
    "D. a set of all the multiples of 3 less then 100 excluding 0\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q87 ##########

number = '87'
correct = 'A'

question = input(
    number + ". What does the // operator in Python 3 allow you to do?\n\n"
    "A. Perform integer division\n"
    "B. Perform operations on exponents\n"
    "C. Find the remainder of a division operation\n"
    "D. Perform floating point division\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q88 ##########

number = '88'
correct = 'A'

question = input(
    number + ". What file is imported to use dates in python?\n\n"
    "A. datetime\n"
    "B. dateday\n"
    "C. daytime\n"
    "D. timedate\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q89 ##########

number = '89'
correct = 'C'

question = input(
    number + ". What is the correct syntax for defining a class called Game?\n\n"
    "A. def Game(): pass\n"
    "B. def Game: pass\n"
    "C. class Game: pass\n"
    "D. class Game(): pass\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q90 ##########

number = '90'
correct = 'C'

question = input(
    number + ". What is the correct syntax for calling an instance method on a class named Game?\n\n"
    "A. my_game = Game(self) self.my_game.roll_dice()\n"
    "B. my_game = Game() self.my_game.roll_dice()\n"
    "C. my_game = Game() my_game.roll_dice()\n"
    "D. my_game = Game(self) my_game.roll_dice(self)\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q91 ##########

number = '91'
correct = 'B'

question = input(
    number + ". What is the output of this code? (NumPy has been imported as np.)?\n"
        "   a = np.array([1,2,3,4])\n"
        "   print(a[[False, True, False, False]])\n\n"
    "A. {0,2}\n"
    "B. [2]\n"
    "C. {2}\n"
    "D. [0,2,0,0]\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q92 ##########

number = '92'
correct = 'B'

question = input(
    number + ". Suppose you have a string variable defined as y=”stuff;thing;junk;”. What would be the output from this code?\n"
        "   z = y.split(‘;’)\n"
        "   len(z)\n\n"
    "A. 17\n"
    "B. 4\n"
    "C. 0\n"
    "D. 3\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q93 ##########

number = '93'
correct = 'B'

question = input(
    number + ". What is the output of this code?\n"
        "   num_list = [1,2,3,4,5]\n"
        "   num_list.remove(2)\n"
        "   print(num_list)\n\n"
    "A. [1,2,4,5]\n"
    "B. [1,3,4,5]\n"
    "C. [3,4,5]\n"
    "D. [1,2,3]\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q94 ##########

number = '94'
correct = 'D'

question = input(
    number + ". Which command will create a list from 10 down to 1? Example:\n"
        "   [10,9,8,7,6,5,4,3,2,1]\n\n"
    "A. reversed(list(range(1,11)))\n"
    "B. list(reversed(range(1,10)))\n"
    "C. list(range(10,1,-1))\n"
    "D. list(reversed(range(1,11)))\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q95 ##########

number = '95'
correct = 'B'

question = input(
    number + ". Which fragment of code will print exactly the same output as this fragment?\n"
        "   import math\n"
        "   print(math.pow(2,10)) # prints 2 elevated to the 10th power\n\n"
    "A. \n"
        "print(2^10)\n"
    "B. \n"
        "print(2**10)\n"
    "C. \n"
        "y = [x*2 for x in range(1,10)]\n"
        "print(y)\n"
    "D. \n"
        "y = 1\n"
        "for i in range(1,10):\n"
        "    y = y * 2\n"
        "print(y)\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q96 ##########

number = '96'
correct = 'D'

question = input(
    number + ". Elements surrounded by [] are _, {} are _, and () are _.\n\n"
    "A. sets only; lists or dictionaries; tuples\n"
    "B. lists; sets only; tuples\n"
    "C. tuples; sets or lists; dictionaries\n"
    "D. lists; dictionaries or sets; tuples\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q97 ##########

number = '97'
correct = 'B'

question = input(
    number + ". What is the output of this code? (NumPy has been imported as np.)\n"
        "   table = np.array([\n"
        "       [1,3],\n"
        "       [2,4]])\n"
        "   print(table.max(axis=1))\n\n"
    "A. [2, 4]\n"
    "B. [3, 4]\n"
    "C. [4]\n"
    "D. [1,2]\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q98 ##########

number = '98'
correct = 'A'

question = input(
    number + ". What will this code print?\n"
        "   number = 3\n"
        "       print (f'The number is {number}')\n\n"
    "A. The number is 3\n"
    "B. the number is 3\n"
    "C. THE NUMBER IS 3\n"
    "D. It throws a TypeError because the integer must be cast to a string.\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q99 ##########

number = '99'
correct = 'C'

question = input(
    number + ". Which syntax correctly creates a variable that is bound to a tuple?\n\n"
    "A. my_tuple tup(2, 'apple', 3.5) %D\n"
    "B. my_tuple [2, 'apple', 3.5].tuple() %D\n"
    "C. my_tuple = (2, 'apple', 3.5)\n"
    "D. my_tuple = [2, 'apple', 3.5]\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q100 ##########

number = '100'
correct = 'B'

question = input(
    number + ". Which mode is not a valid way to access a file from within a Python script?\n\n"
    "A. write('w')\n"
    "B. scan('s')\n"
    "C. append('a')\n"
    "D. read('r')\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q101 ##########

number = '101'
correct = 'A'

question = input(
    number + ". NumPy allows you to multiply two arrays without a for loop. This is an example of _.\n\n"
    "A. vectorization\n"
    "B. attributions\n"
    "C. accelaration\n"
    "D. functional programmingn\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q102 ##########

number = '102'
correct = 'D'

question = input(
    number + ". What built-in Python data type can be used as a hash table?\n\n"
    "A. set\n"
    "B. list\n"
    "C. tuple\n"
    "D. dictionary\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q103 ##########

number = '103'
correct = 'B'

question = input(
    number + ". Which Python function allows you to execute Linux shell commands in Python?\n\n"
    "A. sys.exc_info()\n"
    "B. os.system()\n"
    "C. os.getcwd()\n"
    "D. sys.executable\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q104 ##########

number = '104'
correct = 'A'

question = input(
    number + ". Suppose you have the following code snippet and want to extract a list with only the letters. Which fragment of code will _not_ achieve that goal?\n"        "   \n"
        "   my_dictionary = {\n"
        "       'A': 1,\n"
        "       'B': 2,\n"
        "       'C': 3,\n"
        "       'D': 4,\n"
        "       'E': 5\n"
        "   }\n\n"
    "A. \n"
        "letters = []\n"
        "\n"
        "for letter in my_dictionary.values():\n"
        "    letters.append(letter)\n"
    "B. \n"
        "letters = my_dictionary.keys()\n"
    "C. \n"
        "letters = [letter for (letter, number) in my_dictionary.items()]\n"
    "D. \n"
        "letters4 = list(my_dictionary)\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q105 ##########

number = '105'
correct = 'B'

question = input(
    number + ". When an array is large, NumPy will not print the entire array when given the built-in print function. What function can you use within NumPy to force it to print the entire array?\n\n"
    "A. set_printparams\n"
    "B. set_printoptions\n"
    "C. set_fullprint\n"
    "D. setp_printwhole\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q106 ##########

number = '106'
correct = 'A'

question = input(
    number + ". When would you use a try/except block in code?\n\n"
    "A. You use try/except blocks when you want to run some code, but need a way to execute different code if an exception is raised.\n"
    "B. You use try/except blocks inside of unit tests so that the unit testes will always pass.\n"
    "C. You use try/except blocks so that you can demonstrate to your code reviewers that you tried a new approach, but if the new approach is not what they were looking for, they can leave comments under the except keyword.\n"
    "D. You use try/except blocks so that none of your functions or methods return None.\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q107 ##########

number = '107'
correct = 'A'

question = input(
    number + ". In Python, how can the compiler identify the inner block of a for loop?\n\n"
    "A. because of the level of indentation after the for loop\n"
    "B. because of the end keyword at the end of the for loop\n"
    "C. because of the block is surrounded by brackets ({})\n"
    "D. because of the blank space at the end of the body of the for loop\n\n"
)

if (question == correct.upper() or question == correct.lower()):

    correctAnswers = correctAnswers + 1

else:

    incorrectAnswers.append(f"Question {number} (entered '{question}', correct '{correct}'),")



########## Q108 ##########

number = '108'
correct = 'C'

question = input(
    number + ". What Python mechanism is best suited for telling a user they are using a deprecated function\n\n"
    "A. sys.stdout\n"
    "B. traceback\n"
    "C. warnings\n"
    "D. exceptions\n\n"
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