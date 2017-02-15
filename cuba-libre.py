import sys
import cmd
import random
import shutil

try:
    import cPickle as pickle
except:
    import pickle
import os.path


class Insurgent:
    name = ""
    resources = 0
    availableBases = 0
    availableForces = 0
    eligible = True

    def __init__(self, name, resources, availableBases, availableForces, eligible):
        self.name = name
        self.resources = resources
        self.availableBases = availableBases
        self.availableForces = availableForces
        self.eligible = eligible

    def __repr__(self):
        if self.eligible:
            return "%s\nResources: %d\nAvailable Bases: %d\nAvailable Guerrillas: %d\n" \
                   "The %s is currently eligible." % (self.name, self.resources,
                                                            self.availableBases, self.availableForces, self.name)
        else:
            return "%s\nResources: %d\nAvailable Bases: %d\nAvailable Guerrillas: %d\n" \
                   "The %s is not currently eligible." % (self.name, self.resources,
                                                            self.availableBases, self.availableForces, self.name)


class CounterInsurgent:
    name = ""
    resources = 0
    availableBases = 0
    availableTroops = 0
    availablePolice = 0
    eligible = True

    def __init__(self, name, resources, availableBases, availableTroops, availablePolice, eligible):
        self.name = name
        self.resources = resources
        self.availableBases = availableBases
        self.availableTroops = availableTroops
        self.availablePolice = availablePolice
        self.eligible = eligible

    def __repr__(self):
        if self.eligible:
            return "%s\nResources: %d\nAvailable Bases: %d\nAvailable Troops: %d\nAvailable Police: %d\
            \nThe %s is currently eligible." % (self.name, self.resources, self.availableBases,
                                              self.availableTroops, self.availablePolice, self.name)
        else:
            return "%s\nResources: %d\nAvailable Bases: %d\nAvailable Troops: %d\nAvailable Police: %d\
            \nThe %s is not currently eligible." % (self.name, self.resources, self.availableBases,
                                              self.availableTroops, self.availablePolice, self.name)

