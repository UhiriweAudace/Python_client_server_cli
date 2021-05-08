"""import different required packages"""
import argparse
from main_server import run_server
from helpers import print_current_time, print_device_information


def load_arguments_options():
    """This method will add different options on list in order to be used"""
    parser = argparse.ArgumentParser()

    # adding different options
    parser.add_argument('-c', '--current', action='store_true',
                        help='print out the current time')
    parser.add_argument('-i', '--info', action='store_true',
                        help='print out server system information')
    parser.add_argument('-ps', '--packet_size', type=int,
                        help='Specify how many packet size, you want to receive', required=True)

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
