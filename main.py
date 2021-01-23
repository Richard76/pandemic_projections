'''
Richard Farr
January 2021

Goal: Predict the end of the Coronavirus pandemic for each country
'''

# imports
from datetime import date



# What I know
################################
today = date.today()
print("Today's date:", today)

usa_population = 331000000
usa_infected = 25494983 # People Infected So Far - https://www.worldometers.info/coronavirus/ 
usa_deaths = 426356

usa_vaccinations = 19107000 # Vaccinations So Far - https://www.nytimes.com/interactive/2020/us/covid-19-vaccine-doses.html
usa_vaccinated = usa_vaccinations / 2 # People Vaccinated so far


# What I am estimating
#####################################

# daily infections
usa_infections_daily = 192000 # yesterdays infections

# daily vaccinated
usa_vaccinations_daily = 975540 # yesterdays shots https://www.nytimes.com/interactive/2020/us/covid-19-vaccine-doses.html
usa_vaccinated_daily = usa_vaccinations_daily / 2

# % of people needing to be infected or vaccinated for pandemic to be over
usa_infections_vaccinations_needed = 0.90 

# virus mortality rate
virus_mortality_rate = usa_deaths / usa_infected   # 0.0168 # Infection mortality rate 
# https://www.imperial.ac.uk/news/207273/covid-19-deaths-infection-fatality-ratio-about/




# Projections & Output
############################

# Goal 1: Calculate when the pandemic will be over
print(" ") # print a blank line
print("Goal 1: Calculate when the pandemic will be over")
print(" ")

# 0. US Population
us_pop = "{:,}".format(usa_population)
print(f"There are about {us_pop} people in the USA ")

# 1. Total # of people that have been infected or vaccinated so far?
usa_population_infected_immune = round(usa_infected + usa_vaccinated)
usii = "{:,}".format(usa_population_infected_immune)
print(f"{usii} people have either been infected or vaccinated so far")

# 2. Tell people what percentage of the population that is
pct_of_population = round( 100 * usa_population_infected_immune / usa_population)
print(f"That's {pct_of_population} % of the popluation infected or vaccinated so far")

# 3. Tell people what percentage of the population needs to be infected or vaccinated for the pandemic to end
usa_ivn = round(100 * usa_infections_vaccinations_needed)
print(f"We need {usa_ivn} % of the population to be infected or vaccinated for the pandemic to be over")

# 4. Calculate the Total # People that need to be infected or vaccinated for the pandemic to be over
usa_population_needed = round(usa_infections_vaccinations_needed * usa_population)
usn = "{:,}".format(usa_population_needed)
print(f"A total of {usn} people will need to be vaccinated or infected before the pandemic is over")

# 5. Calculate how many people still need to be infected or vaccinated
people_left = usa_population_needed - usa_population_infected_immune
pl = "{:,}".format(people_left)
print(f"That means {pl} people still need to be vaccinated or infected")


# 6. How many people are getting vaccinated or infected per day?
infected_or_vaccinated_per_day = round(usa_infections_daily + usa_vaccine_immunity_daily)
ivpd = "{:,}".format(infected_or_vaccinated_per_day)
print(f"There are {ivpd} people getting infected or vaccinated per day")

# 6. Estimate how many days it will take at this rate
days_until_pandemic_over = round(people_left / infected_or_vaccinated_per_day)
dupo = "{:,}".format(days_until_pandemic_over)
print(f"That means it will be {dupo} days until the pandemic is over")

# 7. Add the projected number of days to today's date to get the date the pandemic will end
date_pandemic_over = today + datetime.timedelta(days=days_until_pandemic_over)
print(f"The Date that the Pandemic is expected to be over is: {date_pandemic_over}")


# Goal 2: Estimate how many people infected, dead, vaccinated, & untouched
print(" ") # print a blank lines
print("Goal 2: Estimate how many people infected, vaccinated, & untouched?") 


# 1. How many will be infected by the end of the pandemic?
usa_infected_proj = round(usa_infected + (days_until_pandemic_over * usa_infections_daily))
usa_ip = "{:,}".format(usa_infected_proj)
print(f"We project {usa_ip} total people infected in the USA by {date_pandemic_over}")


# 2. How many people will be vaccinated by the end of the pandemic?
usa_vaccinated_proj = round(usa_vaccinated + days_until_pandemic_over * usa_vaccinated_daily)
usa_vp = "{:,}".format(usa_vaccinated_proj)
print(f"We project {usa_vp} total people vaccinated in the USA by {date_pandemic_over}")

# 3. How many people dead so far
dead_so_far = round(usa_infected * virus_mortality_rate)
usa_dsf = "{:,}".format(dead_so_far)
print(f"We estimate the USA to have had {usa_dsf} deaths so far")


# 4. How many people projected to die
usa_dead_projected = round(usa_infected_proj * virus_mortality_rate)
usa_dp = "{:,}".format(usa_dead_projected)
print(f"We estimate the USA to have {usa_dp} deaths by {date_pandemic_over} ")


# 5. How many people more to die
usa_additional_deaths = usa_dead_projected - usa_deaths
usa_ad = "{:,}".format(usa_additional_deaths)
print(f"We estimate {usa_ad} additional deaths in the US over the next {days_until_pandemic_over} days ")

# 6. How many people will be untouched by the end of the pandemic?
usa_people_untouched_proj = round(usa_population - usa_infected_proj - usa_vaccinated_proj)
usa_up = "{:,}".format(usa_people_untouched_proj)
print(f"We project {usa_up} total people untouched by the virus or a vaccine in the USA by {date_pandemic_over}")

# 7. Check to make sure the numbers make sense
# print(usa_population == usa_infected_proj + usa_vaccinated_proj + usa_people_untouched_proj)
# print(usa_population)



#### Part 2 - Make the model Better
######################################################################

# 1. Take into account that the vaccine is not 100% effective
vaccine_effectiveness = 0.90 # just a guess
usa_vaccine_immunity_daily = usa_vaccinated_daily * vaccine_effectiveness

# 2. Take into account either the virus becomes more contagious or vaccine distribution starts going faster
virus_speed_up_rate = 1
vaccine_speed_up_rate = 1

# 3. What happens if the virus kills a higher percentage of people?
virus_mortality_increase = 0.30

# 4. Take into account immunity from infection or vaccination only lasts so long
immunity_time_from_infection = 180 # time in days
immunity_time_from_vaccination = 180 # time in days

# 5. Take into account a mutation that is more resistant to the vaccine

# 6. Add the effects of a new mutation that is completely immune to the vaccine
# We are just absolutely fucked here







