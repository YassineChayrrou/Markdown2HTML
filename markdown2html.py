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
        markups = ["#", "-", "*"]
        i = 0
        while i < len(lines):
            line = lines[i]
            markup = line.split(" ", 1)

            if markup[0][0] == markups[0]:
                heading = len(markup[0])
                fl.write("<h{}>".format(heading))
                fl.write("{}</h{}>\n".format(markup[1][:-1], heading))

            if markup[0][0] == markups[1]:
                fl.write("<ul>\n")
                while markup[0] == "-":
                    fl.write("<li>{}</li>\n".format(markup[1][:-1]))
                    i += 1
                    if i >= len(lines):
                        break
                    markup = lines[i].split(" ", 1)
                fl.write("</ul>\n")
                i -= 1

            if markup[0][0] == markups[2]:
                fl.write("<ol>\n")
                while markup[0] == "*":
                    fl.write("<li>{}</li>\n".format(markup[1][:-1]))
                    i += 1
                    if i >= len(lines):
                        break
                    markup = lines[i].split(" ", 1)
                fl.write("</ol>\n")
                i -= 1

            if markup[0][0] not in markups:
                paragraph = []
                while markup[0][0] not in markups and i < len(lines):
                    markup = lines[i].split(" ")
                    if lines[i] == "\n" or markup[0] in markups:
                        break
                    paragraph.append(lines[i])
                    i += 1
                if len(paragraph) == 1:
                    fl.write("<p>\n\t{}</p>\n".format(paragraph[0]))
                else:
                    for j in range(len(paragraph)):
                        fl.write("\t{}".format(paragraph[j]))
                        if j < len(paragraph) - 1:
                            fl.write("\t<br />\n")
                    fl.write("</p>\n")
            i += 1
        f.close
        fl.close
    except OSError:
        sys.stderr.write("Missing " + sys.argv[1] + "\n")
        exit(1)
    exit(0)
