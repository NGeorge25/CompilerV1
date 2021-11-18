import Parser
file = """for i in range(3):\n
            pass"""
if file != "":

    result = Parser.run(file)
    print(result)

else:
    while True:
        text = input('basic > ')
        result = Parser.run(text)
        print(result)
