from random import randrange
import random

#repeat_rolling = True
#while repeat_rolling:

def sex():
    roll = randrange(1,3)

    if roll <= 1:
        return "Male"

    elif roll > 1:
        return "Female"

    ##print(roll) - - FOR DEBUG 





## A Shit Tonne of Arrays for Racial Choices
gensai = ["Air Gensai", "Earth Gensai", "Fire Gensai", "Water Gensai", "Cansin", "Axani", "Dust Para-Genasai", "Ice Para-Genasai", "Magma Para-Genasai", "Ooze Para-Genasai", "Smoke Para-Genasai"
          , "Steam Para-Genasai", "Glimmerfolk", "Azerblood", "Celadrin", "D'hin", "Worghest", "Fire Mephling", "Air Mephling", "Earth Mephling", "Water Mephling", "Gloaming", "Fey'ri", 
          "Tanarukk"]
halfling = ["Lightfoot Halfling", "Tallfellow Halfling", "Kender", "Shoal Halfling", "Half-Kender", "Glimmerskin Halfling", "Tundra Halfling", "Water Halfling", "Ghostwise Halfling"]
goblin = ["Goblin", "Hobgoblin", "Forestkith Goblin", "Dekanter Goblin", "Bugbear", "Bhuka", "Half-Goblin", "Sunscorched Hobgoblin", "Snow Goblin", "Air Goblin", "Fire Hobgoblin", "Varag", "Vril"]
gnome = ["Forest Gnome", "Rock Gnome", "Deep Gnome", "Wavecrest Gnome", "Whisper Gnome", "Chaos Gnome", "Tinker Gnome", "Fire Gnome", "Half-Gnome", "Stonehunter Gnome", "Ice Gnome", "Air Gnome",
         "Korobokuru"]
dwarf = ["Hill Dwarf", "Deep Dwarf", "Duergar", "Mountain Dwarf", "Gold Dwarf", "Dark Dwarf", "Gully Dwarf", "Dream Dwarf", "Seacliff Dwarf", "Badlands Dwarf", "Frost Dwarf", "Half-Dwarf", 
         "Fireblood Dwarf", "Glacier Dwarf", "Earth Dwarf", "Arctic Dwarf", "Urdunnir"]
elf = [ "High Elf", "Wood Elf", "Drow", "Gray Elf", "Wild Elf", "Wood Elf", "Aquatic Elf", "Aquatic Half-Elf", "Ghost Elf", "Kagonesti", "Qualanesti", "Silvanesti", "Painted Elf", "Phaethon", 
       "Forestlord Elf", "Forestlord Half-Elf", "Deepwyrm Drow", "Deepworm Half-Drow", "Snow Elf", "Fire-Elf", "Fire Half-Elf", "Star Elf", "Avariel"]
lizardfolk = ["Lizardfolk", "Blackscale Lizardfolk", "Poison Dusk Lizardfolk", "Viletooth Lizardfolk"]
draconian = ["Baaz Draconian", "Kapak Draconian", "Bozak Draconian"]
ogre = ["Half-Ogre", "Ogre", "Ogre Mage", "Irda", "Skullcrusher Ogre"]
giant = ["Hill Giant", "Stone Giant", "Half-Giant", "Sand Giant", "Jungle Giant"]
orc = ["Half-Orc", "Orc", "Scab-lands Half-Orc", "Frostblood Orc", "Frostblood Half-Orc", "Water Half-Orc", "Water Orc", "Gray Orc", "Mountain Orc", "Deep Orc"]

##3.5 List. Added PHB, DMG, MM, BED, DCS, EPH, EDWP, TotNH, RoS, RotW, SK, DragMag, MM3, PlHB, Undk, DragCom, RotD, DragM, MM5, MM4, UE, SS
otherRace = [random.choice(goblin), random.choice(gnome), random.choice(dwarf), random.choice(elf), random.choice(lizardfolk), random.choice(draconian), random.choice(ogre), random.choice(giant),
random.choice(orc),  "Hound Archon", "Azer",  "Centaur", "Doppelganger", "Gargoyle", "Janni",  "Githyanki", "Gnoll", "Grimlock", "Kobold","Lycanthrope(AL Based)", "Mind Flayer", "Minotaur",  
"Rakshasas", "Satyr", "Pixie", "Troglodyte", "Troll", "Yuan-Ti Pureblood", "Exhalted Bariaur",   "Krynnish Minotaur", "Blue", "Dromite", "Elan", "Maenad", "Synad", "Thri-Kreen", "Xeph", 
"Cambion", "Hellbred", "Goliath",  "Feral Gargun", "Stonechild",  "Raptorans", "Catfolk", "Killoren", "Hornhead", "Exiled Modron", "Aventi", "Darfellan",  "Hadozee", "Mortif",  "Tortle", 
"Adu'jas", "Guwaar", "Golmoid", "T'kel", "Grippli", "Umbrgen", "Giff", "Insectare", "Scro", "Phanaton", "Aarakocra","Mul", "Pterran", "Cyclops", "Xvart", "Norker", "Cactacae", "Khepri", 
"Vodyoni", "Garuda", "Kir-Lanan", "Shade", "Wemic", "Armand", "Changeling", "Dracotaur", "Flind", "Goatfolk", "Harssaf", "Kenku",  "Lumi", "Nycter", "Quadraphon", "Naztharune Rakshasas",
"Shifter", "Warforged", "Witchknife", "Asherati", "Crucian", "Buomman", "Neraphim", "Shadowswyft", "Spiker", "Wildren", "Chitine", "Deep Imaraski", "Kuo-Toas", "Slyth", "Kyrie", "Thanoi",
"Ursoi", "Daelkyr Half-Blood", "Diaboli", "Diopsid", "Dvati", "Lupin", "Tibbit", "Kalashtar", "Dragonborn", "Spellscale", "Dragonkin", "Neanderthals", "Uldra", "Domovoi", "Frost Folk", 
"Earth Kobold", "Jaebrin", "Windrazor", "Windscythe", "Hagspawn", "Spirit Folk", "Taer", "Volodni", "Hellbred", "Hengeyokai", "Nezumi", "Vanara", "Loxodon", "Tasloi", "Unbodied", "Annis Hag",
"Aranea", "Astral Deva", "Athach", "Barghest", "Belker", "Djinni", "Drider", "Efreeti", "Flamebrother", "Ghaele", "Green Hag", "Grig", "Hamatula", "Harpy", "Imp", "Kyton", "Lillend", "Magmin",
"Medusa", "Nixie", "Succubus", "Trumpet Archon", "Vrock",    ]

