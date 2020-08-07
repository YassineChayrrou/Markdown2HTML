#!/usr/bin/python3
"""Python module that takes 2 arguments : first argument is Markdown file name
   the second is output file name
"""
import sys
import re

if __name__ == "__main__":
    def bold_emphasis_text(text):
        if text is None:
            return None
        bold_match = re.findall('\*\*.*?\*\*', text)
        em_match = re.findall('__.*?__', text)
        if bold_match:
            for word in bold_match:
                text = text.replace(word, "<b>" + word[2:-2] + "</b>")
        if em_match:
            for word in em_match:
                text = text.replace(word, "<em>" + word[2:-2] + "</em>")
        return text
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
            line = bold_emphasis_text(line)
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

            if markup[0][0] == markups[2] and len(markup[0]) == 1:
                fl.write("<ol>\n")
                while markup[0] == "*":
                    fl.write("<li>{}</li>\n".format(markup[1][:-1]))
                    i += 1
                    if i >= len(lines):
                        break
                    markup = lines[i].split(" ", 1)
                fl.write("</ol>\n")
                i -= 1

            paragraph = []
            while markup[0][0] not in markups and i < len(lines):
                markup = lines[i].split(" ")
                if lines[i] == "\n" or markup[0] in markups:
                    break
                newText = bold_emphasis_text(lines[i])
                paragraph.append(newText)
                i += 1
            if paragraph:
                if len(paragraph) == 0:
                    break
                elif len(paragraph) == 1:
                    fl.write("<p>\n\t{}</p>\n".format(paragraph[0]))
                    i -= 1
                else:
                    fl.write("<p>\n")
                    for j in range(len(paragraph)):
                        fl.write("\t{}".format(paragraph[j]))
                        if j < len(paragraph) - 1:
                            fl.write("\t<br />\n")
                    fl.write("</p>\n")
                    i -= 1
            i += 1
        f.close
        fl.close
    except OSError:
        sys.stderr.write("Missing " + sys.argv[1] + "\n")
        exit(1)
    exit(0)
