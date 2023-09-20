outputlist = []
inputstr = ''
 
while inputstr != "done":
    inputstr = input()
    # check if input is sentinel value
    if inputstr != "done":
        inputlist = []
        # fill list with letters from input
        for letter in inputstr:
            inputlist.append(letter)
 
        output = ""
        check = inputlist[0]
        amount = 0
 
        # foreach letter
        i = 0
        while i < len(inputlist):
            # if letter is the same as the letter to check, add 1 to amount
            if inputlist[i] == check:
                amount += 1
            else:
                # if letter is not the same as the letter to check, add amount and letter to output
                # change the letter to check
                # put the amount back to 1
                output += str(amount) + check
                check = inputlist[i]
                amount = 1
            
            i += 1
 
            # if it is the last letter, add amount and letter to output
            if i == len(inputlist):
                output += str(amount) + check
        
        # add output to outputlist
        outputlist.append(output)
 
# print outputlist
for output in outputlist:
    print(output)