run:
	@python -m uvicorn main:app --reload

create-migrations:
	@set PYTHONPATH=%PYTHONPATH:$(pwd) alembic revision --autoregenerate -m $(d)

run-migrations:
	@set PYTHONPATH=PYTHONPATH:$(pwd) alembic upgrade head