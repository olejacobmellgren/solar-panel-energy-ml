# Peter Notes Data

Some simple preliminary intuitons about the dataset

## `date_forecast`

The `date_forecast` value in itself does not give us a lot of information as it is since it is only a linear value (Increasing time and date). While the real world time moves in seasons and in our case we are interested in the two periods throughout the day and also throughout the year. Leaving us with two values: 

```python
# time is an example value.
# Here I assume time is an integer with hours since some date in the past

import math

# changes time value to a periodical day value
def get_day_val(time):
    return math.sin(time/24)

# changes time value to a periodical year value
def get_year_val(time):
    return math.sin(time/8760.25)
```

*Might also be interesting to look at the linear component if time due to environmental changes. Maybe as an opposite exponential function where the later changes becomes less and less relevant?*

## Snow: `snow_density`, `snow_depth`, `snow_drift`, `snow_melt_10min` and `snow_water`

These attributes are interesting when there is snow, however when there is no snow, the rate at which it melts does not matter in terms of solar production (since ther is no snow). 

Thus a state where `snow_melt_10min` = `0` can be very bad when there is snow, and totally irrelevant when there is none. 

> Thoughts: 
> - Maybe a stacking of models where one tries to figure out the relevance of this column? 
> - Maybe possible to ignore these values if `snow_depth` = `0`

## Boolean values: 
- `is_day` -> 0/1
- `is_in_shadow` -> 0/1

## Other int values:
- `dew_or_rime` -> (dew=1, rime=-1, neither=0)
- `elevation` -> The elevation of the solar_panel above ground. 
