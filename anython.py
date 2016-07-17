class AnythonIndentationError(IndentationError):
    pass

with open("test.icss") as fi:
    current_indents = [0]
    new_block = False

    for line in fi.readlines():
        if "\t" in line:
            raise AnythonIndentationError("no tabs allowed")

        new_indent = len(line) - len(line.lstrip())
        line = line.rstrip()

        if line.strip() == "":
            print("")
            continue

        if new_block:
            if new_indent <= current_indents[-1]:
                raise AnythonIndentationError("expected an indented block")
            current_indents.append(new_indent)
            new_block = False

        while new_indent < current_indents[-1]:
            current_indents.pop()
            print((" " * current_indents[-1]) + "}")

        if line.endswith(":"):
            line = line.rstrip(":") + " {"
            new_block = True

        print(line)

    while 0 < current_indents[-1]:
        current_indents.pop()
        print((" " * current_indents[-1]) + "}")
