import subprocess


def backup(target_dir, dest):
    # a space or ';' in target_dir changes the command
    subprocess.call("tar czf " + dest + " " + target_dir, shell=True)
