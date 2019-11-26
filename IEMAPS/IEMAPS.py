#IE Maps Code

  #1st: Create the Hash tables with all the content for each building
pv = {"water_fountain": "floor 0",
      "drinks": "floor -1",
      "snacks": "floor -1",
      "coffee": "floor -1",
      "printers":"floor 0, floor 2",
      "study_tables":"floor -1",
      "pv101-102":"floor -1",
      "pv201-202":"floor 1",
      "pv301": "floor 2",
      "design_studio":"floor 0",
      "toilets":"floor -1, floor 0, floor 1, floor 2, floor 3",
      "professors":"floor -1",
      "degrees": "floor 2",
      "full_time_faculty_meeting_room":"floor 1",
      "teacher's_office":"floor 3",
      "mentorship_society":"floor 1"}

  #2nd: Create the guidance code for each building
    #Pedro de Valdivia
      #How have we proceeded?**
        #1. Ask for the building the person is interested in
        #2. Ask the user what they are looking for
        #3. If they are looking for food&drinks they will be asked what are they looking for
          # -vending_machine: if they are looking for a vending_machine they will be asked if they want:
            # *drinks
            # *snacks
            # *coffee
          # -water_fountain
        #4. If they are looking for other_buildings they will receive a link to a picture of a map that tells them how to go to the building they are looking for
        #5. If they are looking for a study_table they will get the floor where they are located
        #6. If they are looking for classrooms they will be given a list with all the classrooms in this building:
          # -pv101-102
          # -pv201-202
          # -pv301
          # -design_studio
        #7. If they are looking for toilets they will be given the floors where these are located
        #8. If they are looking for faculty_offices they will be given two options:
          # -Offices:
            # *Professors:
              # -Bernadette_Bullinger
              # -Isabel_de_Sivatte
              # -Maya_Kumar
              # -Mariano_Mastrogiorgio
              # -Andrew_Bertoli
              # -Daniel_Flynn
              # -Johanna_Glauber
              # -Stephanie_Lackner
              # -Carlos_Lastra
              # -Irene_Menéndez
            # *Degrees:
              # -Law_Office
              # -BBA_faculty
              # -International_Relations_Faculty_Office
              # -IE_Business_School_Humanities_Program
              # -Saudi_spanish_center_for_Islamic_Economics_and_Finance
            # *Services:
              # -full_time_faculty_meeting_room
              # -teacher's_office
              # -mentorship_society
        #9. If they are looking for printers they will be given the floors where these are located.
# Whenever they make a choice from one of the lists proposed to them, they will receive the floor where this choice is.
#After they have received the information they are looking for they will be asked if they are still looking for something else.
  # -If the program receives a yes, they will be given the option to ask for something else
  # -If the program receives a no, it will stop

