import cdsapi

c = cdsapi.Client()

def lds_level_1_request(year, month, days, area, filename):
    return c.retrieve(
    'reanalysis-era5-land',
    {
        'variable': 'soil_temperature_level_1',
        'year': year,
        'month': month,
        'day': days,
        'time': [
            '00:00', '01:00', '02:00',
            '03:00', '04:00', '05:00',
            '06:00', '07:00', '08:00',
            '09:00', '10:00', '11:00',
            '12:00', '13:00', '14:00',
            '15:00', '16:00', '17:00',
            '18:00', '19:00', '20:00',
            '21:00', '22:00', '23:00',
        ],
        'area': area,
        'format': 'grib',
    },
    filename
    )

# Solheimar specific function
def get_solheimar( year, month, days ):
  area = [ 64.07, -20.65, 64.06, -20.64 ]
  filename = f'{year}-{month}.grib'
  return lds_level_1_request(year, month, days, area, filename)