#!/usr/bin/env python3

"""import different required packages"""
import argparse
import sys
import platform
from datetime import datetime
from main_server import run_server

def load_arguments_options():
    """This method will add different options on list in order to be used"""
    parser = argparse.ArgumentParser()

    # adding different options
    parser.add_argument('-c', '--current', action='store_true',
                        help='print out the current time')
    parser.add_argument('-i', '--info', action='store_true',
                        help='print out server system information')
    parser.add_argument('-ps', '--packet_size', type=int,
                        help='Specify how many packet size, you want to receive')

    return parser.parse_args()


def handle_arguments_options(args):
    """This method will handle different actions based on the provided arguments"""
    if args.current:
        print_current_time()

    if args.info:
        print_device_information()

    if args.packet_size:
        run_server(args.packet_size)

    return "Invalid argument options"


def print_device_information():
    """This method will print out the device system information"""
    print("\nServer System information")
    print("----------------------------")
    print(str(f"platform detail : {platform.platform()}"))
    print(str(f"system name : {platform.system()}"))
    print(str(f"processor name : {platform.processor()}"))
    print(str(f"architectural detail : {platform.architecture()}\n"))
    sys.exit(1)


def print_current_time():
    """This method will print out the current date and time on the server which is up running"""
    print('Current Date and Time is ', datetime.now())
    sys.exit(1)
