# https://school.programmers.co.kr/learn/courses/30/lessons/92341
import math

def cal_cost(fees, parking_time):
    basic_time, basic_fee, per_min, per_fee = fees[0], fees[1], fees[2], fees[3]
    if parking_time <= basic_time:
        return basic_fee
    else:
        return basic_fee + (math.ceil((parking_time - basic_time) / per_min) * per_fee)

def count_time(time):
    h, m = map(int, time.split(':'))
    return (h * 60) + m

def solution(fees, records):
    data = dict()
    answer = []
    len_records = len(records)

    for i in range(len_records):
        time, number, inout = map(str, records[i].split())
        sec_time = count_time(time)
        if inout == 'IN':
            if number in data:
                tmp_val = data[number]
                data[number] = tmp_val - sec_time
            else:
                data[number] = -sec_time
        else:
            tmp_val = data[number]
            data[number] = tmp_val + sec_time
    for key in data:
        if data[key] <= 0:
            tmp_val = data[key]
            data[key] = tmp_val + count_time('23:59')
            print(tmp_val, key)
    # https://wooono.tistory.com/286 참조 정렬
    sorted_dic = sorted(data.items())  # dictionary key로 정렬
    for val in sorted_dic:
        parking_time = val[1]
        answer.append(cal_cost(fees, parking_time))
    return answer