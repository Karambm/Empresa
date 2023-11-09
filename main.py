import filewriters as fw
import loaders as l
import pandas as pd

l.fastf1.plotting.setup_mpl()


def allcardata(session, combinedcardata=[]):
    """
    # TODO: Beschrijving
    """
    for driver in session.drivers:
        lap = 1
        while lap <= session.total_laps:
            try:
                lstdriver, x = [], 1
                df = session.laps.pick_driver(
                    driver).pick_lap(int(lap)).get_car_data()
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


def alllapdata(session, lap=1, combinedlapdata=[]):
    """
    # TODO: Beschrijving
    """
    while lap <= session.total_laps:
        lapinfo = l.loadlap(session, lap)
        combinedlapdata.append(lapinfo)
        lap += 1
    return pd.concat(combinedlapdata)


def circuit_info(session):
    circuit_info = session.get_circuit_info()  # VRAAG: is dit een kaart?
    try:
        fw.writecsv('ci_cornerinfo', circuit_info.corners)
        fw.writecsv('ci_marshallights', circuit_info.marshal_lights)
        fw.writecsv('ci_marshalsectors', circuit_info.marshal_sectors)
    except TypeError as te:
        print(f'\x1b[31mTypeError: {te}\x1b[0m')


def main(session):
    # SESSION RESULTS
    fw.writecsv('session_results', session.results)
    pass


"""
CHECKLIST:
- DONE: Load a session with given parameters, which can call other actions.
- DONE: Race Schedule for a given season.
- DONE: Remaining Races given the latest season.
- DONE: Aquire lap data to which information as position and laptimes are given.
- BUSY: An aggregated list of car data per lap per driver.
- DONE: Acquire weather data of the given session.
"""

if __name__ == "__main__":
    year, location, sprinttype = 2023, 'Bahrain', 'R'

    print("\x1b[32m")
    session = l.loadsession(year, location, sprinttype)  # Requests the session
    print("\x1b[0m")

    # Writes available circuit information containing cornering; marshals.
    circuit_info(session)
    # Writes all available lap data of the requested session
    fw.writecsv("lapdata", alllapdata(session))
    # Writes all available car data of the requested session
    fw.writecsv("cardata", allcardata(session))
    # Writes the schedule of the given year
    fw.writecsv(f'schedule_{year}', l.loadschedule(year))
    # Writes the remaining sessions of the season
    fw.writecsv('remaining_sessions', l.loadremaining())
    fw.writecsv('weather_data', session.weather_data)  # Writes weather data
    # Writes track status which contains green; yellow flags; safety cars
    fw.writecsv('track_status', session.track_status)

    main(session)

# l.fastf1.Cache.clear_cache()
