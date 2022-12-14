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
    success_fail(rn, value)
