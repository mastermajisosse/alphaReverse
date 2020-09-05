def solution(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz' 
    return_str = ""
    list_ = s.split(" ")
    trans = str.maketrans(alphabet, alphabet[::-1], ' ')
    for item in list_: 
        return_str += item.translate(trans) + " " 
    return return_str.strip()

print(solution("ana"))
