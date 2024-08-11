import check50
import re

@check50.check()
def fileExists():
    """ does ur file exist sussy amongus """
    check50.exists("syntax-errors.py")

@check50.check(fileExists)
def test0():
    """ Tests if the program runs as expected (H = 6, R = 9, expected = 508.94)"""
    program_output = check50.run("python syntax-errors.py").stdin("6").stdin("9").stdout()
    program_output = re.search(r"(\d+\.\d+)", program_output)
    if not program_output:
        raise check50.Failure("Output does not contain a numeric value")
    
    program_output = int(program_output.group(1))
    expected_output = 508.94

    if program_output != expected_output:
        raise check50.Mismatch(str(expected_output), str(program_output))


@check50.check(fileExists)
def test1():
    """ Tests if the program runs as expected (H = 2, R = 2, expected 8.38)"""
    program_output = check50.run("python syntax-errors.py").stdin("2").stdin("2").stdout()
    program_output = re.search(r"(\d+\.\d+)", program_output)
    if not program_output:
        raise check50.Failure("Output does not contain a numeric value")
    
    program_output = int(program_output.group(1))
    expected_output = 8.38

    if program_output != expected_output:
        raise check50.Mismatch(str(expected_output), str(program_output))
    

@check50.check(fileExists)
def test2():
    """ Tests if the program runs as expected (H = 4, R = 20, expected 335.1)"""
    program_output = check50.run("python syntax-errors.py").stdin("4").stdin("20").stdout()
    program_output = re.search(r"(\d+\.\d+)", program_output)
    if not program_output:
        raise check50.Failure("Output does not contain a numeric value")
    
    program_output = int(program_output.group(1))
    expected_output = 1675.52

    if program_output != expected_output:
        raise check50.Mismatch(str(expected_output), str(program_output))
    