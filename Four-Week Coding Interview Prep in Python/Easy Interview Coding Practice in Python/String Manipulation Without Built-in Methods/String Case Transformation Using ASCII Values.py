def solution(input_string):
    transformed_string = ""

    for character in input_string:
        if "a" <= character <= "z":
            character = chr(ord("A") + (ord(character) - ord("a")))
        elif "A" <= character <= "Z":
            character = chr(ord("a") + (ord(character) - ord("A")))

        transformed_string += character

    return transformed_string
