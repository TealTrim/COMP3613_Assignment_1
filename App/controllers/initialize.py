#from .user import create_user
from .competition import create_competition
from .result import create_result
from App.database import db


def initialize():
    db.drop_all()
    db.create_all()
    #create_user('bob', 'bobpass')
    create_competition(1, "Scripting Soldiers")
    create_competition(2, "Fortran Fighters")
    create_competition(3, "C++ Champions")
    create_competition(4, "Typescript Troppers")
    create_competition(5, "Java Janitors")
    create_competition(6, "Super Scratch")
    create_competition(7, "Terminal Terminators")
    create_competition(8, "C Challengers")
    create_competition(9, "Memory Management Masters")
    create_competition(10, "Assembly Anihilators")
    create_result(101, 1, "Ada Lovlace", 8)
    create_result(202, 2, "Linus Torvalds", 16)
    create_result(303, 3, "Alan Turing", 24)
    create_result(404, 4, "Dennis Ritchie", 32)
    create_result(505, 5, "Grace Hopper", 64)
