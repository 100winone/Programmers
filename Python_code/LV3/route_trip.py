checked = [False for _ in range(10001)]
answer = []


def dfs(tickets, depart, tmp_str):
    tmp_str.append(depart)

    if len(tmp_str) == len(tickets) + 1:
        for i in tmp_str:
            answer.append(i)

    for i in range(len(tickets)):
        if checked[i] == False and tickets[i][0] == depart:
            checked[i] = True
            dfs(tickets, tickets[i][1], tmp_str)
            checked[i] = False
    tmp_str.pop()


def solution(tickets):
    tmp = []
    tickets.sort()

    dfs(tickets, "ICN", tmp)

    return answer[:len(tickets) + 1]

# # 수정필요
# answer = []
# # tmp = []
# icn_list = []
# checked = [0 for _ in range(10002)]
# max_cnt = 0
#
# def dfs(tickets, departure, cnt, tmp): # tickets, 0, 0, 4
#
#     # global answer
#     tmp.append(departure) # tickets[0][0] == "ICN"
#     print(tmp)
#     if len(tmp) == len(tickets) + 1:
#         answer.append(tmp)
#
#     # if target_cnt == len(tmp):
#     #     answer.append(tmp)
#     #     return
#     # print(tmp)
#     # checked[departure] = 1  # checked[0] == 1
#     for i in range(0, len(tickets)):
#         if checked[i] == 0:
#             if tickets[i][0] == departure:
#                 checked[i] = 1
#                 dfs(tickets, tickets[i][1], cnt + 1, tmp)
#                 checked[i] = 0
#
#     tmp.pop()
# def solution(tickets):
#     # for i in range(0, len(tickets)):
#     #     if "ICN" in tickets[i][0]:
#     #         icn_list.append(i)
#     #
#     # for i in range(0, len(icn_list)):
#     #     checked = [0 for _ in range(10002)]
#     #     tmp = []
#     #     tmp.append("ICN")
#     tmp = []
#     sorted(tickets)
#     dfs(tickets, "ICN", 0, tmp) # tickets, 0, 1, 4
#
#     return answer

# print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))
# print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))