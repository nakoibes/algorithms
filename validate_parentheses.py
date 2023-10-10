def validate_parentheses(string: str):
    counter = 0
    for symbol in string:
        if symbol == "(":
            counter += 1
        else:
            counter -= 1

        if counter < 0:
            return False

    return True
