import nltk
import clips
import inspect
from tkinter import *

# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')

# input -> Today morning, Arthur felt very good

def pos_tagg(sentence):
    sentence_post_tagged = ""
    tokens = nltk.word_tokenize(sentence)
    tagged = nltk.pos_tag(tokens)

    for i in tagged:
        if (i[1] == "."):
            sentence_post_tagged = sentence_post_tagged + i[1]
        else:
            sentence_post_tagged = sentence_post_tagged + i[1] + " "
    return sentence_post_tagged

def parse_input(sentence):
    sentence_post_tagged = pos_tagg(sentence)
    env = clips.Environment()
    env.clear()
    env.load('LAL.clp')
    env.reset()

    ''' Facts - Base parsing rules '''

    fact = env.assert_string('(text S ' + sentence_post_tagged + ')')
    fact = env.assert_string('(answer)')
    fact = env.assert_string('(rule G1  S NN A)')
    fact = env.assert_string('(rule G2  A NN B)')
    fact = env.assert_string('(rule G3  B , C)')
    fact = env.assert_string('(rule G4  C NNP D)')
    fact = env.assert_string('(rule G5  D VBD E)')
    fact = env.assert_string('(rule G6  E RB F)')
    fact = env.assert_string('(rule G7  F JJ H)')
    fact = env.assert_string('(rule G8  H . EPS)')

    print("Input received: " + sentence)
    print("POS Tagged version: " + sentence_post_tagged)
    print("Result from CLIPS code: ")

    env.run()

''' GUI '''

root = Tk()
root.geometry("500x500")

Label(root, text="Learn a Language", fg="black", font=('times', 20, 'normal')).pack()
Label(root, text="", fg="red").pack()

def click1():
    input_data = entry.get()
    parse_input(input_data)

# Apeleaza aceleasi functii ca si click1 (verifica daca inputul poate fi parsat pe baza regulilor date manual)

def click2():
    input_data = entry.get()
    parse_input(input_data)

topframe = Frame(root)
topframe.winfo_toplevel().title("LAL")
entry = Entry(topframe, width=50)
entry.pack()

Label(topframe, text="", fg="red").pack()

button1 = Button(topframe, text="Learn a grammer", bg='black', fg='white', command=click1)
button1.pack(side=LEFT)
button2 = Button(topframe, text="Parse an input", bg='black', fg='white', command=click2)
button2.pack(side=RIGHT)

topframe.pack(side=TOP)

bottomframe = Frame(root)

my_finishURL = Label(bottomframe, text="")
my_finishURL.pack(pady=20)
bottomframe.pack()
root.mainloop()