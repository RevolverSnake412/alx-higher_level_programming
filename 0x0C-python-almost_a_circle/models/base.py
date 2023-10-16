#!/usr/bin/python3
"""base.py"""
import json
import turtle
import csv


class Base:
    """The Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializing"""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """dict to json string"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save to file"""
        file_path = cls.__name__ + ".json"
        with open(file_path, "w") as json_file:
            if list_objs is None:
                json_file.write("[]")
            else:
                list_dicts = [i.to_dictionary() for i in list_objs]
                json_file.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """from json string"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """create"""
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """load from file"""
        file_path = str(cls.__name__) + ".json"
        try:
            with open(file_path, "r") as json_file:
                list_dicts = Base.from_json_string(json_file.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write the CSV serialization of a list of objects to a file.

        Args:
            list_objs (list): A list of inherited Base instances.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """load from file csv"""
        file_path = cls.__name__ + ".csv"
        try:
            with open(file_path, "r", newline="") as csv_file:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csv_file, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """draw using turtle lib"""
        tur = turtle.Turtle()
        tur.screen.bgcolor("#000000")
        tur.shape("blank")

        tur.color("#228B22")
        for rectangle in list_rectangles:
            tur.up()
            tur.goto(rectangle.x, rectangle.y)
            tur.down()
            for i in range(2):
                tur.forward(rectangle.width)
                tur.right(90)
                tur.forward(rectangle.height)
                tur.right(90)

        for square in list_squares:
            tur.up()
            tur.goto(square.x, square.y)
            tur.down()
            for i in range(2):
                tur.forward(square.width)
                tur.left(90)
                tur.forward(square.height)
                tur.left(90)

        turtle.exitonclick()
