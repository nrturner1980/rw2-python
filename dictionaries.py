# Dictionaries
band = {
    "vocals":"Plant",
    "guitar": "Page",
}

band2 = dict(vocals="Plant", guitar="Page")

print(band)
print(band2)
print(type(band))
print(len(band))

# Access items
print(band["vocals"])
print(band.get("guitar"))

# list all keys
print(band.keys())

# list all values
print(band.values())

# list of key/value pairs as tuples
print(band.items())



print("triangle" in band)

# Change values
band["vocals"] = "Coverdale"
band.update({"bass"; "JPJ"})

print(band)
