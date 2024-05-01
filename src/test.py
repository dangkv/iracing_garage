import os
from iracing_connect import iRacingConnect
from dotenv import load_dotenv


if __name__ == "__main__":
    load_dotenv()

    username = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")

    iRacing = iRacingConnect(username, password)

    subsession_id = 64059658
    customer_id = 937417
    car_id = 142

    # get_result = iRacing.results.summary(subsession_id, 0)
    # get_result = iRacing.results.lap_data(subsession_id, 0)
    # get_result = iRacing.results.event_log(subsession_id, 0)
    # get_result = iRacing.results.lap_chart_data(subsession_id, 0)
    # get_result = iRacing.stats.member_bests(customer_id=customer_id, car_id=car_id)
    # get_result = iRacing.stats.member_yearly(customer_id=customer_id)
    # get_result = iRacing.stats.member_career(customer_id=customer_id)
    # get_result = iRacing.stats.member_recent_races(customer_id=customer_id)
    get_result = iRacing.stats.member_summary(customer_id=customer_id)

    # get_result = iRacing.stats.membership(customer_id=customer_id)

    print(get_result)
