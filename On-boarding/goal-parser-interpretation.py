class Solution:
    def interpret(self, command: str) -> str:
        gp = ""
        command = list(command)
        for i in range(len(command)):
            if command[i] == "G":
                gp += "G"
            elif command[i] == "(":
                i +=1
                if command[i] == ")":
                    gp += "o"
                if command[i] == "a":
                    gp += "al"
            i += 1
        return gp
            
            
