import keysList as k
class Parser:
    rawArr = []
    process1 = []
    def __init__(self, rawStr):
        tempArr = []
        for i in str(rawStr).split("\n"):
            for o in i.split(" "):
                tempArr.append(o)
        for i in range(tempArr.count('')): 
            tempArr.remove('') 
        self.rawArr = tempArr
    def scanFunc(self):
        overrallArr = []
        pos = 0
        for i in self.rawArr:
            tempDict = {}
            if i in k.functionDenoters:
                tempArr = self.rawArr[pos:]

                for elements in tempArr:
                    if "{" in elements:
                        endPos = tempArr.index(elements)
                        break
                fullStatement = ""
                tempDict["Execution Type"] = "Function"
                tempDict["Keyword"] = i
                print(i)
                for index in range(endPos):
                    fullStatement += str(tempArr[index + 1] + " ").replace("{", "")
                tempDict["Condition"] = fullStatement[:-1]
                print(fullStatement + "\n")
                overrallArr.append(tempDict)
            
            pos += 1
        return overrallArr
        
  