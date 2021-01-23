'''
Richard Farr
January 2021

Goal: Predict the end of the Coronavirus pandemic for each country
'''

# imports
import datetime




# What I know
################################
today = date.today()

usa_population = 331000000
usa_infected = 25410000 # https://www.worldometers.info/coronavirus/

usa_vaccinations = 19107000 # https://www.nytimes.com/interactive/2020/us/covid-19-vaccine-doses.html
usa_vaccinated = usa_vaccinations / 2


# What I am estimating
#####################################


usa_infections_daily = 192000 # yesterdays infections
usa_vaccinations_daily = 975540 # yesterdays shots https://www.nytimes.com/interactive/2020/us/covid-19-vaccine-doses.html

usa_infections_vaccinations_needed = 0.90
vaccine_effectiveness = 0.90

immunity_time_from_infection = 180 # time in days
immunity_time_from_vaccination = 180 # time in days




# Projections
############################

# Calculate when the pandemic will be over
print(" ") # print a blank line

# 1. People that need to be infected or vaccinated for the pandemic to be over
usa_population_needed = usa_infections_vaccinations_needed * usa_population

# 2. How many people left to get?
usa_people_left = round(usa_population_needed - usa_infected - (vaccine_effectiveness * usa_vaccinated))
plc = "{:,}".format(usa_people_left)
print(f"{plc} people will need to be vaccinated or infected before the pandemic is over")

# 3. How many people are getting vaccinated or infected per day
infected_or_vaccinated_per_day = usa_infections_daily + usa_vaccinations_daily

# 4. Estimate how many days it will take at this rate
days_until_pandemic_over = usa_people_left / infected_or_vaccinated_per_day

# 5. Add the projected number of days to todays date to get the 
date_pandemic_over = today + datetime.timedelta(days=days_until_pandemic_over)
print(f"The Date that the Pandemic is expected to be over is: {date_pandemic_over}")


# Calculate how many people infected, vaccinated, & untouched

# 1. How many infected?

usa_infected_proj = round(usa_infected + days_until_pandemic_over * usa_infections_daily)
usaip = "{:,}".format(usa_infected_proj)
print(f"We project {usaip} total infections in the USA by {date_pandemic_over}")

usa_infections_to_go = round(usa_infected_proj - usa_infected)
print(f"Thats {usa_infected_proj} more people infected by {date_pandemic_over}")




# Output
################

print(f"The Date that the Pandemic is expected to be over is: {date_pandemic_over}")

'''
name = 'Tushar'
age = 23
print(f"Hello, My name is {name} and I'm {age} years old.")
'''
