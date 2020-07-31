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
        f = open(sys.argv[1])
    except OSError:
        sys.stderr.write("Missing " + sys.argv[1] + "\n")
        exit(1)
    exit(0)
