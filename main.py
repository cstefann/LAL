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
    (slot ruleG1 (type STRING))
    (slot ruleG2 (type STRING)) 
    (slot ruleG3 (type STRING)) 
    (slot ruleG4 (type STRING)) 
    (slot ruleG5 (type STRING)) 
    (slot ruleG6 (type STRING)) 
    (slot ruleG7 (type STRING)) 
    (slot ruleG8 (type STRING))     
)
"""

''' -------------- '''

env = clips.Environment()
 
env.build(template_string)
 
template = env.find_template('input')
 
fact = template.new_fact()
fact.update({
    "sentence" : sentence_post_tagging,
    "ruleG1" : "S NN A",
    "ruleG2" : "A NN B",
    "ruleG3" : "B , C",
    "ruleG4" : "C NNP D",
    "ruleG5" : "D VBD E",
    "ruleG6" : "E RB F",
    "ruleG7" : "F JJ G",
    "ruleG8" : "G ."
})
fact.assertit()
 
for fact in env.facts():
    print(fact)
