#!/usr/bin/python2
import string

class SM():
    parsing = 0
    full = 1
    end = 2

    def begin(c, env):
        if c in string.whitespace:
            return SM.begin, {}
        elif c == '#':
            return SM.comment, {}
        elif c == "*" or c in string.digits:
            return SM.job, {"buf": c, "quote": "", "escape": False}
        else:
            return SM.variable, {"buf": c, "quote": "", "escape": False}
            
    def comment(c, env):
        if c == '\n':
            return SM.begin, {}
        else:
            return SM.comment, {}

    def job(c, env):
        state, env = SM.fill_buffer(c, env)
        if state == SM.fill_buffer:
            return SM.job, env
        elif state == SM.job:
            buf = env["buf"]
            if buf == "*":
                env["job"].append(None)
            else:
                env["job"].append(int(env["buf"]))
            env[env["field"]] = env["buf"]
            env[
        else:
            return SM.state, env



    def fill_buffer(c, env):
        if env["escape"]:
            env["buf"] += c
            env["escape"] == False
        elif c == "\\":
            env["escape"] = True
        elif env["quote"]:
            if c == env["quote"]:
                env["quote"] = ""
            else:
                env["buf"] += c
        elif c in "'\"":
            env["quote"] = c
        elif c  in "\n;":
            return SM.begin, {}
        elif c == "#":
            return SM.comment, {}
        else:
            env["buf"] += c

        return SM.fill_buffer, env

    def variable(c, env):
        pass



def parse(crontab):
    state = SM.begin
    env = {}
    f = open(crontab)
    for c in f.read():
        state, env = state(c, env)

parse("tmpcron")
