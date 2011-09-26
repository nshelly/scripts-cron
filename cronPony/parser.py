#!/usr/bin/python
import re
import string

__parse_job = re.compile(r"""^
                           (?P<minute>\S+)
                           \s+
                           (?P<hour>\S+)
                           \s+
                           (?P<day_of_month>\S+)
                           \s+
                           (?P<month>\S+)
                           \s+
                           (?P<day_of_week>\S+)
                           \s+
                           (?P<quote>['"])?
                               (?P<command>.+?)
                           (?(quote)(?=quote)|$)
                           """, re.X)

__parse_variable = re.compile(r"""^
                                (?P<q1>['"])?
                                (?P<key>(?(q1).+?|\S+?))
                                (?(q1)(?P=q1))
                                \s*=\s*
                                (?P<q2>['"])?
                                (?P<val>.+?)
                                (?(q2)(?P=q2)|$)
                                """, re.X)

def read(crontab):
    jobs = []
    env = {}
    with open(crontab, "r") as f:
        for line in f.readlines():
            line = line.strip()
            if not line or line[0] == "#":
                continue;
            elif line[0] in string.digits + "*":
                m = __parse_job.match(line)
                if m:
                    job = m.groupdict()
                    if "quote" in job:
                        del job["quote"]
                    jobs.append(job)
            else:
                m = __parse_variable.match(line)
                if m:
                    env[m.group("key")] = m.group("val")

    return env, jobs

def write(crontab, env, jobs):
    with open(crontab, "w") as f:
        for key, val in env.items():
            f.write("\"%s\" = \"%s\"\n" % (key, val))

        for job in jobs:
            f.write("%(minute)s\t%(hour)s\t%(day_of_month)s\t%(month)s\t%(day_of_week)s\t%(command)s\n" % job)

