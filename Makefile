# Makefile

.PHONY: generate cleanup

generate:
    @echo "Generating data..."
    @python generate_data.py
    @echo "Data generation complete."

cleanup:
    @echo "Running cleanup tasks..."
    @rm -f temp_data.txt
    @echo "Cleanup complete."
