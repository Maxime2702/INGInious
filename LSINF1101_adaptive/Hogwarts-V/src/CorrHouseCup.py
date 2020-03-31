#!/usr/bin/python3
# -*- coding: utf-8 -*-


students = {'gryffindor': ['Harry', 'Hermione', 'Ron', 'Ginny', 'Fred', ' Georges', 'Neville'],
            'ravenclaw': ['Cho', 'Luna', 'Sybill', 'Marcus', 'Marietta', 'Terry', 'Penelope'],
            'hufflepuff': ['Pomona', 'Zacharias', 'Teddy', 'Cedric', 'Nymphadora', 'Newton', 'Justin'],
            'slytherin': ['Malfoy', 'Severus', 'Dolores', 'Horace', 'Blaise', 'Pansy', 'Bellatrix']}

def maximum(scores):
    max_value = max(scores.values())
    winners = []
    for house in scores:
        if scores[house] == max_value: winners.append(house)
    if len(winners) == 1: return winners[0]
    return winners

def winning_house(file):
    score = {house: 0 for house in students.keys()}
    try:
        with open(file, 'r') as f:
            for line in f:
                tmp = line.split()
                student, points = tmp[0], int(tmp[1])
                team = None
                for house in students.keys():
                    if student in students[house]: team = house
                score[team] += points
    except IOError:
        raise IOError("File does not exist.")
    return maximum(score)