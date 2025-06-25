# --------------------------------------------------
# Atom class Test
# Author: ad2108
# Version: 1.0
# Date: 2025-02-24
# License: MIT
# --------------------------------------------------

import unittest
from proton_neutron_electron import Proton, Neutron, Electron
from atom import Atom
from periodic_table import PeriodicTable

class TestAtom(unittest.TestCase):
	lead = PeriodicTable.Pb()
	def test_charge(self):
		expected = 0
		actual = self.lead.charge()
		self.assertEqual(expected, actual)

	def test_mass(self):
		expected = 82 * Proton.mass() + 125 * Neutron.mass() + 82 * Electron.mass()
		actual = self.lead.mass()
		self.assertAlmostEqual(expected, actual)

	def test_shell_number(self):
		expected = 5
		actual = self.lead.shell_number()
		self.assertEqual(expected, actual)

	def test_outher_shell(self):
		expected = 22
		actual = self.lead.outher_shell()
		self.assertEqual(expected, actual)

# --------------------------------------------------
# End of file
# --------------------------------------------------

