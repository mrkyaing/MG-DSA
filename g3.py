import pandas as pd

# Manually recreate the dummy data
dummy_data_manual = {
    "No": [1, 2, 3, 4, 5],
    "House Type": ["Condo", "Villa", "Townhouse", "Detached", "Condo"],
    "Address": [
        "101 Moo 5, Chiang Mai",
        "102 Moo 6, Chiang Mai",
        "103 Moo 3, Chiang Mai",
        "104 Moo 4, Chiang Mai",
        "105 Moo 2, Chiang Mai"
    ],
    "Township": ["Mueang", "Hang Dong", "San Sai", "Mae Rim", "Mueang"],
    "District": ["City Center", "Suburb", "Rural Area", "Suburb", "City Center"],
    "Bed Room": [2, 3, 2, 3, 1],
    "Single Room": [1, 1, 2, 1, 1],
    "Lat/Long": [
        "18.751234, 98.975432",
        "18.765432, 98.984321",
        "18.743210, 98.965432",
        "18.732145, 98.978901",
        "18.749876, 98.962345"
    ],
    "Price (THB)": [3200000, 5600000, 2800000, 4500000, 2200000],
    "Map Location": [
        "https://maps.example.com/location1",
        "https://maps.example.com/location2",
        "https://maps.example.com/location3",
        "https://maps.example.com/location4",
        "https://maps.example.com/location5"
    ],
    "Remark": ["New listing", "Fully furnished", "Price negotiable", "Urgent sale", "New listing"]
}

# Create DataFrame
dummy_df_manual = pd.DataFrame(dummy_data_manual)

# Save as CSV
csv_file_path = "D:\\works\\MG-DSA\\ChiangMai_RealEstate_DummyData.csv"
dummy_df_manual.to_csv(csv_file_path, index=False)

csv_file_path
