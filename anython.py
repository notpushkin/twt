class TwtIndentationError(ValueError):
    pass


def all_equal(value, iterable):
    return all(map(lambda x: x == value, iterable))


def twt(lines, insert_semi=True,
        braces_begin="([{", braces_end=")]}", quote_marks="\"'`",
        block_begin="{", block_end="}"):
    """
    Takes an iterable of lines (ignores line endings) and does its magic.

    Yields lines (no line endings).
    """

    current_indents = [0]
    open_braces = {ch: 0 for ch in braces_begin}
    brace_map = dict(zip(braces_end, braces_begin))
    open_quotes = {ch: False for ch in quote_marks}
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
            yield (" " * current_indents[-1]) + block_end

        if insert_semi:
            skip_next = False
            for ch in line:
                if skip_next:
                    skip_next = False
                    continue

                if ch == "\\":
                    skip_next = True
                elif ch in braces_begin:
                    open_braces[ch] += 1
                elif ch in braces_end:
                    open_braces[brace_map[ch]] -= 1
                elif ch in quote_marks:
                    open_quotes[ch] = not open_quotes[ch]

        if line.endswith(":"):
            line = line.rstrip(":") + " " + block_begin
            new_block = True

        if insert_semi \
                and not new_block \
                and line[-1] not in ";\\" \
                and all_equal(0, open_braces.values()) \
                and all_equal(False, open_quotes.values()):
            line += ";"

        yield line

    while 0 < current_indents[-1]:
        current_indents.pop()
        yield (" " * current_indents[-1]) + block_end


if __name__ == '__main__':
    import sys
    import json
    for line in twt(sys.stdin, **json.loads(sys.argv[1])):
        print(line)
