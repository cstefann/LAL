(defrule apply_rule
        (rule ?g ?nonterminal ?first ?next)
        ?a <- (text ?nonterminal ?first $?rest)
        ?b <- (answer $?steps)
        =>
        (assert (text ?next $?rest))
        (assert (answer $?steps ?g))

        (retract ?a)
        (retract ?b)
)

(defrule success
        ?a <- (text EPS)
        (answer $?steps)
        =>
        (printout t "YES" $?steps crlf)

        (retract ?a)
)

(defrule failure
        ?a <- (text $?)
        =>
        (printout t "NO" crlf)

        (retract ?a)
)