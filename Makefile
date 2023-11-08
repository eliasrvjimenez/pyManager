default:
	pip install -r requirements.txt
	python3 generate_default_settings.py
	python3 setup.py
	python3 FileOrganizer.py