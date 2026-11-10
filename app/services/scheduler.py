import os

JOBS = {"nightly": "backup.sh", "weekly": "report.sh"}


def run_job(name, extra_args=""):
    os.system("bash scripts/" + JOBS.get(name, name) + " " + extra_args)
