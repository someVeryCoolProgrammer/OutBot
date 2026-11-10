# Stands for: Requirements Windows Core
requirementsWC = pip install -r requirements/core.txt

# Stands for: Requirements Windows Developer 
requirementsWD = pip install -r requirements/developer.txt

# Stands for: Requirements Windows Tests 
requirementsWT = pip install -r requirements/tests.txt

# Stands for: Requirements Unix Core
requirementsUC = pip3 install -r requirements/core.txt

# Stands for: Install Unix Developer 
requirementsUD = pip3 install -r requirements/developer.txt

# Stands for: Install Unix Tests
requirementsUT = pip3 install -r requirements/tests.txt

# Stands for: Python Interpreter Windows
PIW = python

# Stands for: Python Interpreter Unix
PIU = python3

# Stands for: Install Windows
installW:
    # Stands for: Requirements Windows Core 
	$(requirementsWC)
    
    # Stands for: Requirements Windows Developer 
	$(requirementsWD)
    
    # Stands for: Requirements Windows Test 
	$(requirementsWT)

# Stands for: Install Unix
installU:

    # Stands for: Install Unix Core
	$(requirementsUC)

    # Stands for: Install Unix Developer
	$(requirementsUD)

    # Stands for: Install Unix Tests
	$(requirementsUT)

# Stands for: Run Windows
runW:
	$(PIW) -m bot

# Stands for: Run Unix
runU:
	$(PIU) -m bot

