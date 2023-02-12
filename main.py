
import glassdoor_scraper as gs
import pandas as pd


path = "C:/Users/lenovo/Documents/ds_salary_project/chromedriver"
df = gs.get_jobs('data_scientist', 15, False, path, 15)
