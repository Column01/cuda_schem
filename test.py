import nbtlib


nbt_file = nbtlib.load("shiba3.nbt")
print(nbt_file["palette"])
