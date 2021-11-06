# Almanak.ai Python Tools

## 1. Data Grabber SDK

A simple wrapper for to get LTS data from https://cds.climate.copernicus.eu/

### Local setup

1. install `pipenv` (see https://github.com/pypa/pipenv)
1. `pipenv install`
1. create `.cdsapirc` file and add the following:
```
url: https://cds.climate.copernicus.eu/api/v2
key: <insert your api key here>
```

### Usage