#!/usr/bin/env pybricks-micropython
import time

def write_log(x, y, angle, distance):
    date_string = time.strftime("%d-%m-%Y")
    time_string = time.strftime("%H:%M:%S")
    message = "{};{};{};{}\n".format(x, y, angle, distance)

    # Écrire la donnée dans le fichier txt
    with open('log.txt', 'a') as file:
        file.write(message)

def clear_log():
    with open("log.txt", "w") as f:
        f.write("")

#command : python, evcurves.py log.txt courbes