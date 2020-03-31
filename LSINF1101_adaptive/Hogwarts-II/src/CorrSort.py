#!/usr/bin/python3
# -*- coding: utf-8 -*-

from itertools import permutations

knowledge = [['Gryffindor', ['brave', 'strong', 'bold']],
             ['Ravenclaw', ['smart', 'wise', 'curious']],
             ['Hufflepuff', ['loyal', 'patient', 'hard-working']],
             ['Slytherin', ['cunning', 'wily', 'malignant']]]

def house_designation(student_qualities):
    ranking = []
    for lst in knowledge:
        count = 0
        for q in student_qualities:
            if q in lst[1]:
                count += 1
        ranking.append(count)
    ans = []
    for _ in range(4):
        ans.append(knowledge[ranking.index(max(ranking))][0])
        ranking[ranking.index(max(ranking))] = -1
    return ans


def multi_house_designation(student_qualities):
    ranking = []
    for lst in knowledge:
        count = 0
        for q in student_qualities:
            if q in lst[1]:
                count += 1
        ranking.append(count)
    ans = []
    j = 0
    while j < 4:
        m = max(ranking)
        indices = [i for i, x in enumerate(ranking) if x == m]
        if len(ans) == 0:
            ans = [list(x) for x in list(permutations([knowledge[i][0] for i in indices]))]
        else:
            tmp = []
            for l1 in ans:
                for l2 in [list(x) for x in list(permutations([knowledge[i][0] for i in indices]))]:
                    tmp.append(l1 + l2)
            ans = tmp
        for i in indices:
            ranking[i] = -1
            j += 1
    return ans
