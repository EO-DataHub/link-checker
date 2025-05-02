import logging
import subprocess
import sys


def run_npm_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)

    if result.stderr:
        logging.error(result.stderr)


def install():
    logging.info("Install npm")
    run_npm_command("npm install")
    run_npm_command("npm install npx")
    run_npm_command("npm install whatwg-url")
    run_npm_command("npm install linkinator")


def main(url):
    install()
    result = subprocess.run(f"npx linkinator {url}", shell=True, capture_output=True, text=True)

    if errors := result.stderr:
        logging.error(errors)
        raise Exception(errors)


if __name__ == "__main__":
    url = sys.argv[1]
    main(url)
