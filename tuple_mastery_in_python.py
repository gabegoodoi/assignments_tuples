'''
Task 1: Formatting Flight Itineraries 

Create a Python function that takes a list of tuples as an argument. Each tuple contains information about a flight itinerary: (traveler_name, origin, destination). The function should format and return a string that lists each itinerary. For example, if the input is `[("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]`, the output should be a string formatted as:

"Itinerary 1: Alice - From New York to London
 Itinerary 2: Bob - From Tokyo to San Francisco"
 '''

# This was the first way I solved the problem, but later determined enum is not necessary to use on a list, better for a tuple

# def format_itinerary(list_of_tuples):
#     for enum, info in enumerate(list_of_tuples):
#         print(f"Itinerary {enum + 1}: {info[0]} - From {info[1]} to {info[2]}")

def format_itinerary(list_of_tuples):
    for info in list_of_tuples:
        print(f"Itinerary {list_of_tuples.index(info) + 1}: {info[0]} - From {info[1]} to {info[2]}")

sample_list = [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]

format_itinerary(sample_list)