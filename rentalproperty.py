import pandas as pd

# Define the data again after environment reset
commercial_properties = {
    "Property": ["Studio Commercial Space", "3-Bedroom Commercial Building", "Land with Construction"],
    "Location": ["Chang Phueak", "Chang Phueak", "Suthep"],
    "Size": ["200 sqm", "224 sqm", "645 Sq.wah"],
    "Rent (THB/month)": [20000, 30000, 150000],
    "Features": [
        "3-storey building, suitable for various businesses",
        "Corner unit with advertising space, fully furnished, 5 air conditioners, suitable for hostel, cafe, salon",
        "Land with existing construction, suitable for commercial purposes"
    ],
    "Source": [
        "https://nestopa.com/th-en/property/chiang-mai-mueang-chiang-mai-chang-phueak/studio-commercial-for-rent-and-sale-in-mueang-chiang-mai-512786?utm_source=chatgpt.com",
        "https://nestopa.com/th-en/property/chiang-mai-mueang-chiang-mai-chang-phueak/3-bed-commercial-for-rent-and-sale-in-mueang-chiang-mai-515600?utm_source=chatgpt.com",
        "https://propertieschiangmai.com/commercial-properties-for-sale-and-rent-in-chiang-mai/?utm_source=chatgpt.com"
    ]
}

# Create DataFrame
df_properties = pd.DataFrame(commercial_properties)

# Save to CSV
csv_output_path = "D:\\works\\MG-DSA\\ChiangMai_Commercial_Rentals.csv"
df_properties.to_csv(csv_output_path, index=False)

csv_output_path
