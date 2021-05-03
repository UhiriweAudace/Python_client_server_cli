#!/usr/bin/env python3

"""import different handlers"""
from options_controller import load_arguments_options, handle_arguments_options

if __name__ == "__main__":
    ARGUMENTS = load_arguments_options()
    handle_arguments_options(ARGUMENTS)
