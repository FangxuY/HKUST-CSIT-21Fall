import json
from pathlib import Path
import os
import pandas

'''
    check SiteInfo.json
'''


def check_SiteInfo(json_file):
    with json_file.open() as f:
        json_result = json.load(f)

    flag = True
    # print(json_result)
    for name, values in json_result.items():
        if name == 'SiteAddress':
            if type(values).__name__ != 'str':
                print(name, 'Error value:', values)
                flag = False
            # else:
            #     print(name, 'Pass')

        elif name == 'BuildingID':
            if type(values).__name__ != 'str':
                print(name, 'Error value:', values)
                flag = False
            # else:
            #     print(name, 'Pass')

        elif name == 'OutdoorSiteID':
            if type(values).__name__ != 'str':
                print(name, 'Error value:', values)
                flag = False
            # else:
            #     print(name, 'Pass')

        elif name == 'SiteOwner':
            if type(values).__name__ != 'str':
                print(name, 'Error value:', values)
                flag = False
            # else:
            #     print(name, 'Pass')

        elif name == 'Contacts':
            if type(values).__name__ != 'str':
                print(name, 'Error value:', values)
                flag = False
            # else:
            #     print(name, 'Pass')

        elif name == 'IndoorSite':
            if not (values == True or values == False):
                print(name, 'Error value:', values)
                flag = False
            # else:
            #     print(name, 'Pass')

    if flag:
        print(json_file, "Pass")


'''
    check BuildingLocSetting.json and OutdoorLocSetting.json
'''


def check_LocSetting(json_file):
    with json_file.open() as f:
        json_result = json.load(f)

    flag = True
    # print(json_result)
    for name, values in json_result.items():
        if name == 'BuildingID':
            if type(values).__name__ != 'str':
                print(name, 'Error value:', values)
                flag = False
            # else:
            #     print(name, 'Pass')

        elif name == 'OutdoorSiteID':
            if type(values).__name__ != 'str':
                print(name, 'Error value:', values)
                flag = False
            # else:
            #     print(name, 'Pass')

        elif name == 'ShareSiteSignal':
            if not (values == True or values == False):
                print(name, 'Error value:', values)
                flag = False
            # else:
            #     print(name, 'Pass')

        elif name == 'SiteSignalMode':
            if type(values).__name__ != 'list':
                print(name, 'Error value:', values)
                flag = False
            else:
                for mode in values:
                    if type(mode).__name__ != 'str':
                        print(name, 'Error value:', values)
                        flag = False

        elif name == 'CloudLocSignalMode':
            if type(values).__name__ != 'list':
                print(name, 'Error value:', values)
                flag = False
            else:
                for mode in values:
                    if type(mode).__name__ != 'str':
                        print(name, 'Error value:', values)
                        flag = False

        elif name == 'Boundary':
            if type(values).__name__ != 'list':
                print(name, 'Error value:', values)
                flag = False
            else:
                for value in values:
                    if type(value).__name__ != 'list':
                        print(name, 'Error value:', values)
                        flag = False
                    else:
                        if not check_longAndLat(value):
                            print(name, 'Error value:', values)
                            flag = False

        elif name == 'RemoteCloudLocUploadURL':
            if type(values).__name__ != 'str':
                print(name, 'Error value:', values)
                flag = False

        elif name == 'RemoteCloudLocDownloadURL':
            if type(values).__name__ != 'str':
                print(name, 'Error value:', values)
                flag = False
            # else:
            #     print(name, 'Pass')
        elif name == 'RemoteSignalDownloadURL':
            if type(values).__name__ != 'str':
                print(name, 'Error value:', values)
                flag = False
            # else:
            #     print(name, 'Pass')

    if flag:
        print(json_file, "Pass")


'''
    check OutdoorSite.json
'''


