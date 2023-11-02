from matplotlib import pyplot as plt
import fastf1
import fastf1.plotting
import filewriters

def loadsession(year, circuit, sessiontype):
    """
    Loads a given session defined by:
    - year (int): the year the race was held.
    - circuit (name: str | id: int): the circuit which was raced on in the given year
    - sessiontype (str): which type of session it is (Qualifying, Race, etc.)
    """
    fastf1.plotting.setup_mpl()
    session = fastf1.get_session(year, circuit, sessiontype)
    session.load()
    return session

def loadremaining():
    """
    Loads the remaining sessions given the latest year that's available
    """
    filewriters.writecsv('remaining_sessions', fastf1.get_events_remaining())

def main():
    session = loadsession(2023, 'Monza', 'R')
    circuit_info = session.get_circuit_info()
    # filewriters.writejson('sessioninfo', session.session_info)
    car_data = session.laps.pick_driver('VER').pick_fastest().get_car_data()
    
    t, vCar = car_data['Time'], car_data['Speed']

    filewriters.writecsv('lap_data', car_data)

    loadremaining()

main()