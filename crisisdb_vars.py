MYINT = ['IntegerField', 'NumberInput']
MYDEC = ['DecimalField', 'NumberInput']
MYTXT = ['CharField', 'TextInput']
# for these we need, the pandas dfs to smartly select the choices, put them in a tuple or list
MYTXT_CH = ['CharField', 'Select']
MYFOREIGN = ['ForeignKey', 'Select']

varhiers_dic = {'Economy Variables': {'Productivity': ['agricultural_population',
                                                       'arable_land',
                                                       'arable_land_per_farmer',
                                                       'gross_grain_shared_per_agricultural_population',
                                                       'net_grain_shared_per_agricultural_population',
                                                       'surplus',
                                                       'gdp_per_capita'],
                                      'State Finances': ['military_expense', 'silver_inflow', 'silver_stock']},
                'Social Complexity Variables': {'Social Scale': ['total_population']},
                'Well Being': {'Biological Well-Being': ['drought_event',
                                                         'locust_event',
                                                         'socioeconomic_turmoil_event',
                                                         'crop_failure_event',
                                                         'famine_event',
                                                         'disease_outbreak']}}

vars_dic = {
    "human_sacrifice": {"notes": "This is a new model definition for Human Sacrifice", "main_desc": "The deliberate and ritualized killing of a person to please or placate supernatural entities (including gods, spirits, and ancestors) or gain other supernatural benefits.", "main_desc_source": "", "cols": 1, "section": "Conflict Variables", "subsection": "External Conflicts Subsection", "null_meaning": "The value is not available.", "col1": {"dtype": ['CharField', 'Select'], "varname": "human_sacrifice", "var_exp": "The Human Sacrifce", "var_exp_source": None, "choices": ['U', 'A;P', 'P*', 'P', 'A~P', 'A', 'A*', 'P~A']}},
    "external_conflict": {"notes": "This is a new model definition for External conflicts", "main_desc": "Main Descriptions for the Variable external_conflict are missing!", "main_desc_source": "", "cols": 1, "section": "Conflict Variables", "subsection": "External Conflicts Subsection", "null_meaning": "The value is not available.", "col1": {"dtype": ["CharField", "TextInput"], "varname": "conflict_name", "var_exp": "The unique name of this external conflict", "var_exp_source": None}},
    "internal_conflict": {"notes": "This is a new model definition for internal conflicts", "main_desc": "Main Descriptions for the Variable internal_conflict are missing!", "main_desc_source": "", "cols": 4, "section": "Conflict Variables", "subsection": "Internal Conflicts Subsection", "null_meaning": "The value is not available.", "col1": {"dtype": ["CharField", "TextInput"], "varname": "conflict", "var_exp": "The name of the conflict", "var_exp_source": None}, "col2": {"dtype": ["DecimalField", "NumberInput"], "varname": "expenditure", "var_exp": "The military expenses in millions silver taels.", "units": "silver taels", "min": None, "max": None, "scale": 1000000, "decimal_places": 0, "max_digits": 20, "var_exp_source": None}, "col3": {"dtype": ["CharField", "TextInput"], "varname": "leader", "var_exp": "The leader of the conflict", "var_exp_source": None}, "col4": {"dtype": ["IntegerField", "NumberInput"], "varname": "casualty", "var_exp": "The number of people who died in this conflict.", "units": "People", "min": None, "max": None, "scale": 1, "var_exp_source": None}}, "external_conflict_side": {"notes": "This is a new model definition for External conflict sides", "main_desc": "Main Descriptions for the Variable external_conflict_side are missing!", "main_desc_source": "", "cols": 4, "section": "Conflict Variables", "subsection": "External Conflicts Subsection", "null_meaning": "The value is not available.", "col1": {"dtype": ["ForeignKey", "Select"], "varname": "conflict_id", "var_exp": "The external_conflict which is the actual conflict we are talking about", "var_exp_source": None, "foreign_key": "External_conflict", "foreign_key_related_name": "External_conflicts"}, "col2": {"dtype": ["DecimalField", "NumberInput"], "varname": "expenditure", "var_exp": "The military expenses (from this side) in silver taels.", "units": "silver taels", "min": None, "max": None, "scale": 1, "decimal_places": 0, "max_digits": 20, "var_exp_source": None}, "col3": {"dtype": ["CharField", "TextInput"], "varname": "leader", "var_exp": "The leader of this side of conflict", "var_exp_source": None}, "col4": {"dtype": ["IntegerField", "NumberInput"], "varname": "casualty", "var_exp": "The number of people who died (from this side) in this conflict.", "units": "People", "min": None, "max": None, "scale": 1, "var_exp_source": None}},
    "agricultural_population": {"notes": "Notes for the Variable agricultural_population are missing!", "main_desc": "No Explanations.", "main_desc_source": "", "cols": 1, "section": "Economy Variables", "subsection": "Productivity", "null_meaning": "The value is not available.", "col1": {"dtype": ["IntegerField", "NumberInput"], "varname": "agricultural_population", "var_exp": "No Explanations.", "units": "People", "min": 0, "max": None, "scale": 1000, "var_exp_source": None}}, "arable_land": {"notes": "Notes for the Variable arable_land are missing!", "main_desc": "No Explanations.", "main_desc_source": "", "cols": 1, "section": "Economy Variables", "subsection": "Productivity", "null_meaning": "The value is not available.", "col1": {"dtype": ["IntegerField", "NumberInput"], "varname": "arable_land", "var_exp": "No Explanations.", "units": "mu?", "min": None, "max": None, "scale": 1000, "var_exp_source": None}}, "arable_land_per_farmer": {"notes": "Notes for the Variable arable_land_per_farmer are missing!", "main_desc": "No Explanations.", "main_desc_source": "", "cols": 1, "section": "Economy Variables", "subsection": "Productivity", "null_meaning": "The value is not available.", "col1": {"dtype": ["IntegerField", "NumberInput"], "varname": "arable_land_per_farmer", "var_exp": "No Explanations.", "units": "mu?", "min": None, "max": None, "scale": 1, "var_exp_source": None}}, "gross_grain_shared_per_agricultural_population": {"notes": "Notes for the Variable gross_grain_shared_per_agricultural_population are missing!", "main_desc": "No Explanations.", "main_desc_source": "", "cols": 1, "section": "Economy Variables", "subsection": "Productivity", "null_meaning": "The value is not available.", "col1": {"dtype": ["IntegerField", "NumberInput"], "varname": "gross_grain_shared_per_agricultural_population", "var_exp": "No Explanations.", "units": "(catties per capita)", "min": None, "max": None, "scale": 1, "var_exp_source": None}}, "net_grain_shared_per_agricultural_population": {"notes": "Notes for the Variable net_grain_shared_per_agricultural_population are missing!", "main_desc": "No Explanations.", "main_desc_source": "", "cols": 1, "section": "Economy Variables", "subsection": "Productivity", "null_meaning": "The value is not available.", "col1": {"dtype": ["IntegerField", "NumberInput"], "varname": "net_grain_shared_per_agricultural_population", "var_exp": "No Explanations.", "units": "(catties per capita)", "min": None, "max": None, "scale": 1, "var_exp_source": None}}, "surplus": {"notes": "Notes for the Variable surplus are missing!", "main_desc": "No Explanations.", "main_desc_source": "", "cols": 1, "section": "Economy Variables", "subsection": "Productivity", "null_meaning": "The value is not available.", "col1": {"dtype": ["IntegerField", "NumberInput"], "varname": "surplus", "var_exp": "No Explanations.", "units": "(catties per capita)", "min": None, "max": None, "scale": 1, "var_exp_source": None}}, "military_expense": {"notes": "Not sure about Section and Subsection.", "main_desc": "Main Descriptions for the Variable military_expense are missing!", "main_desc_source": "https://en.wikipedia.org/wiki/Disease_outbreak", "cols": 2, "section": "Economy Variables", "subsection": "State Finances", "null_meaning": "The value is not available.", "col1": {"dtype": ["CharField", "TextInput"], "varname": "conflict", "var_exp": "The name of the conflict", "var_exp_source": None}, "col2": {"dtype": ["DecimalField", "NumberInput"], "varname": "expenditure", "var_exp": "The military expenses in millions silver taels.", "units": "silver taels", "min": None, "max": None, "scale": 1000000, "decimal_places": 15, "max_digits": 20, "var_exp_source": None}}, "silver_inflow": {"notes": "Needs suoervision on the units and scale.", "main_desc": "Silver inflow in Millions of silver taels??", "main_desc_source": "", "cols": 1, "section": "Economy Variables", "subsection": "State Finances", "null_meaning": "The value is not available.", "col1": {"dtype": ["IntegerField", "NumberInput"], "varname": "silver_inflow", "var_exp": "Silver inflow in Millions of silver taels??", "units": "silver taels??", "min": None, "max": None, "scale": 1000000, "var_exp_source": None}}, "silver_stock": {"notes": "Needs suoervision on the units and scale.", "main_desc": "Silver stock in Millions of silver taels??", "main_desc_source": "", "cols": 1, "section": "Economy Variables", "subsection": "State Finances", "null_meaning": "The value is not available.", "col1": {"dtype": ["IntegerField", "NumberInput"], "varname": "silver_stock", "var_exp": "Silver stock in Millions of silver taels??", "units": "silver taels??", "min": None, "max": None, "scale": 1000000, "var_exp_source": None}}, "total_population": {"notes": "Note that the population values are scaled.", "main_desc": "Total population or simply population, of a given area is the total number of people in that area at a given time.", "main_desc_source": "", "cols": 1, "section": "Social Complexity Variables", "subsection": "Social Scale", "null_meaning": "The value is not available.", "col1": {"dtype": ["IntegerField", "NumberInput"], "varname": "total_population", "var_exp": "The total population of a country (or a polity).", "units": "People", "min": 0, "max": None, "scale": 1000, "var_exp_source": None}}, "gdp_per_capita": {"notes": "The exact year based on which the value of Dollar is taken into account is not clear.", "main_desc": "The Gross Domestic Product per capita, or GDP per capita, is a measure of a country's economic output that accounts for its number of people. It divides the country's gross domestic product by its total population.", "main_desc_source": "https://www.thebalance.com/gdp-per-capita-formula-u-s-compared-to-highest-and-lowest-3305848", "cols": 1, "section": "Economy Variables", "subsection": "Productivity", "null_meaning": "The value is not available.", "col1": {
        "dtype": ["DecimalField", "NumberInput"], "varname": "gdp_per_capita", "var_exp": "The Gross Domestic Product per capita, or GDP per capita, is a measure of a country's economic output that accounts for its number of people. It divides the country's gross domestic product by its total population.", "units": "Dollars (in 2009?)", "min": None, "max": None, "scale": 1, "decimal_places": 15, "max_digits": 20, "var_exp_source": "https://www.thebalance.com/gdp-per-capita-formula-u-s-compared-to-highest-and-lowest-3305848"}}, "drought_event": {"notes": "Notes for the Variable drought_event are missing!", "main_desc": "number of geographic sites indicating drought", "main_desc_source": "https://www1.ncdc.noaa.gov/pub/data/paleo/historical/asia/china/reaches2020drought-category-sites.txt", "cols": 1, "section": "Well Being", "subsection": "Biological Well-Being", "null_meaning": "The value is not available.", "col1": {"dtype": ["IntegerField", "NumberInput"], "varname": "drought_event", "var_exp": "number of geographic sites indicating drought", "units": "Numbers", "min": 0, "max": None, "scale": 1, "var_exp_source": None}}, "locust_event": {"notes": "Notes for the Variable locust_event are missing!", "main_desc": "number of geographic sites indicating locusts", "main_desc_source": "https://www1.ncdc.noaa.gov/pub/data/paleo/historical/asia/china/reaches2020drought-category-sites.txt", "cols": 1, "section": "Well Being", "subsection": "Biological Well-Being", "null_meaning": "The value is not available.", "col1": {"dtype": ["IntegerField", "NumberInput"], "varname": "locust_event", "var_exp": "number of geographic sites indicating locusts", "units": "Numbers", "min": 0, "max": None, "scale": 1, "var_exp_source": None}}, "socioeconomic_turmoil_event": {"notes": "Notes for the Variable socioeconomic_turmoil_event are missing!", "main_desc": "number of geographic sites indicating socioeconomic turmoil", "main_desc_source": "https://www1.ncdc.noaa.gov/pub/data/paleo/historical/asia/china/reaches2020drought-category-sites.txt", "cols": 1, "section": "Well Being", "subsection": "Biological Well-Being", "null_meaning": "The value is not available.", "col1": {"dtype": ["IntegerField", "NumberInput"], "varname": "socioeconomic_turmoil_event", "var_exp": "number of geographic sites indicating socioeconomic turmoil", "units": "Numbers", "min": 0, "max": None, "scale": 1, "var_exp_source": None}}, "crop_failure_event": {"notes": "Notes for the Variable crop_failure_event are missing!", "main_desc": "number of geographic sites indicating crop failure", "main_desc_source": "https://www1.ncdc.noaa.gov/pub/data/paleo/historical/asia/china/reaches2020drought-category-sites.txt", "cols": 1, "section": "Well Being", "subsection": "Biological Well-Being", "null_meaning": "The value is not available.", "col1": {"dtype": ["IntegerField", "NumberInput"], "varname": "crop_failure_event", "var_exp": "number of geographic sites indicating crop failure", "units": "Numbers", "min": 0, "max": None, "scale": 1, "var_exp_source": None}}, "famine_event": {"notes": "Notes for the Variable famine_event are missing!", "main_desc": "number of geographic sites indicating famine", "main_desc_source": "https://www1.ncdc.noaa.gov/pub/data/paleo/historical/asia/china/reaches2020drought-category-sites.txt", "cols": 1, "section": "Well Being", "subsection": "Biological Well-Being", "null_meaning": "The value is not available.", "col1": {"dtype": ["IntegerField", "NumberInput"], "varname": "famine_event", "var_exp": "number of geographic sites indicating famine", "units": "Numbers", "min": 0, "max": None, "scale": 1, "var_exp_source": None}}, "disease_outbreak": {"notes": "Notes for the Variable disease_outbreak are missing!", "main_desc": "A sudden increase in occurrences of a disease when cases are in excess of normal expectancy for the location or season.", "main_desc_source": "https://en.wikipedia.org/wiki/Disease_outbreak", "cols": 6, "section": "Well Being", "subsection": "Biological Well-Being", "null_meaning": 'The value is not available.', "col1": {"dtype": ["DecimalField", "NumberInput"], "varname": "longitude", "var_exp": "The longitude (in degrees) of the place where the disease was spread.", "units": "Degrees", "min": -180, "max": 180, "scale": 1, "decimal_places": 15, "max_digits": 20, "var_exp_source": None}, "col2": {"dtype": ["DecimalField", "NumberInput"], "varname": "latitude", "var_exp": "The latitude (in degrees) of the place where the disease was spread.", "units": "Degrees", "min": -180, "max": 180, "scale": 1, "decimal_places": 15, "max_digits": 20, "var_exp_source": None}, "col3": {"dtype": ["DecimalField", "NumberInput"], "varname": "elevation", "var_exp": "Elevation from mean sea level (in meters) of the place where the disease was spread.", "units": "Meters", "min": 0, "max": 5000, "scale": 1, "decimal_places": 15, "max_digits": 20, "var_exp_source": None}, "col4": {"dtype": ["CharField", "Select"], "varname": "sub_category", "var_exp": "The category of the disease.", "var_exp_source": None, "choices": ["Peculiar Epidemics", "Pestilence", "Miasm", "Pox", "Uncertain Pestilence", "Dysentery", "Malaria", "Influenza", "Cholera", "Diptheria", "Plague"]}, "col5": {"dtype": ["CharField", "Select"], "varname": "magnitude", "var_exp": "How heavy the disease was.", "var_exp_source": None, "choices": ["Uncertain", "Light", "Heavy", "No description", "Heavy- Multiple Times", "No Happening", "Moderate"]}, "col6": {"dtype": ["CharField", "Select"], "varname": "duration", "var_exp": "How long the disease lasted.", "var_exp_source": None, "choices": ["No description", "Over 90 Days", "Uncertain", "30-60 Days", "1-10 Days", "60-90 Days"]}}}
