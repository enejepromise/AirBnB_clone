#!/usr/bin/python3
"""module defines HBNBCommand """
import cmd

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    
    def do_quit(self, _):
        """quits the command to exit the program"""
        return True
    def do_EOF(self , _):
        """ctrl+D"""
        print()
        return True
    def emptyline(self):
        """Emptyline"""
        pass
    pass
if __name__ == "__main__":
    HBNBCommand().cmdloop()
