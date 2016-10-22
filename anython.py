class TwtIndentationError(ValueError):
    pass


def all_equal(value, iterable):
    return all(map(lambda x: x == value, iterable))


def twt(lines, insert_semi=True):
    """
    Takes an iterable of lines (ignores line endings) and does its magic.

    Yields lines (no line endings).
    """

    current_indents = [0]
    open_braces = [0, 0, 0]  # (), [], {}
    open_quotes = [False, False, False]  # "", '', ``
    new_block = False

    for line in lines:
        if "\t" in line:
            raise TwtIndentationError("no tabs allowed")

        new_indent = len(line) - len(line.lstrip())
        line = line.rstrip()

        if line.strip() == "":
            yield ""
            continue

        if insert_semi:
            for ch in line:
                if ch == "(":
                    open_braces[0] += 1
                elif ch == ")":
                    open_braces[0] -= 1
                elif ch == "[":
                    open_braces[1] += 1
                elif ch == "]":
                    open_braces[1] -= 1
                elif ch == "{":
                    open_braces[2] += 1
                elif ch == "}":
                    open_braces[2] -= 1
                elif ch == '"':
                    open_quotes[0] ^= True
                elif ch == "'":
                    open_quotes[1] ^= True
                elif ch == "`":
                    open_quotes[2] ^= True

        if new_block:
            if new_indent <= current_indents[-1]:
                raise TwtIndentationError("expected an indented block")
            current_indents.append(new_indent)
            new_block = False

        while new_indent < current_indents[-1]:
            current_indents.pop()
            yield (" " * current_indents[-1]) + "}"

        if line.endswith(":"):
            line = line.rstrip(":") + " {"
            new_block = True

        if insert_semi and all_equal(0, open_braces) \
                       and all_equal(False, open_quotes) \
                       and not new_block:
            yield line + ";"
        else:
            yield line

    while 0 < current_indents[-1]:
        current_indents.pop()
        yield (" " * current_indents[-1]) + "}"


if __name__ == '__main__':
    import sys
    for line in twt(sys.stdin):
        print(line)
