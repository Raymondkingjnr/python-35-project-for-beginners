print("🎨 COLOR MIXER 🎨")

color_mixes = {
    ("red", "blue"): "purple",
    ("red", "yellow"): "orange",
    ("blue", "yellow"): "green",
    ("blue", "green"): "teal",
    ("white", "red"): "pink",
    ("red", "green"): "brown",
}

while True:
    color1 = input("\nEnter first color: ").lower().strip()
    color2 = input("\nEnter second color: ").lower().strip()

    mix = None

    if (color1, color2) in color_mixes:
        mix = color_mixes[(color1, color2)]
    elif (color2, color1) in color_mixes:
        mix = color_mixes[(color2, color1)]
        if mix:
            print(f"\nThe mix of {color1} and {color2} is {mix}.")
        else:
            print(f"\nSorry, I don't know the mix of {color1} and {color2}.")
    if input("\ndo you want to continue? (y/n): ").lower() != 'y':
        break
