import random

from flask import flash


# Random number generated to simulate a return of success or failure of Lambda invocation.
# If even number, successful; else failed
def get_rand():
    r1 = random.randint(0, 10)
    return r1


def run_lambda1():
    print("Lambda 1 ran")
    rn = get_rand()
    if rn % 2 == 0:
        flash("Option 1 selected. Lambda invocation successful")
    else:
        flash("Option 1 selected. Lambda invocation failed")


def run_lambda2():
    print("Lambda 2 ran")
    rn = get_rand()
    if rn % 2 == 0:
        flash("Option 2 selected. Lambda invocation successful")
    else:
        flash("Option 2 selected. Lambda invocation failed")


def run_lambda3():
    print("Lambda 3 ran")
    rn = get_rand()
    if rn % 2 == 0:
        flash("Option 3 selected. Lambda invocation successful")
    else:
        flash("Option 3 selected. Lambda invocation failed")


def run_lambda4():
    print("Lambda 4 ran")
    rn = get_rand()
    if rn % 2 == 0:
        flash("Option 4 selected. Lambda invocation successful")
    else:
        flash("Option 4 selected. Lambda invocation failed")


def run_lambda5():
    print("Lambda 5 ran")
    rn = get_rand()
    if rn % 2 == 0:
        flash("Option 5 selected. Lambda invocation successful")
    else:
        flash("Option 5 selected. Lambda invocation failed")


def run_lambda6():
    print("Lambda 6 ran")
    rn = get_rand()
    if rn % 2 == 0:
        flash("Option 6 selected. Lambda invocation successful")
    else:
        flash("Option 6 selected. Lambda invocation failed")


def run_lambda7():
    print("Lambda 7 ran")
    rn = get_rand()
    if rn % 2 == 0:
        flash("Option 7 selected. Lambda invocation successful")
    else:
        flash("Option 7 selected. Lambda invocation failed")


def run_lambda8():
    print("Lambda 8 ran")
    rn = get_rand()
    if rn % 2 == 0:
        flash("Option 8 selected. Lambda invocation successful")
    else:
        flash("Option 8 selected. Lambda invocation failed")


def run_lambda9():
    print("Lambda 9 ran")
    rn = get_rand()
    if rn % 2 == 0:
        flash("Option 9 selected. Lambda invocation successful")
    else:
        flash("Option 9 selected. Lambda invocation failed")
