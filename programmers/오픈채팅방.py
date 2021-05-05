# 1차 시도: Error
# 풀이: record를 split하는 과정에서 command가 Leave인 경우에는 nickname 값이 없기때문에 오류가 발생했습니다.
def solution(records):
    user_infos = {}
    logs = []
    for record in records:
        command, uid, nickname = record.split(" ")
        if command == "Enter":
            logs.append([uid, "님이 들어왔습니다."])
            user_infos[uid] = nickname
        elif command == "Leave":
            logs.append([uid, "님이 나갔습니다."])
        elif command == "Change":
            user_infos[uid] = nickname
    return ["".join([user_infos[log[0]], log[1]]) for log in logs]


# 2차 시도 : 100%
def solution(records):
    user_infos = {}
    logs = []
    for record in records:
        record = record.split()
        command, uid = record[0], record[1]
        if command == "Enter":
            logs.append([uid, "님이 들어왔습니다."])
            user_infos[uid] = record[2]
        elif command == "Leave":
            logs.append([uid, "님이 나갔습니다."])
        elif command == "Change":
            user_infos[uid] = record[2]
    return ["".join([user_infos[log[0]], log[1]]) for log in logs]
