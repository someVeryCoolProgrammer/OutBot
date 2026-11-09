# Stands for: requirements windows
requirementsW = pip install pip install -r requirements/core.txt | pip install pip install -r requirements/developer.txt | pip install -r pip install -r requirements/tests.txt

# Stands for: requirements unix
requirementsU = pip3 install pip install -r requirements/core.txt | pip3 install pip install -r requirements/developer.txt | pip3 install -r pip install -r requirements/tests.txt

# Stands for: Python Interpreter Windows
PIW = python

# Stands for: Python Interpreter Unix
PIU = python3

# Stands for: install windows
installW:
	$(requirementsW)

# Stands for: install unix
installU:
	$(requiriementsU)

# Stands for run windows
runW:
	$(PIW) -m bot

# Stands for: run unix
runU:
	$(PIU) -m bot

# Stands for: venv  activate windows
venvAW:
	$(PIW) -m venv .venv

# Stands for: venv activate unix
venvAU:
	$(PIU) -m venv .venv

# Stands for: venv windows
venvW:
	.venv\Scripts\Activate.ps1

# Stands for: venv unix
venvAU:
	source .venv/bin/activate