class MapSpace():
    name = ""
    type = ""
    links = []
    population = 0
    supportVsOpposition = 0
    control = ""
    openCasinos = 0
    closedCasinos = 0
    syndicateUndergroundGuerrillas = 0
    syndicateActiveGuerrillas = 0
    govtBases = 0
    troops = 0
    police = 0
    m26Bases = 0
    m26UndergroundGuerrillas = 0
    m26ActiveGuerrillas = 0
    drBases = 0
    drUndergroundGuerrillas = 0
    drActiveGuerrillas = 0
    terrorMarkers = 0
    sabotage = False

    def __init__(self, name, type, links, population, supportVsOpposition, control, openCasinos, closedCasinos, syndicateUndergroundGuerrillas,
                 syndicateActiveGuerrillas, govtBases, troops, police, m26Bases, m26UndergroundGuerrillas, m26ActiveGuerrillas, drBases,
                 drUndergroundGuerrillas, drActiveGuerrillas, terrorMarkers, sabotage):
        self.name = name
        self.type = type
        self.links = links
        self.population = population
        self.supportVsOpposition = supportVsOpposition
        self.control = control
        self.openCasinos = openCasinos
        self.closedCasinos = closedCasinos
        self.syndicateUndergroundGuerrillas = syndicateUndergroundGuerrillas
        self.syndicateActiveGuerrillas = syndicateActiveGuerrillas
        self.govtBases = govtBases
        self.troops = troops
        self.police = police
        self.m26Bases = m26Bases
        self.m26UndergroundGuerrillas = m26UndergroundGuerrillas
        self.m26ActiveGuerrillas = m26ActiveGuerrillas
        self.drBases = drBases
        self.drUndergroundGuerrillas = drUndergroundGuerrillas
        self.drActiveGuerrillas = drActiveGuerrillas
        self.terrorMarkers = terrorMarkers
        self.sabotage = sabotage
        
    def printMapSpace(self):
        print self.name
        print self.getSupVsOpp()
        if self.control != "":
            print "Control: " + self.control
        if self.openCasinos > 0:
            print "Open Casinos: " + str(self.openCasinos)
        if self.closedCasinos > 0:
            print "Closed Casinos: " + str(self.closedCasinos)
        if self.syndicateUndergroundGuerrillas > 0:
            print "Underground Syndicate Guerrillas: " + str(self.syndicateUndergroundGuerrillas)
        if self.syndicateActiveGuerrillas > 0:
            print "Active Syndicate Guerrillas: " + str(self.syndicateActiveGuerrillas)
        if self.govtBases > 0:
            print "Government Bases: " + str(self.govtBases)
        if self.troops > 0:
            print "Troops: " + str(self.troops)
        if self.police > 0:
            print "Police: " + str(self.police)
        if self.m26Bases > 0:
            print "M26July Bases: " + str(self.m26Bases)
        if self.m26UndergroundGuerrillas > 0:
            print "Underground M26July Guerrillas: " + str(self.m26UndergroundGuerrillas)
        if self.m26ActiveGuerrillas > 0:
            print "Active M26July Guerrillas: " + str(self.m26ActiveGuerrillas)
        if self.drBases > 0:
            print "Directorio Bases: " + str(self.drBases)
        if self.drUndergroundGuerrillas > 0:
            print "Underground Directorio Guerrillas: " + str(self.drUndergroundGuerrillas)
        if self.drActiveGuerrillas > 0:
            print "Active Directorio Guerrillas: " + str(self.drActiveGuerrillas)
        if self.terrorMarkers > 0:
            print "Terror Markers: " + str(self.terrorMarkers)
        if self.sabotage:
            print "Sabotage Marker: Yes"

    def __repr__(self):
        if self.sabotage:
            return "%s\nType: %s\nAdjacent to: %s\nPopulation: %d\nCurrent Support/Opposition: %s\nControl: %s\nOpen Casinos: %d\nClosed Casinos: %d\
        \nSyndicate Underground Guerrillas: %d\nSyndicate Active Guerrillas: %d\nGovernment Bases: %d\nGovernment Troops: %d\nGovernment Police: %d\
        \nM26July Bases: %d\nM26July Underground Guerrillas: %d\nM26July Active Guerrillas: %d\nDirectorio Bases: %d\nDirectorio Underground Guerrillas: %d\
        \nDirectorio Active Guerrillas: %d\nTerror Markers: %d\nSabotage Marker: Yes" % (self.name, self.type, self.links, self.population, self.getSupVsOpp(),
                                                                                         self.control, self.openCasinos, self.closedCasinos,
                                                                                         self.syndicateUndergroundGuerrillas, self.syndicateActiveGuerrillas,
                                                                                         self.govtBases, self.troops, self.police, self.m26Bases,
                                                                                         self.m26UndergroundGuerrillas, self.m26ActiveGuerrillas,
                                                                                         self.drBases, self.drUndergroundGuerrillas, self.drActiveGuerrillas,
                                                                                         self.terrorMarkers)
        else:
            return "%s\nType: %s\nAdjacent to: %s\nPopulation: %d\nCurrent Support/Opposition: %s\nControl: %s\nOpen Casinos: %d\nClosed Casinos: %d\
        \nSyndicate Underground Guerrillas: %d\nSyndicate Active Guerrillas: %d\nGovernment Bases: %d\nGovernment Troops: %d\nGovernment Police: %d\
        \nM26July Bases: %d\nM26July Underground Guerrillas: %d\nM26July Active Guerrillas: %d\nDirectorio Bases: %d\nDirectorio Underground Guerrillas: %d\
        \nDirectorio Active Guerrillas: %d\nTerror Markers: %d\nSabotage Marker: No" % (self.name, self.type, self.links, self.population, self.getSupVsOpp(),
                                                                                         self.control, self.openCasinos, self.closedCasinos,
                                                                                         self.syndicateUndergroundGuerrillas, self.syndicateActiveGuerrillas,
                                                                                         self.govtBases, self.troops, self.police, self.m26Bases,
                                                                                         self.m26UndergroundGuerrillas, self.m26ActiveGuerrillas,
                                                                                         self.drBases, self.drUndergroundGuerrillas, self.drActiveGuerrillas,
                                                                                         self.terrorMarkers)

    def getSupVsOpp(self):
        if self.supportVsOpposition == 2:
            return "Active Support"
        elif self.supportVsOpposition == 1:
            return "Passive Support"
        elif self.supportVsOpposition == 0:
            return "Neutral"
        elif self.supportVsOpposition == -1:
            return "Passive Opposition"
        else:
            return "Active Opposition"

