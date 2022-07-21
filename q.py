map_ = {}
while True:
    stud_info = input()
    """
    stop
    maths shivank
    maths aman
    english aman
    """
    stud_info = stud_info.split()
    """
    ["stop"]
    ["maths", "shivank"]
    ["maths", "aman"]
    """
    if stud_info[0] == 'stop':
        break
    else:
        if stud_info[0] in map_:
            map_[stud_info[0]].add(stud_info[1])
        else:
            map_[stud_info[0]] = {stud_info[1]}
            # map_[stud_info[0]].add(stud_info[1])

print(map_)
