import exceptionCollection

class DFA(object):
    
    def __init__(self,alphabets, states, initialState, finalStates, transitionRule):
        self.alphabets = alphabets
        self.states = states
        self.initialState = initialState
        self.finalStates = finalStates
        self.transitionRule = transitionRule
        self.currentState = None
        if not self.checkDFA():
            raise exceptionCollection.NDFAError(self.transitionRule)

    def checkDFA(self):
        try:
            for state in  self.states:
                for alphabet in self.alphabets:
                    self.transitionRule[(state,alphabet)]
        except KeyError:
            return False
        return True

    def setInitalState(self):
        self.currentState = self.initialState

    def resetState(self):
        self.currentState = None

    def checkFinalState(self):
        if set(self.currentState) & self.finalStates:
                return True
        else:
                return False

    def checkString(self):
        if len(set([i for i in self.inputString]) - self.alphabets):
           return False
        return True
        
    def processAlphabet(self):
        for i in self.inputString:
            self.currentState = self.transitionRule[(self.currentState, i)]
        
    def start(self, inputString):
        self.inputString = inputString
        if inputString:
            if not self.checkString():
                raise exceptionCollection.StringError(self.inputString)
            self.setInitalState()
            self.processAlphabet()
            return self.checkFinalState()
        elif set(self.initialState) & set(self.finalStates):
            return True
        return False

if __name__ == '__main__':
    
    alphabets = set(['0','1'])
    states = set(['a','b'])
    initialState = set('a')
    endState = set(list('b'))
    transitionRule = {
        ('a','0') : 'b',
        ('a', '1') : 'a',
        ('b','0') : 'b',
        ('b','1'): 'a'
    }
    dfa = DFA(alphabets,states,initialState,endState,transitionRule)
    print(dfa.start(input('> ')))