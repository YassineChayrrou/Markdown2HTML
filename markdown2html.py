#!/usr/bin/python3
"""Python module that takes 2 arguments : first argument is Markdown file name
   the second is output file name
"""
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        exit(1)
    try:
        f = open(sys.argv[1], 'r')
        fl = open(sys.argv[2], 'w')
        for line in f:
            markup = line.split(" ", 1)
            heading = len(markup[0])
            if markup[0][0] == "#":
                fl.write("<h{}>\n".format(heading))
                fl.write(markup[1])
                fl.write("</h{}>\n".format(heading))
        fl.close()
        f.close()
    except OSError:
        sys.stderr.write("Missing " + sys.argv[1] + "\n")
        exit(1)
    exit(0)
