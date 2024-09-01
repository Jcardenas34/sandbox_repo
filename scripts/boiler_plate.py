#! /usr/bin/env python

'''
Description:
--------------
This is a script thatcontaions the basic main function that will
be used as the basis for other scripts

'''

import argparse
import os


def main(args):

    print("Testing")



if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="For now a standard arg parse for input arguments")
    parser.add_argument("infile", type=str, help="Input file path" )    
    args = parser.parse_args()
    main(args)
