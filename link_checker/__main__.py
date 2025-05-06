import logging
import subprocess
import sys


def main(url):
    result = subprocess.run(  # nosec
        f"npx linkinator --recurse --verbosity error {url}",
        shell=True,
        capture_output=True,
        text=True,
    )

    if all_responses := result.stderr:
        warnings = {}
        for error in all_responses.split("\n"):
            if error.startswith("["):  # Some of the lines contain description with emojis
                code, link = error.split()
                logging.info(f"Found: {code} {link}")
                if not warnings.get(code):
                    warnings[code] = []
                warnings[code].append(link)
        errors = warnings.pop("[404]", [])

        logging.warning(f"Warnings: {warnings}")
        logging.error(f"Errors: {errors}")
        raise Exception(errors)


if __name__ == "__main__":
    args = sys.argv[1:]
    main(args)
