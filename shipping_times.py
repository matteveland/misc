import datetime
import holidays

def main():
    print(shipping_times())


# current_time = datetime.datetime.utcnow()


def shipping_times():
    now = datetime.datetime.now()
    current_hour = now.strftime("%H")
    today = datetime.date.today()
    us_holidays = holidays.country_holidays("US")

    if int(current_hour) >= 12:
        print(
            "Shipment missed today's cut-off and will ship tomorrow if entered before noon (12 p.m.)"
        )
        for i in range(25):
            given_date = today + datetime.timedelta(days=i)
            if given_date in us_holidays:
                print(
                    f"{str(given_date)} *** shipment may be impacted by a holiday. Shipment will ship the day following the holiday. ***"
                )

            else:
                pass

    else:
        print("Shipment made today's shipment and will ship today.")


if __name__ == "__main__":
    main()
