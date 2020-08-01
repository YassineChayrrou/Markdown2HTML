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
        lines = f.readlines()
        i = 0
        while i < len(lines):
            line = lines[i]
            markup = line.split(" ", 1)
            if markup[0][0] == "#":
                heading = len(markup[0])
                fl.write("<h{}>{}</h{}>\n".format(heading, markup[1][:-1], heading))
            if markup[0][0] == "-":
                fl.write("<ul>\n")
                while markup[0] == "-":
                    fl.write("<li>{}</li>\n".format(markup[1][:-1]))
                    i += 1
                    markup = lines[i].split(" ", 1)
                fl.write("</ul>\n")
                i -= 1
            i += 1 
        f.close
        fl.close
    except OSError:
        sys.stderr.write("Missing " + sys.argv[1] + "\n")
        exit(1)
    exit(0)