def check_Outdoor(json_file):
    with json_file.open() as f:
        json_result = json.load(f)

    flag = True
    # print(json_result)
    for name, values in json_result.items():
        if name == 'OutdoorSiteID':
            if type(values).__name__ != 'str':
                print(name, 'Error value:', values)
                flag = False
            # else:
            #     print(name, 'Pass')

        elif name == 'OutdoorSiteName':
            if type(values).__name__ != 'str':
                print(name, 'Error value:', values)
                flag = False
            # else:
            #     print(name, 'Pass')

        elif name == 'Boundary':
            if type(values).__name__ != 'list':
                print(name, 'Error value:', values)
                flag = False
            else:
                for value in values:
                    if type(value).__name__ != 'list':
                        print(name, 'Error value:', values)
                        flag = False
                    else:
                        if not check_longAndLat(value):
                            print(name, 'Error value:', values)
                            flag = False

        elif name == 'MapDataID':
            if type(values).__name__ != 'str':
                print(name, 'Error value:', values)
                flag = False

            # else:
            #     print(name, 'Pass')

    if flag:
        print(json_file, "Pass")


'''
    check Builiding.json
'''


def check_Building(json_file):
    with json_file.open() as f:
        json_result = json.load(f)

    flag = True
    # print(json_result)
    for name, values in json_result.items():
        if name == 'BuildingID':
            if type(values).__name__ != 'str':
                print(name, 'Error value:', values)
                flag = False
            # else:
            #     print(name, 'Pass')

        elif name == 'Name':
            if type(values).__name__ != 'str':
                print(name, 'Error value:', values)
                flag = False
            # else:
            #     print(name, 'Pass')

        elif name == 'MapDataIDs':
            if type(values).__name__ != 'list':
                print(name, 'Error value:', values)
                flag = False
            else:
                for mapDataID in values:
                    if type(mapDataID).__name__ != 'str':
                        print(name, 'Error value:', values)
                        flag = False

        elif name == 'ChildrenFloors':
            if type(values).__name__ != 'list':
                print(name, 'Error value:', values)
                flag = False
            else:
                for mapDataID in values:
                    if type(mapDataID).__name__ != 'str':
                        print(name, 'Error value:', values)
                        flag = False

        elif name == 'DefaultFloorID':
            if type(values).__name__ != 'str':
                print(name, 'Error value:', values)
                flag = False
            # else:
            #     print(name, 'Pass')

        elif name == 'Boundary':
            if type(values).__name__ != 'list':
                print(name, 'Error value:', values)
                flag = False
            else:
                for value in values:
                    if type(value).__name__ != 'list':
                        print(name, 'Error value:', values)
                        flag = False
                    else:
                        if not check_longAndLat(value):
                            print(name, 'Error value:', values)
                            flag = False

            # else:
            #     print(name, 'Pass')

    if flag:
        print(json_file, "Pass")


'''
    check Floor.json
'''


def check_Floor(json_file):
    with json_file.open() as f:
        json_result = json.load(f)

    flag = True
    # print(json_result)
    for name, values in json_result.items():
        if name == 'FloorNo':
            if type(values).__name__ != 'str':
                print(name, 'Error value:', values)
                flag = False
            # else:
            #     print(name, 'Pass')

        elif name == 'Name':
            if type(values).__name__ != 'str':
                print(name, 'Error value:', values)
                flag = False
            # else:
            #     print(name, 'Pass')

        elif name == 'MapDataIDs':
            if type(values).__name__ != 'list':
                print(name, 'Error value:', values)
                flag = False
            else:
                for mapDataID in values:
                    if type(mapDataID).__name__ != 'str':
                        print(name, 'Error value:', values)
                        flag = False

        elif name == 'ChildrenRegions':
            if type(values).__name__ != 'list':
                print(name, 'Error value:', values)
                flag = False
            else:
                for mapDataID in values:
                    if type(mapDataID).__name__ != 'str':
                        print(name, 'Error value:', values)
                        flag = False

        elif name == 'ParentID':
            if type(values).__name__ != 'str':
                print(name, 'Error value:', values)
                flag = False
            # else:
            #     print(name, 'Pass')

        elif name == 'DefaultRegionID':
            if type(values).__name__ != 'str':
                print(name, 'Error value:', values)
                flag = False

    if flag:
        print(json_file, "Pass")


