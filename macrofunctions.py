import pandas as pd
import loaders as l
from time import perf_counter

def cacheall(year):
    schedule = l.loadschedule(year)
    for name in schedule.OfficialEventName:
        print("\x1b[32m")
        l.loadsession(year, name, 'R')
        print("\x1b[0m")


def allcardata(year, session, combinedcardata=[]):
    """
    # TODO: Beschrijving
    """
    try:
        for driver in session.drivers:
            lap = 1
            while lap <= session.total_laps:
                try:
                    lstdriver, lstyear, x = [], [], 1
                    df = session.laps.pick_driver(driver).pick_lap(int(lap)).get_car_data()
                    while x <= df.Brake.size:
                        lstdriver.append(driver)
                        lstyear.append(year)
                        x += 1
                    df["driverID"] = lstdriver
                    df['year'] = lstyear
                    combinedcardata.append(df)
                except KeyError as ke:
                    print(f"\x1b[31m{ke}\x1b[0m")
                except ValueError as ve:
                    print(f"\x1b[31m{ve}\x1b[0m")
                lap += 1
    except AttributeError as ae:
        print(f"\x1b[31m{ae}\x1b[0m")
    return pd.concat(combinedcardata)


def alllapdata(year, session, lap=1, combinedlapdata=[]):
    """
    # TODO: Beschrijving
    """
    try:
        while lap <= session.total_laps:
            lapinfo = l.loadlap(session, lap)
            combinedlapdata.append(lapinfo)
            lap += 1
        return pd.concat(combinedlapdata)
    except AttributeError as ae:
        print(f"\x1b[31m{ae}\x1b[0m")

    
def seasoncardata(year, sessiontype, eventiter=0):
    schedule = l.loadschedule(year)
    for event in schedule.OfficialEventName:
        print(f'\n\n{eventiter}')
        try:
            pd.read_csv(f'cardata_{year}.csv')
            print(f'cardata_{year}.csv exists')
            break
        except FileNotFoundError as fnfe:
            starttijd = perf_counter()
            print(f'\x1b[32mGetting Car Telemetry Data... {event}')
            cardata = allcardata(year, l.loadsession(year, event, sessiontype))
            # TODO VRAAG: Data voegt zichzelf toe zonder append?
            print(f"Tijd: \x1b[31m{(perf_counter() - starttijd) * 1000:.0f}ms")
            eventiter += 1
            print(f'\x1b[0m{cardata}')
            pass
        except AttributeError as ae:
            print(f"\x1b[31m{ae}\x1b[0m")
        except FileExistsError as fee:
            print(f"\x1b[31m{fee}\x1b[0m")
    print(f"Season {year} Car Data written!")
    return cardata

def seasonlapdata(year, sessiontype, eventiter=0):
    schedule = l.loadschedule(year)
    for event in schedule.OfficialEventName:
        print(f'\n\n{eventiter}')
        try:
            pd.read_csv(f'lapdata_{year}.csv')
            print(f'lapdata_{year}.csv exists')
            break
        except FileNotFoundError as fnfe:
            starttijd = perf_counter()
            print(f'\x1b[32mGetting Car Telemetry Data... {event}')
            lapdata = alllapdata(year, l.loadsession(year, event, sessiontype))
            print(f"Tijd: \x1b[31m{(perf_counter() - starttijd) * 1000:.0f}ms")
            eventiter += 1
            print(f'\x1b[0m{lapdata}')
            pass
        except AttributeError as ae:
            print(f"\x1b[31m{ae}\x1b[0m")
        except FileExistsError as fee:
            print(f"\x1b[31m{fee}\x1b[0m")
    print(f"Season {year} Lap Data written!")
    return lapdata