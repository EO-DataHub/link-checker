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
    # result = subprocess.run(f"npx linkinator --recurse --verbosity error {url}", shell=True, capture_output=True, text=True)
    result = subprocess.run(f"npx linkinator {url}", shell=True, capture_output=True, text=True)

    if all_responses := result.stderr:
        warnings = {}
        for error in all_responses.split('\n'):
            if error.startswith('['):  # Some of the lines contain description with emojisht
                code, link = error.split()
                if not warnings.get(code):
                    warnings[code] = []
                warnings[code].append(link)
        errors = warnings.pop('[404]')

        logging.warning(f"Warnings: {warnings}")
        logging.error(f"Errors: {errors}")
        raise Exception(errors)


if __name__ == "__main__":
    url = sys.argv[1]
    main(url)
