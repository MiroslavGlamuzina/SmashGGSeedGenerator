from scrape import get_seed_data
from scrape import mutate_phase_seeding
from scrape import get_entrant_data
from scrape import get_user_winrate
import sys

tournamentName = ''

# Check for tournament name
try:
    tournamentName = "tournament/" + sys.argv[1]
    print('Tournament: "'+tournamentName+'"')
except:
    print('Tournament name not set.')
    print('Usage: main.py my-tournament-name-here')
    exit()

# Gather data for tournament
raw_data = get_entrant_data(tournamentName)
event_data = raw_data['data']['tournament']['events'][0]
entrant_data = event_data['entrants']['nodes']
seed_data_master = get_seed_data(tournamentName)
seed_data = seed_data_master['seed_data']
phase_id = seed_data_master['phase_id']

# Add winrate data
for curr_user in entrant_data:
    try:
        user_id = curr_user['participants'][0]['user']['id']
        curr_user['winrate'] = get_user_winrate(user_id)
    except:
        curr_user['winrate'] = -1

entrant_data.sort(key=lambda x: x['winrate'], reverse=True)  # sort

# Generate new seed data + print data
print('')
new_seed_mapping = []
for idx, entrant in enumerate(entrant_data):
    seed_num = idx + 1;
    new_seed_mapping.append({"seedId": seed_data[entrant['participants'][0]['id']]['seedId'], "seedNum": idx+1})
    print('{0: <5}{1: <25}{2: <25}'.format(str(seed_num), entrant['name'], entrant['winrate']))

mutate_phase_seeding(phase_id, new_seed_mapping)

print('All Done!')

