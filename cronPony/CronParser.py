#!/usr/bin/python
import re
import string
import subprocess
from tempfile import NamedTemporaryFile

parsers = {
    "job": re.compile(r"""^
        (?P<minute>\S+)          # Minute
        \s+
        (?P<hour>\S+)            # Hour
        \s+
        (?P<day_of_month>\S+)    # Day of The Month
        \s+
        (?P<month>\S+)           # Month
        \s+
        (?P<day_of_week>\S+)     # Day Of The Week
        \s+
        (?P<quote>['"])?
           (?P<command>.+?)     # Command
        (?(quote)(?=quote)|$)
        """, re.X),

    "variable": re.compile(r"""^
        (?P<q1>['"])?
        (?P<key>(?(q1).+?|\S+?))
        (?(q1)(?P=q1))
        \s*=\s*
        (?P<q2>['"])?
        (?P<val>.+?)
        (?(q2)(?P=q2)|$)
        """, re.X),
}

def read():
    jobs = []
    env = {}
    crontab = subprocess.Popen(["crontab", "-l"], stdout=subprocess.PIPE).communicate()[0]
    for line in crontab.split('\n'):
        line = line.strip()
        if not line or line[0] == "#":
            continue;
        elif line[0] in string.digits + "*":
            m = parsers["job"].match(line)
            if m:
                job = m.groupdict()
                if "quote" in job:
                    del job["quote"]
                jobs.append(job)
        else:
            m = parsers["variable"].match(line)
            if m:
                env[m.group("key")] = m.group("val")

    return env, jobs

def write(env, jobs):
    with NamedTemporaryFile(prefix='cronpony', delete=True) as crontab:
        for key, val in env.items():
            if ' ' in key:
                key = "\"%s\"" % key
            if val[0] == ' ' or val[-1] == ' ':
                val = "\"%s\"" % val
            crontab.write("%s = %s\n" % (key, val))

        for job in jobs:
            crontab.write("%(minute)s\t%(hour)s\t%(day_of_month)s\t%(month)s\t%(day_of_week)s\t%(command)s\n" % job)

        crontab.flush()
        subprocess.call(["crontab", crontab.name])

