# --------------------------------------------------
# Substance class
# Author: ad2108
# Version: 1.0
# Date: 2025-02-24
# License: MIT
# --------------------------------------------------

from molecule import Molecule

class Substance:
	def __init__(self, molecule_list, percent_list):
		self.molecule_list = molecule_list
		self.percent_list = percent_list

	def charge(self):
		charge = 0
		for i in range(len(self.molecule_list)):
			charge += self.molecule_list[i].charge() * self.percent_list[i] / 100
		return charge

	def mass(self):
		atomic_mass = 0
		percent = 0
		for i in range(len(self.molecule_list)):
			percent += self.percent_list[i] / 100
			atomic_mass += self.molecule_list[i].mass() * self.percent_list[i] / 100
		if percent <= 1:
			return atomic_mass
		else:
			return "Over 100% given!"
 
# --------------------------------------------------
# End of file
# --------------------------------------------------
	
