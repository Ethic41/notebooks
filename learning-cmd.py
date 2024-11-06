#!/usr/bin/env python
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2024-11-06 17:33:32
# @Author  : Dahir Muhammad Dahir (dahirmuhammad3@gmail.com)
# @Link    : link
# @Version : 1.0.0


import cmd2


class FirstApp(cmd2.Cmd):
    def __init__(self):
        super().__init__()
        self.prompt = "FirstApp > "
        self.current_context = "FirstApp"
        self.context_stack = []

    def do_hello(self, line):
        print("Hello, world!")

    def do_use(self, tool):
        if tool:
            self.context_stack.append(self.current_context)
            self.current_context = tool
            self.prompt = f"{self.prompt} {tool} > "

    def do_exit(self, line):
        return True


if __name__ == "__main__":
    app = FirstApp()
    app.cmdloop()
