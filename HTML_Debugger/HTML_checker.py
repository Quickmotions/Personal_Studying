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
        self.test_tag_structure()
        self.file.close()

    @staticmethod
    def collect_tags(line: str) -> tuple[list, list]:
        open_pos = []
        close_pos = []

        for pos in range(len(line)):
            if line[pos] == "<":
                open_pos.append(pos)
            if line[pos] == ">":
                close_pos.append(pos)

        return open_pos, close_pos

    # TODO: Create multiple files and classes for each debug test
    def nested_tag_check(self):
        print("---Test 1---")
        print("Testing Nested Tags\n ----------\n")
        time.sleep(0.1)

        # stores if tag is open and its line num
        line_num = 0
        tags = {}

        for line in self.file.readlines():
            line_num += 1
            open_pos, close_pos = self.collect_tags(line)

            if len(open_pos) != len(close_pos):
                print(f"ERROR on line {line_num} of {self.file_name} --- uneven amount of '<>' in line")
                continue

            for tag_pos in range(len(open_pos)):
                tag = line[open_pos[tag_pos]:close_pos[tag_pos] + 1]
                tag = self.configure_tag(tag)

                closing_tag = False
                if "/" in tag:
                    closing_tag = True

                self.all_tags.append([tag, line_num])
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

    def test_surroundings(self, tag_name: str, surroundings: list, line_num: int = 1) -> None:
        # TODO: Improve the efficiency of this function

        html_rules = {
            "<body>": ["<html>"],
            "<p>": ["<body>"],
            "<head>": ["<html>"],
            "<b>": ["<p>"],
            "<br>": ["<p>"],
            "<title>": ["<head>"],

        }

        for rule, restriction in html_rules.items():
            if tag_name == rule:
                if restriction not in surroundings:
                    print(f"ERROR on line {line_num} of {self.file_name} --- "
                          f"tag '{tag_name}' was opened before a '{restriction}' tag")

    def test_tag_structure(self) -> None:
        """Finds errors with tags opened in wrong context"""
        print("---Test 2---")
        print("Testing Tag Structure\n ----------\n")
        time.sleep(0.1)

        main_index = 0
        for main_tag, line_num in self.all_tags:
            # only check tag openers
            if main_tag[1] == "/":
                main_index += 1
                continue

            surrounding_tags = []
            # find tags which main tag is inside of
            opening_index = 0
            for opening_tag, _ in self.all_tags[:main_index]:
                if opening_index == main_index or opening_tag[1] == "/":
                    opening_index += 1
                    continue

                # check if main tag in located inside
                closing_tag = "</" + opening_tag[1:]
                closing_index = 0

                for tag, _ in self.all_tags[main_index:]:
                    # find opening tags, closing equivalent
                    if tag == closing_tag:
                        surrounding_tags.append(opening_tag)
                        break
                    closing_index += 1
                opening_index += 1
            self.test_surroundings(main_tag, surrounding_tags, line_num)
            main_index += 1

    @staticmethod
    def configure_tag(tag: str) -> str:
        """formats tags"""
        tag = tag.lower()

        # remove optional tag args
        tag = tag.split(" ", maxsplit=1)
        if len(tag) > 1:
            tag = tag[0] + ">"
        else:
            tag = tag[0]
        return tag


def main():
    debugger = Debugger()

    print("\nStarting debugger...")
    time.sleep(0.3)
    debugger.start()
    print("\n---Finished Debugging---")


if __name__ == "__main__":
    main()
