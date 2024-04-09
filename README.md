## Explore US Bikeshare Data for the first 6 months of 2017
### Date created
April 10, 2024

### Description
This Python project using pandas library to learn about bike share use in Chicago, New York City, and Washington by computing a variety of descriptive statistics

### Installations
- Python: Download and install Python 3.6 or above in https://www.python.org/downloads/
    - Note: Check python version by using this command in terminal:
    ```
    $ python --version
    ```

- Anaconda: Download and install Anaconda in https://docs.anaconda.com/free/anaconda/install/
    - Note: Check python version by using this command in terminal:
    ```
    $ conda --version
    ```

### Usage
Run this command `$ python bikeshare.py` in the terminal

## The Datasets
Randomly selected data for the first six months of 2017 are provided for all three cities. All three of the data files contain the same core six (6) columns:

- Start Time (e.g., 2017-01-01 00:07:57)
- End Time (e.g., 2017-01-01 00:20:53)
- Trip Duration (in seconds - e.g., 776)
- Start Station (e.g., Broadway & Barry Ave)
- End Station (e.g., Sedgwick St & North Ave)
- User Type (Subscriber or Customer)

> Note: The Chicago and New York City files also have the following two columns Gender & Birth Year

## Statistics Computed
### Popular times of travel (i.e., occurs most often in the start time)
- Most common month
- Most common day of week
- Most common hour of day

### Popular stations and trip
- Most common start station
- Most common end station
- Most common trip from start to end (i.e., most frequent combination of start station and end station)

### Trip duration
- Total travel time
- Average travel time

### User info
- Counts of each user type
- Counts of each gender (only available for NYC and Chicago)
- Earliest, most recent, most common year of birth (only available for NYC and Chicago)

## The files 
We use data of three large cities: Chicago, New York City, and Washington, DC, provided by [Motivate](https://motivateco.com/), a bike share system provider for many major cities in the United States, to uncover bike share usage patterns.
- chicago_csv
- new_york_city.csv
- washington.csv
- bikeshare.py - Python script file helps computing a variety of descriptive statistics


## Credits
This project is released under the MIT license. [See LICENSE](https://github.com/dongan2212/pdsnd_github/blob/master/LICENSE) for details.
