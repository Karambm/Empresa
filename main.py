import filewriters as fw
import loaders as l

l.fastf1.plotting.setup_mpl()

"""
CHECKLIST:
- DONE: Load a session with given parameters, which can call other actions.
- DONE: Race Schedule for a given season.
- DONE: Remaining Races given the latest season.
- BUSY: Aquire lap data to which information as position and laptimes are given.
- BUSY: An aggregated list of car data per lap per driver.
"""

def main():
    # LAP INFORMATION
    lap = 1
    while lap < session.total_laps:
        print(l.loadlap(session, lap))
        lap += 1

    # CAR TELEMETRY DATA
    car_individual = l.loadcardata(session, 1, 4)
    fw.writecsv('car_data', l.loadallcardata(session)) # KRIJGT ValueError
    
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

year, location, sprinttype = 2022, 'Francorchamps', 'R'

# CHECKLIST MIRROR
session = l.loadsession(year, location, sprinttype)
fw.writecsv(f'schedule_{year}', l.loadschedule(year)) # Writes the schedule of the given year
fw.writecsv('remaining_sessions', l.loadremaining()) # Writes the remaining sessions of the season
fw.writecsv('weather_data', session.weather_data)
fw.writecsv('track_status', session.track_status)

main()

l.fastf1.Cache.clear_cache()