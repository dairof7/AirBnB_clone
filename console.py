#!/usr/bin/python3
"""This module contain the HBNB console"""

import cmd
from models.base_model import BaseModel
from models.user import User
from models import storage
import inspect
import models


class HBNBCommand(cmd.Cmd):
    """Command line interpreter HBNB"""
    prompt = "(hbnb) "
    class_list = ["BaseModel", "User"]
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
        """Creates a new class instance and print the Id"""
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
        """Prints the string representation of an instance based
        on the class name and id"""
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

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id
        updating JSON file"""
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
            dict_objects = storage.all()
            for key, obj in dict_objects.items():
                if key == in_key:
                    del dict_objects[key]
                    sw = 1
                    storage.save()
                    storage.reload()
                    return
            if sw == 0:
                print("** no instance found **")
    def do_all(self, args):
        """Prints all string representation of all instances
        based or not on the class name"""
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

    def do_update(self, args):
        """Updates an instance based on the class name and id by adding or
        updating attribute, saving on JSON file"""
        arg = args.split()
        sw = 0
        if len(arg) < 1:
            print("** class name missing **")
        elif arg[0] not in HBNBCommand.class_list:
            print("** class doesn't exist **")
        elif len(arg) < 2:
            print("** instance id missing **")
        elif len(arg) < 3:
            print("** attribute name missing **")
        elif len(arg) < 4:
            print("** value missing **")
        else:
            in_key = (arg[0] + "." +  arg[1])
            for key, obj in storage.all().items():
                if key == in_key:
                    value = arg[3]
                    if hasattr(obj, arg[2]):
                        value = type(getattr(obj, arg[2]))(arg[3])
                    setattr(obj, arg[2], value)
                    sw = 1
                    storage.save()
                    storage.reload()
            if sw == 0:
                print("** no instance found **")



if __name__ == "__main__":
    comand = HBNBCommand()
    comand.cmdloop()
