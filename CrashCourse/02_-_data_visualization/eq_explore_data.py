import json

filename = 'data/eq_data_1_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)

# Hac un nuevo JSON formateado
readable_file = 'data/readable_eq_data.json'
with open(readable_file, 'w') as f:
    json.dump(all_eq_data, f, indent=4)

all_eq_dicts = all_eq_data['features']
print(len(all_eq_dicts))
print(all_eq_dicts)
