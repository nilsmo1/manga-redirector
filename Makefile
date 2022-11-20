install:
	@echo "Installing manga-redirector"
	sh INSTALL

clean:
	@echo "Removing json files.."
	rm -f name.json
	rm -f stored.json
