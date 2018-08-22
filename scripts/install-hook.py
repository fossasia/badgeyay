import os
import subprocess

# Script to install 'pre-push-hook.py' in '.git/hooks' directory
# Make sure you have a '.git/hooks/pre-push.sample' file before running this script.


def main():

    path_file = os.path.abspath(os.path.join(os.path.abspath(__file__), '..'))
    path_hook = os.path.abspath(os.path.join(path_file, '../.git/hooks'))
    subprocess.run(['mv', path_hook + '/pre-push.sample', path_hook + '/pre-push'])
    subprocess.run(['chmod', '+x', path_hook + '/pre-push'])
    subprocess.run(['cp', path_file + '/pre-push-hook.py', path_hook + '/pre-push'])
    print('Git pre-push-hook successfully installed.')


if __name__ == '__main__':
    main()
