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
    (slot answer (type STRING))
    (slot G1 (type STRING))
    (slot G2 (type STRING)) 
    (slot G3 (type STRING)) 
    (slot G4 (type STRING)) 
    (slot G5 (type STRING)) 
    (slot G6 (type STRING))
)
"""
read_input_rule_string = """
(defrule read_input
    ?a <- (sentence)
    =>
    (assert (text S (explode$ (sentence))))
    (retract ?a)
)
"""

apply_rule_string = """
(defrule apply_rule
    (?g ?nonterminal ?first ?next)
    ?a <- (text ?nonterminal ?first $?rest)
    ?b <- (answer $?steps)
    =>
    (assert (text ?next $?rest))
    (assert (answer $?steps ?g))
    (retract ?a)
    (retract ?b)
)
"""

succes_rule_string = """
(defrule success
    ?a <- (text EPS)
    (answer $?steps)
    =>
    (printout t "YES" $?steps crlf)
    (retract ?a)
)
"""

fail_rule_string = """
(defrule failure
    ?a <- (text $?)
    =>
    (printout t "NO" crlf)
    (retract ?a)
)
"""

''' -------------- '''

env = clips.Environment()
 
env.build(template_string)
env.build(read_input_rule_string)
 
template = env.find_template('input')
 
fact = template.new_fact()
fact.update({
    "sentence" : sentence_post_tagging,
    "answer" : "",
    "G1" : "S NN A",
    "G2" : "A NN B",
    "G3" : "B NNP C",
    "G4" : "C VBD D",
    "G5" : "D RB E",
    "G6" : "E JJ F"
})
fact.assertit()
 
for fact in env.facts():
    print(fact)

for rule in env.rules():
    print(rule)
