# --------------------------------------------------
# Molecule table
# Author: ad2108
# Version: 1.0
# Date: 2025-02-24
# License: MIT
# --------------------------------------------------

from molecule import Molecule
from periodic_table import PeriodicTable as PT

class ImportantMolecules:
	def Water():
		return Molecule([PT.H(), PT.O()], [2, 1])
	def AceticAcid():
		return Molecule([PT.C(), PT.H(), PT.O()], [2, 4, 2])
	def Acetone():
		return Molecule([PT.C(), PT.H(), PT.O()], [3, 6, 1])
	def Acetylene():
		return Molecule([PT.C(), PT.H()], [2, 2])
	def AcetylsalicylicAcid():
		return Molecule([PT.C(), PT.H(), PT.O()], [9, 8, 4])
	def Adenine():
		return Molecule([PT.C(), PT.H(), PT.N()], [5, 5, 5])
	def AdenosineTriphosphate():
		return Molecule([PT.C(), PT.H(), PT.N(), PT.O(), PT.P()],
										[10, 16, 5, 13, 3])
	def AdipicAcid():
		return Molecule([PT.C(), PT.H(), PT.O()], [6, 10, 4])
	def AluminumIIIOxide():
		return Molecule([PT.Al(), PT.O()], [2, 3])
	def Ammonia():
		return Molecule([PT.N(), PT.H()], [1, 3])
	def AscorbicAcid():
		return Molecule([PT.C(), PT.H(), PT.O()], [6, 8, 6])
	def Aspartame():
		return Molecule([PT.C(), PT.H(), PT.N(), PT.O()],
										[14, 18, 2, 5])
	def Benzene():
		return Molecule([PT.C(), PT.H()], [6, 6])
	def BenzoicAcid():
		return Molecule([PT.C(), PT.H(), PT.O()], [7, 6, 2])
	def Biphenyl():
		return Molecule([PT.C(), PT.H()], [12, 10])
	def Butane():
		return Molecule([PT.C(), PT.H()], [4, 10])
	def Butene():
		return Molecule([PT.C(), PT.H()], [4, 8])
	def ButyricAcid():
		return Molecule([PT.C(), PT.H(), PT.O()], [4, 8, 2])
	def Caffeine():
		return Molecule([PT.C(), PT.H(), PT.N(), PT.O()],
										[8, 10, 4, 2])
	def CalciumCarbonate():
		return Molecule([PT.Ca(), PT.C(), PT.O()], [1, 1, 3])
	def CalciumOxide():
		return Molecule([PT.Ca(), PT.O()], [1, 1])
	def CalciumSulfate():
		return Molecule([PT.Ca(), PT.S(), PT.O()], [1, 1, 4])
	def CarbonDioxide():
		return Molecule([PT.C(), PT.O()], [1, 2])
	def CarbonMonoxide():
		return Molecule([PT.C(), PT.O()], [1, 1])
	def Chloroform():
		return Molecule([PT.C(), PT.H(), PT.Cl()], [1, 1, 3])
	def Chlorophyll():
		return Molecule([PT.C(), PT.H(), PT.Mg(), PT.N(), PT.O()],
										[55, 72, 1, 4, 5])
	def Cholesterol():
		return Molecule([PT.C(), PT.H(), PT.O()], [27, 46, 1])
	def CitricAcid():
		return Molecule([PT.C(), PT.H(), PT.O()], [6, 8, 7])
	def Cocaine():
		return Molecule([PT.C(), PT.H(), PT.N(), PT.O()], 
										[17, 21, 1, 4])
	def Cytosine():
		return Molecule([PT.C(), PT.H(), PT.N(), PT.O()],
										[4, 5, 3, 1])
	def Thymine():
		return Molecule([PT.C, PT.H(), PT.N(), PT.O()],
										[6, 6, 2, 2])
	def Uracil():
		return Molecule([PT.C(), PT.H(), PT.N(), PT.O()],
										[4, 4, 2, 2])
	def DDT():
		return Molecule([PT.C(), PT.H(), PT.Cl()], [14, 9, 5])
	def DEET():
		return Molecule([PT.C(), PT.H(), PT.N(), PT.O()],
										[12, 17, 1, 1])
	def CFC12():
		return Molecule([PT.C(), PT.Cl(), PT.F()], [1, 2, 2])
	def Dopamine():
		return Molecule([PT.C(), PT.H(), PT.N(), PT.O()],
										[8, 11, 1, 2])
	def Adrenaline():
		return Molecule([PT.C(), PT.H(), PT.N(), PT.O()],
										[9, 13, 1, 3])
	def Ethane():
		return Molecule([PT.C(), PT.H()], [2, 6])
	def Ethene():
		return Molecule([PT.C(), PT.H()], [2, 4])
	def Ether():
		return Molecule([PT.C(), PT.H(), PT.O(), PT.C()],
										[2, 10, 1, 2])
	def Ethanol():
		return Molecule([PT.C(), PT.H(), PT.O()], [2, 6, 1])
	def EDTA():
		return Molecule([PT.C(), PT.H(), PT.N(), PT.O()],
										[10, 16, 2, 8])
	def Fluoxetine():
		return Molecule([PT.C(), PT.H(), PT.F(), PT.N(), PT.O()],
										[17, 18, 3, 1, 1])
	def Formaldehyde():
		return Molecule([PT.C(), PT.H(), PT.O()], [1, 2, 1])
	def FormicAdid():
		return Molecule([PT.C(), PT.H(), PT.O()], [1, 2, 2])
	def Glucose():
		return Molecule([PT.C(), PT.H(), PT.O()], [6, 12, 6])
	def Glycerin():
		return Molecule([PT.C(), PT.H(), PT.O()], [3, 8, 3])
	def Guanine():
		return Molecule([PT.C(), PT.H(), PT.N(), PT.O()],
										[5, 5, 5, 1])
	def HydrochloricAcid():
		return Molecule([PT.H(), PT.Cl()], [1, 1])
	def HydrogenPeroxide():
		return Molecule([PT.H(), PT.O()], [2, 2])
	def HydrogenSulfide():
		return Molecule([PT.H(), PT.S()], [2, 1])
	def Ibuprofen():
		return Molecule([PT.C(), PT.H(), PT.O()], [13, 18, 2])
	def Indigo():
		return Molecule([PT.C(), PT.H(), PT.N(), PT.O()],
										[16, 10, 2, 2])
	def Insulin():
		return Molecule([PT.C(), PT.H(), PT.N(), PT.O(), PT.S()],
										[257, 383, 65, 77, 6])
	def IronIIIOxide():
		return Molecule([PT.Fe(), PT.O()], [2, 3])
	def Isooctane():
		return Molecule([PT.C(), PT.H()], [8, 18])
	def Isoprene():
		return Molecule([PT.C(), PT.H()], [5, 8])
	def Methane():
		return Molecule([PT.C(), PT.H()], [1, 4])
	def Methanol():
		return Molecule([PT.C(), PT.H(), PT.O()], [1, 4, 1])
	def Ritalin():
		return Molecule([PT.C(), PT.H(), PT.N(), PT.O()],
										[14, 19, 1, 2])
	def Morphine():
		return Molecule([PT.C(), PT.H(), PT.N(), PT.O()],
										[17, 19, 1, 3])
	def Naphtalene():
		return Molecule([PT.C(), PT.H()], [10, 8])
	def Nicotine():
		return Molecule([PT.C(), PT.N(), PT.H()], [10, 14, 2])
	def NitricAcid():
		return Molecule([PT.H(), PT.N(), PT.O()], [1, 1, 3])
	def NitricDioxide():
		return Molecule([PT.N(), PT.O()], [1, 2])
	def NitrogenMonoxide():
		return Molecule([PT.N(), PT.O()], [1, 1])
	def DinitrogenOxide():
		return Molecule([PT.N(), PT.O()], [2, 1])
	def Nitroglycerin():
		return Molecule([PT.C(), PT.H(), PT.N(), PT.O()],
										[3, 5, 3, 9])
	def Norethidrone():
		return Molecule([PT.C(), PT.H(), PT.O()], [20, 26, 2])
	def Penicilin():
		return Molecule([PT.C(), PT.H(), PT.N(), PT.O(), PT.S()],
										[6, 18, 2, 4, 1])
	def Phenol():
		return Molecule([PT.C(), PT.H(), PT.O()], [6, 6, 1])
	def PhosphoricAcid():
		return Molecule([PT.H(), PT.P(), PT.O()], [3, 1, 4])
	def	Piperine():
		return Molecule([PT.C(), PT.H(), PT.N(), PT.O()],
										[17, 19, 1, 3])
	def PotassiumCarbonate():
		return Molecule([PT.K(), PT.C(), PT.O()], [2, 1, 3])
	def PotassiumNitrate():
		return Molecule([PT.K(), PT.N(), PT.O()], [1, 1, 3])
	def Propane():
		return Molecule([PT.C(), PT.H()], [3, 8])
	def Propylene():
		return Molecule([PT.C(), PT.H()], [3, 6])
	def Quinine():
		return Molecule([PT.C(), PT.H(), PT.N(), PT.O()],
										[20, 24, 2, 2])
	def Saccharin():
		return Molecule([PT.C(), PT.H(), PT.N(), PT.O(), PT.S()],
										[7, 5, 1, 3, 1])
	def SiliconDioxide():
		return Molecule([PT.Si(), PT.O()], [1, 2])
	def SodiumBicarbonate():
		return Molecule([PT.Na(), PT.H(), PT.C(), PT.O()],
										[1, 1, 1, 3])
	def SodiumCarbonate():
		return Molecule([PT.Na(), PT.C(), PT.O()], [2, 1, 3])
	def SodiumChloride():
		return Molecule([PT.Na(), PT.Cl()], [1, 1])
	def SodiumHydroxide():
		return Molecule([PT.Na, PT.O(), PT.H()], [1, 1, 1])
	def SodiumHypochloride():
		return Molecule([PT.Na(), PT.O(), PT.Cl()], [1, 1, 1])
	def Strychnine():
		return Molecule([PT.C(), PT.H(), PT.N(), PT.O()],
										[21, 22, 2, 2])
	def Styrene():
		return Molecule([PT.C(), PT.H()], [8, 8])
	def Sucrose():
		return Molecule([PT.C(), PT.H(), PT.O()], [12, 22, 11])
	def SulfuricAcid():
		return Molecule([PT.H(), PT.S(), PT.O()], [2, 1, 4])
	def Tetrafluorethylene():
		return Molecule([PT.C(), PT.F()], [2, 4])
	def THC():
		return Molecule([PT.C(), PT.H(), PT.O()], [21, 30, 2])
	def TNT():
		return Molecule([PT.C(), PT.H(), PT.N(), PT.O()],
										[7, 5, 3, 6])
	def Toluene():
		return Molecule([PT.C(), PT.H()], [7, 8])
	def TriuraniumOctaoxide():
		return Molecule([PT.U(), PT.O()], [3, 8])
	def Urea():
		return Molecule([PT.C(), PT.H(), PT.N(), PT.O()],
										[1, 4, 2, 1])
	def Vanillin():
		return Molecule([PT.C(), PT.H(), PT.O()], [8, 8, 3])
	def VinylChloride():
		return Molecule([PT.C(), PT.H(), PT.Cl()], [2, 3, 1])
	def Xylene():
		return Molecule([PT.C(), PT.H()], [8, 10])

# --------------------------------------------------
# End of file
# --------------------------------------------------

