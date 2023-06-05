import datetime
import holidays
import pytz


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
    shipping_times()
    # print(shipping_times("2023-06-23", "15"))


def shipping_times():
    now = datetime.datetime.now()  # "2023-06-16 15:47:20.799617"
    # current_hour = now.strftime("%H")  # hour  # 14
    eastern = pytz.timezone("US/Eastern")
    easter_time = now.astimezone(eastern)
    current_hour = easter_time.strftime("%H")
    today = datetime.date.today()  # today
    us_holidays = holidays.country_holidays("US")

    count = 0
    for i in range(4):
        given_date = today + datetime.timedelta(days=i)

        if given_date in us_holidays:
            weekday = given_date.isoweekday()

            if (
                today.isoweekday() == 6
                or today.isoweekday() == 7
                and is_holidays._is_monday(given_date)
            ):
                # return 1
                print(
                    f"{str(given_date)} {weekdays[weekday]} *** Shipment may be impacted by a holiday. Shipment will ship the day following the holiday ({weekdays[2]}). ***"
                )
                break
            elif (
                is_holidays._is_monday(given_date)
                and int(current_hour) < 8
                and is_holidays._is_friday(today)
            ):
                # return 2
                print("Shipment made today's shipment and will ship today.")

                break
            elif (
                is_holidays._is_monday(given_date)
                and int(current_hour) > 8
                and is_holidays._is_friday(today)
            ):
                # return 3
                print(
                    f"{str(given_date)} {weekdays[weekday]} *** Shipment may be impacted by a holiday. Shipment will ship the day following the holiday ({weekdays[2]}). ***"
                )
                break
            elif (
                is_holidays._is_tuesday(given_date)
                and int(current_hour) < 12
                and is_holidays._is_monday(today)
            ):
                # return 4
                print("Shipment made today's shipment and will ship today.")
                break
            elif (
                is_holidays._is_tuesday(given_date)
                and int(current_hour) > 12
                and is_holidays._is_monday(today)
            ):
                # return 5
                print(
                    f"{str(given_date)} {weekdays[weekday]} *** Shipment may be impacted by a holiday. Shipment will ship the day following the holiday ({weekdays[3]}). ***"
                )
            elif (
                is_holidays._is_wednesday(given_date)
                and int(current_hour) < 12
                and is_holidays._is_tuesday(today)
            ):
                # return 6
                print("Shipment made today's shipment and will ship today.")
                break
            elif (
                is_holidays._is_wednesday(given_date)
                and int(current_hour) > 12
                and is_holidays._is_tuesday(today)
            ):
                # return 7
                print(
                    f"{str(given_date)} {weekdays[weekday]} *** Shipment may be impacted by a holiday. Shipment will ship the day following the holiday ({weekdays[4]}). ***"
                )
            elif (
                is_holidays._is_thursday(given_date)
                and int(current_hour) < 12
                and is_holidays._is_wednesday(today)
            ):
                # return 8
                print("Shipment made today's shipment and will ship today.")
                break
            elif (
                is_holidays._is_thursday(given_date)
                and int(current_hour) > 12
                and is_holidays._is_wednesday(today)
            ):
                # return 9
                print(
                    f"{str(given_date)} {weekdays[weekday]} *** Shipment may be impacted by a holiday. Shipment will ship the day following the holiday ({weekdays[5]}). ***"
                )
            elif (
                is_holidays._is_friday(given_date)
                and int(current_hour) < 12
                and is_holidays._is_thursday(today)
            ):
                # return 10
                print("Shipment made today's shipment and will ship today.")
                break
            elif (
                is_holidays._is_friday(given_date)
                and int(current_hour) > 12
                and is_holidays._is_thursday(today)
            ):
                # return 11
                print(
                    f"{str(given_date)} {weekdays[weekday]} *** Shipment may be impacted by a holiday. Shipment will ship the day following the holiday ({weekdays[1]}). ***"
                )
                break

            else:
                # return 12
                print(
                    "Shipment missed today's cutoff annd will ship the next business day."
                )
                break
        count += 1
        if count == 4 and int(current_hour) > 12:
            # return 13
            print("Shipment missed today's cutoff and will ship the next business day.")
        elif count == 4 and int(current_hour) < 12:
            # return 14
            print("Shipment made today's shipment and will ship today.")
        else:
            pass


if __name__ == "__main__":
    main()
