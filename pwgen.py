#!/usr/bin/python
import string
import secrets
from argparse import ArgumentParser


def pass_gen(args):
   chars = string.ascii_uppercase + string.ascii_lowercase

   if ( args.number == True ):
      chars += string.digits

   if ( args.special == True ):
      chars += '!@#$%^&*()-_=+|`~[{]};:",<.>/?'

   return ''.join(secrets.choice(chars) for x in range(args.length))


def main():
   parser = ArgumentParser()
   parser.add_argument('-l', '--length', type=int, default=8, help='Password Length')
#   parser.add_argument('-c', '--char', type=bool, default=True, help='Include Charactors')
   parser.add_argument('-n', '--number', action='store_true', help='Include Numbers')
   parser.add_argument('-s', '--special', action='store_true', help='Include Special Words')

   print("password: ", end='')
   print(pass_gen(parser.parse_args()))


if __name__ in '__main__':
   main()
