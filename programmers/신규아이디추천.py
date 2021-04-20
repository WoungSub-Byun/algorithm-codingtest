# 1차 : 100%
# 정규식에 대한 이해가 부족했다. 이번 문제를 풀면서 정규식에 대한 공부를 할 수 있었다.
import re


def solution(new_id):
    new_id = new_id.lower()
    c2 = re.compile("[^a-z0-9-_.]")
    listed_id = list(new_id)
    for x in c2.findall(new_id):
        del listed_id[listed_id.index(x)]

    new_id = re.sub("[.]+", ".", "".join(listed_id)).strip(".")
    if not new_id:
        new_id = "a"
    if len(new_id) >= 16:
        new_id = new_id[:15].rstrip(".")
    if len(new_id) <= 2:
        while len(new_id) != 3:
            new_id += new_id[-1]
    return new_id


# 2차 시도
import re


def solution(new_id):
    new_id = new_id.lower()
    c2 = re.compile("[^a-z0-9-_.]")
    listed_id = list(new_id)
    for x in c2.findall(new_id):
        del listed_id[listed_id.index(x)]

    new_id = re.sub("[.]+", ".", "".join(listed_id)).strip(".")
    if not new_id:
        new_id = "a"
    if len(new_id) >= 16:
        new_id = new_id[:15].rstrip(".")
    if len(new_id) <= 2:
        new_id += new_id[-1] * (3 - len(new_id))
    return new_id


# 3차 시도: 최대한 정규식을 사용하여 풀이
import re


def solution(new_id):
    new_id = new_id.lower()
    new_id = re.sub("[^a-z0-9-_.]", "", new_id)
    new_id = re.sub("\.+", ".", new_id).strip(".")
    new_id = "a" if len(new_id) == 0 else new_id[:15].rstrip(".")
    new_id = new_id if len(new_id) > 2 else new_id + new_id[-1] * (3 - len(new_id))
    return new_id