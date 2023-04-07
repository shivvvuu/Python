# Tutorial on Find most freq item

from collections import Counter

text = "Southwest Airlines initiated a significant travel disruption that misplaced travelers all across the country."\

"Flights were canceled, re-booking services were temporarily unavailable, and thousands of customers were furious."\

"According to Southwest, the travel interruptions took place between December 24, 2022 and January 2, 2023. However, earlier weather-related flight delays ultimately catapulted the airline into an operational crisis."\

"The most wonderful time of year? Not so much for Southwest."

word = text.split()

counter = Counter(word)
top_three =counter.most_common(3)
print(top_three)