# --------------------------------------------------
# Molecule class
# Author: ad2108
# Version: 1.0
# Date: 2025-02-24
# License: MIT
# --------------------------------------------------

class Molecule:
	def __init__(self, atom_list, amount_list):
		self.atom_list = atom_list
		self.amount_list = amount_list

	def __str__(self):
		return f'atoms: {self.atom_list}\namount: {self.amount_list}'

	def charge(self):
		charge = 0
		for i in range(len(self.atom_list)):
			charge += self.atom_list[i].charge() * self.amount_list[i]
		return charge	

	def mass(self):
		mass = 0
		for i in range(len(self.atom_list)):
			mass += self.amount_list[i] * self.atom_list[i].mass()
		return mass

# --------------------------------------------------
# End of file
# --------------------------------------------------

