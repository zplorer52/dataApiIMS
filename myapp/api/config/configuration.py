import os
import json


def read_cred(area=None):
    # conf_file = 'D:/Dutta/apiIMS/api/config/conf.json'
    conf_file = os.path.dirname(os.path.realpath(__file__))+'/conf.json'
    # print('conf file:', conf_file)
    flag = None
    if not area:
        return parsed_json
    if not os.path.exists(conf_file):
        print('Configuration file is not found: ', conf_file)
        return flag

    try:
        with open(conf_file) as conf:
            parsed_json = json.load(conf)
            # print(parsed_json)
            for loc in parsed_json["credential"]:
                # print(loc)
                if loc["area"] == area:
                    return loc
    except Exception as e:
        print(e)
        return flag
