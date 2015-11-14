_dungeon= {}
start_position = (0, 0)

def load_rooms():
	with open('resources.map.txt', 'r') as map:
		rows = map.readlines()
	x_max = len(rows[0].split('\t'))
	for i in range(len(rows)):
		columns = rows[y].split('\t')
		for x in range(x_max):
			room_name = columns[x].replace('\n', '')
			if room_name == "StartingRoom":
				global starting_position = (x, y)
			_dungeon[(x, y)] = None if room_name == '' else getattr(__import__('rooms'), room_name)(x, y)

def room_exists(x, y):
	return _dungeon.get((x, y))