def solution(numbers,hand):
    a = []
    l_pos = 10
    r_pos = 12
    r_dis = 1
    l_dis = 1

    print(numbers)
    for i in numbers:
        print(i)
        if i == 0:
            i = 11
        if i ==3 or i==6 or i==9:
            a.append('R')
            print('369')
            r_pos = i
        elif i ==1 or i==4 or i==7:
            a.append('L')
            print('147')
            l_pos = i
        elif i == 2 or i == 5 or i == 8 or i == 11:
            if abs(r_pos-i) == 1 or abs(r_pos-i) == 3:
                r_dis = 1
            elif abs(r_pos-i) == 2 or abs(r_pos-i) == 4 or abs(r_pos-i) == 6:
                r_dis = 2
            elif abs(r_pos-i) == 5 or abs(r_pos-i) == 7:
                r_dis = 3
            elif abs(r_pos-i) == 8:
                r_dis = 4
            elif abs(r_pos-i) == 0:
                r_dis = 0

            if abs(l_pos-i) == 1 or abs(l_pos-i) == 3:
                l_dis = 1
            elif abs(l_pos-i) == 2 or abs(l_pos-i) == 4 or abs(l_pos-i) == 6:
                l_dis = 2
            elif abs(l_pos-i) == 5 or abs(l_pos-i) == 7:
                l_dis = 3
            elif abs(l_pos-i) == 10:
                l_dis = 4
            elif abs(l_pos-i) == 0:
                l_dis = 0

            if r_dis<l_dis:
                a.append('R')
                r_pos = i
            elif r_dis>l_dis:
                a.append('L')
                l_pos = i
            elif r_dis == l_dis:
                if hand == 'R':
                    a.append('R')
                    r_pos = i
                if hand == 'L':
                    a.append('L')
                    l_pos = i

    answer = a
    return answer



print(solution((1,3,6,0,2,4),'R'))


'''
1칸 1 3
2칸 2 4 6 
3칸 5 7
4칸 9

1 2 3
4 5 6
7 8 9
* 0 #


'''