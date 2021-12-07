###############################################################
#       ART GENERATOR BY PHOENIX "OCCULTNIX" KANE, 2017       #
#                                                             #
# - Colors list from Color Thesaurus by Ingrid Sundberg       #
# - Adjectives list via gingersoftware.com                    #
# - Emotions list from Emotion Knowledge by Dr Phillip Shaver #
###############################################################

# import packages
import sqlite3
import random
from sqlite3 import Error
from tkinter import *

# initiate packages and variables
random.seed()
root = Tk()
line1 = StringVar()
line2 = StringVar()
line3 = StringVar()
expressions = [ "aroused", "desperate", "flustered", "concerned", "glaring" ]

conjunction = [" and ", " or "]

# grab random info from the database and save it to our variables
def random_stuff():
    # connect to the database and set our cursor
    conn = sqlite3.connect('artfuel.db')
    c = conn.cursor()

    # randomize the colors and grab two, then set them to line1
    c.execute("SELECT color FROM COLORS ORDER BY RANDOM() LIMIT 2")
    colors = c.fetchall()
    line1.set(colors[0][0] + conjunction[random.randrange(len(conjunction))] + colors[1][0])

    # randomize the adjectives and grab two, then set them to line2
    c.execute("SELECT adjective FROM ADJECTIVES ORDER BY RANDOM() LIMIT 2")
    adjectives = c.fetchall()
    line2.set(adjectives[0][0] + conjunction[random.randrange(len(conjunction))] + adjectives[1][0])

    # randomize the emotions and grab one, then set it to line3
    c.execute("SELECT emotion FROM EMOTIONS ORDER BY RANDOM() LIMIT 1")
    emotions = c.fetchall()
    line3.set("evocative of " + emotions[0][0])

    # close connection to the database
    conn.commit()
    conn.close()

# define a window with labels for colors/adjectives/emotion and a generate button
line1_label = Label(root, width=25, height=1, textvariable = line1).pack()
line2_label = Label(root, width=25, height=1, textvariable = line2).pack()
line3_label = Label(root, width=25, height=1, textvariable = line3).pack()
generate_button =  Button(root, width=15, height=2, text="New", command=random_stuff).pack()

# establish the generator's loop from tkinter
root.mainloop()