def display_heading():
    print("\n=========== Geological Rock Classification ===========")
    print("A Tool for Identifying Rocks Based on Composition and Grain Size")
    print("========================================================\n")

if __name__ == "__main__":
    display_heading()


def identify_rock(input_percentages, grain_size):
    total_percentage = sum(input_percentages.values())
    if total_percentage != 100:
        print(f"Warning: Total input percentages ({total_percentage}%) do not add up to 100%.")

    rock_compositions = {
        "Granite": {
            "Quartz": (20, 60), "Plagioclase": (10, 40), "Orthoclase": (10, 40), "Microcline": (10, 40), "Muscovite": (5, 15),
            "Biotite": (0, 10), "Hornblende": (0, 20), "Olivine": (0, 8), "Pyroxene": (0, 5), "Zircon": (0, 1), "Apatite": (0, 1)
        },
        "Basalt": {
            "Quartz": (5, 15), "Plagioclase": (40, 60), "Orthoclase": (0, 5), "Microcline": (0, 5), "Muscovite": (0, 5),
            "Biotite": (5, 20), "Hornblende": (0, 5), "Olivine": (5, 50), "Pyroxene": (15, 40), "Magnetite": (0, 5), "Ilmenite": (0, 5)
        },
        "Rhyolite": {
            "Quartz": (20, 40), "Plagioclase": (15, 50), "Orthoclase": (10, 25), "Microcline": (0, 10), "Muscovite": (0, 5),
            "Biotite": (0, 5), "Hornblende": (0, 5), "Olivine": (0, 5), "Pyroxene": (0, 5), "Zircon": (0, 2), "Apatite": (0, 2)
        },
        "Gabbro": {
            "Quartz": (5, 15), "Plagioclase": (35, 70), "Orthoclase": (15, 25), "Microcline": (0, 5), "Muscovite": (0, 5),
            "Biotite": (5, 15), "Hornblende": (0, 5), "Olivine": (0, 15), "Pyroxene": (25, 50), "Magnetite": (2, 10), "Ilmenite": (2, 10), "Apatite": (0, 1)
        },
        "Diorite": {
            "Quartz": (0, 10), "Plagioclase": (35, 60), "Biotite": (5, 25), "Hornblende": (15, 35), "Olivine": (0, 5), "Pyroxene": (0, 5)
        },
        "Andesite": {
            "Quartz": (5, 15), "Plagioclase": (40, 60), "Hornblende": (10, 30), "Olivine": (0, 5), "Pyroxene": (0, 5), "Magnetite": (0, 1)
        },
        "Peridotite": {
            "Quartz": (0, 5), "Plagioclase": (0, 5), "Orthoclase": (0, 5), "Microcline": (0, 5),
            "Olivine": (35, 70), "Pyroxene": (20, 45), "Magnetite": (5, 15), "Chlorite": (5, 15)
        },
        "Obsidian": {
            "Quartz": (50, 70), "Plagioclase": (10, 30), "Magnetite": (0, 5), "Hematite": (0, 1), "Ilmenite": (0, 1)
        },
        "Pumice": {
            "Quartz": (15, 40), "Plagioclase": (20, 45), "Orthoclase": (15, 20), "Biotite": (0, 5), "Hornblende": (0, 5),
            "Magnetite": (0, 3)
        },
        "Schist": {
            "Quartz": (30, 70), "Mica": (10, 50), "Feldspar": (5, 30), "Chlorite": (0, 20), "Garnet": (0, 10), "Kyanite": (0, 5)
        },
        "Marble": {
            "Calcite": (90, 100), "Quartz": (0, 5), "Mica": (0, 5), "Feldspar": (0, 5)
        },
        "Gneiss": {
            "Quartz": (30, 60), "Feldspar": (20, 40), "Mica": (10, 30), "Biotite": (0, 20), "Hornblende": (0, 20)
        },
        "Slate": {
            "Quartz": (30, 60), "Mica": (10, 30), "Chlorite": (5, 20), "Clay Minerals": (10, 40)
        },
        "Sandstone": {
            "Quartz": (50, 90), "Feldspar": (5, 25), "Mica": (0, 10), "Calcite": (0, 10), "Clay Minerals": (0, 10)
        },
        "Limestone": {
            "Calcite": (90, 100), "Quartz": (0, 5), "Clay Minerals": (0, 10), "Dolomite": (0, 5)
        },
        "Shale": {
            "Clay Minerals": (50, 80), "Quartz": (10, 30), "Feldspar": (5, 15), "Mica": (5, 15), "Calcite": (0, 5)
        },
        "Conglomerate": {
            "Quartz": (30, 70), "Feldspar": (0, 30), "Calcite": (0, 30), "Clay Minerals": (0, 10), "Mica": (0, 10)
        }
    }

    
    grain_size_ranges = {
    "Granite": (1, 5),        
    "Basalt": (0, 0.5),      
    "Sandstone": (0.1, 2),   
    "Conglomerate": (2, 256), 
    "Limestone": (0.01, 1),   
    "Gneiss": (0.5, 3),       
    "Marble": (0.1, 3),      
    
}
    
    rock_descriptions = {
        "Granite": "Granite is a coarse-grained intrusive felsic Igneous rock, rich in quartz and feldspar, with visible interlocking crystals.",
        "Basalt": "Basalt is a dark-colored, fine-grained extrusive mafic Igneous rock, commonly formed from lava flows.",
        "Rhyolite": "Rhyolite is a light-colored, fine-grained extrusive felsic Igneous rock, chemically equivalent to granite.",
        "Gabbro": "Gabbro is a dark-colored, coarse-grained intrusive mafic Igneous rock, primarily composed of plagioclase and pyroxene, with minor amounts of olivine and amphibole.",
        "Diorite": "Diorite is a medium- to coarse-grained intrusive intermediate Igneous rock, characterized by a salt-and-pepper appearance.",
        "Andesite": "Andesite is a fine-grained extrusive intermediate Igneous rock, typically gray or brown, commonly found in volcanic regions.",
        "Peridotite": "Peridotite is a coarse-grained ultramafic intrusive Igneous rock, rich in olivine and pyroxene.",
        "Obsidian": "Obsidian is a naturally occurring volcanic glass, formed from the rapid cooling of silica-rich lava.",
        "Pumice": "Pumice is a highly vesicular, lightweight extrusive volcanic Igneous rock, formed during explosive eruptions.",
        "Schist": "Schist is a foliated metamorphic rock with well-developed parallel layers of mica and other minerals.",
        "Marble": "Marble is a non-foliated metamorphic rock, primarily composed of recrystallized calcite or dolomite.",
        "Gneiss": "Gneiss is a foliated metamorphic rock with alternating layers of light and dark minerals.",
        "Slate": "Slate is a fine-grained, foliated metamorphic rock, primarily composed of clay minerals.",
        "Sandstone": "Sandstone is a clastic sedimentary rock, primarily composed of sand-sized mineral grains, mostly quartz.",
        "Limestone": "Limestone is a sedimentary rock composed primarily of calcite.",
        "Shale": "Shale is a fine-grained sedimentary rock formed from the compaction of clay, silt, and other tiny particles.",
        "Conglomerate": "Conglomerate is a clastic sedimentary rock consisting of rounded fragments of rocks and minerals."
    }


    possible_matches = []

    for rock, composition in rock_compositions.items():
        match = True

        for mineral, (min_range, max_range) in composition.items():
            percentage = input_percentages.get(mineral, 0)
            if percentage < min_range or percentage > max_range:
                match = False
                break

        if match:
            grain_min, grain_max = grain_size_ranges.get(rock, (None, None))
            if grain_min is not None and grain_max is not None:
                if grain_min <= grain_size <= grain_max:
                    possible_matches.append(rock)

    if not possible_matches:
        return None, "No rock type matches the given composition and grain size."

    return possible_matches, [rock_descriptions.get(rock, "Description not available.") for rock in possible_matches]


