# Train Departure Web Scraper
This repository is for getting live departure information for UK train stations and exporting it to a json file. Live data is scrapped from the [National Rail live departures pages](https://realtime.nationalrail.co.uk/ldbcis/departures.aspx?u=039B1CD1-14D4-4CB9-83B1-A84CC3AEDF83&crs=NCL&H=1080). 

## How to use
To export departure information, run `main.py`. The outputted departures are stored in `exported_times.json`. 

The station can be change by changing the `station` variable to be the station code of the desired station. Station codes can be found at: https://www.nationalrail.co.uk/stations_destinations/48541.aspx

### JSON values
The outputted json file has the following name/value pairs: 

- `destination` - Destination of the train service. 
- `platform` - The platform that the service will leave the selected station from. If the service is cancelled this will be empty. 
- `departs` - Time the service is scheduled to depart the selected station. 
- `expected` - When the service is expected to arrive at the selected station. 
- `header` - Header text for the list of calling points. 
- `calling_points` - List of stations the service stops at. If expected arrival times are available they will be separate items in the list. 

The following are use if the last report a service made is available. The last report contains information about where a service is currently located (e.g. between two stations or departing a station)

- `last_report_label` - Text label for the last report (usually "Last report:")
- `last_report_status` - Status of the train (e.g. Departing, Between)
- `last_report_station` - The station the report is linked to
- `last_report_time` - The time the report happened. 

The following are name/value pairs are used when there are unscheduled changes to a service. 

- `cancellation_reason` - The reason for a service being cancelled. 
- `late_reason` - The reason for a service being delayed. 
- `not_calling_list` - A string containing a list of stations that a service will no longer stop at. 
