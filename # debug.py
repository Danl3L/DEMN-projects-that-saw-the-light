import datetime

def parse_time(time_str):
    time_parts = time_str.split()
    if ':' in time_parts[0]:
        hour, minute = map(int, time_parts[0].split(":"))
    else:
        hour = int(time_parts[0])
        minute = 0  # Default to 0 if minute part is not specified
    if len(time_parts) > 1 and time_parts[1].upper() == 'PM' and hour != 12:
        hour += 12
    return hour, minute

def calculate_new_schedule(intensity, current_schedule, course_duration):
    new_schedule = []  # List to store new events
    number_of_weeks = 0  # Initialize number of weeks

    # Parse start and end times
    start_time_str, end_time_str = current_schedule.split(" - ")
    start_hour, start_minute = parse_time(start_time_str)
    end_hour, end_minute = parse_time(end_time_str)

    # Calculate start and end datetime objects
    start_datetime = datetime.datetime.combine(datetime.date.today(), datetime.time(start_hour, start_minute))
    end_datetime = datetime.datetime.combine(datetime.date.today(), datetime.time(end_hour, end_minute))

    # Calculate time delta
    delta = (end_datetime - start_datetime) / 5  # Divide by 5 for 5 working days

    # Determine study duration per day based on intensity
    if "5 hours" in intensity:
        duration_per_day = 1  # 1 hour per day for 5 hours per week
    elif "10 hours" in intensity:
        duration_per_day = 2  # 2 hours per day for 10 hours per week
    elif "12 hours" in intensity:
        duration_per_day = 2.4  # 2.4 hours per day for 12 hours per week
    else:
        # Custom intensity: divide total study hours evenly across 6 days
        total_study_hours = float(course_duration.split()[0]) * 4 * float(intensity.split()[0])  # Assuming 4 weeks per month
        duration_per_day = total_study_hours / 6  # Divide evenly across 6 study days

        # Calculate number of weeks required
        number_of_weeks = total_study_hours / float(intensity.split()[0])  # Assuming intensity is hours per week

    # Generate events for each day
    for i in range(int(total_study_hours)):  # Assuming Monday to Friday
        event_start = start_datetime + delta * i
        event_end = event_start + datetime.timedelta(hours=duration_per_day)
        new_schedule.append((event_start, event_end))

    return new_schedule, number_of_weeks

# Define test inputs
intensity = "10 hours per week"
current_schedule = "9 AM - 5 PM"
course_duration = "3 months"  # Placeholder duration for testing

# Call the calculate_new_schedule function
new_schedule, number_of_weeks = calculate_new_schedule(intensity, current_schedule, course_duration)

# Print the results for debugging
print("New Schedule:")
for idx, event in enumerate(new_schedule, 1):
    start, end = event
    print(f"Week {idx}: {start.strftime('%Y-%m-%d %H:%M')} - {end.strftime('%H:%M')}")

print("Number of Weeks:", number_of_weeks)
