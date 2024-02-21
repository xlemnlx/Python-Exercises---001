def country_area_for_earth(country_area):
    earth_area = 148940000
    percentage = round(((country_area[1] / earth_area) * 100), 2)
    output = f"{country_area[0]} is {percentage}% of the total world's landmass."
    return output