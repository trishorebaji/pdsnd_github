import time
import pandas as pd

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
        city=input()
        if city not in ('chicago','new york city','washington'):
            continue
        else:
            break
    
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month=input()
        if month not in ('all','january','february','march','april','may','june'):
            continue
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day=input()
        if day not in ('all','monday','tuesday','wednesday','thursday','friday','saturday','sunday'):
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
    df=pd.read_csv(CITY_DATA[city])
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['month']=df['Start Time'].dt.month
    df['day_name']=df['Start Time'].dt.weekday_name
    
    if month!='all':
        months=['january','february','march','april','may','june']
        month=months.index(month)+1
        df=df[df['month']==month]
        
    if day!='all':
        df=df[df['day_name']==day.title()]
        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_commen_month=df['month'].mode()[0]
    print('most common month ',most_commen_month)
    # TO DO: display the most common day of week
    most_common_day=df['day_name'].mode()[0]
    print('most common day of week ',most_common_day)

    # TO DO: display the most common start hour
    df['hour']=df['Start Time'].dt.hour
    most_start_hour=df['hour'].mode()[0]
    print('most common start hour ',most_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station=df['Start Station'].value_counts().idxmax()
    print('most commonly used start station',start_station)

    # TO DO: display most commonly used end station
    end_station=df['End Station'].value_counts().idxmax()
    print('most commonly used end station',end_station)

    # TO DO: display most frequent combination of start station and end station trip
    
    print('most frequent combination of start station and end station trip',start_station,'and',end_station)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    tot_travel_time=df['Trip Duration'].sum()
    print('total travel time',tot_travel_time)

    # TO DO: display mean travel time
    tot_mean_time=df['Trip Duration'].mean()
    print('mean travel time',tot_mean_time)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types_count=df['User Type'].value_counts()
    print('counts of user types',user_types_count)


    # TO DO: Display counts of gender
    try:
        gender_counts=df['Gender'].value_counts()
        print('counts of gender',gender_counts)
    except KeyError:
        print('there is no such column gender')

    # TO DO: Display earliest, most recent, and most common year of birth
    
    try: 
        earliest_year=df['Birth Year'].min()
        print('earliest Birth year',earliest_year)
    except KeyError:
        print('there is no birth Year')
    
    try:
        most_recent_year=df['Birth Year'].max()
        print('most recent Birth year',most_recent_year)
    except KeyError:
        print('there is no Birth Year')
    
    try:
        most_common_birth_year=df['Birth Year'].value_counts().idxmax()
        print('most commen Birth year',most_common_birth_year)
    except:
        print('There is no Birth Year')
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
def display_data(df):
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
    start_loc = 0
    while (True):
        print(df.iloc[start_loc:start_loc+5])
        start_loc += 5
        view_data = input("Do you wish to continue?: ").lower()
        if view_data!='yes':
            print("view_data")
            break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            print(restart.lower())
            break
        


if __name__ == "__main__":
	main()
