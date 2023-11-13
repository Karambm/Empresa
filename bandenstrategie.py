import fastf1
import fastf1.plotting
from matplotlib import pyplot as plt

session = fastf1.get_session(2023, "Bahrain", 'R')
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

# Verbindingsreeks naar je Azure Storage-account
connection_string = "DefaultEndpointsProtocol=https;AccountName=speedwaydynamics;AccountKey=RFnPL7pNNGg0byh+bC6zKT++NuvqtPM4VURdmhW1GCVYAvkxIwLN4Z7+uaGwZT02rECSZvl0J08O+AStFgG/ig==;EndpointSuffix=core.windows.net"

# Maak een BlobServiceClient
blob_service_client = BlobServiceClient.from_connection_string(connection_string)

# Maak een ContainerClient (dit is vergelijkbaar met een map in Blob Storage)
container_name = "yourcontainer"
container_client = blob_service_client.get_container_client(container_name)

# Definieer de naam van het bestand dat je wilt uploaden
file_name = "example_data.csv"

# Definieer de gegevens die je wilt uploaden
data_to_upload = b"Your data content here."

# Maak een BlobClient voor het bestand
blob_client = container_client.get_blob_client(file_name)


# Upload de gegevens naar Blob Storage
blob_client.upload_blob(data_to_upload, overwrite=True)


session = fastf1.get_session(2022, "Hungary", 'R')
session.load()
laps = session.laps

drivers = session.drivers
print(drivers)

drivers = [session.get_driver(driver)["Abbreviation"] for driver in drivers]
print(drivers)

stints = laps[["Driver", "Stint", "Compound", "LapNumber"]]
stints = stints.groupby(["Driver", "Stint", "Compound"])
stints = stints.count().reset_index()


stints = stints.rename(columns={"LapNumber": "StintLength"})
print(stints)

fig, ax = plt.subplots(figsize=(5, 10))

for driver in drivers:
    driver_stints = stints.loc[stints["Driver"] == driver]

    previous_stint_end = 0
    for idx, row in driver_stints.iterrows():
        plt.barh(
            y=driver,
            width=row["StintLength"],
            left=previous_stint_end,
            color=fastf1.plotting.COMPOUND_COLORS[row["Compound"]],
            edgecolor="black",
            fill=True
        )

        previous_stint_end += row["StintLength"]


plt.title("2022 Hungarian Grand Prix Strategies")
plt.xlabel("Lap Number")
plt.grid(False)
ax.invert_yaxis()

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)

plt.tight_layout()
plt.show()