class Card():
    number = 0
    name = ""
    factionOrder = []

    def __init__(self, number, name, factionOrder):
        self.number = number
        self.name = name
        self.factionOrder = factionOrder

    def playEvent(self):
        pass


#change to a cmd class?
class CubaLibre():
    
    map = {}
    mapSetup()
    
    def mapSetup():
      map["Pinar del Rio"] = MapSpace("Pinar del Rio", "Forest", ["Economic Center 1", "La Habana"], 1, 2, "Syndicate", 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, False)
      map["Havana"] = MapSpace("Havana", "City", ["La Habana"], 6, 2, "Government", 1, 0, 0, 0, 0, 6, 4, 0, 0, 0, 0, 2, 0, 0, False)
      map["Economic Center 1"] = MapSpace("Economic Center 1", "Economic Center", ["Pinar del Rio", "La Habana"], 3, 0, "None", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, False)
      map["La Habana"] = MapSpace("La Habana", "Grassland", ["Pinar del Rio", "Economic Center 1", "Havana", "Matanzas"], 1, 1, "None", 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, False)
      map["Matanzas"] = MapSpace("Matanzas", "Grassland", ["La Habana", "Las Villas"], 1, 1, "None", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, False)
      map["Las Villas"] = MapSpace("Las Villas", "Mountain", ["Matanzas", "Economic Center 2", "Camaguey (Province)"], 2, 0, "Government", 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, False)
      map["Economic Center 2"] = MapSpace("Economic Center 2", "Economic Center", ["Las Villas", "Camaguey (Province)"], 3, 0, "None", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, False)
      map["Camaguey (Province)"] = MapSpace("Camaguey (Province)", "Forest", ["Las Villas", "Economic Center 2", "Camaguey (City)", "Oriente"], 1, -1, "Directorio", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, False)
      map["Camaguey (City"] = MapSpace("Camaguey (City", "City", ["Camaguey (Province"], 1, 1, "Government", 0, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 0, False)
      map["Oriente"] = MapSpace("Oriente", "Forest", ["Camaguey (Province)", "Economic Center 3", "Sierra Maestra"], 2, -1, "None", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, False)
      map["Economic Center 3"] = MapSpace("Economic Center 3", "Economic Center", ["Oriente", "La Sierra Maestra"], 2, 0, "None", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, False)
      map["Sierra Maestra"] = MapSpace("Sierra Maestra", "Mountain", ["Oriente", "Economic Center 3", "Santiago de Cuba"], 1, -2, "M26July", 0, 0, 0, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0, False)
      map["Santiago de Cuba"] = MapSpace("Santiago de Cuba", "City", ["Sierra Maestra"], 1, 0, "Government", 0, 0, 0, 0, 0, 2, 2, 0, 1, 0, 0, 0, 0, 0, False)
    

#Faction Setup
government = CounterInsurgent("Government", 15, 2, 15, 15, True)
syndicate = Insurgent("Syndicate", 15, 10, 6, True)
m26july = Insurgent("M26July", 10, 4, 15, True)
directorio = Insurgent("Directorio", 5, 4, 15, True)

#Add markers setup (support totals, bases, etc. CASH Markers available, US Alliance


#edit available forces after mapsetup



#prints full mapstate
def printMap(self):
    for i in self:
        print self[i]
        raw_input("Press Enter to Continue")
        print
