def check_brackets(string):
    """
    return True if all brackets have a closing pair and False if not
    """

    if len(string) % 2 != 0: return False

    brackets = {
        ')': '(',
        ']': '[',
        '}': '{',
    }

    # split `string` in 2 parts and reverse second part
    firstpart, secondpart = string[:len(string) // 2], string[len(string) // 2:][::-1]

    for index, element in enumerate(firstpart):
        try:
            if element != brackets[secondpart[index]]:
                return False
        except KeyError:
            return False
    return True
