change_hat(Hats.Purple_Hat)

while get_pos_x() > 0:
    move(West)
while get_pos_y() > 0:
    move(South)

while True:
    # Variables (Change value count)
    number_of_hay = num_items(Items.Hay) < 10000
    number_of_wood = num_items(Items.Wood) < 10000
    number_of_carrot = num_items(Items.Carrot) < 10000
    number_of_pumpkin = num_items(Items.Pumpkin) < 10000
    number_of_sunflower = num_items(Items.Power) < 100

    for i in range(get_world_size()):
        plant(Entities.Bush)
        # if get_entity_type() == Entities.Bush:
        # do_a_flip()
        if can_harvest():
            harvest()
        move(North)

    move(East)
