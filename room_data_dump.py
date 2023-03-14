import csv
from django.db.models import Sum
from bidding.models import *
from django.db.models import Q


with open("room_training_data.csv", "w") as csvfile:
    filew = csv.writer(csvfile)
    filew.writerow([
        'Dealer',
        'Order Type',
        'Exterior Material',
        'Cabinet Interior',
        'Drawer Box Type',
        'Drawer Glide',
        'Door Style',
        'Finish Options',
        'Number of Cabinets',
    ])

    # print(ds)
    rooms = Room.objects.filter(
        deleted__isnull=True,
        bid__approved_by_dealer__gt='2021-01-01',
    )

    roomCount = 1
    totalRooms = len(rooms)

    for room in rooms:
        cabs = room.cabinet_set.filter(deleted__isnull=True)
        if room.cabinet_box_interior:
            cabinet_box_interior = room.cabinet_box_interior.name
        else:
            cabinet_box_interior = "None"

        if room.drawer_glide:
            drawer_glide = room.drawer_glide.name
        else:
            drawer_glide = "None"

        filew.writerow([
            # 'Normal' if room.bid.order_type is 1 else 'Hot List' if room.bid.order_type is 2 else 'Sample',
            room.bid.order_type,
            room.bid.dealer.name,
            room.wood_type.name,
            cabinet_box_interior,
            drawer_glide,
            room.door_style.name,
            ", ".join([f.name for f in room.finishes.all()]),
            len(cabs),
        ])

        print(str(round((roomCount / totalRooms) * 100, 2)) + '%')
        roomCount += 1
