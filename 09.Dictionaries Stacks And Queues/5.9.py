import csv
import json


def read_provinces(path='province.csv') -> dict:
    province_dict = dict()
    with open(path, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            province_dict[row['Letter']] = row['Name']
    return province_dict


def read_plates(path='vehicle.txt') -> list:
    with open(path, 'r') as f:
        plates = f.read().split('\n')
    return plates


def count_plates_per_region(plates, provinces):
    province_counts = {province: 0 for province in provinces.values()}

    for plate in plates:
        first_letter = plate[0]
        province_counts[provinces[first_letter]] += 1

    return province_counts



provinces = read_provinces()
plates = read_plates()
province_counts = count_plates_per_region(plates, provinces)
print(json.dumps(province_counts, indent=4, ensure_ascii=False))

