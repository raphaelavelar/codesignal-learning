def solution(s):
    shifted_string = ""
    wrap = {"Z": "A", "z": "a"}

    for character in s:
        if "a" <= character <= "z" or "A" <= character <= "Z":
            if character in wrap.keys():
                character = wrap[character]
            else:
                character = chr(ord(character) + 1)

        shifted_string += character

    return shifted_string
