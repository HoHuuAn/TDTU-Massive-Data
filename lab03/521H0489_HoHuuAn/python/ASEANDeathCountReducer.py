#!/usr/bin/python
# -*-coding:utf-8 -*
import sys


def reducer():
    current_country = None
    total_deaths = 0

    for line in sys.stdin:
        country, deaths = line.strip().split("\t")

        if current_country and current_country != country:
            print("{}\t{}".format(current_country, total_deaths))
            total_deaths = 0

        current_country = country
        total_deaths += int(deaths)

    if current_country:
        print("{}\t{}".format(current_country, total_deaths))


if __name__ == "__main__":
    reducer()
