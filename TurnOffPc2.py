#! python3
#A better version of the original program

import sys
import os


def convert(time, x_in_seconds=3600):
    converted_time = float(time) * x_in_seconds
    return int(converted_time)


try:
    if sys.argv[1].lower().startswith('h'):
        in_seconds = convert(sys.argv[2])
        os.system(f'shutdown -s -t {int(in_seconds)}')
        #print("Pc will be turning off in: " + sys.argv[2] + " Hours")

    elif sys.argv[1].lower().startswith('m'):
        in_seconds = convert(sys.argv[2], 60)
        os.system(f'shutdown -s -t {in_seconds}')
        #print("Pc will be turning off in: " + sys.argv[2] + " Minutes")

    else:
        raise ValueError("Usage: 'turnoffpc [Time Type(Hour or Minute)] [Amount(1, 1.5, 2, 2.5, ...)]'")

    print("Pc will be turning off in: " + sys.argv[2] + sys.argv[1])

except ValueError as err:
    print(str(err))

except IndexError as err:
    print(str("Usage: 'turnoffpc [Time Type(Hour or Minute)] [Amount(1, 1.5, 2, 2.5, ...)]'"))




