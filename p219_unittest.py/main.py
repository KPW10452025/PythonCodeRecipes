import sample_lib

answer = sample_lib.mod01.Addition(10, 20)
print(answer)

# In the Project Folder has two Package Foders named sample_lib and test 
# There have several models in the sample_lib folder: __init__.py, mod1.py, mod2.py, ...etc
# There have several models in the test folder: __init__.py, test_mod1.py. test_mod2.py, ...etc

# In the __init__.py file, need to code:
# from {Package Folder's Name} import {Model's Name}

# For example, the code in __init__.py in sample_lib folder:
# from sample_lib import mod01
# from sample_lib import mod02

# The same, the code in __init__.py in the test folder:
# from test import test_mod01
# from test import test_mod02

# when we want to use the model in the package, we need to code like this:
# import {Package's Name}
# {Package's name}.{Model's Name}.{Function's Name}

# For example, the code in __init__.py in test folder:
# import unittest                                                     # Import unittest
# import sample_lib                                                   # Import the package

# class TestDmo(unittest.TestCase):
#     def test_123(self):
#         self.assertEqual(sample_lib.mod01.Addition(4, 2), 6)        # "sample_lib.mod01.Addition()" is correct.
#     def test_234(self):                                             # It'll go error when we only code "Addition()".  
#         self.assertEqual(sample_lib.mod01.Subtraction(4, 2), 2)

# When we want to run the test, change crrent working directory to  the project folder and code
# python3 -m unittest
