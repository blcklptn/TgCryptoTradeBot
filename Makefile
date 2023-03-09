dev:
	cd SourceFiles && poetry run python3 __main__.py

clean:
	find . -type d -name __pycache__ -exec rm -r {} \+ && find . -name ".DS_Store" -delete

install-requirements:
	poetry install

vars:
	export $(grep -v '^#' .env | xargs)

docker:
	docker compose --env-file .env up

new_vars:
	export $(xargs < .env)