import re
def solution(new_id):
    # 1, 2단계: 소문자 치환 및 특수문자 제거('-_.' 제외)
    new_id = re.sub('[^0-9a-z_-.]+','.',new_id.lower())
    # 3, 4단계: 마침표가 두 개 이상 있으면 하나로 치환, 처음이나 끝에 마침표가 있다면 제거
    new_id = re.sub('\.+','.',new_id).strip('.')
    # 5단계: new_id가 빈 문자열이라면, new_id에 "a"를 대입
    if new_id == '': new_id = 'a'
    # 6단계: new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거. 이후 마침표가 new_id의 끝에 위치한다면 끝에 위치한 마침표 제거
    new_id = new_id[:15].rstrip('.')
    # 7단계: new_id의 길이가 2 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙임
    while len(new_id)<=2: new_id = new_id + new_id[-1]

    return new_id


"""
참고

def solution(new_id):
    st = new_id
    st = st.lower()
    st = re.sub('[^a-z0-9\-_.]', '', st)
    st = re.sub('\.+', '.', st)
    st = re.sub('^[.]|[.]$', '', st)
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    return st

"""