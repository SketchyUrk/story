from time import sleep

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
    print("""Commands:
          Interact with an item with 'USE <item>'
          Look around by using 'look'
          Move around using 'goto <location>'
          You can view these commands anytime with 'help'
          Good Luck!""")
    
def gameStart():
    print("You wake up in your home, but fi")