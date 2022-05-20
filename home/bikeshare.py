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
    # TO DO: get user input for city chicago,new york city,washington. HINT: Use a while loop to handle invalid input
    while True :
       city=input("Enter city name from chicago,washington,new yor city").lower()
       if city in CITY_DATA:
           break
       else:     
         print("invalid city")
       # TO DO: get user input for month (all, january, february, ... , june)
    while True:
       months=['all','january','february','march','april','may','june']
       month= input('Enter the month').lower()
       if month in months:
          break
       else:
          print("invaild month")
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
       days=['all','monday','tuesday','wedensday','thursday','friday','saturday','sunday']
       day= input('enter the day').lower()
       if day in days:
          break
       else: 
        print("invalid day")   
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
    df['start time']=pd.to_datetime(df['Start Time'])
    df['month']=df['Start Time'].dt.month
    df['day']=df['Start Time'].dt.weekday.name
    df['start hour']=df['Start Time'].dt.hour
    if month != 'all':
       df=df[df['month']==month].lower()    
    if day!= 'all':
       df =df[df['day']==day.lower()]
    return df
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # TO DO: display the most common month
    common_month=df['month'].mode(0)
    print("the most common month is:",common_month)
    # TO DO: display the most common day of week
    common_day=df['day'].mode(0)
    print("the most common day is :",common_day)
    # TO DO: display the most common start hour
    common_hour=df[' start hour'].mode(0)
    print("the most common hour is:",common_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    # TO DO: display most commonly used start station
    common_start=df['Start Station'].mode(0)
    print("the most common start station is :",common_start)
    # TO DO: display most commonly used end station
    common_end=df['End Station'].mode(0)
    print(" the most common end station is :",common_end)
    # TO DO: display most frequent combination of start station and end station trip
    common_trip=df['Start Station']+","+df['End Station']
    print("the most common road trip is :",common_trip)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    # TO DO: display total travel time
    total_time=df['Trip Duration'].sum()
    print("the total travel time is :",total_time)
    # TO DO: display mean travel time
    avg_time=df['Trip Duration'].mean()
    print(" the total time is :",avg_time)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def user_stats(df):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    # TO DO: Display counts of user types
    user_types=df['User Types'].value_counts()
    print("user types are",user_types)
    # TO DO: Display counts of gender
    if 'Gender' in df:
        gender=df['Gender'].value_counts()
        print("gender is :",gender)
        # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earlist_year=df['Birth Year'].min()
        print("the earlist year of birth is :",earlist_year)
        latest_year=df['Birth Year'].max()
        print(" the latest year of birth is :",latest_yaer)
        common_year=df['Birth Year'].mode(0)
        print("the most common year of birth is :",common_year)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def Display_data (df):
     while True:
        i=0
        out=input("would you like to see the first 5 rows? choose either yes or no").lower
        if out=="no":
           break
           print(df[i:i+5])
        out=input("would you like to display the next 5 rows? choose either yes or no").lower
        i+=5
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
            break
    if __name__ == "__main__":
	    main()
