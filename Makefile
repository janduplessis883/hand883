install:
	@pip install -e .
	@echo "🌵 pip install -e . completed!"

clean:
	@echo "Cleaning up..."
	@rm -f */version.txt
	@rm -f .DS_Store
	@rm -f .coverage
	@rm -rf */.ipynb_checkpoints
	@rm -Rf build
	@rm -Rf dist # Added to remove the dist directory
	@rm -Rf *.egg-info # Added to remove egg-info directories
	@rm -Rf */__pycache__
	@rm -Rf */*.pyc
	@echo "🧽 Cleaned up successfully!"

all: install clean

app:
	@streamlit run hand883/interface/streamlit_app.py

git_merge:
	$(MAKE) lint
	@python hand883/automation/git_merge.py
	@echo "👍 Git Merge (master) successfull!"

git_push:
	$(MAKE) lint
	@python hand883/automation/git_push.py
	@echo "👍 Git Push (branch) successfull!"

test:
	@pytest -v tests

# Specify package name
lint:
	@black hand883/
