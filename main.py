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
usa_infected = 25410000 # People Infected So Far - https://www.worldometers.info/coronavirus/ 

usa_vaccinations = 19107000 # Vaccinations So Far - https://www.nytimes.com/interactive/2020/us/covid-19-vaccine-doses.html
usa_vaccinated = usa_vaccinations / 2 # People Vaccinated so far


# What I am estimating
#####################################

# daily infections
usa_infections_daily = 192000 # yesterdays infections

# daily vaccinated
usa_vaccinations_daily = 975540 # yesterdays shots https://www.nytimes.com/interactive/2020/us/covid-19-vaccine-doses.html
usa_vaccinated_daily = usa_vaccinations_daily / 2

vaccine_effectiveness = 0.90 # just a guess
usa_vaccine_immunity_daily = usa_vaccinated_daily * vaccine_effectiveness

usa_infections_vaccinations_needed = 0.90 # % of people needing to be infected or vaccinated for pandemic to be over



#### Not added to the model yet - to add to v2 of the model later
###################################################################

immunity_time_from_infection = 180 # time in days
immunity_time_from_vaccination = 180 # time in days




# Projections & Output
############################

# Goal 1: Calculate when the pandemic will be over
print(" ") # print a blank line
print("Goal 1: Calculate when the pandemic will be over")
print(" ")

# 1. Total # of people that have been infected or vaccinated so far?
usa_population_infected_immune = round(usa_infected + usa_vaccinated)
usii = "{:,}".format(usa_population_infected_immune)
print(f"{usii} people have either been infected or vaccinated so far")


# 2. Total # People that need to be infected or vaccinated for the pandemic to be over
usa_population_needed = round(usa_infections_vaccinations_needed * usa_population)
usn = "{:,}".format(usa_population_needed)
print(f"{usn} people will need to be vaccinated or infected before the pandemic is over")


# 3. Calculate how many people still need to be infected or vaccinated
people_left = usa_population_needed - usa_population_infected_immune
print(f"That means {people_left} people will need to be vaccinated or infected before the pandemic is over")


# 4. How many people left to get?
usa_people_left = round(usa_population_needed - usa_infected - (vaccine_effectiveness * usa_vaccinated))
plc = "{:,}".format(usa_people_left)
print(f"{plc} people will need to be vaccinated or infected before the pandemic is over")

# 5. How many people are getting vaccinated or infected per day
infected_or_vaccinated_per_day = usa_infections_daily + usa_vaccine_immunity_daily

# 6. Estimate how many days it will take at this rate
days_until_pandemic_over = usa_people_left / infected_or_vaccinated_per_day

# 7. Add the projected number of days to today's date to get the date the pandemic will end
date_pandemic_over = today + datetime.timedelta(days=days_until_pandemic_over)
print(f"The Date that the Pandemic is expected to be over is: {date_pandemic_over}")


# Goal 2: Estimate how many people infected, vaccinated, & untouched
print(" ") # print a blank lines
print("Goal 2: Estimate how many people infected, vaccinated, & untouched?") 


# 1. How many will be infected by the end of the pandemic?
usa_infected_proj = round(usa_infected + (days_until_pandemic_over * usa_infections_daily))
usa_ip = "{:,}".format(usa_infected_proj)
print(f"We project {usa_ip} total people infected in the USA by {date_pandemic_over}")


# 2. How many people will be vaccinated by the end of the pandemic?
usa_vaccinated_proj = round(usa_vaccinated + days_until_pandemic_over * usa_vaccinations_daily)
usa_vp = "{:,}".format(usa_vaccinated_proj)
print(f"We project {usa_vp} total people vaccinated in the USA by {date_pandemic_over}")


# 3. How many people will be untouched by the end of the pandemic?
usa_people_untouched_proj = round(usa_population - usa_infected_proj - usa_vaccinated_proj)
usa_up = "{:,}".format(usa_people_untouched_proj)
print(f"We project {usa_up} total people untouched by the virus or a vaccine in the USA by {date_pandemic_over}")

# 4. Check to make sure the numbers make sense
# print(usa_population)
# print(usa_infected_proj + usa_vaccinated_proj + usa_people_untouched)





