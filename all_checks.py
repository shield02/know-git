#!/usr/bin/env python3 - a shabang line
import os
import sys

def check_reboot():
    """Returns True if the computer has pending reboot."""
    return os.path.exists("/run/reboot-required") 
    # this is the file that is created on our computer when some software requires a reboot

def main():
    if check_reboot():
        print("Pending Reboot.")
        sys.exit(1)
    print("Everything ok.")
    sys.exit(0)

main()