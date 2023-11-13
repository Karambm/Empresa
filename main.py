import pandas as pd
import filewriters as fw
import loaders as l
import macrofunctions as mf
from time import perf_counter
import os

l.fastf1.plotting.setup_mpl()


def circuit_info(session):
    circuit_info = session.get_circuit_info()  # VRAAG: is dit een kaart?
    try:
        fw.writecsv('ci_cornerinfo', circuit_info.corners)
        fw.writecsv('ci_marshallights', circuit_info.marshal_lights)
        fw.writecsv('ci_marshalsectors', circuit_info.marshal_sectors)
    except TypeError as te:
        print(f'\x1b[31mTypeError: {te}\x1b[0m')


def writeallsingle(session, year):
    """
    Schrijft alles gedefinieerd naar csv.

    Result
    - CSV-bestanden van alles gedefinieerd, waaronder telemetries; etc.
    """
    fw.writecsv(f'schedule_{year}', l.loadschedule(year)) # Writes the schedule of the given year
    circuit_info(session) # Writes available circuit information containing cornering; marshals.
    fw.writecsv("lapdata", mf.alllapdata(session)) # Writes all available lap data of the requested session
    fw.writecsv("cardata", mf.allcardata(session)) # Writes all available car data of the requested session
    fw.writecsv('remaining_sessions', l.loadremaining()) # Writes the remaining sessions of the season
    fw.writecsv('weather_data', session.weather_data) # Writes weather data
    fw.writecsv('track_status', session.track_status) # Writes track status which contains green; yellow flags; safety cars

    # SESSION RESULTS
    fw.writecsv('session_results', session.results)


def writeallseason(year):
    """
    - Laps
    - Cars
    - Weather
    """
    # CARDATA
    try:
        fw.writecsv(f'cardata_{year}', mf.seasoncardata(year, sprinttype))
    except UnboundLocalError as ule:
        print(f"\x1b[31m{ule}\x1b[0m")
    pass

    # LAPDATA
    try:
        fw.writecsv(f'lapdata_{year}', mf.seasonlapdata(year, sprinttype))
    except UnboundLocalError as ule:
        print(f"\x1b[31m{ule}\x1b[0m")
    pass


"""
TODO's:
- DONE: Load a session with given parameters, which can call other actions.
- DONE: Race Schedule for a given season.
- DONE: Remaining Races given the latest season.
- DONE: Aquire lap data to which information as position and laptimes are given.
- DONE: An aggregated list of car data per lap per driver.
- DONE: Acquire weather data of the given session.
- TODO: Write all available data iteratively to csv.
- TODO: Match all columns with obtained datasets via ergast.
"""

if __name__ == "__main__":
    year, location, sprinttype = 2023, 'monza', 'R'

    # THE WHOLE SEASON
    gocache = 'n'
    if gocache == 'j':
        try:
            starttijd = perf_counter()
            mf.cacheall(year)
            print(f" Tijd: \x1b[31m{(perf_counter() - starttijd) * 1000:.0f}ms\x1b[32m)")
        except:
            pass
    writeallseason(year)
    
    # ONE SESSION
    print("\x1b[32m")
    session = l.loadsession(year, location, sprinttype)  # Requests the session
    print("\x1b[0m")

    # WRITE ONE SESSION
    writeallsingle(session, year)


# l.fastf1.Cache.clear_cache()