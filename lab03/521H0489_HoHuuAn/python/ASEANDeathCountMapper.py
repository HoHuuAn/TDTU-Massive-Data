#!/usr/bin/python
# -*-coding:utf-8 -*
import sys


def mapper():
    for line in sys.stdin:
        columns = line.strip().split("\t")
        if columns[1] == "South-East Asia":
            country = columns[0]
            deaths = int(columns[7].replace(",", "").split(".")[0])
            print("{}\t{}".format(country, deaths))


if __name__ == "__main__":
    mapper()
