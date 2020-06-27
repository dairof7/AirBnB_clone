#!/usr/bin/python3
"""This module contain the HBNB console"""

import cmd
from models.base_model import BaseModel
from models import storage
import inspect
import models


class HBNBCommand(cmd.Cmd):
    """Command line interpreter HBNB"""
    prompt = "(hbnb) "
    class_list = ["BaseModel"]
    def do_quit(self, args):
        """Quit command to exit the console\n"""
        return True

    def do_EOF(self, args):
        """EOF command to exit the console\n"""
        return True

    def emptyline(self):
        """Perform nothing when there's no commmand passed to the console"""
        pass

    def do_create(self, args):
        try:
            if args == "":
                raise Exception("** class name missing **")
            a = eval(args)()
            print(a.id)
        except NameError:
            print("** class doesn't exist **")
        except:
            print("** class name missing **")

    def do_show(self, args):
        sw = 0
        arg = args.split()
        if args == "":
            print("** class name missing **")
        elif arg[0] not in HBNBCommand.class_list:
            print("** class doesn't exist **")
        elif len(arg) < 2:
            print("** instance id missing **")
        else:
            in_key = (arg[0] + "." +  arg[1])
            for key, obj in storage.all().items():
                if key == in_key:
                    print(obj)
                    sw = 1
            if sw == 0:
                print("** no instance found **")

    def do_destroy(self):
        pass
    def do_all(self, args):
        l = []
        if args == "":
            for key, obj in storage.all().items():
                l.append(str(obj))
            print(l)
        elif args in HBNBCommand.class_list:
            for key, obj in storage.all().items():
                if args == key.split(".")[0]:
                        l.append(str(obj))
            print(l)
        else:
            print("** class doesn't exist **")


if __name__ == "__main__":
    comand = HBNBCommand()
    comand.cmdloop()
