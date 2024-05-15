build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

install:
	poetry install

brain-games:
	poetry run brain-games


lint:
	poetry run flake8 brain_games

even-game:
	poetry run brain-even

calc-game:
	poetry run brain-calc

gcd-game:
	poetry run brain-gcd

progression-game:
	poetry run brain-progression
