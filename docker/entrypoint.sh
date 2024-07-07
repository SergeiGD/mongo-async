#!/bin/sh

echo Migraiting data

python src/migrations.py || exit 1

echo Migrations is done

echo Starting app

uvicorn --reload --host 0.0.0.0 --port 8000 src.main:app