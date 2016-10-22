class TwtIndentationError(ValueError):
    pass


def twt(lines):
    """
    Takes an iterable of lines (ignores line endings) and does its magic.

    Yields lines (no line endings).
    """

    current_indents = [0]
    new_block = False

    for line in lines:
        if "\t" in line:
            raise TwtIndentationError("no tabs allowed")

        new_indent = len(line) - len(line.lstrip())
        line = line.rstrip()

        if line.strip() == "":
            yield ""
            continue

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

        yield line

    while 0 < current_indents[-1]:
        current_indents.pop()
        yield (" " * current_indents[-1]) + "}"
