def solution(input_string):
    i = 0
    j = len(input_string) - 1

    while i < j:
        a = ord(input_string[i])
        b = ord(input_string[j])

        if not (65 <= a <= 90 or 97 <= a <= 122):
            i += 1
            continue
        if not (65 <= b <= 90 or 97 <= b <= 122):
            j -= 1
            continue

        if (a > b and a - 32 == b) or (a < b and a + 32 == b) or a == b:
            i += 1
            j -= 1
            continue

        return False

    return True
