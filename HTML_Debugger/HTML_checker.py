import time
import re
from typing import TextIO


class Debugger:
    file_name: str
    file_location: str
    file: TextIO
    all_tags: list = []

    def start(self):

        self.file_name = input("Enter filename: ") + ".html"
        self.file_location = "HTML_files\\" + self.file_name
        try:
            self.file = open(self.file_location, "r")
        except FileNotFoundError:
            print("File Not Found --- Make sure you have placed the file into this directory")
            exit()
        self.nested_tag_check()

    def nested_tag_check(self):
        print("---Test 1---")
        print("Testing for Handing nested tags\n ----------\n")
        time.sleep(0.1)

        # stores if tag is open and its line num
        line_num = 0
        tags = {}

        # create a tree type list by putting stuff inside each other
        # structure = <body><p>test</p><body><h1></h1>
        # structure = [
        #               ["<body>", ["<p>", []]],
        #               ["<h1>, []]
        #             ]

        for line in self.file.readlines():
            line_num += 1
            open_pos = []
            close_pos = []
            for pos in range(len(line)):
                if line[pos] == "<":
                    open_pos.append(pos)
                if line[pos] == ">":
                    close_pos.append(pos)
            if len(open_pos) != len(close_pos):
                print(f"ERROR on line {line_num} of {self.file_name} --- uneven amount of '<>' in line")
                continue
            for tag_pos in range(len(open_pos)):
                tag = line[open_pos[tag_pos]:close_pos[tag_pos] + 1]
                closing_tag = False
                if "/" in tag:
                    closing_tag = True

                self.all_tags.append(tag)
                tag = re.sub('/', '', tag)  # remove / from tags

                if tag not in tags:
                    tags[tag] = [False, 0]

                is_open, last_line = tags[tag]
                if closing_tag:
                    if not is_open:
                        print(f"ERROR on line {line_num} of {self.file_name} --- "
                              f"tried to close tag '{tag}' however tag '{tag}' on line {last_line} was already closed")
                    tags[tag] = [False, line_num]

                else:
                    if is_open:
                        print(f"ERROR on line {line_num} of {self.file_name} --- "
                              f"tried to open tag '{tag}' however tag '{tag}' on line {last_line} was already opened")
                    tags[tag] = [True, line_num]

        # test all unclosed tags
        for tag in tags:
            is_open, last_line = tags[tag]
            if is_open:
                print(f"ERROR on line {last_line} of {self.file_name} --- "
                      f"tag '{tag}' was opened but never closed")

        # TODO: Use this structure below to find illegally opened tags.
        print(self.create_html_structure())
        self.file.close()

    def create_html_structure(self):
        """creates and returns the tag structure of the html file"""
        if len(self.all_tags) == 0:
            return []
        open_tag = self.all_tags[0]

        # check next tag is instantly closed
        if "<" + self.all_tags[1][2:] == open_tag and len(self.all_tags) > 2:
            self.all_tags.remove("</" + open_tag[1:])
            self.all_tags.remove(open_tag)
            return [{open_tag: []}, self.create_html_structure()]

        # remove the outer tags and move rest of tags inside it
        self.all_tags.remove("</" + open_tag[1:])
        self.all_tags.remove(open_tag)
        return {open_tag: self.create_html_structure()}


def main():
    debugger = Debugger()

    print("\nStarting debugger...")
    time.sleep(0.3)
    debugger.start()
    print("\n---Finished Debugging---")


main()
