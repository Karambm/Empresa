import fastf1
import fastf1.plotting

def loadsession(year, circuit, sessiontype):
    """
    Loads a given session defined by:
    - year (int): the year the race was held.
    - circuit (name: str | id: int): the circuit which was raced on in the given year.
    - sessiontype (str): which type of session it is (Qualifying, Race, etc.).

    Results:
    - session (DataFrame): which contains a variety of information regarding the requested session.
    """
    session = fastf1.get_session(year, circuit, sessiontype)
    session.load()
    return session

def loadremaining():
    """
    Loads the remaining sessions given the latest year that's available.

    Results:
    - remaining (DataFrame): which contains the remaining sessions within the latest season.
    """
    return fastf1.get_events_remaining()

def loadschedule(year):
    """
    Loads the schedule for a given year.
    - year (int): the year of which the schedule is loaded for.

    Results:
    - schedule (DataFrame): the schedule of the given year.
    """
    return fastf1.get_event_schedule(int(year))