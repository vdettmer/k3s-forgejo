import os
import argparse

port = 222

def executeCommand(input):
    os.system(generateCommand(input))

def generateCommand(input):
    Repo = cutRepo(input)
    firstbit = Repo[0]
    lastbit = Repo[-1]
    return("git clone ssh://"+firstbit+":"+str(port)+"/"+lastbit)

def cutRepo(input):
    return(input.split(':'))

def main(*args):
    parser = argparse.ArgumentParser()
    parser.add_argument("pfad")
    args = parser.parse_args()
    executeCommand(args.pfad)

if __name__ == "__main__":
    main()
