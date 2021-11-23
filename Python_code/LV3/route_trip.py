answer = []
# tmp = []
icn_list = []
checked = [0 for _ in range(10002)]


def dfs(tickets, departure, cnt, target_cnt, tmp): # tickets, 0, 0, 4
    # print(target_cnt)
    tmp.append(tickets[departure][1]) # tickets[0][0] == "ICN"
    if target_cnt == len(tmp):
        answer.append(tmp)
        return
    # print(tmp)
    checked[departure] = 1  # checked[0] == 1
    arrival = tickets[departure][1]  # "JFK"
    for i in range(0, len(tickets)):
        if checked[i] == 0:
            if tickets[i][0] == arrival:
                checked[i] = 1
                dfs(tickets, i, cnt + 1, target_cnt, tmp)
                checked[i] = 0


def solution(tickets):

    target_cnt = len(tickets) + 1
    for i in range(0, len(tickets)):
        if "ICN" in tickets[i][0]:
            icn_list.append(i)

    for i in range(0, len(icn_list)):
        checked = [0 for _ in range(10002)]
        tmp = []
        tmp.append("ICN")
        dfs(tickets, icn_list[i], 1, target_cnt, tmp) # tickets, 0, 1, 4

    return sorted(answer)[0]
# print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))
print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))