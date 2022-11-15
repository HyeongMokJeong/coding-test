import re
def solution(new_id):
    id = new_id.lower()
    
    id = re.sub('[^0-9a-z\-_.]','',id)
    id = re.sub('[\.]+','.', id)
    id = id.rstrip('.')
    id = id.lstrip('.')
    if id == '':
        id = 'a'
    if len(id) >= 16:
        id = id[:15]
        if id[-1] == '.':
            id = id.rstrip('.')
    elif len(id) <= 2:
        txt = id[-1]
        while len(id) != 3:
            id += txt
    return id

print(solution(	"z-+.^."))