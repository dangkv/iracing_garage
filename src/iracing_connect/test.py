import os
from client import Client
from dotenv import load_dotenv


if __name__ == "__main__":
    load_dotenv()

    username = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")

    iRacing = Client(username, password)

    subsession_id = 64059658
    customer_id = 937417
    car_id = 142

    # get_result = iRacing.RaceData(subsession_id=subsession_id)
    get_result = iRacing.lap_chart_data(subsession_id=subsession_id)
    # get_result = iRacing.member_bests(customer_id=customer_id, car_id=142)
    # get_result = iRacing.member_yearly(customer_id=customer_id)
    # get_result = iRacing.membership(customer_id=customer_id)
    # get_result = iRacing.event_log(subsession_id=subsession_id)
    # get_result = iRacing.member_recent_races(customer_id=customer_id)
    # get_result = iRacing.member_summary(customer_id=customer_id)

    print(get_result)
