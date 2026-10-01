import requests
from playsound3 import playsound
import time

# ==========================================
# SETTINGS
# ==========================================

CITY = ["amsterdam"]
MAX_PRICE = 1.5

CHECK_INTERVAL = 0

REGIONS_URL = "https://hostvds.com/api/regions/"
PLANS_URL = "https://hostvds.com/api/plans/"

# وضعیت قبلی هر Plan در هر Region
previous_status = {}


# ==========================================
# GET TARGET REGIONS
# ==========================================

def get_target_regions():
    try:
        response = requests.get(
            REGIONS_URL,
            timeout=2
        )
        response.raise_for_status()

        regions = response.json()

        result = []

        for region in regions:
            city_code = str(region.get("city_code", "")).lower()

            for city in CITY:
                if city.lower() in city_code:
                    result.append(region)

        return result

    except Exception:
        return []


# ==========================================
# CHECK PLANS
# ==========================================

def check():
    regions = get_target_regions()

    for region in regions:

        city_code = str(region.get("city_code", ""))

        # این همان کدی است که باید برای /api/plans/?region= استفاده شود.
        region_code = (
            region.get("region")
        )

        if not region_code:
            continue

        try:
            response = requests.get(
                PLANS_URL,
                params={"region": region_code},
                timeout=2
            )
            response.raise_for_status()

            plans = response.json()

        except Exception:
            continue

        for plan in plans:

            name = plan.get("name")
            price = plan.get("monthly")

            # قیمت نامعتبر
            if price is None:
                continue

            try:
                price = float(price)
            except (TypeError, ValueError):
                continue

            # ==========================
            # PRICE FILTER
            # ==========================

            if price > MAX_PRICE:
                continue

            # ==========================
            # STOCK
            # ==========================

            available = not plan.get("is_out_of_stock", True)

            low_stock = plan.get("is_low_stock", True)

            key = f"{region_code}:{name}"

            # اولین بار فقط وضعیت را ذخیره کن
            if key not in previous_status:

                print(
                    f"[INIT] {city_code} | "
                    f"{name} | "
                    f"{price} | "
                    f"{'AVAILABLE' if available else 'OUT OF STOCK'}"
                    f"{' | LOW STOCK' if available and low_stock else ''}"
                )

            # ==========================
            # OUT OF STOCK -> AVAILABLE
            # ==========================

            if (key not in previous_status or not previous_status[key]) and available:
                
                previous_status[key] = available

                print()
                print("=" * 55)
                print("🔥 SERVER AVAILABLE 🔥")
                print(f"Region : {city_code}")
                print(f"Plan   : {name}")
                print(f"Price  : {price}")
                print(f"Currency: {plan.get('currency', '?')}")
                print(f"CPU    : {plan.get('vcpus')}")
                print(f"RAM    : {plan.get('ram')} MB")
                print(f"Disk   : {plan.get('disk')} MB")

                if low_stock:
                    print("Stock  : LOW STOCK")

                print("=" * 55)
                print()

                playsound("beep.mp3")

            previous_status[key] = available


# ==========================================
# MAIN LOOP
# ==========================================

while True:
    check()
    time.sleep(CHECK_INTERVAL)
