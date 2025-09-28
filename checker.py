import requests
from playsound import playsound
import time

def fetch_regions_and_check_conditions():
    url = "https://hostvds.com/api/regions/"

    try:
        response = requests.get(url, timeout=1)
        response.raise_for_status()

        regions = response.json()

        for region in regions:
            if (
                region.get("is_available") and
                not region.get("is_out_of_stock") and
                not region.get("is_maintenance") and
                not region.get("is_read_only") and
                region.get("available_ips_v4") and
                region.get("city_code") in {"paris"}
            ):
                print(f"Region {region.get('city_code')} meets the conditions.")
                playsound("beep.mp3")

    except Exception as e:
        pass
    
    return

while True:
    fetch_regions_and_check_conditions()
    time.sleep(0.5)

