## Description of the Command Interpreter
""" The project also tested the ability of students to create a command interpreter for the project since the front-end design would come later. The 'cmd' module helped us create a command interpreter that was customized to manipulate our file storage. The interpreter had various data manipulation methods such as SHOW, CREATE, DESTROY, and UPDATE, which are conventionally used to manipulate data in SQL. """

## How to Start It
""" To start the console, clone it to your local machine and run the following command on your terminal:

Windows: 'python console.py'
Linux: './console.py' """
## How to Use It
""" After running the command, it gives a prompt for you to enter commands. You can start by typing 'help'. The 'help' command will give a list of all commands that the console carries out. If you type 'help ', it will give you information about what the command does and how to use it. """

## Examples
"""

'create User': This creates a new user and gives it a unique id which is displayed immediately.

'User.show("a5193d6d-3ad2-4bf4-a0d3-813714c2c777")': This will show the details of the specific user with the id you specified in the bracket.

'User.count()': This gives you the number of instances of the class 'User'.

'User.destroy("a5193d6d-3ad2-4bf4-a0d3-813714c2c777")': This destroys the instance whose id you have specified in the brackets. """
