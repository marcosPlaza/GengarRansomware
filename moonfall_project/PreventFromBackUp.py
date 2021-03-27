# info here - https://www.phillipsj.net/posts/executing-powershell-from-python/

# imports
import os
import subprocess

# class definition


class PreventFromBackUp:
    def delete_shadowcopy():
        pass


        def run_command(self, cmd):
        completed = subprocess.run(
                ["powershell", "-Command", cmd], capture_output=True)
        return completed


if __name__ == '__main__':
    # test code here
    hello_command = "write-host 'Hello Wolrd!'"
    hello_info = run(hello_command)
    if hello_info.returncode != 0:
        print("An error occured: %s", hello_info.stderr)
    else:
        print("Hello command executed successfully!")

    print("-------------------------")

    bad_syntax_command = "write-host 'Incorrect syntax command!'"
    bad_syntax_info = run(bad_syntax_command)
    if bad_syntax_info.returncode != 0:
        print("An error occured: %s", bad_syntax_info.stderr)
    else:
        print("Bad syntax command executed successfully!")
