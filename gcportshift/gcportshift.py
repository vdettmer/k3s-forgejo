import os
import argparse
import logging
logging.basicConfig(filename='mylog.log',level=logging.DEBUG)

port = 222

def executeCommand(input):
    os.system(generateCommand(input))

def generateCommand(input):
    Repo = cutRepo(input)
    firstbit = Repo[0]+"//"+Repo[2] #ssh://git@git.vincent.lan
    lastbit = Repo[-2]+"/"+Repo[-1] #vincent/test.git
    logging.debug("input = "+input)
    logging.debug("firstbit ="+firstbit)
    logging.debug("lastbit ="+lastbit)
    logging.debug("output example: ssh://git@git.vincent.lan:222/vincent/test.git")
    output = firstbit+":"+str(port)+"/"+lastbit
    logging.debug("actual output: "+output)
    return("git clone "+output)

def cutRepo(input):
    return(input.split('/'))

def main(*args):
    parser = argparse.ArgumentParser()
    parser.add_argument("pfad")
    args = parser.parse_args()
    executeCommand(args.pfad)

if __name__ == "__main__":
    main()
