# Stands for: Requirements Windows
requirementsW := pip install pip install -r requirements/core.txt 
prequirements += Wip install pip install -r requirements/developer.txt 
requirementsW += pip install -r pip install -r requirements/tests.txt

# Stands for: Requirements Unix
requirementsU := pip3 install pip install -r requirements/core.txt && pip3 install pip install -r requirements/developer.txt && pip3 install -r pip install -r requirements/tests.txt

# Stands for: Python Interpreter Windows
PIW = python

# Stands for: Python Interpreter Unix
PIU = python3

# Stands for: Install Windows
installW:
	$(requirementsW)

# Stands for: Install Unix
installU:
	$(requirementsU)

# Stands for Run Windows
runW:
	$(PIW) -m bot

# Stands for: Run Unix
runU:
	$(PIU) -m bot

