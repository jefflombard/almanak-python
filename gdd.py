# Running Calculations



def calculate_gdd_addition(temp_min, temp_max, temp_base):
  if(temp_min < temp_base):
    return 0
  return ((temp_max-temp_min)/2)-temp_base

def calculate_gdd(time_series,temp_base):
  gdd = 0
  for time in time_series:
    gdd += calculate_gdd_addition(time.temp_min, time.temp_max, temp_base)
  return gdd
