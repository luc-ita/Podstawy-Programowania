import json


data_path = 'reservations.json'


def read_data(path):
    with open(path, 'r') as f:
        data = json.load(f)
    return data['reservations']


def get_number_of_room(reservations):
    rooms = set([r.get('room_number') for r in reservations])
    return len(rooms)


def get_paid_count(reservations):
    paid_reservation_ids = set([r['reservation_id'] for r in reservations if r['paid'] is True])
    return len(paid_reservation_ids)


def get_unpaid_count(reservations):
    paid_reservation_ids = set([r['reservation_id'] for r in reservations if r['paid'] is not True])
    return len(paid_reservation_ids)


def get_paid_total_value(reservations):
    paid_reservations_value = [r['nights'] * r['price_per_night'] for r in reservations if r['paid'] is True]
    return sum(paid_reservations_value)


def get_unpaid_total_value(reservations):
    unpaid_reservations_value = [r['nights'] * r['price_per_night'] for r in reservations if r['paid'] is not True]
    return sum(unpaid_reservations_value)



reservations = read_data(path=data_path)
room_cnt = get_number_of_room(reservations)
paid_reservations = get_paid_count(reservations)
unpaid_reservations = get_unpaid_count(reservations)
paid_value = get_paid_total_value(reservations)
unpaid_value = get_unpaid_total_value(reservations)

print(f"Number of rooms: {room_cnt}\n"      
        f"Reservations counts:\t {paid_reservations} paid,\t\t{unpaid_reservations} unpaid\n"
        f"Total value:\t\t\t {paid_value} paid, \t {unpaid_value} unpaid"
        )
