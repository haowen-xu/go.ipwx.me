#!/bin/bash

HOST="${HOST:-0.0.0.0}"
PORT="${PORT:-8000}"
NUM_PROCESSES="${NUM_PROCESSES:-2}"
export PYTHONPATH="/app:$(pwd):${PYTHONPATH}"

gunicorn \
    -w "${NUM_PROCESSES}" \
    -b "${HOST}:${PORT}" \
    --worker-class sanic.worker.GunicornWorker \
    "go.application:app"
