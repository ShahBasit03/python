# import argparse

# parser=argparse.ArgumentParser(description="Simple Calculator")



# parser.add_argument("num1", type=float,help="First Number")
# parser.add_argument("num2", type=float,help="Second Number")

# parser.add_argument ("operation",choices=["add","sub","div","mul"] ,help="operation to perform")

# args=parser.parse_args()

# print(args)


# if(args.operation== "add"):
#   print(f"The result is {args.num1 + args.num2}")
 
# elif(args.operation== "sub"):
#   print(f"The result is {args.num1 - args.num2}")
 
# elif(args.operation== "mul"):
#   print(f"The result is {args.num1 * args.num2}")
 
# elif(args.operation== "div"):
#   print(f"The result is {args.num1 / args.num2}")
 
# else:
#   print("some error occured.") 



import argparse
import re

# Create argument parser
parser = argparse.ArgumentParser(description="Password Strength Checker")

# Positional argument: password
parser.add_argument(
    "password",
    help="Password to check strength"
)

# Optional argument: minimum length
parser.add_argument(
    "--min-length",
    type=int,
    default=8,
    help="Minimum required length (default: 8)"
)

# Parse arguments
args = parser.parse_args()

password = args.password
min_length = args.min_length

score = 0

# Length check
if len(password) >= min_length:
    score += 1

# Uppercase check
if re.search(r"[A-Z]", password):
    score += 1

# Lowercase check
if re.search(r"[a-z]", password):
    score += 1

# Digit check
if re.search(r"[0-9]", password):
    score += 1

# Special character check
if re.search(r"[@$!%*?&#]", password):
    score += 1

# Strength decision
if score <= 2:
    strength = "WEAK ❌"
elif score <= 4:
    strength = "MEDIUM ⚠️"
else:
    strength = "STRONG ✅"

print(f"Password strength: {strength}")
print(f"Score: {score}/5")
