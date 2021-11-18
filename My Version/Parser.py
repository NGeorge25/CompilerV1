import keywords

def run(data):
    parser = Parser(data)
    parser.processLine()

class Token:
    def __init__(this, TK, startPos, endPos):
        this.token = TK
        this.startIndex = startPos
        this.endIndex = endPos
    def toString(this):
        return f'Token: \'{this.token}\' at Index {this.startIndex} : {this.endIndex}'

class Parser:
    def __init__(this, data):
        this.data = data
        this.currentChar = None
        this.currentLine = None
        this.Lines = str(data).split("\n")
        print(this.Lines)
        this.pos = -1
        this.advance()

    def processLine(this):
        tokens = []
        for i in list(keywords.words.keys()):
            if i in this.data:
                location = str(this.data).index(i)
                tokens.append(Token(i, location, location + len(i)))
        print(tokens[0].toString())

    def functions(this, keyword):
        variables = []
        instructions = keywords.words[keyword]|None
        if instructions:
            for i in instructions:
                if i == "VAR":
                    variables.append(str(this.data).s)

    def advance(this):
        this.pos += 1
        this.currentChar = this.data[this.pos]
        while this.currentChar in " \t":
            this.pos += 1
            this.currentChar = this.data[this.pos]
