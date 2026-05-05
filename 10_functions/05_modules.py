# two types of modukes in python 
# -Build in modules
# - External module
# The listof modules is here https://docs.python.org/3/py-modindex.html
import math
import mymodule
mymodule.hello()
import requests 
r = requests.get("https://www.google.com")
print(r.text)

print(math.sqrt(16))

