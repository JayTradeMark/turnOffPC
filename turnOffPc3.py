#! python3
# An even better version of the program lol

import os, sys, re


def timeInSeconds():
    args = sys.argv[1:]
    numArg = []
    alphaArg = []
    for i in args:
        if i.isalpha():
            alphaArg.append(i[0].lower())
        elif re.search("[0-9]", i):
            numArg.append(i)

    def makeItHappen():
        for index, s in enumerate(alphaArg):
            match s:
                case "h":
                    alphaArg[index] = 3600
                case "m":
                    alphaArg[index] = 60

    makeItHappen()
    return (int(numArg[0]) * alphaArg[0]) + (int(numArg[1]) * alphaArg[1])


if __name__ == "__main__":
    time = timeInSeconds()
    os.system(f'shutdown -s -t {time}')
