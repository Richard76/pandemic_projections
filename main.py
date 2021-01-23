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



#### to add to v2 of the model
#################################


usa_infections_vaccinations_needed = 0.90 # % of people needing to be infected or vaccinated
vaccine_effectiveness = 0.90
usa_vaccine_immunity_daily = usa_vaccinated_daily * vaccine_effectiveness

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
infected_or_vaccinated_per_day = usa_infections_daily + usa_vaccine_immunity_daily

# 4. Estimate how many days it will take at this rate
days_until_pandemic_over = usa_people_left / infected_or_vaccinated_per_day

# 5. Add the projected number of days to todays date to get the 
date_pandemic_over = today + datetime.timedelta(days=days_until_pandemic_over)
print(f"The Date that the Pandemic is expected to be over is: {date_pandemic_over}")


# Calculate how many people infected, vaccinated, & untouched

# 1. How many will be infected by the end of the pandemic?
print(" ") # print a blank lines

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

# 4. Do the 3 numbers above total the us population like it should? (Yes)
# print(usa_population)
# print(usa_infected_proj + usa_vaccinated_proj + usa_people_untouched)



# Output
################