from PIL import Image
import requests
from io import BytesIO
from urllib.request import urlopen
while True:
  building = input("Which building are you in <PV, MM31, MM31BIS, MM11, MM12, MM15, VE130, PINAR15, PINAR18, CP, SERR99, SERR105>? \n").upper()
  if ((building != "PV") and (building != "MM31") and (building != "MM31BIS") and (building != "MM11") and (building != "MM12") and (building != "MM15") and (building != "VE130") and (building != "PINAR15") and (building != "PINAR18") and (building != "CP") and (building != "SERR99") and (building != "SERR105")):
    print("Please enter one of the buildings")
  elif building == "PV":
    need = input("What are you looking for <food&drinks, other_buildings, study_tables, classrooms, toilets, faculty_offices, printers>?  \n").lower()
    # Food&drinks
    if need == "food&drinks":
      food_drinks = input("What are you looking for <vending_machine, water_fountain>?  \n").lower()
      if food_drinks == "vending_machine":
        vending_machineq = input("What are you looking for <drinks, snacks, coffee>?  \n").lower()
        if vending_machineq == "drinks":
          print("Go to", pv.get("drinks"))
        elif vending_machineq == "snacks":
          print("Go to", pv.get("snacks"))
        elif vending_machineq == "coffee":
          print("Go to", pv.get("coffee"))
        else:
          print("Option not available. Make sure you've typed the words as shown above.")
      elif food_drinks == "water_fountain":
        print("Go to", pv.get("water_fountain"))
      else:
          print("Option not available. Make sure you've typed the words as shown above.")

   # Other buildings
    elif need == "other_buildings":
      other_buildings = input("What are you looking for <mm31, mm31bis, mm11, mm12, mm15, ve130, pinar15, pinar18, cp, serr99, serr105>?  \n").lower()
      if other_buildings == "mm31":
        img_pv_mm31 = Image.open(urlopen('https://i.imgur.com/6IVV6LX.jpg'))
        img_pv_mm31 = img_pv_mm31.save("./img_pv_mm31.jpg")
        print("The image of the map has been saved in the repository.")
      elif other_buildings == "mm31bis":
        img_pv_mm31b = Image.open(urlopen('https://i.imgur.com/2Ec4OvA.jpg'))
        img_pv_mm31b =img_pv_mm31b.save("./img_pv_mm31b.jpg")
        print("The image of the map has been saved in the repository.")
      elif other_buildings == "mm11":
        img_pv_mm11 = Image.open(urlopen('https://i.imgur.com/1bas2h2.jpg'))
        img_pv_mm11 = img_pv_mm11.save("./img_pv_mm11.jpg")
        print("The image of the map has been saved in the repository.")
      elif other_buildings == "mm12":
        img_pv_mm12 = Image.open(urlopen('https://i.imgur.com/XtuNBdE.jpg'))
        img_pv_mm12 = img_pv_mm12.save("./img_pv_mm12.jpg")
        print("The image of the map has been saved in the repository.")
      elif other_buildings == "mm15":
        img_pv_mm15 = Image.open(urlopen('https://i.imgur.com/7WcIESG.jpg'))
        img_pv_mm15 = img_pv_mm15.save("./img_pv_mm15.jpg")
        print("The image of the map has been saved in the repository.")
      elif other_buildings == "ve130":
        img_pv_ve130 = Image.open(urlopen('https://i.imgur.com/3qONTYX.jpg'))
        img_pv_ve130 = img_pv_ve130.save("./img_pv_ve130.jpg")
        print("The image of the map has been saved in the repository.")
      elif other_buildings == "pinar15":
        img_pv_pinar15 = Image.open(urlopen('https://i.imgur.com/a6mh8d4.jpg'))
        img_pv_pinar15 = img_pv_pinar15.save("./img_pv_pinar15.jpg")
        print("The image of the map has been saved in the repository.")
      elif other_buildings == "pinar18":
        img_pv_pinar18 = Image.open(urlopen('https://i.imgur.com/4EpufIp.jpg'))
        img_pv_pinar18 = img_pv_pinar18.save("./img_pv_pinar18.jpg")
        print("The image of the map has been saved in the repository.")
      elif other_buildings == "cp":
        img_pv_cp = Image.open(urlopen('https://i.imgur.com/XgOfC8B.jpg'))
        img_pv_cp = img_pv_cp.save("./img_pv_cp.jpg")
        print("The image of the map has been saved in the repository.")
      elif other_buildings == "serr99":
        img_pv_serr99 = Image.open(urlopen('https://i.imgur.com/6nWSgns.jpg'))
        img_pv_serr99 = img_pv_serr99.save("./img_pv_serr99.jpg")
        print("The image of the map has been saved in the repository.")
      elif other_buildings == "serr105":
        img_pv_serr105 = Image.open(urlopen('https://i.imgur.com/XJMFHyl.jpg'))
        img_pv_serr105 = img_pv_serr105.save("./img_pv_serr105.jpg")
        print("The image of the map has been saved in the repository.")
      else:
          print("Option not available. Make sure you've typed the words as shown above.")

    # Study tables
    elif need == "study_tables":
      print("Go to", pv.get("study_tables"))

    # Classrooms
    elif need == "classrooms":
      classroomsq = input("What are you looking for <pv101-102, pv201-202, pv301, design_studio>?  \n").lower()
      if classroomsq == "pv101-102":
        print("Go to", pv.get("pv101-102"))
      elif classroomsq == "pv201-202":
        print("Go to", pv.get("pv201-202"))
      elif classroomsq == "pv301":
        print("Go to", pv.get("pv301"))
      elif classroomsq == "design_studio":
        print("Go to", pv.get("design_studio"))
      else:
          print("Option not available. Make sure you've typed the words as shown above.")

    # Toilets
    elif need == "toilets":
      print("Go to", pv.get("toilets")[0:35], "or to", pv.get("toilets")[37:44])

    # Faculty offices
    elif need == "faculty_offices":
      faculty_officesq = input("What are you looking for <offices, services>?  \n").lower()
      if faculty_officesq == "offices":
        officesq = input("What are you looking for <professors, degrees>?  \n").lower()
        if officesq == "professors":
          professors =  input("What are you looking for <Bernadette_Bullinger, Isabel_de_Sivatte, Maya_Kumar, Mariano_Mastrogiorgio, Andrew_Bertoli, Daniel_Flynn, Johanna_Glauber, Stephanie_Lackner, Carlos_Lastra, Irene_Menéndez>?  \n")
          print("Go to", pv.get("professors"))
        elif officesq == "degrees":
          degrees = input("What are you looking for <Law_Office, BBA_faculty, International_Relations_Faculty_Office, IE_Business_School_Humanities_Program, Saudi_spanish_center_for_Islamic_Economics_and_Finance>?  \n")
          print("Go to", pv.get("degrees"))
        else:
          print("Option not available. Make sure you've typed the words as shown above.")
      elif faculty_officesq == "services":
        servicesq = input("What are you looking for <full_time_faculty_meeting_room, teacher's_office, mentorship_society>?  \n").lower()
        if servicesq == "full_time_faculty_meeting_room" or services == "mentorship_society":
          print("Go to", pv.get("mentorship_society"))
        elif servicesq == "teacher's_office":
          print("Go to", pv.get("teacher's_office"))
        else:
          print("Option not available. Make sure you've typed the words as shown above.")
      else:
          print("Option not available. Make sure you've typed the words as shown above.")

    # Printers
    elif need == "printers":
      print("Go to", pv.get("printers")[0:7], "or to", pv.get("printers")[9:16])
    else:
      print("Option not available. Make sure you've typed the words as shown above.")
   #Preventing Errors
  elif ((building == "MM31") or (building == "MM31BIS") or (building == "MM11") or (building == "MM12") or (building == "MM15") or (building == "VE130") or (building == "PINAR15") or (building == "PINAR18") or (building == "CP") or (building == "SERR99") or (building == "SERR105")):
    print("Sorry building not available at the moment.")
   # Suggesting to run the program again
  cont = input("Do you want to look for something else <yes/no>?  \n").lower()
  if ((cont != "yes") and (cont != "no")):
    print("Please enter <yes> or <no>")
  while cont.lower() not in ("yes","no"):
      cont = input("Do you want to look for something else <yes/no>?  \n").lower()
  if cont == "no":
      break
