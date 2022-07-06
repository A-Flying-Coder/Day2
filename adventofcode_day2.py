position = 0
depth = 0
aim = 0

with open('day2_input.txt', 'r') as f:
	commands = f.readlines()

for line in commands:
	line_text = line.split()
	direction = line_text[0]
	number = int(line_text[1].replace('\n', ''))
	if direction == 'forward':
		position += number
		increase = aim * number
		depth += increase
	elif direction == 'down':
		aim += number
		# depth += number
		#for step 1
	else: 
		# depth -= number
		#for step 1
		aim -= number
		
print(f'Position = {position}')
print(f'Depth = {depth}')
print(f'Aim = {aim}')
multiple = position * depth
print(f'Multiple = {multiple}')