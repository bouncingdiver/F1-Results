import fastf1
fastf1.Cache.enable_cache('C:/Programming/ProjectBoredom/F1/Cache')
need_name = False

round_number = input ('Round number (type NAME if you would rather input the name):\n')
if round_number == 'NAME':
    need_name = True
    round_name = input ("What is its' name (this can be a particular name, name of region or name of host country)?\n")


year = input('From which season?\n')
year = int(year)
schedule = fastf1.get_event_schedule(year)

if need_name == False:
    round_number = int(round_number)
    event = fastf1.get_event(year, round_number)
    event_name = event.EventName
else:
    event = fastf1.get_event(year, round_name)
    event_name = event.EventName
    requested_gp = schedule.get_event_by_name(event_name)
    round_number = int(requested_gp.RoundNumber)

interest = ('unchanged')
while interest != 'FINISH':
    interest = input('Please type:\nQUALI to load Qualifying results,\nRACE to load race results,\nPOLE to display the driver who got pole position,\nor WINNER to display the winner of this Grand Prix.\nAlternatively, type FINISH to finish.\n')
    print ('Please wait while the event data is loaded')
    session = fastf1.get_event(year, round_number)
    if interest == 'QUALI':
        quali = fastf1.get_session(year, round_number, 'Q')
        quali.load()
        print (quali.results)
        
    elif interest == 'RACE':
        race = fastf1.get_session(year, round_number, 'R')
        race.load()
        print (race.results)

    elif interest == 'POLE':
        pole = fastf1.get_session(year, round_number, 'Q')
        pole.load()
        print (pole.results.FullName[0], 'with a ', pole.results.Time[0])

    elif interest == 'WINNER':
        winner = fastf1.get_session(year, round_number, 'R')
        winner.load()
        print (winner.results.FullName[0], ' from ', winner.results.GridPosition[0], ' on the grid. ')
    
