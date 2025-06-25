# --------------------------------------------------
# Proton, Neutron and Electron class Test
# Author: ad2108
# Version: 1.0
# Date: 2025-02-24
# License: MIT
# --------------------------------------------------

import unittest
from proton_neutron_electron import Proton, Neutron, Electron

#Proton Value Test
class TestProton(unittest.TestCase):
	def test_charge(self):
		expected = 1
		actual = Proton.charge()
		self.assertEqual(expected, actual)

	def test_mass(self):
		expected = 1.007276466879

		actual = Proton.mass()
		self.assertEqual(expected, actual)

#Neutron Value Test
class TestNeutron(unittest.TestCase):
	def test_charge(self):
		expected = 0
		actual = Neutron.charge()
		self.assertEqual(expected, actual)

	def test_mass(self):
		expected = 1.00866491600
		actual = Neutron.mass()
		self.assertEqual(expected, actual)

#Electron Value Test
class TestElectron(unittest.TestCase):
	def test_charge(self):
		expected = -1
		actual = Electron.charge()
		self.assertEqual(expected, actual)

	def test_mass(self):
		expected = 5.4857990907E-4
		actual = Electron.mass()
		self.assertEqual(expected, actual)

# --------------------------------------------------
# End of file
# --------------------------------------------------

