import math
import sys
import re
from decimal import Decimal
from fractions import Fraction
from string import whitespace, punctuation

print("Hello World")

print(math.log(sys.maxsize, 2))
print(math.factorial(52))

print(sys.int_info)
print(sys.maxsize)

print(id(1))

my_str = "Sammy likes declaring strings."
print(len(my_str))

tax_rate = Decimal('7.25')/Decimal(100)
purchase_amout = Decimal('2.95')
amount = Decimal(tax_rate * purchase_amout)
print(amount)

penny = Decimal('0.01')

total_amount = purchase_amout + tax_rate * purchase_amout
total_amount.quantize(penny)
print(total_amount)

sugar_cups = Fraction('2.5')
scale_factor = Fraction(5/8)
print(sugar_cups * scale_factor)
print(Fraction(24/16))

print((19/155)*(155/19))
answer = (19/155)*(155/19)
print(round(answer, 3))

print(1-answer)

#floor division
#//, %

# 3600 secs in one hour
total_seconds = 7385
hours = total_seconds//3600
remaining_seconds = total_seconds % 3600

minutes = remaining_seconds//60
seconds = remaining_seconds % 60
print(hours, minutes, seconds)

title = "Recipe 5: Rewriting, and the Immutable String"
colon_position = title.index(':')
print(colon_position)

discard_text, post_colon_text = title[:colon_position], title[colon_position+1:]
# above is the same as a = x, b = y

print(discard_text)
print(post_colon_text)

test = "testing @ mikeyb"
at_position = test.index('@')
before_at = test[:at_position]
after_at = test[at_position+1:] # the +1 is the position after @, so not to include it in the string
print(before_at)
print(after_at)

pre_colon_text, _, post_colon_text = title.partition(':')
# .partition returns three items, the part before the target, the target, and the part after the target.
# '_' is the target string
print(pre_colon_text)
print(post_colon_text)
print(_)

#post_colon_text = post_colon_text.replace(' ', '_')
#post_colon_text = post_colon_text.replace(',', '_')
print(post_colon_text)

for character in whitespace + punctuation:
    post_colon_text = post_colon_text.replace(character, '_')
print(post_colon_text)

post_colon_text = post_colon_text.lower().strip('_')
#strip() removes leading and trailing characters
print(post_colon_text)

while '__' in post_colon_text:
    post_colon_text = post_colon_text.replace('__', '_')
print(post_colon_text)


ingredient = "Kumquat: 2 cups"
# (ingredient words): (amount digits) (unit words)
#Rewrite the pattern into Regular Expression (RE) notation
pattern_text = r'(?P<ingredient>\w+):\s+(?P<amount>\d+)\s+(?P<unit>\w+)'
pattern = re.compile(pattern_text)
match = pattern.match(ingredient)
match is None # ???

match.groups()
print(match)

print(match.group('ingredient'))
print(match.group('amount'))
print(match.group('unit'))

id = "IAD"
location = "Duties Intl Airport"
max_temp = 32
min_temp = 13
precipitation = 0.4

# template string
# '{id:3d}  : {location:19s} : {max_temp:3d} / {min_temp:3d} / {precipitation:5.2f}'
# s for string
# d for decimal number
# f for floating-point number
# number is the lenght value

print('{id:3s}  : {location:19s} : {max_temp:3d} / {min_temp:3d} / {precipitation:5.2f}'.format(
    id=id,
    location=location,
    max_temp=max_temp,
    min_temp=min_temp,
    precipitation=precipitation
))

# defining it as a dictionary object
data = dict(
    id=id,
    location=location,
    max_temp=max_temp,
    min_temp=min_temp,
    precipitation=precipitation
)
print('{id:3s}  : {location:19s} : {max_temp:3d} / {min_temp:3d} / {precipitation:5.2f}'.format_map(data))
# The built-in vars() function builds a dictionary of all of the local variables for us:
# The vars() function is very handy for building a dictionary automatically.
print('{id:3s}  : {location:19s} : {max_temp:3d} / {min_temp:3d} / {precipitation:5.2f}'.format_map(vars()))

#storing template as a string
test_template = '{id:3s}  : {location:19s} : {max_temp:3d} / {min_temp:3d} / {precipitation:5.2f}'
print(test_template.format_map(vars()))


print("End of Main")
