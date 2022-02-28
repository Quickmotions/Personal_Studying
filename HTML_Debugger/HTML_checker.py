import time
import re

filename = "HTML_file\\" + input("Enter filename: ") + ".html"

try:
    f = open(filename, "r")
except FileNotFoundError:
    print("File Not Found --- Make sure you have placed the file into this directory")
    exit()

print("Starting debugger...")
time.sleep(0.3)

print("---Test 1---")
print("Testing for Handing nested tags\n ----------\n")
time.sleep(0.1)

# stores if tag is open and its line num
tags = {}
line_num = 0

for line in f.readlines():
    line_num += 1
    open_pos = []
    close_pos = []

    for pos in range(len(line)):
        if line[pos] == "<":
            open_pos.append(pos)
        if line[pos] == ">":
            close_pos.append(pos)
    if len(open_pos) != len(close_pos):
        print(f"ERROR on line {line_num} of {filename} --- uneven amount of '<>' in line")
        continue
    for tag_pos in range(len(open_pos)):
        tag = line[open_pos[tag_pos]:close_pos[tag_pos] + 1]
        closing_tag = False
        if "/" in tag:
            closing_tag = True

        tag = re.sub('/', '', tag)
        if tag not in tags:
            tags[tag] = [False, 0]

        is_open, last_line = tags[tag]
        if closing_tag:
            if not is_open:
                print(f"ERROR on line {line_num} of {filename} --- "
                      f"tried to close tag '{tag}' however tag '{tag}' on line {last_line} was already closed")
            tags[tag] = [False, line_num]

        else:
            if is_open:
                print(f"ERROR on line {line_num} of {filename} --- "
                      f"tried to open tag '{tag}' however tag '{tag}' on line {last_line} was already opened")
            tags[tag] = [True, line_num]

    # error for all unclosd tags
    for tag in tags:
        is_open, last_line = tags[tag]
        if is_open:
            print(f"ERROR on line {last_line} of {filename} --- "
                  f"tag '{tag}' was opened but never closed")

print("---Finished Debugging---")
