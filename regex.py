import re


play_num_color = 'play/5/blue'

play_pattern = re.compile(r'^([\w\-]+)')
play = play_pattern.finditer(play_num_color)

number_pattern = re.compile(r'\d')
number = number_pattern.finditer(play_num_color)

color_pattern  = re.compile(r'\b(\w+)\W*$')
color = color_pattern.finditer(play_num_color)

for k in color:
  color = (k.group(0))

print(color)

for k in number:
    number = (k.group(0))
print(number)

for k in play:
  play = (k.group(0)) 

print(play)