'''
    check Region.json
'''


def check_Region(json_file):
    with json_file.open() as f:
        json_result = json.load(f)

    flag = True
    # print(json_result)
    for name, values in json_result.items():
        if name == 'RegionNo':
            if type(values).__name__ != 'str':
                print(name, 'Error value:', values)
                flag = False
            # else:
            #     print(name, 'Pass')

        elif name == 'Name':
            if type(values).__name__ != 'str':
                print(name, 'Error value:', values)
                flag = False
            # else:
            #     print(name, 'Pass')

        elif name == 'MapDataIDs':
            if type(values).__name__ != 'list':
                print(name, 'Error value:', values)
                flag = False
            else:
                for mapDataID in values:
                    if type(mapDataID).__name__ != 'str':
                        print(name, 'Error value:', values)
                        flag = False

        elif name == 'ConnectedRegions':
            if type(values).__name__ != 'list':
                print(name, 'Error value:', values)
                flag = False
            else:
                for ConnectedRegion in values:
                    if type(ConnectedRegion).__name__ != 'dict':
                        print(name, 'Error value:', values)
                        flag = False
                    else:
                        if not check_ConnectedRegions(ConnectedRegion):
                            print(name, 'Error value:', values)
                            flag = False

        elif name == 'ParentID':
            if type(values).__name__ != 'str':
                print(name, 'Error value:', values)
                flag = False
            # else:
            #     print(name, 'Pass')

    if flag:
        print(json_file, "Pass")


'''
    check Map.json
'''


def check_Map(json_file):
    with json_file.open() as f:
        json_result = json.load(f)

    flag = True
    # print(json_result)
    for name, values in json_result.items():
        if name == 'MapID':
            if type(values).__name__ != 'str':
                print(name, 'Error value:', values)
                flag = False
            # else:
            #     print(name, 'Pass')

        elif name == 'MapFormat':
            if type(values).__name__ != 'str':
                print(name, 'Error value:', values)
                flag = False
            # else:
            #     print(name, 'Pass')

        elif name == 'Boundary':
            if type(values).__name__ != 'list':
                print(name, 'Error value:', values)
                flag = False
            else:
                for value in values:
                    if type(value).__name__ != 'list':
                        print(name, 'Error value:', values)
                        flag = False
                    else:
                        if not check_longAndLat(value):
                            print(name, 'Error value:', values)
                            flag = False

        elif name == 'GeodeticPoints':
            if type(values).__name__ != 'list':
                print(name, 'Error value:', values)
                flag = False
            else:
                for GeodeticPoint in values:
                    if type(GeodeticPoint).__name__ != 'dict':
                        print(name, 'Error value:', values)
                        flag = False
                    else:
                        if not check_GeodeticPoint(GeodeticPoint):
                            print(name, 'Error value:', values)
                            flag = False

        elif name == 'AttachedPrimalSpaceID':
            if type(values).__name__ != 'str':
                print(name, 'Error value:', values)
                flag = False
            # else:
            #     print(name, 'Pass')

        elif name == 'Filename':
            if type(values).__name__ != 'str':
                print(name, 'Error value:', values)
                flag = False
            # else:
            #     print(name, 'Pass')

        elif name == 'Validation':
            if not (values == True or values == False):
                print(name, 'Error value:', values)
                flag = False
            # else:
            #     print(name, 'Pass')

    if flag:
        print(json_file, "Pass")


def check_longAndLat(long_lat: list):
    long = long_lat[0]
    lat = long_lat[1]
    if 113.0 <= long <= 114.5 and 22.1 <= lat <= 22.8:
        return True
    return False


