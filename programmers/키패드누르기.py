# 1차 시도: 10 %
def solution(numbers, hand):
    lhand_dir, rhand_dir = 10, 12
    answer = ""
    for number in numbers:
        if number == 0:
            number == 11
        if number in [1, 4, 7]:
            answer += "L"
            lhand_dir = number
        elif number in [3, 6, 9]:
            answer += "R"
            rhand_dir = number
        else:
            board = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
            hands_cnt = []

            for hand_dir in [lhand_dir, rhand_dir]:
                cnt = 0
                y, x = hand_dir // 3, -4 + hand_dir % 3
                if hand_dir % 3 == 0:
                    y -= 1
                    x = 2
                if -1 <= number - board[y][x] <= 1:
                    cnt += 1
                else:
                    cnt += (number // 3) - (board[y][x] // 3) + 1
                hands_cnt.append(cnt)
            if hands_cnt[0] == hands_cnt[1]:
                if hand == "right":
                    answer += "R"
                    rhand_dir = number
                else:
                    answer += "L"
                    lhand_dir = number
            elif hands_cnt[0] > hands_cnt[1]:
                rhand_dir = number
                answer += "R"
            else:
                lhand_dir = number
                answer += "L"
    return answer


# 2차 시도 : 기억이 잘안나지만 낮은 점수(틀림)
def solution(numbers, hand):
    lhand_dir, rhand_dir = 10, 12
    answer = ""
    for number in numbers:
        if number == 0:
            number = 11
        if number in [1, 4, 7]:
            answer += "L"
            lhand_dir = number
        elif number in [3, 6, 9]:
            answer += "R"
            rhand_dir = number
        else:
            map = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
            hands_cnt = []

            for hand_dir in [lhand_dir, rhand_dir]:
                cnt = 0
                y, x = hand_dir // 3, -4 + hand_dir % 3
                if hand_dir % 3 == 0:
                    y -= 1
                    x = -1
                while number == map[y][x]:
                    if -1 <= number - map[y][x] <= 1:
                        cnt += 1
                        break
                    else:
                        y += 1
                        cnt += 1
                    hands_cnt.append(cnt)

            if hands_cnt[0] == hands_cnt[1]:
                if hand == "right":
                    answer += "R"
                    rhand_dir = number
                else:
                    answer += "L"
                    lhand_dir = number
            elif hands_cnt[0] > hands_cnt[1]:
                rhand_dir = number
                answer += "R"
            else:
                lhand_dir = number
                answer += "L"
        print(
            "lhand_dir:{}, rhand_dir:{}, number:{}, answer:{}".format(
                lhand_dir, rhand_dir, number, answer
            )
        )
    return answer


# 3차 시도: 다른 사람 코드 100%
def solution(numbers, hand):
    answer = ""
    lhand_dir, rhand_dir = 10, 12
    for number in numbers:
        if number in [1, 4, 7]:
            answer += "L"
            lhand_dir = number
        elif number in [3, 6, 9]:
            answer += "R"
            rhand_dir = number
        else:
            number = 11 if number == 0 else number
            abs_l = abs(number - lhand_dir)
            abs_r = abs(number - rhand_dir)
            if sum(divmod(abs_l, 3)) == sum(divmod(abs_r, 3)):
                if hand == "left":
                    answer += "L"
                    lhand_dir = number
                else:
                    answer += "R"
                    rhand_dir = number
            elif sum(divmod(abs_l, 3)) > sum(divmod(abs_r, 3)):
                answer += "R"
                rhand_dir = number
            else:
                answer += "L"
                lhand_dir = number
    return answer