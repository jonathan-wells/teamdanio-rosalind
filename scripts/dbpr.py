#!/usr/bin/env python3

from Bio import ExPASy
from Bio import SwissProt

handle = ExPASy.get_sprot_raw('Q5SLP9')
# record = SwissProt.read(handle)

print(handle.read())
