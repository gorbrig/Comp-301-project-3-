  vals = [
        158,
        146,
        144,
        147,
        238,
        243,
        236,
        240,
        239,
        232,
        237,
        228
        ]
characters = []
for val in vals:
	charcter = chr((val ^ 220) + 1)
	characters.append(character) 
print("".join(characters))
