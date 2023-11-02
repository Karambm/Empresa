import filewriters
import loaders

loaders.fastf1.plotting.setup_mpl()

def main():
    session = loaders.loadsession(2023, 'Monza', 'R')
    
    circuit_info = session.get_circuit_info() # is dit een kaart?


    # filewriters.writejson('sessioninfo', session.session_info)
    lap_data = session.laps.pick_driver('LEC').pick_fastest().get_car_data()
    drivers = session.drivers
    # driverlist = [int[driver] for driver in drivers]


    t, vCar = lap_data['Time'], lap_data['Speed']
    """
    filewriters.writecsv('t', car_data['Time'])
    filewriters.writecsv('vCar', car_data['Speed'])
    """
    filewriters.writecsv('lap_data', lap_data)

filewriters.writecsv('schedule', loaders.loadschedule(2023)) # Writes the schedule of the given year
filewriters.writecsv('remaining_sessions', loaders.loadremaining()) # Writes the remaining sessions of the season
main()

loaders.fastf1.Cache.clear_cache()