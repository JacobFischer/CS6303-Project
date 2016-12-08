from argparse import ArgumentParser
from query import query

# here we set up the CLI args,
parser = ArgumentParser(
    description='Runs the sample HS100 Hacker Program'
)

parser.add_argument('host', help='The ip/location of the HS100 to hack')
parser.add_argument(
    'command',
    help='the command to run, see commands.py, or raw json to send'
)

args = parser.parse_args()

# now that the args are parsed run the query and print the response
print("Running command '{}'".format(args.command))
response = query(args.host, args.command)
print("Response: {}".format(response))
