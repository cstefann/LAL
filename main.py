import nltk
import clips
import inspect

# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')

'''POS Tagging'''

sentence_post_tagging = ""
sentence = """Today morning, Arthur felt very good."""
tokens = nltk.word_tokenize(sentence)
tagged = nltk.pos_tag(tokens)

for i in tagged:
    if (i[1] == "."):
        sentence_post_tagging = sentence_post_tagging + i[1]
    else:
        sentence_post_tagging = sentence_post_tagging + i[1] + " "

''' ------------------------------------------------------- '''

''' Clips Part'''

template_string = """
(deftemplate input
    (slot sentence (type STRING))
    (slot G1 (type STRING))
    (slot G2 (type STRING)) 
    (slot G3 (type STRING)) 
    (slot G4 (type STRING)) 
    (slot G5 (type STRING)) 
    (slot G6 (type STRING)) 
    (slot G7 (type STRING)) 
    (slot G8 (type STRING))     
)
"""

''' -------------- '''

env = clips.Environment()
 
env.build(template_string)
 
template = env.find_template('input')
 
fact = template.new_fact()
fact.update({
    "sentence" : sentence_post_tagging,
    "G1" : "S NN A",
    "G2" : "A NN B",
    "G3" : "B , C",
    "G4" : "C NNP D",
    "G5" : "D VBD E",
    "G6" : "E RB F",
    "G7" : "F JJ G",
    "G8" : "G ."
})
fact.assertit()
 
for fact in env.facts():
    print(fact)
