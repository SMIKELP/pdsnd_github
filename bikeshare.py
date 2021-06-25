import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('Choose a city (Chicago, New York City, or Washington): ')
        city = city.lower()
        if city not in ('chicago', 'new york city', 'washington'):
            print('Please choose a city from the options above.')
            continue
        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('Choose the month you\'d like to filter by between January and June. Or type all if you wouldn\'t like to filter. Month: ')
        month = month.lower()
        if month not in ('january', 'february', 'march', 'april', 'may', 'june', 'all'):
            print('Please choose a month between January and June or type all.')
            continue
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Choose the day of the week you\'d like to filter by or type all if you wouldn\'t like to filter. Day: ')
        day = day.lower()
        if day not in ('sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all'):
            print('Please choose a day of the week or type all.')
            continue
        else:
            break

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day of week'] = df['Start Time'].dt.weekday_name

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

    df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day of week'] == day.title()]




#def trip_data(df):
    view_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no? ")
    view_data = view_data.lower()
    start_loc = 0
    end_loc = start_loc+5
    while True:
        if view_data not in ('yes'):
            return df
        print(df.iloc[start_loc:end_loc])
        start_loc += 5
        end_loc +=5
        view_data = input("Would you like to see 5 more rows?: ")
        view_data = view_data.lower()
        while True:
            if view_data not in ('yes'):
                return df
            print(df.iloc[start_loc:end_loc])
            break

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print('Most Common Month To Travel: ', common_month)

    # TO DO: display the most common day of week
    common_day = df['day of week'].mode()[0]
    print('Most Common Day Of The Week To Travel: ', common_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('Most Common Hour Of The Day To Travel (in military time): ', common_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('Most Commonly Used Start Station: ', common_start_station)

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('Most Commonly Used End Station: ', common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    common_start_end = df.groupby(['Start Station','End Station']).count().idxmax()[0]
    print('Most Frequent Combination Of Start End End Stations: ', common_start_end)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time_seconds = sum(df['Trip Duration'])
    #total_travel_time_formatted = time.strftime("%d:%H:%M:%S",time.gmtime(total_travel_time_seconds))
    print('Total Travel Time (in seconds): ', total_travel_time_seconds)
    #print('Total Travel Time (formatted): ', total_travel_time_formatted)

    total_travel_time_hours = sum(df['Trip Duration'])/3600
    print('Total Travel Time (in hours): ', total_travel_time_hours)

    total_travel_time_days = sum(df['Trip Duration'])/86400
    print('Total Travel Time (in days): ', total_travel_time_days,'\n')

    # TO DO: display mean travel time

    mean_travel_time_seconds = df['Trip Duration'].mean()
    mean_travel_time_formatted = time.strftime("%H:%M:%S",time.gmtime(mean_travel_time_seconds))
    #decided to format the travel time to make it easier for users to read
    print('Average Travel Time (in seconds): ', mean_travel_time_seconds)
    print('Average Travel Time (formatted): ', mean_travel_time_formatted)

    mean_travel_time_hours = (df['Trip Duration'].mean())/3600
    print('Average Travel Time (in hours): ', mean_travel_time_hours)

    mean_travel_time_days = (df['Trip Duration'].mean())/86400
    print('Average Travel Time (in days): ', mean_travel_time_days)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('User Types: ', user_types)

    # TO DO: Display counts of gender
    try:
        genders = df['Gender'].value_counts()
        print('Genders: ', genders)
    except KeyError:
        print('No data available for gender.')

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_birth_year = df['Birth Year'].min()
        print('Earliest Birth year: ', earliest_birth_year)
        recent_birth_year = df['Birth Year'].max()
        print('Most Recent Birth Year: ', recent_birth_year)
        common_birth_year = df['Birth Year'].mode()[0]
        print('Most Common Birth Year: ', common_birth_year)
    except KeyError:
        print('No data available for birth year.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
