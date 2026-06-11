#!/usr/bin/env python3

# Imports

import sys
import re
import logging

# Configuration

logging.basicConfig(
    filename = "pipeline_autid.log",
    filemode = "a",
    level = logging.INFO,
    format = "%(asctime)s - %(levelname)s - %(message)s"
)

# Functions

def youtube_id_checker(youtube_id):
    '''
    checks if the Youtube ID has 11 characters and contains that proper Character Set
    '''
    return bool(re.fullmatch(r'^[A-Za-z0-9_-]{11}$', youtube_id))

def main():
    '''
    Function runs main script logic to check valid Youtube IDs

    Output: If valid, echoes the Youtube ID. Else, nothing is echoed and an error is logged

    Exception: Handles Keyboard interrupts
    '''
    try:
        # iterate through all lines in user input or cat command input
        for line in sys.stdin:
            # strip line of whitespace
            youtube_id = line.strip()
            # checks if Youtube ID is valid
            if youtube_id_checker(youtube_id):
                # echo Youtube ID to user
                sys.stdout.write(f"{youtube_id}\n")
            else:
                # writes error log to proper file
                logging.error(f"Invalid Youtube ID Provided: {youtube_id}")
    except KeyboardInterrupt:
        # handles Ctrl-C user input
        sys.exit(0)

# Main Check

if __name__ == "__main__":
    main()
