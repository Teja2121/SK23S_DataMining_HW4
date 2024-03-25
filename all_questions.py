# Add import files
import pickle



# -----------------------------------------------------------
def question1():
    answers = {}

    # string "yes" or "no"
    answers["(a)"] = "no"
    answers["(b)"] = "no"
    answers["(c)"] = "yes"
    answers["(d)"] = "yes"

    # explain-string: explanation in english prose
    answers["(a) explain"] = "No, the rules are not mutually exclusive because if we see the first two rules and if there is a tuple that says homeowner = yes, marital status = single, then that would trigger the first two rules."
    answers["(b) explain"] = "The rule set is not exhaustive because marital status = divorced is not covered by any of the rule set."
    answers["(c) explain"] = "Ordering is needed for the given set of rules because we have seen a conflict in part a, so to avoid that ordering is needed for the given rule set."
    answers["(d) explain"] = "A default class is necessary because the rule set is not exhaustive."

    return answers


# -----------------------------------------------------------
def question2():
    answers = {}

    # string "yes" or "no"
    answers["(a)"] = None
    answers["(b)"] = None
    answers["(c)"] = None
    answers["(d)"] = None

    # explain_string: explanation in english prose
    answers["(a) explain"] = None
    answers["(b) explain"] = None
    answers["(c) explain"] = None
    answers["(d) explain"] = None

    return answers
# -----------------------------------------------------------
def question3():
    answers = {}

    # string "yes" or "no"
    answers["(a)"] = "no"
    answers["(b)"] = "no"
    answers["(c)"] = "yes"

    # explain-string: explanation in english prose
    answers["(a) example"] = "The rules are not mutually exclusive because if we take the example of pigeon, it is warm blooded which triggers rule R3 and it also triggers rule R1 because give birth = no and aerial creature = yes."
    answers["(b) example"] = "The rules are not exhaustive because if we take the example of turtle, it is cold blooded, gives birth = no, aerial creature = no and aquatic creature = semi. But there is no rule to classify turtle."
    answers["(c) example"] = "Ordering is needed because there is overlapping of rules for pigeons and there might be others issues too."

    return answers
# -----------------------------------------------------------
def question7():
    answers = {}

    # bool: True/False
    answers["(a)"] = None
    answers["(b)"] = None
    answers["(c)"] = None
    answers["(d)"] = None

    # explain_string: explanation in english prose
    answers["(a) explain"] = None
    answers["(b) explain"] = None
    answers["(c) explain"] = None
    answers["(d) explain"] = None

    return answers

# -----------------------------------------------------------
def question8():
    answers = {}


    answers["(d) P(A=1)"] = None
    answers["(e) P(X_1=1, X_2=1|Class=+)"] = None
    answers["(e) P(X_1=1|Class=+)"] = None
    answers["(e) P(X_2=1|Class=+)"] = None

    # string: "yes" or "no"
    answers["(e) A and B conditionally independent?"] = None

    # float
    answers["(d) Training error rate"] = None



    answers["(d) P(A=1)"] = None
    answers["(d) P(X_1=1, X_2=1|Class=+)"] = None
    answers["(d) P(X_1=1|Class=+)"] = None
    answers["(d) P(X_2=1|Class=+)"] = None

    # string: "yes" or "no"
    answers["(d) A and B conditionally independent?"] = None

    # float
    answers["(d) Training error rate"] = None

    return answers

# --------------------------------------------------------
def question9():
    answers = {}

    # int
    answers["(a) K"] = 1
    answers["(b) K"] = 5

    # explain_string
    answers["(a) explain"] = "K = 1 is better for a because there is a clear boundary of seperation between the two points. Though there be chance of overfitting, a clear seperation between the points."
    answers["(b) explain"] = "k = 5 is better for b because taking k = 1 might misclassify some data and k = 50 might be too large of a value and might lead to underfitting."

    return answers

