clear()

change_hat(Hats.Purple_Hat)

while get_pos_x() > 0:
    move(West)
while get_pos_y() > 0:
    move(South)

while True:
    # Variables (Change value count)
    number_of_hay = num_items(Items.Hay) < 1000
    number_of_wood = num_items(Items.Wood) < 1000
    number_of_carrot = num_items(Items.Carrot) < 1000
    number_of_pumpkin = num_items(Items.Pumpkin) < 1000
    number_of_sunflower = num_items(Items.Power) < 1000

    for i in range(get_world_size()):
        if can_harvest():
            harvest()
        if number_of_hay:
            plant(Entities.Grass)
        elif number_of_wood:
            plant(Entities.Tree)
            move(North)
            plant(Entities.Bush)
        elif number_of_carrot:
            if get_ground_type() == Grounds.Grassland:
                till()
                plant(Entities.Carrot)
            elif get_ground_type() == Grounds.Soil:
                plant(Entities.Carrot)

        move(North)

    move(East)
