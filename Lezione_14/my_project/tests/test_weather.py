from my_project.weather import check_weather

#passed
def test_check_weather():
    assert check_weather(21.00) =="hot",'temperature greather than 20 degree\
    must be considered as hot'
    