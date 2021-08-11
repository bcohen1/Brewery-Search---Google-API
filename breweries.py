import yaml
from decimal import Decimal
import requests
import pandas as pd
import time


def get_creds():
    """read in personal info from .yml file"""
    with open("credentials.yml", "r") as f:
        return yaml.load(f, Loader=yaml.FullLoader)


def generate_lat_long(my_addr):
    """Generate list of lat-longs to search"""
    lat_longs = []
    my_addr_lat = my_addr.split(",")[0]
    my_addr_long = my_addr.split(",")[1].strip()

    # 1 degree = 111,320m
    # 1 mile = 1609.34m

    for i in range(0, 3):
        combine = (
            str(my_addr_lat)
            + ", "
            + str(round(Decimal(my_addr_long) - Decimal(i * 0.2), 7))
        )
        lat_longs.append(combine)

    for i in range(0, 3):
        combine = (
            str(round(Decimal(my_addr_lat) - Decimal(0.2), 6))
            + ", "
            + str(round(Decimal(my_addr_long) - Decimal(i * 0.2), 7))
        )
        lat_longs.append(combine)

    return lat_longs


def get_search_results(lat_longs, api_key):
    """search nearby breweries and return list of results - search radii will overlap to avoid 60 item API limit and ensure no breweries are missed"""
    api_base = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?"
    radius = "25000"
    full_results = []

    for lat_long in lat_longs:
        api_str = (f"{api_base}location={lat_long}&radius={radius}&keyword=brewery&key={api_key}")
        api_resp = requests.get(api_str).json()
        results = api_resp["results"]
        time.sleep(3)

        while "next_page_token" in api_resp:
            token = api_resp["next_page_token"]
            api_str_token = f"{api_base}&pagetoken={token}&key={api_key}"
            api_resp = requests.get(api_str_token).json()
            results.extend(api_resp["results"])

        full_results.extend(results)
    return full_results


def clean_full_results(full_results):
    '''cleans list of API results and return as dataframe'''
    df = pd.DataFrame(full_results)
    df = df[
        [
            "place_id",
            "business_status",
            "rating",
            "user_ratings_total",
            "name",
            "vicinity"
        ]
    ]
    df.sort_values(by=["rating", "user_ratings_total"], ascending=False, inplace=True)
    df.drop(df[df["business_status"] != "OPERATIONAL"].index, inplace=True)
    df.drop_duplicates(subset=["name"], inplace=True)
    df.reset_index(drop=True, inplace=True)
    df["vicinity"] = df["vicinity"].str.replace("#", "")
    return df


def get_driving_distance(my_addr, api_key, df):
    """get drive time from home and return as column in dataframe"""
    dist_api_base = "https://maps.googleapis.com/maps/api/directions/json?"
    durations = []

    for i in df["vicinity"]:
        dist_api_str = (f"{dist_api_base}origin={my_addr}&destination={i}&key={api_key}")
        dist_api_resp = requests.get(dist_api_str).json()
        duration = dist_api_resp["routes"][0]["legs"][0]["duration"]["text"]
        durations.append(duration)

    df["duration"] = durations
    return df


def main():
    creds = get_creds()
    my_addr = creds["my_addr"]
    api_key = creds["api_key"]
    lat_longs = generate_lat_long(my_addr)
    full_results = get_search_results(lat_longs, api_key)
    df = clean_full_results(full_results)
    df = get_driving_distance(my_addr, api_key, df)
    df.to_csv("breweries.csv", index=False)
    return df


if __name__ == "__main__":
    main()