def get_input_percentages():
    minerals = [
        "Quartz", "Feldspar", "Mica", "Plagioclase", "Orthoclase", "Microcline", "Muscovite",
        "Biotite", "Hornblende", "Olivine", "Pyroxene", "Magnetite", "Chlorite", "Zircon", "Apatite", "Ilmenite", "Hematite",
        "Calcite", "Garnet", "Kyanite", "Clay Minerals", "Dolomite"
    ]

    input_percentages = {}

    for mineral in minerals:
        while True:
            try:
                percentage = input(f"Enter the percentage of {mineral} (or press Enter for 0): ")
                percentage = float(percentage) if percentage else 0
                if 0 <= percentage <= 100:
                    input_percentages[mineral] = percentage
                    break
                else:
                    print("Please enter a percentage between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

    return input_percentages


def get_grain_size():
    while True:
        try:
            grain_size = float(input("Enter the grain size (in mm): "))
            if grain_size > 0:
                return grain_size
            else:
                print("Please enter a positive value for grain size.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


if __name__ == "__main__":
    input_percentages = get_input_percentages()
    grain_size = get_grain_size()
    rocks, descriptions = identify_rock(input_percentages, grain_size)

    if rocks:
        print("The input mineral composition and grain size correspond to:")
        for rock, description in zip(rocks, descriptions):
            print(f"- {rock}: {description}")
    else:
        print("No rock type matches the given input composition and grain size.")

