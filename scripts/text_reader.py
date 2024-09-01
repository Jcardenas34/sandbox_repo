#! /usr/bin/env python

'''
Description:
--------------
This is another test file for git repo

'''

import argparse
import os


def main(args):

#    print("Testing")
    with open(args.infile) as infile:
        for k in infile.readlines():
            print(k)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="For now a standard arg parse for input arguments")
    parser.add_argument("infile", type=str, help="Input file path" )    
    args = parser.parse_args()
    main(args)
