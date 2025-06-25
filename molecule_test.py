# --------------------------------------------------
# Molecule class Test
# Author: ad2108
# Version: 1.0
# Date: 2025-02-24
# License: MIT
# --------------------------------------------------

import unittest
from atom import Atom
from periodic_table import PeriodicTable as PT
from molecule import Molecule
from molecule_table import ImportantMolecules as IM

class TestMolecule(unittest.TestCase):
	ethanol = IM.Ethanol()
	so4_2 = Molecule([Atom(16, 16, 18), PT.O()], [1, 4])

	def test_charge(self):
		expected = -2
		actual = self.so4_2.charge()
		self.assertEqual(expected, actual)

	def test_mass(self):
		expected = PT.C().mass() * 2 + PT.H().mass() * 6 + PT.O().mass()
		actual = self.ethanol.mass()
		self.assertAlmostEqual(expected, actual)

# --------------------------------------------------
# End of file
# --------------------------------------------------

