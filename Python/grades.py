#!usr/bin/env python

import sys


def usage():
    print >> sys.stderr, "Usage: python %s <filename>" % (sys.argv[0])


def main():
    if len(sys.argv) != 2:
        usage()
        sys.exit(1)

    try:
        fp = open(sys.argv[1], "r")
    except IOError, e:
        print >> sys.stderr, "Argument is not a valid filename"
        usage()
        sys.exit(1)

    text = list(fp)
    line = text[0]
    minim = line.split()[3]
    minim = float(minim)
    maxim = minim
    linemin = line
    linemax = line
    for i in range(1,len(text)):
        line = text[i]
        aux = line.split()[3]
        aux = float(aux)
        if minim > aux:
            minim = aux
            linemin = line
        if maxim < aux:
            maxim = aux
            linemax = line

    print "Nota cea mai mare este obtinuta de: ", linemax,
    print "Nota cea mai mica este obtinuta de: ", linemin,

if __name__ == "__main__":
    sys.exit(main())
