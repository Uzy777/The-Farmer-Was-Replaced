# clear()
change_hat(Hats.Wizard_Hat)


while get_pos_x() > 0:
    move(West)
while get_pos_y() > 0:
    move(South)

while True:
    # Variables
    number_of_hay = num_items(Items.Hay) < 10000
    number_of_wood = num_items(Items.Wood) < 10000
    number_of_carrot = num_items(Items.Carrot) < 10000
    number_of_pumpkin = num_items(Items.Pumpkin) < 10000
    number_of_sunflower = num_items(Items.Power) < 100

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
            # use_item(Items.Water)
            till()
            plant(Entities.Carrot)
        elif number_of_pumpkin:
            till()
            plant(Entities.Pumpkin)
        elif number_of_sunflower:
            # use_item(Items.Water)
            till()
            plant(Entities.Sunflower)

        # else:

        move(North)
    move(East)
