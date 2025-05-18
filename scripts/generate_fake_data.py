from faker import Faker
import pandas as pd
import os

#Initialize Faker
fake = Faker()

#Generate Fake Data
data=[]
for _ in range(100):
    data.append({
        "id": fake.uuid4(),
        "name": fake.name(),
        "email": fake.email(),
        "address": fake.address(),
        "created_at": fake.date_time_this_year().isoformat()
    })


#Convert to DataFrame
df= pd.DataFrame(data)

#save to CSV
output_path = os.path.join("..", "data", "fake_users.csv") #navigate to /data
df.to_csv(output_path, index=False)

print(f"Data Saved {output_path}")