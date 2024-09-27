def time_converter(hour, minute):
    if not isinstance(hour, int) or not isinstance(minute, int):
        raise TypeError("Hour and minute must be integers.")

    if minute == 0:
        return f"{hour % 12} o'clock"
    elif minute == 1:
        return f"one minute past {hour}"
    elif minute == 15:
        return f"quarter past {hour}"
    elif minute == 30:
        return f"half past {hour}"
    elif minute == 45:
        return f"quarter to {(hour+1) % 12}"
    elif minute == 59:
        return f"one minute to {(hour+1) % 12}"
    elif minute < 30:
        return f"{minute} minutes past {hour}"
    else:
        return f"{60-minute} minutes to {(hour+1) % 12}"


# time converter a 12 hours timer
print(time_converter(13, 00))