def race(): # Sigil Demographics
    ##Population 650,000 (37% human, 12% tiefling, 9% half-elf, 6% aasimar, 5% githzerai, 3% bariaur, 2% genasi, 1% halfling, 25% other) 
    
    roll = randrange(1,100)
  
    if roll <= 37:
        return "Human"

    elif roll <= 49:
        return "Tiefling"

    elif roll <= 58:
        return "Half-Elf"

    elif roll <= 63:
        return "Aasimar"

    elif roll <= 68:
        return "Githzerai"

    elif roll <= 71:
        return "Bariaur"
    
    elif roll <= 73:
        return (random.choice(gensai))

    elif roll <= 74:
        return (random.choice(halfling))
        ##race = halfling

    elif roll >=75 :
        return (random.choice(otherRace))
        ##race = other
    
    ##print(roll) #DEBUG prints the roll



charClass= ["Mystic", "Warlock", "Favoured Soul", "Ninja", "Scout", "Monk", "Spellthief", "Knight", "Psion", "Psychic Warrior", "Wilder", "Soulknife", "Dragonfire Adept", "Beguiler", 
            "Dragon Shaman", "Duskblade", "Warmage", "Wu Jen", "Shugenja", "Spirit Shaman", "Ardent", "Divine Mind", "Erudite", "Lurk", "Hexblade", "Samurai", "Swashbuckler", "Mariner", "Master",
            "Nightstalker", "Noble", "Artificer", "Shaman", "Sohei", "Ancestral Speaker", "Arcane Disciple", "Aspirant", "Benevolent", "Crusader", "Evangelist", "Metal Master", "Sidhe Scholar",
            "Storm Druid", "Totem Druid", "Wild Reaper", "Wind Walker", "Winter Warden", "Chaos Monk", "Sidewinder Monk", "Wild Monk", "Anarch", "Anti-Paladin", "Avenger", "Paladin", "Corrupter",
            "Despot", "Enforcer", "Incarnate", "Sentinel", "Mystic Ranger", "Wild Defender", "Anagakok", "Death Walker", "Filidh", "Fleshcrafter", "Soul Reaper", "Fangshield Barbarian", 
            "Planar Barbarian", "Planar Bard", "Planar Cleric", "Purple Staff Cleric", "Fangshield Druid", "Planar Druid", "Darksong Knight", "Planar Fighter", "Zhentarim Soldier", "Broken One",
            "Dark Moon Disciple", "Illuminated Monk", "Phoenix Disciple", "Planar Monk", "Skarn Monk", "Berronar Valkyrie", "Claw of the Sun and the Ankh", "Eternal Order", "Golden Cup", "Golden Lion",
            "Harmonious Knight", "Holy Judge", "Lion Legionnaire", "Mystic Fire Knight", "Noble Heart", "Paladin of Light", "Planar Paladin", "Red Falcon", "Ruby Rose Knight", "Shadow Cloak Knight", 
            "Solstice KNight", "Vigilant Eye of Helm", "Wary Swordknight", "Wayward Warden", "Fangshiled Ranger", "Moon Warder Ranger", "Planar Ranger", "Shadow Sword", "Shooting Star", 
            "Breath Stealer", "Golden Hand of Vergadain", "Holy Stalker", "Lunar Rogue", "Planar Rogue", "Rilkan Rogue", "Dragonblood Sorcerer", "Planar Sorcerer", "Dukar", "High One Warrior-Wizard",
            "Planar Wizard"]

def job():
    roll = randrange(1,100)

    if roll <= 10:
        return "Barbarian"

    elif roll <= 15:
        return ("Bard")

    elif roll <= 25:
        return ("Cleric")

    elif roll <= 30:
        return ("Druid")
    
    elif roll <= 50:
        return ("Fighter")

    elif roll <= 55:
        return ("Monk")

    elif roll <= 60:
        return ("Ranger")

    elif roll <= 80:
        return ("Rogue")

    elif roll <= 85:
        return ("Sorcerer")

    elif roll <= 90:
        return ("Wizard")

    elif roll >= 91:
        return(random.choice(charClass))

    ##print(roll) - FOR DEBUG 

def roll_char():
    return f"{sex()} {race()} {job()}\n"

roll_again = True
while roll_again:
    print (roll_char())
    repeat = input("Roll another? (y/n)").strip().lower()
    if repeat != 'y':
        roll_again = False

