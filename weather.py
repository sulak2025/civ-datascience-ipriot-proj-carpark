import random

def get_current_temperature():
    # In practice, read from file or weather API
    return round(random.uniform(18.0, 35.0), 1)