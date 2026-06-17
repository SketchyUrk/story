from time import sleep

interact = ["use","read","open"]

def gapPrint(text):
    print("\n"+str(text)+"\n")

def tprint(text:str, delay:float=.1):
    for char in text:
        print(
            char,
            end="",
            flush=True
        )
        sleep(delay)



def commandHelp():
    print("""
          Commands:
          Interact with an item with 'USE/READ/OPEN <item>'
          Look around by using 'look'
          Move around using 'goto <location>'
          You can view these commands anytime with 'help'
          
          Items you can interact with will be indicated: *<item>*
          Good Luck!
          """)

def getCommand(whereAreWe:function ,locations:list=[], items:list=[]):
    
    command = input("> ")

    for i in range(len(interact)):
        if interact[i] in command.lower():
            return "interact"
    
    if 'look' in command.lower():
        return 'look'
    
    elif 'goto' in command.lower():
        for i in range(len(locations)):
            if locations[i] in command.lower():
                return f'goto {locations[i]}'

    elif 'help' in command.lower():
        commandHelp()
        whereAreWe()

    else:
        gapPrint("That is not a valid command. Try again.")
        getCommand()



def actOne():
    
    print("You wake up in your home, but find that a *brick* has been thrown through your window.\n" \
    "Tied to the *brick* is a *letter*.\n")

