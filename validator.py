"""Input validation module."""


def get_valid_name():
    """Ask for a non-empty name."""
    while True:
        name = input("enter your name: ").strip()
        if name:
            return name
        print("invalid input! please enter your name.")


def get_valid_measurement():
    """Ask for valid heartbeat count and time in seconds."""
    while True:
        try:
            beats = int(input("enter the number of heartbeats counted : "))
            time = int(input("enter the time in seconds: "))

            if beats < 0:
                print("\ninvalid input! number of beats cannot be negative.")
                continue

            if time <= 0:
                print("\ninvalid input! time must be greater than zero.")
                continue

            return beats, time

        except ValueError:
            print(
                "\ninvalid input! enter valid whole numbers "
                "for beats and time in seconds."
            )
