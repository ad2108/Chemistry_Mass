# --------------------------------------------------
# Atom class
# Author: ad2108
# Version: 1.0
# Date: 2025-02-24
# License: MIT
# --------------------------------------------------

from proton_neutron_electron import Proton, Neutron, Electron
from math import sqrt

class Atom:
	def __init__(self, protons, neutrons, electrons):
		self.protons = protons
		self.neutrons = neutrons
		self.electrons = electrons

	def __str__(self):
		return f'protons: {self.protons}, mass: {self.mass()}'

	def charge(self):
		pr_charge = self.protons * Proton.charge()
		nr_charge = self.neutrons * Neutron.charge()
		el_charge = self.electrons * Electron.charge()
		return pr_charge + nr_charge + el_charge

	def mass(self):
		pr_mass = self.protons * Proton.mass()
		nr_mass = self.neutrons * Neutron.mass()
		el_mass = self.electrons * Electron.mass()
		return pr_mass + nr_mass + el_mass

	def shells(self):
		electrons = self.electrons
		shell_number = 0
		
		while True:
			if electrons > 0:
				shell_number += 1
				electrons -= (2 * shell_number * shell_number)
			else:
				return [shell_number, electrons]
				break

	def shell_number(self):
		return self.shells()[0]

	def outher_shell(self):
		shells = self.shell_number()
		return (2 * shells * shells) - abs(self.shells()[1])

# --------------------------------------------------
# End of file
# --------------------------------------------------

