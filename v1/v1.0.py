clear()
change_hat(Hats.Wizard_Hat)

while True:
    # Variables
    number_of_hay = num_items(Items.Hay) < 10000
    number_of_wood = num_items(Items.Wood) < 5000
    number_of_carrot = num_items(Items.Carrot) < 1000

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
        # else:

        move(North)
    move(East)