def check_ConnectedRegions(Connected_region: dict):
    flag = True
    for name, values in Connected_region.items():
        if name == 'TransitionArea':
            if not type(values).__name__ == 'list':
                print(name, 'Error value:', values)
                flag = False
            else:
                for value in values:
                    if type(value).__name__ != 'list':
                        print(name, 'Error value:', values)
                        flag = False
                    else:
                        if not check_longAndLat(value):
                            print(name, 'Error value:', values)
                            flag = False
        elif name == 'ArrivalArea':
            if type(values).__name__ != 'list':
                print(name, 'Error value:', values)
                flag = False
            else:
                for value in values:

                    if type(value).__name__ != 'dict':
                        print(name, 'Error value:', values)
                        flag = False
                    else:
                        for sub_name, sub_values in value.items():
                            if sub_name == 'RegionID':
                                if type(sub_values).__name__ != 'str':
                                    print(name, sub_name, 'Error value:', sub_values)
                                    flag = False
                            elif sub_name == 'Area':
                                if type(sub_values).__name__ != 'list':
                                    print(name, sub_name, 'Error value:', sub_values)
                                    flag = False
                                else:
                                    for sub_value in sub_values:
                                        if not check_longAndLat(sub_value):
                                            print(name, sub_name, 'Error value:', sub_value)
                                            flag = False
    return flag


def check_GeodeticPoint(GeodeticPoint: dict):
    flag = True
    for name, values in GeodeticPoint.items():
        if name == 'x':
            if not type(values).__name__ == 'int':
                print(name, 'Error value:', values)
                flag = False
        elif name == 'y':
            if type(values).__name__ != 'int':
                print(name, 'Error value:', values)
                flag = False
            # else:
            #     print(name, 'Pass')
        elif name == 'lon':
            if type(values).__name__ != 'float':
                print(name, 'Error value:', values)
                flag = False
            else:
                if not 113.0 <= values <= 114.5:
                    print(name, 'Error value:', values)
                    flag = False
        elif name == 'lat':
            if type(values).__name__ != 'float':
                print(name, 'Error value:', values)
                flag = False
            else:
                if not 22.1 <= values <= 22.8:
                    print(name, 'Error value:', values)
                    flag = False

    return flag


if __name__ == '__main__':
    root_dir = 'HKSTP_outdoor_2.0'
    path = Path(root_dir)
    all_json_file = list(path.glob('**/*.json'))
    for json_file in all_json_file:
        print('Scanning:', json_file, '...')
        # service_name = json_file.parent.stem
        # print(service_name)
        file_name = json_file.name
        # print(is_json(json_file))
        # print(is_json(json_str)
        if file_name == 'SiteInfo.json':
            try:
                check_SiteInfo(json_file)
            except BaseException:
                print("Warning:", json_file, "Error")
        elif file_name == 'BuildingLocSetting.json':
            try:
                check_LocSetting(json_file)
            except BaseException:
                print("Warning:", json_file, "Error")
        elif file_name == 'LocSetting.json':
            try:
                check_LocSetting(json_file)
            except BaseException:
                print("Warning:", json_file, "Error")
        elif file_name == 'Building.json':
            try:
                check_Building(json_file)
            except BaseException:
                print("Warning:", json_file, "Error")
        elif file_name == 'Floor.json':
            try:
                check_Floor(json_file)
            except BaseException:
                print("Warning:", json_file, "Error")
        elif file_name == 'Map.json':
            try:
                check_Map(json_file)
            except BaseException:
                print("Warning:", json_file, "Error")
        elif file_name == 'Region.json':
            try:
                check_Region(json_file)
            except BaseException:
                print("Warning:", json_file, "Error")
        elif file_name == 'OutdoorSite.json':
            try:
                check_Outdoor(json_file)
            except BaseException:
                print("Warning:", json_file, "Error")
        # with json_file.open() as f:
        #     json_result = json.load(f)
        # print(json_result)
