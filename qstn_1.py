import pycountry

def search(countryList, search_key):
    if str(search_key) in countryList:
        print(search_key)
    

    else:
        print("Not found")    



country_names = []
countries = list(pycountry.countries)[:20]
for c in countries:
    country_names.append(c.name)       

search(country_names,'Angola')

    