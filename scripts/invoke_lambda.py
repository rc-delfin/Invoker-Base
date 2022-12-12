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
        flash("Button 1 pressed. Lambda invocation successful")
    else:
        flash("Button 1 pressed. Lambda invocation failed")


def run_lambda2():
    print("Lambda 2 ran")
    rn = get_rand()
    if rn % 2 == 0:
        flash("Button 2 pressed. Lambda invocation successful")
    else:
        flash("Button 2 pressed. Lambda invocation failed")


def run_lambda3():
    print("Lambda 3 ran")
    rn = get_rand()
    if rn % 2 == 0:
        flash("Button 3 pressed. Lambda invocation successful")
    else:
        flash("Button 3 pressed. Lambda invocation failed")


def run_lambda4():
    print("Lambda 4 ran")
    rn = get_rand()
    if rn % 2 == 0:
        flash("Button 4 pressed. Lambda invocation successful")
    else:
        flash("Button 4 pressed. Lambda invocation failed")


def run_lambda5():
    print("Lambda 5 ran")
    rn = get_rand()
    if rn % 2 == 0:
        flash("Button 5 pressed. Lambda invocation successful")
    else:
        flash("Button 5 pressed. Lambda invocation failed")


def run_lambda6():
    print("Lambda 6 ran")
    rn = get_rand()
    if rn % 2 == 0:
        flash("Button 6 pressed. Lambda invocation successful")
    else:
        flash("Button 6 pressed. Lambda invocation failed")


def run_lambda7():
    print("Lambda 7 ran")
    rn = get_rand()
    if rn % 2 == 0:
        flash("Button 7 pressed. Lambda invocation successful")
    else:
        flash("Button 7 pressed. Lambda invocation failed")


def run_lambda8():
    print("Lambda 8 ran")
    rn = get_rand()
    if rn % 2 == 0:
        flash("Button 8 pressed. Lambda invocation successful")
    else:
        flash("Button 8 pressed. Lambda invocation failed")


def run_lambda9():
    print("Lambda 9 ran")
    rn = get_rand()
    if rn % 2 == 0:
        flash("Button 9 pressed. Lambda invocation successful")
    else:
        flash("Button 9 pressed. Lambda invocation failed")


def run_lambda0():
    print("Lambda 0 ran")
    rn = get_rand()
    if rn % 2 == 0:
        flash("Button 0 pressed. Lambda invocation successful")
    else:
        flash("Button 0 pressed. Lambda invocation failed")
