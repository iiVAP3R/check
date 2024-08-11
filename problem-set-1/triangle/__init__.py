import check50


@check50.check()
def fileExists():
    """ check file exist """
    check50.exists("triangle.py")
    check50.include("1.txt", "6.txt", "9.txt", "12.txt")


@check50.check(fileExists)
def check_reject_negative():
    """ check reject negative """
    check50.run("python3 triangle.py").stdin("-69").reject()


@check50.check(fileExists)
def check_reject_empty():
    """ check reject empty input """
    check50.run("python3 triangle.py").stdin("").reject()


@check50.check(fileExists)
def check_reject_zero():
    """ check reject zero """
    check50.run("python3 triangle.py").stdin("0").reject()


@check50.check(fileExists)
def check_input_1():
    """ check if output correct if input = 1"""
    program_output = check50.run("python3 triangle.py").stdin("-1").reject().stdin("1").stdout()
    expected_output = open("1.txt").read()
    check_output(expected_output, program_output)


@check50.check(fileExists)
def check_input_6():
    """ check if output correct if input = 6"""
    program_output = check50.run("python3 triangle.py").stdin("6").stdout()
    expected_output = open("6.txt").read()
    check_output(expected_output, program_output)


@check50.check(fileExists)
def check_input_9():
    """ check if output correct if input = 9"""
    program_output = check50.run("python3 triangle.py").stdin("9").stdout()
    expected_output = open("9.txt").read()
    check_output(expected_output, program_output)


@check50.check(fileExists)
def check_input_12():
    """ check if output correct if input = 12"""
    program_output = check50.run("python3 triangle.py").stdin("12").stdout()
    expected_output = open("12.txt").read()
    check_output(expected_output, program_output)



def check_output(program_output, expected_output):
    if program_output == expected_output:
        return

    output = [line for line in program_output.splitlines() if line != ""]
    correct = expected_output.splitlines()

    help = None
    if len(output) == len(correct):
        if all(ol.rstrip() == cl for ol, cl in zip(output, correct)):
            help = "Did you add too much trailing whitespace to the end of your pyramid?"
        elif all(ol[1:] == cl for ol, cl in zip(output, correct)):
            help = "Are you printing an additional character at the beginning of each line?"

    raise check50.Mismatch(expected_output, program_output, help=help)