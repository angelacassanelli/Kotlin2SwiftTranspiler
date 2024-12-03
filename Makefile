# Variabili
PYTHON = python3
ANTLR_DIR = antlr
SRC_DIR = src
TEST_DIR = tests
GRAMMAR = $(ANTLR_DIR)/Kotlin.g4
OUTPUT_DIR = generated

# Targets

.PHONY: all clean build test generate_antlr run

# Genera il parser ANTLR e costruisce il progetto
all: generate_antlr build

# Target per generare il codice ANTLR
generate_antlr:
	mkdir -p $(OUTPUT_DIR)
	antlr4 -Dlanguage=Python3 -o $(OUTPUT_DIR) $(GRAMMAR)

# Target per costruire il progetto
build:
	$(PYTHON) -m pip install -r requirements.txt
	echo "Project build complete!"

# Esegui i test unitari
test:
	$(PYTHON) -m unittest discover -s $(TEST_DIR)

# Esegui il transpiler
run:
	$(PYTHON) $(SRC_DIR)/Transpiler.py $(KOTLIN_FILE)

# Pulisci i file generati e di output
clean:
	rm -rf $(OUTPUT_DIR)
	rm -f *.pyc
	rm -rf __pycache__
