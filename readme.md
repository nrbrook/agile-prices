# Octopus Agile price fetcher

These python scripts fetch and store the Octopus Agile prices. `store_prices.py` is designed to be run as a cron job, and `get_prices_from_db.py` is designed to be imported by other scripts to fetch the upcoming prices.

First, install the requirements:

```
pip install -r requirements.txt
```

## Cron scheduling

`store_prices.py` can be scheduled to fetch the latest prices in crontab (run `crontab -e`):

```
05 * * * * cd /path/to/this/dir; /usr/bin/python3 store_prices.py -r <region> -t <agile_tariff> > /path/to/your/log.log
```

You should replace  and  with your local paths, and `<region>` and `<agile_tariff>` as follows:

- Go to the octopus developer page and scroll to "Unit rates"
- There you will see a URL, for example "https://api.octopus.energy/v1/products/AGILE-FLEX-22-11-25/electricity-tariffs/E-1R-AGILE-FLEX-22-11-25-M/standard-unit-rates/"
- Look at this part: "E-1R-AGILE-FLEX-22-11-25-M". This is in the format E-1R-AGILE-<tariff>-<region>. The tariff is the part following "AGILE-", e.g. "FLEX-22-11-25". The region is the letter at the end, e.g. "M".

## Obtaining prices

Upcoming prices can be fetched from another python script as follows:
```
import get_prices_from_db

get_prices_from_db(path_to_db, max_num_entries)
```

## Credits

Modified from [octopus-agile-pi-prices](https://github.com/pufferfish-tech/octopus-agile-pi-prices)