from collections import namedtuple

# ImageGlossary uri files is the only required value, the rest default to an empty string for now
#
ImageGlossary = namedtuple('ImageGlossary', 'uri title alt source', defaults=["", "", ""])

def make_image_glossary():
  return {
  "Lunar LRV":
    ImageGlossary("/_static/images/accent/LLRV-pilot-kluever.jpg"
                 ,"Lunar Lander Research Vehicle Pilot - Kluever"
                 ,"A picture of the NASA Lunar Research Vehice with the pilot (Kleuver) standing beside it"
                 ,"NASA Image Archive"),

  "Margaret Hamilton Code Stack":
    ImageGlossary("/_static/images/accent/MargaretHamiltonCodeStack.jpg"
                 ,"Margaret Hamilton - Code Stack"
                 ,"A picture of Margaret Hamilton standing next to a tall stack of printouts for the Apollo Lunar Lander"
                 ,"NASA Image Archive"),

 "Gene Kranz At Console":
   ImageGlossary("/_static/images/accent/GeneKranzAtConsole.jpg"
                ,"Gene Kranz - At Console"
                ,"A picture of Gene Kranz looking intently at a console in NASA Mission Control"
                ,"NASA Image Archive"),

 "Calatrava Arts and Sciences":
   ImageGlossary("/_static/images/accent/CalatravaArtsAndSciences.jpg"
                ,"Valencia - City of Arts and Sciences"
                ,"The City of Arts and Sciences in Valencia - Santiago Calatrava"
                ,"Ralph Hempel"),

 "HAL 9000 Front Panel":
   ImageGlossary("/_static/images/accent/Hal_9000_Panel.jpg"
                ,"Hal-9000 Front Panel"
                ,"A picture of the Hal-9000 Front Panel From 2001: A Space Odyssey"
                ,"https://en.wikipedia.org/wiki/HAL_9000"),
 
"Wool Sheep":
   ImageGlossary("/_static/images/accent/WoolSheep.jpg"
                ,"Wool Sheeep"
                ,"Woolen sheep of various sizes in a wooden box with dividers"
                ,"Ralph Hempel"),

"787 Wing Load":
   ImageGlossary("/_static/images/accent/Boeing787WingStressTest.jpg"
                ,"Boeing 787 Wig Stress Test"
                ,"A Boeing 787 Wing is bending under extreme stress"
                ,"Boeing Image Repository"),

"Flight Director Emily Nelson":
   ImageGlossary("/_static/images/accent/FlightDirectorEmilyNelson.jpg"
                ,"Flight Director Emily Nelson"
                ,"ISS flight director Emily Nelson monitors data at her console in the space station flight control room in the Mission Control Center at NASA's Johnson Space Center during STS-132/ULF-4"
                ,"https://images.nasa.gov/details/jsc2010e081946"),

"GE Kitchen Hub Microwave":
   ImageGlossary("/_static/images/products/ge_kitchen_hub_microwave.jpg"
                ,"GE Kitchen Hub Microwave"
                ,"GE Kitchen Hub Microwave"
                ,"https://images.nasa.gov/details/jsc2010e081946"),

  }
