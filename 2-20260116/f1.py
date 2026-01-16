clear()
change_hat(Hats.Purple_Hat)

# Move to bottom-left corner
while get_pos_x() > 0:
	move(West)
while get_pos_y() > 0:
	move(South)

going_up = True

while True:

	# Resource
	hay = num_items(Items.Hay)
	wood = num_items(Items.Wood)
	carrot = num_items(Items.Carrot)
	pumpkin = num_items(Items.Pumpkin)
	power = num_items(Items.Power)

	for _ in range(get_world_size()):
		x = get_pos_x()
		y = get_pos_y()

		# Harvest first (always optimal)
		if can_harvest():
			harvest()

		# === Planting priority ===
		#if wood < hay * 2:
		if wood < hay:
			if (x + y) % 2 == 0:
				plant(Entities.Tree)
		
		elif hay < wood:
			plant(Entities.Grass)
		
		elif carrot < hay:
			if get_ground_type() == Grounds.Grassland:
				till()
			plant(Entities.Carrot)

		#elif need_pumpkin:
			#if get_ground_type() == Grounds.Grassland:
				#till()
			#plant(Entities.Pumpkin)

		#elif need_power:
			#plant(Entities.Sunflower)

		# === Movement ===
		if going_up:
			move(North)
		else:
			move(South)

	move(East)
	going_up = not going_up
	