from subprocess import Popen, PIPE

def execute(cwd, executable, *args):
    """
    Executes command, return a tuple:
    returncode, output, error message
    """
    command = [executable] + list(args)
    process = Popen(command, stdout=PIPE, stderr=PIPE, cwd=cwd)
    out, err = process.communicate()

    return process.returncode, str(out, 'utf-8'), str(err, 'utf-8')