# --------------------------------------------------------
def question10():
    answers = {}

    # float
    '''p(+) = 5/10 = 0.5, p(-) = 5/10 = 0.5'''
    '''p(a = 1|+) = 3/5 = 0.6'''
    '''p(b = 1|+) = 2/5 = 0.4'''
    '''p(c = 1|+) = 4/5 = 0.8'''
    '''p(a = 1|-) = 2/5 = 0.4'''
    '''p(b = 1|-) = 2/5 = 0.4'''
    '''p(c = 1|-) = 1/5 = 0.2'''
    answers["(a) P(A=1|+)"] = 0.6
    answers["(a) P(B=1|+)"] = 0.4
    answers["(a) P(C=1|+)"] = 0.8
    answers["(a) P(A=1|-)"] = 0.4
    answers["(a) P(B=1|-)"] = 0.4
    answers["(a) P(C=1|-)"] = 0.2

    # type: explanatory string
    answers["(a) P(A=1|+) explain your answer"] = "First we have to count the + cases which are 5 (this will be the denominator), now we count how many instances are both 1 and +, which is 3 (this will be the numerator), now we do 3/5 for the case of P(A=1|+) which is 0.6"
  
    # type: float
    # note: R is the sample (A=1,B=1,C=1)
    ''' P(R|+) = P(A=1|+) * P(B=1|+) * P(C=1|+) = 0.6 * 0.4 * 0.8 = 0.192
    P(R|-) = P(A=1|-) * P(B=1|-) * P(C=1|-) = 0.4 * 0.4 * 0.2 = 0.032
    '''
    answers["(b) P(+|R)"] = None  # WRONG
    answers["(b) P(R|+)"] = 0.192
    answers["(b) P(R|-)"] = 0.032

    # string, '+' or '-'
    answers["(b) class label"] = "+"

    # explain_string
    answers["(b) Explain your reasoning"] = "The test sample given was (A = 1, B = 1, C = 1), so there are two class labels to predict (+ or -) which is P(+|R) = ((P(R|+) * P(+)) / P(R)) and P(-|R) = ((P(R|-) * P(-)) / P(R)). But in this case, P(+) and P(-) are the same that is 0.5 and P(R) is constant. So we only have to find P(R|+) and P(R|+) and the greater one among these two will be the class label."
  
    # float
    answers["(c) P(A=1)"] = 0.5
    answers["(c) P(B=1)"] = 0.4
    answers["(c) P(A=1,B=1)"] = 0.2

    # type: string, 'yes' or 'no'
    answers["(c) A independent of B?"] = "yes"
  
    # type: float
    answers["(d) P(A=1)"] = 0.5
    answers["(d) P(B=0)"] = 0.6
    answers["(d) P(A=1,B=0)"] = 0.3

    # type: string: 'yes' or 'no'
    answers["(d) A independent of B?"] = "yes"
  
    # type: float
    answers["(e) P(A=1,B=1|+)"] = 0.2
    answers["(e) P(A=1|+)"] = 0.6
    answers["(e) P(B=1|+)"] = 0.4

    # type: string: 'yes' or 'no'
    answers["(e) A independent of B given class +?"] = "no"

    # type: explanatory string
    answers["(e) A and B conditionally independent given class +, explain"] =  "A and B are not conditonally independent given class B because P(A=1|+) = 0.6 and P(B=1|+) = 0.4 and the product between them is 0.24 but P(A=1,B=1|+) = 0.2 and 0.24 is not equal to 0.2"
  
    return answers
# --------------------------------------------------------
if __name__ == '__main__':
    answers_dict = {}
    answers_dict['question1'] = question1()
    answers_dict['question2'] = question2()
    answers_dict['question3'] = question3()
    answers_dict['question7'] = question7()
    answers_dict['question8'] = question8()
    answers_dict['question9'] = question9()
    answers_dict['question10'] = question10()

    with open('answers.pkl', 'wb') as f:
        pickle.dump(answers_dict, f)
