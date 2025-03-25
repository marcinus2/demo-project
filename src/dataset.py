import pandas

data = {
    "name": ["John", "Anna", "Peter", "Linda"],
    "location": ["New York", "Paris", "Berlin", "London"],
    "age": [24, 13, 53, 33],
}

df = pandas.DataFrame(data)

df.head(2)
