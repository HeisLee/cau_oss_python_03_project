class parking_spot: 
    def __init__(self, name, city, district, ptype, longitude, latitude):
        self.__item ={
            'name':name,
            'city':city,
            'district':district,
            'ptype':ptype,
            'longitude':longitude,
            'latitude':latitude
        }
    def receive(self, keyword='name'):
        return self.__item.receive(keyword)
    # you have to implement 'constructor(생성자)' and 'receive' method
    def __str__(self):
        item = self.__item
        s  = f"[{item['name']}({item['ptype']})] "
        s += f"{item['city']} {item['district']}"
        s += f"(lat:{item['latitude']}, long:{item['longitude']})"
        return s

def str_list_to_class_list(str_list):
    spots=[]
    for line in str_list:
        data = line.split(',')
        name=data[1]
        city=data[2]
        district=data[3]
        ptype=data[4]
        longitude=float(data[5])
        latitude=float(data[6])
        spot=parking_spot(name, city, district, ptype, longitude, latitude)
        spots.append(spot)
    return spots

def print_spots(spots):
    print(f"---print elements({len(spots)})---")
    for spot in spots:
        print(spot)

# 각 단계별로 테스트 (테스트할때 주석해제 후 사용)
if __name__ == '__main__':
    print("Testing the module...")
    # version#2
    import file_manager
    str_list = file_manager.read_file("./input/free_parking_spot_seoul.csv")
    spots = str_list_to_class_list(str_list)
    print_spots(spots)

    # version#3
    # spots = filter_by_district(spots, '동작')
    # print_spots(spots)
    
    # version#4
    # spots = sort_by_keyword(spots, 'name')
    # print_spots(spots)