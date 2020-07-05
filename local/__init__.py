from local.localparse import parse
from local.localast import walk_the_tree


def output_code(code):
    """Return string, which is target Python program."""
    # Initialize variables
    import_convertdist = False
    import_dist = False
    # import_sys = False
    # Determine if we need to import anything
    if "convertdist(" in code:
        import_convertdist = True
    if " dist(" in code:
        import_dist = True
    # if "argv[" in code:
    #     import_sys = True
    # Split on newlines, then we'll remove emtpy lines
    code = code.split("\n")
    # One can go insane making newlines/empty lines perfect throughout the
    # compiler, or they can be stripped out here
    clean_code = []  # add import statments here if need be
    if import_convertdist:
        clean_code.append("from local.libs.conversion import convertdist")
    if import_dist:
        clean_code.append("from local.libs.haversine import dist")
    for line in code:
        if not line.strip():
            # Blank line
            continue
        else:
            clean_code.append(line)
    # Print file sans empty lines
    return "\n".join(clean_code)


def tester(testinput):
    """Driver function to be used by test suite."""
    ast_test = parse(testinput)
    code = walk_the_tree(ast_test)
    return output_code(code)