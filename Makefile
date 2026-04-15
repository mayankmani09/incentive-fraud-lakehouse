.PHONY: bootstrap up down seed demo lint test dbt-run quality explain deploy-dev

bootstrap:
	bash scripts/bootstrap_local.sh

up:
	docker compose up -d --build

down:
	docker compose down -v

seed:
	PYTHONPATH=src python scripts/seed_reference_data.py
	PYTHONPATH=src python scripts/generate_demo_events.py

demo:
	bash scripts/run_demo.sh

lint:
	ruff check src tests jobs dags
	sqlfluff lint dbt/models

test:
	PYTHONPATH=src pytest -q

dbt-run:
	bash scripts/run_dbt.sh

quality:
	bash scripts/run_quality_checks.sh

explain:
	PYTHONPATH=src python -m incentive_fraud.ai.explain_claim --claim-id $(CLAIM_ID)

deploy-dev:
	@echo "See terraform/environments/dev and .github/workflows/deploy.yml"
