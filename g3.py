import pandas as pd
import random

# List of real Chiang Mai townships (amphoes/subdistricts)
townships = [
    "Mueang", "Hang Dong", "San Sai", "Mae Rim", "Saraphi", "San Kamphaeng", "Doi Saket", "San Pa Tong",
    "Mae On", "Mae Taeng", "Chom Thong", "Doi Lo", "Hot", "Omkoi", "Samoeng", "Phrao", "Mae Chaem", "Wiang Haeng",
    "Mae Wang", "Doi Tao", "Chiang Dao", "Mae Ai"
]

house_types = ["Condo", "Villa", "Townhouse", "Detached", "Apartment", "Bungalow"]
districts = ["City Center", "Suburb", "Rural Area", "Old Town", "New Town"]
remarks = ["New listing", "Fully furnished", "Price negotiable", "Urgent sale", "Renovated", "Great view", "Near school", "Near market", "Quiet area", "Investment opportunity"]

records = []
for i in range(1, 3001):
    township = random.choice(townships)
    house_type = random.choice(house_types)
    address = f"{100 + i} Moo {random.randint(1, 10)}, Chiang Mai"
    district = random.choice(districts)
    bed_room = random.randint(1, 5)
    single_room = random.randint(1, 3)
    lat = round(random.uniform(18.6, 19.0), 6)
    lng = round(random.uniform(98.8, 99.1), 6)
    latlong = f"{lat}, {lng}"
    price = random.randint(1500000, 12000000)
    map_location = f"https://maps.example.com/location{i}"
    remark = random.choice(remarks)
    records.append({
        "No": i,
        "House Type": house_type,
        "Address": address,
        "Township": township,
        "District": district,
        "Bed Room": bed_room,
        "Single Room": single_room,
        "Lat/Long": latlong,
        "Price (THB)": price,
        "Map Location": map_location,
        "Remark": remark
    })

# Create DataFrame
dummy_df_manual = pd.DataFrame(records)

# Save as CSV
csv_file_path = "D:\\works\\MG-DSA\\ChiangMai_RealEstate_DummyData.csv"
dummy_df_manual.to_csv(csv_file_path, index=False)

csv_file_path
