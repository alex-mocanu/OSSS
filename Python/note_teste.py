#!/usr/bin/env python

import sys


def main():
    students = []
    fp = open(sys.argv[1], "r")
    
    for line in list(fp):
        tokens = line.strip().strip('\'').split(',')
        if tokens[3] == "":
            tokens[3] = 0
        student = {
                'test1': tokens[0].strip('"'),
                'test2': tokens[1].strip('"'),
                'liceu': tokens[2].strip('"'),
                'nume': tokens[3].strip('"'),
                'nota': int(tokens[4].strip('"'))
                }
        students.append(student)
    
    max_grade = -1
    test1 = students[0]['test1']
    test2 = students[0]['test2']
    for s in students:
        if test1 != s['test1']:

            print "Maximul de %s puncte pentru %s,%s: %s, %s" % (max_grade, max_test1, max_test2, max_student, max_liceu)
            test1 = s['test1']
            max_grade = -1
        if max_grade < s['nota']:
            max_grade = s['nota']
            max_test1 = s['test1']
            max_test2 = s['test2']
            max_liceu = s['liceu']
            max_student = s['nume']

    print "Maximul de %s puncte pentru %s,%s: %s, %s" % (max_grade, max_test1, max_test2, max_student, max_liceu)
if __name__ == '__main__':
    sys.exit(main())
