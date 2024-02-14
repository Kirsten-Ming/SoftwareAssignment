import argparse

parser = argparse.ArgumentParser(
                    description='Say Hello to things')
parser.add_argument('target', help='Name of person to greet')
parser.add_argument('--repeat', 
                    '-r', 
                    type=int, 
                    default=1, 
                    help="Number of times to greet")
parser.add_argument('--goodbye', 
                    '-g', 
                    action='store_true',
                    help='Say goodbye instead of hello')

args = parser.parse_args()

if args.goodbye == True:
    greeting = 'Goodbye'
else:
    greeting = 'Hello'

for _ in range(args.repeat):
    print(f'{greeting} {args.target}!')
