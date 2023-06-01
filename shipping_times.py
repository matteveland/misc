import datetime
import holidays

is_holidays = holidays.HolidayBase()
weekdays = {
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    7: "Sunday",
}


def main():
    print(shipping_times())


def shipping_times():
    now = datetime.datetime.now()
    current_hour = 13  # now.strftime("%H")
    today = datetime.date.today()
    us_holidays = holidays.country_holidays("US")
    tomorrow_date = today + datetime.timedelta(days=1)
    tomorrow_day = tomorrow_date.isoweekday()
    next_week_date = today + datetime.timedelta(days=3)
    next_week_day = tomorrow_date.isoweekday()

    if int(current_hour) < 12:
        print("Shipment request made the cut-off and will ship today.")

    else:
        for i in range(4):
            given_date = today + datetime.timedelta(days=i)

            if given_date in us_holidays:
                weekend = given_date.isoweekday()

                if is_holidays._is_monday(given_date):
                    print(
                        f"{str(given_date)} {weekdays[weekend]} *** Shipment may be impacted by a holiday. Shipment will ship the day following the holiday ({weekdays[2]}). ***2"
                    )
                    break
                elif is_holidays._is_friday(given_date):
                    print(
                        f"{str(given_date)} {weekdays[weekend]} *** Shipment may be impacted by a holiday. Shipment will ship the day following the holiday ({weekdays[1]}). ***3"
                    )
                    break
                elif is_holidays._is_weekend(given_date):
                    pass

                else:
                    next_day = weekend + 1
                    print(
                        f"{str(given_date)} {weekdays[weekend]} *** Shipment may be impacted by a holiday. Shipment will ship the day following the holiday ({weekdays[next_day]}). ***4"
                    )
                    break
        if tomorrow_day == 6 or tomorrow_day == 7:
            print(
                f"*** Shipment missed shipping time for Friday and will process/ship on Monday, {next_week_date}. ***"
            )

        elif is_holidays._is_monday(next_week_date):
            print(
                f"{str(next_week_date)} *** Shipment may be impacted by a holiday. Shipment will ship the day following the holiday ({weekdays[next_week_day]}). ***1"
            )
        else:
            print("Shipment missed today's cutoff and will ship tomorrow.")


"""
    else:
        print("Shipment made today's shipment and will ship today.")
"""
if __name__ == "__main__":
    main()
