def solution(s):
    vowels = list()
    
    for index, character in enumerate(s):
        if character.lower() in ["a", "e", "i", "o", "u"]:
            vowels.append(index)
    
    return vowels