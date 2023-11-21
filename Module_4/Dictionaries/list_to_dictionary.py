# List to Dictionary
# Write a function that takes a list of dictionaries and 
# aggregates values for each key into a single dictionary

def aggregate_dicts(data_list):
    aggregated_data = {}
    for data in data_list:
        for key, value in data.items():
            if key in aggregated_data:
                aggregated_data[key].append(value)
            else:
                aggregated_data[key] = [value]
    return aggregated_data