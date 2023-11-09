import filewriters as fw
import loaders as l
import pandas as pd

l.fastf1.plotting.setup_mpl()

def lapinformation(session, lap=1, combinedlapdata=[]):
    # LAP INFORMATION
    while lap <= session.total_laps:
        lapinfo = l.loadlap(session, lap)
        combinedlapdata.append(lapinfo)
        lap += 1
    return pd.concat(combinedlapdata)

def cardata(session, combinedcardata=[]):
    for driver in session.drivers:
        lap = 1
        while lap <= session.total_laps:
            try:
                lstdriver, x = [], 1
                df = session.laps.pick_driver(driver).pick_lap(int(lap)).get_car_data()
                while x <= df.Brake.size:
                    lstdriver.append(driver)
                    x += 1
                df["driverID"] = lstdriver
                combinedcardata.append(df)
                # print(session.laps.pick_driver(str(driver)).pick_lap(int(lap)).get_car_data())
            except KeyError as ke:
                print(f"\x1b[31mKeyError: {ke}\x1b[0m")
            except ValueError as ve:
                print(f"\x1b[31mValueError: {ve}\x1b[0m")
            lap += 1
    return pd.concat(combinedcardata)

def main():
    # SESSION RESULTS
    fw.writecsv('session_results', session.results)

    # CIRCUIT INFO
    circuit_info = session.get_circuit_info() # VRAAG: is dit een kaart?
    try:
        fw.writecsv('ci_cornerinfo', circuit_info.corners)
        fw.writecsv('ci_marshallights', circuit_info.marshal_lights)
        fw.writecsv('ci_marshalsectors', circuit_info.marshal_sectors)
    except TypeError as te:
        print(f'\x1b[31mTypeError: {te}\x1b[0m')
    pass

"""
CHECKLIST:
- DONE: Load a session with given parameters, which can call other actions.
- DONE: Race Schedule for a given season.
- DONE: Remaining Races given the latest season.
- BUSY: Aquire lap data to which information as position and laptimes are given.
- BUSY: An aggregated list of car data per lap per driver.
"""

year, location, sprinttype = 2023, 'Monza', 'R'

# CHECKLIST MIRROR
session = l.loadsession(year, location, sprinttype)

fw.writecsv("lapinfo", lapinformation(session))
fw.writecsv("cardata", cardata(session))
fw.writecsv(f'schedule_{year}', l.loadschedule(year)) # Writes the schedule of the given year
fw.writecsv('remaining_sessions', l.loadremaining()) # Writes the remaining sessions of the season
fw.writecsv('weather_data', session.weather_data) # Writes weather data
fw.writecsv('track_status', session.track_status) # Writes track status which contains green; yellow flags; safety cars

main()

# l.fastf1.Cache.clear_cache()