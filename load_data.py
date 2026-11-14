import pandas as pd
from pathlib import Path

url = "https://data.cityofchicago.org/api/v3/views/4ijn-s7e5/export.csv?accessType=DOWNLOAD"

data_path = Path("data/food_inspections.csv")
data_path.parent.mkdir(parents=True, exist_ok=True)

if data_path.exists():
    print("Loading local dataset...")
    df = pd.read_csv(data_path, low_memory=False)
else:
    print("Downloading dataset...")
    df = pd.read_csv(url, low_memory=False)
    df.to_csv(data_path, index=False)

print(df.shape)