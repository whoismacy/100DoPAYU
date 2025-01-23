from copy import copy

# YES YOU CAN RETURN AN OBJECT FROM A FUNCTION.
# OBJECTS ARE MUTABLE.

# Copy module provides copy a method that can duplicate any object
# When you copy a module the original and the copied are not the same object
# We can use copy to write pure functions
# Functions that don't modify their parameters
# orig_obj is copy_obj will print out False and so will orig_obj == copy_obj

class Time:
    """Represents time during the day."""

def print_time(time):
    """A function that takes a time object as a parameter
    and prints out the time in the correct format."""
    print(f"{time.hour:02d}:{time.minute:02d}:{time.second:02d}")

def make_time(hour, minute, second):
    """A function that creates a Time object
    assigning it attributes hour minute and second
    and returns the created time object"""
    time = Time()
    time.hour = hour
    time.minute = minute
    time.second = second
    return time

def increment_time(time, hours, minutes, seconds):
    """Increments the time, given the particular values
    and object, objects are mutable."""
    time.hour += hours
    time.minute += minutes
    time.second += seconds

    carry, time.second = divmod(time.second, 60)
    carry, time.minute = divmod(time.minute + carry, 60)
    carry, time.hour = divmod(time.hour + carry, 24)

def add_time(time, hours, minutes, seconds):
    total = copy(time)
    increment_time(total, hours, minutes, seconds)
    return total

time_start = make_time(8, 30, 0)
end = add_time(time_start, 3, 85, 128)

print_time(time_start)
print_time(end)

# Suggest writing pure functions, whenever reasonable and only resort
# to modifiers if there is a compelling advantage.
# A Functional programming style
