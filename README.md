# Documentation Chemistry Mass

This is a simple chemistry package. All of the code examples are made for IDLE.

## 1. Proton, Neutron and Electron

### 1.1 Proton

The proton class contains the charge and mass of a proton. This class does not take any arguments. This class has 2 methods:

```python
from proton_neutron_electron import Proton

Proton.charge() #returns 1
Proton.mass() #returns 1.007276466879
```

### 1.2 Neutron

The neutron class is like the proton class. It can be used the same. The values are different. Charge returns 0 and mass returns 1.008664916.

### 1.3 Electron

The electron class is very comparable. It returns a charge of -1 and a mass of 0.00054857990907.

## 2. Atom

### 2.1 Atom class

This class take the number of protons, neutrons and electrons to initialize.

```python
from atom import Atom

sodium = Atom(11, 11, 11)

sodium.charge() #returns 0
sodium.mass() #returns atomic mass (22.181389590668772)
sodium.shell_number() #returns number of shells (3)
sodium.outher_shell() #returns number of electrons in outer shell (1)
```

### 2.2 Periodic table

This file contains a major part of the elements in the periodic table. The standard chemical names are used for Atom declaration.

```python
from periodic_table import PeriodicTable as PT

lithium = PT.Li()
lead = PT.Pb()

#all atom methods can be used
lithium.charge() #returns 0
lead.mass() #returns 208.72476833662174
```

## 3. Molecule

### 3.1 Molecule class

This class takes lists of atoms and their numbers in a list.

```python
from molecule import Molecule
from periodic_table import PeriodicTable as PT

water = Molecule([PT.H(), PT.O()], [2, 1])
#the first list takes the atoms. The periodic table can be used
#the second take the amount of the atoms. H2O -> 2 * H, 1 * O

water.charge() #returns 0
water.mass() #returns the atomic mass of the molecule (17.1389048798807)
```

### 3.2 Molecule table

This is a list of common molecules.

```python
from molecule_table import ImportantMolecules as IM

ethanol = IM.Ethanol()
sulfuric_acid = IM.SulfuricAcid()

#this class can use all the molecule operations
ethanol.charge() #returns 0
sulfuric_acid.mass() #returns the atomic mass of the molecule (94.77250864340351)
```

## 4. Substance

### 4.1 Substance class

A substance is a mixture of molecules. It take a list of molecules and their percentages as input.

```python
from substance import Substance
from molecule_table import ImportantMolecules as IM

brine = Substance([IM.SodiumChloride(), IM.Water()], [3.5, 96.5])
#the first list contains the molecules salt(NaCl) and water (H2O)
#the second list contains the percentages of the molecules
#(3.5% salt and 96.5% water)

brine.mass() #returns 18.550506644677185
```

### 4.2 Substance table

Not implemented by now

## 5. Complex example

```python
#water with S04-2 Ions

from atom import Atom
from molecule import Molecule
from molecule_table import ImportantMolecules as IM
from substance import Substance

sulfur = Atom(16, 16, 16) #standart sulfur PT could also be used
oxygen = Atom(8, 7, 8)#standart oxygen PT could also be used
oxygen_1 = Atom(8, 7, 9) #special oxygen with one more electron
#this leads to it having a negative charge

oxygen_1.charge() #returns -1

so4_2 = Molecule([sulfur, oxygen, oxygen_1], [1, 2, 2])
#this Ion as a negative charge, because 2 oxygens have 1 electron more
#this makes the Ion negative

water_with_ions = Substance([IM.Water(), so4_2], [98.3 ,1.7])
#this is water that contains 98.3% water and 1.7% SO4-2 Ions

water_with_ions.mass() #returns 18.424428743986702
water_with_ions.charge() #returns -2
```

