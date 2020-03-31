#!/usr/bin/python3
# -*- coding: utf-8 -*-


def referee(file):
    score = {}
    try:
        with open(file, 'r') as f:
            f = f.readlines()
            score[f[0].strip()], score[f[1].strip()] = 0, 0
            for line in f[2:]:
                print(line)
                tmp = line.split()
                team, points = tmp[0], int(tmp[1])
                score[team] += points
                if points == 150:
                    print('there')
                    break
    except IOError:
        raise IOError("File does not exist.")
    return max(score, key=score.get)
