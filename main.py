from argparse import ArgumentParser
from client import query

# here we set up the CLI args,
parser = ArgumentParser(
    description='Runs the sample HS100 Hacker Program'
)

parser.add_argument('host', help='The ip/location of the HS100 to hack')
parser.add_argument('command', help='the command to run, see commands.py')

args = parser.parse_args()

print("Running command '{}'".format(args.command))
response = query(args.host, args.command)
print("Response: {}".format(response))
