clear()

change_hat(Hats.Purple_Hat)

while get_pos_x() > 0:
    move(West)
while get_pos_y() > 0:
    move(South)

while True:
    for i in range(get_world_size()):
        if can_harvest():
            harvest()
            till()
            plant(Entities.Carrot)

        move(North)

    move(East)
