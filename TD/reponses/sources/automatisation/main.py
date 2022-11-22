import harvester as hv
env = 'dev'

def get_all_parking(request):
    headers = {'Content-Type': 'application/json'}
    h = hv.Harvester(env=env)
    h.get_and_save_parking_lr()
    h.get_and_save_parking_nantes()
    h.get_and_save_parking_yelolr()
    return ({"msg": "Parking data successfully saved."}, 200, headers)
