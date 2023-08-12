import os

previous_parent_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print ( previous_parent_directory )