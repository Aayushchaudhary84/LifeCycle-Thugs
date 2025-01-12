# API Information

Currently, the EarthquakeApi class has 3 methods:
1. `getAllData()` fetches all data between 2 specified dates and saves the data as monthly json files (for each month of a search parameter, it will generate an individual json file). Breaking up the data by months is to avoid the API request limit (a user can only receive 20,000 data points in a single request, that is why we cannot simply get all of the data at once). The problem with this method is that the size of the all of the data will be around 40gb. So, **we shouldn't use this method, since it consumes a lot of storage space.**
1. `getParsedData()` will fetch monthly data to avoid the request limit, but filters the more important data to save storage space. Currently, we get time, location, magnitude, title, and a URL, but we can easily get different data if needed. It will output to a single json file.
1. `getParsedDataTXT()` works similar to `getParsedData()` except that it will generate a text file instead, saving much storage space.
1. `getLast24Hours()` gets the results from the last 24 hours. My intent is that it will be used every 10 minutes (or whatever interval we decide upon) and then place the new results in the database.
