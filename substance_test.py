# --------------------------------------------------
# Substance class Test
# Author: ad2108
# Version: 1.0
# Date: 2025-02-24
# License: MIT
# --------------------------------------------------

import unittest
from substance import Substance
from molecule_table import ImportantMolecules as IM

class TestSubstance(unittest.TestCase):
	vodka = Substance([IM.Water(), IM.Ethanol()], [61.3, 38.7])
	def test_charge(self):
		expected = 0
		actual = self.vodka.charge()
		self.assertEqual(expected, actual)

	def test_mass(self):
		expected = IM.Water().mass() * 0.613 + IM.Ethanol().mass() * 0.387
		actual = self.vodka.mass()
		self.assertAlmostEqual(expected, actual)

# --------------------------------------------------
# End of file
# --------------------------------------------------

