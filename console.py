#!/usr/bin/python3
"""This module contain the HBNB console"""

import cmd

class HBNBCommand(cmd.Cmd):
    """Command line interpreter HBNB"""
    prompt = "(hbnb) "

    def do_quit(self, args):
        """Quit command to exit the console\n"""
        return True

    def do_EOF(self, args):
        """EOF command to exit the console\n"""
        return True

    def emptyline(self):
        """Perform nothing when there's no commmand passed to the console"""
        pass


if __name__ == "__main__":
    comand = HBNBCommand()
    comand.cmdloop()
