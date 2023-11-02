from matplotlib import pyplot as plt
import fastf1
import fastf1.plotting
import json

def writecsv(name, data):
    data.to_csv(f"{name}.csv", index=False)

def writejson(name, data):
    with open(f"{name}.json", "w") as json_file:
        json.dump(list(data), json_file, indent=4)  # De 'indent' parameter zorgt voor nette opmaak

def loadsession():
    fastf1.plotting.setup_mpl()
    session = fastf1.get_session(2023, 'Monza', 'R')
    session.load()
    lec_car_data = session.laps.pick_driver('LEC').pick_fastest().get_car_data()
    
    remaining = fastf1.get_events_remaining()
    print(remaining)
    
    t, vCar = lec_car_data['Time'], lec_car_data['Speed']

    writecsv('remaining_sessions', remaining), writecsv('lap_data', lec_car_data)


"""
# The rest is just plotting
fig, ax = plt.subplots()
ax.plot(t, vCar, label='Fast')
ax.set_xlabel('Time')
ax.set_ylabel('Speed [Km/h]')
ax.set_title('Leclerc is')
ax.legend()
plt.show()
"""    


loadsession()