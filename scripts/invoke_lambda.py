import random

from flask import flash


# Random number generated to simulate a return of success or failure of Lambda invocation.
# If even number, successful; else failed
def get_rand():
    r1 = random.randint(0, 10)
    return r1


def success_fail(rn, value):
    if rn % 2 == 0:
        flash("Option " + value + " selected. Lambda invocation successful")
    else:
        flash("Option " + value + " selected. Lambda invocation failed")

def run_lambda(value):
    rn = get_rand()
    if value == "b1":
        print("Lambda 1 ran")
        success_fail(rn, value)
    elif value == "b2":
        print("Lambda 2 ran")
        success_fail(rn, value)
    elif value == "b3":
        print("Lambda 3 ran")
        success_fail(rn, value)
    elif value == "b4":
        print("Lambda 4 ran")
        success_fail(rn, value)
    elif value == "b5":
        print("Lambda 5 ran")
        success_fail(rn, value)
    elif value == "b6":
        print("Lambda 6 ran")
        success_fail(rn, value)
    elif value == "b7":
        print("Lambda 7 ran")
        success_fail(rn, value)
    elif value == "b8":
        print("Lambda 8 ran")
        success_fail(rn, value)
    elif value == "b9":
        print("Lambda 9 ran")
        success_fail(rn, value)
    else:
        pass
