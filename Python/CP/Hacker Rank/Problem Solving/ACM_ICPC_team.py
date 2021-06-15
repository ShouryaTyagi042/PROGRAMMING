#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the acmTeam function below.


def acmTeam(topic):
    no_topics = len(topic[0])
    no_attendees = len(topic)
    a = []
    for i in range(no_attendees):
        for k in range(i + 1, no_attendees):
            ans = 0
            for j in range(no_topics):
                if topic[i][j] == "1" or topic[k][j] == "1":
                    ans += 1
            a.append(ans)
    sub = max(a)
    team = a.count(sub)
    x = [sub, team]
    return x


# l1 = ["10101", "11100", "11010", "00101"]
# result = acmTeam(l1)
# print(result)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
