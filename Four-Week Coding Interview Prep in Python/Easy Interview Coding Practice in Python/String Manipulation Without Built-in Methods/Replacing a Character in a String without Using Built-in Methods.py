def replace_character(input_string, c1, c2):
    replaced_string = ""

    for character in input_string:
        if character == c1:
            replaced_string += c2
            continue
        replaced_string += character

    return replaced_string
