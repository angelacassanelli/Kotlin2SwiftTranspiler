# Variables
PYTHON = python3
ANTLR_DIR = antlr
SRC_DIR = src
TEST_DIR = tests
GRAMMAR = $(ANTLR_DIR)/Kotlin.g4
OUTPUT_DIR = generated

# Targets

.PHONY: all clean build test generate_antlr run

# Generate the ANTLR parser and build the project
all: generate_antlr build

# Target to generate the ANTLR code
generate_antlr:
	mkdir -p $(OUTPUT_DIR)
	antlr4 -Dlanguage=Python3 -o $(OUTPUT_DIR) $(GRAMMAR)

# Target to build the project
build:
	$(PYTHON) -m pip install -r requirements.txt
	echo "Project build complete!"

# Run the transpiler
run:
	$(PYTHON) $(SRC_DIR)/Transpiler.py $(KOTLIN_FILE)

# Clean the generated and output files
clean:
	rm -rf $(OUTPUT_DIR)
	rm -f *.pyc
	rm -rf __pycache__
