import json


def shortest_path():
    with open('subway/data/subway.json') as data_file:
        data = json.load(data_file)

    return data

    # pprint(data)  # data는 json 전체를 dictionary 형태로 저장하고 있음
    #
    # # -----여기까지 동일-----
    #
    # SUBWAY_LINES = [item for item in data]
    #
    #
    # print("==================")
    # pprint(SUBWAY_LINES)
    # print("==================\n")