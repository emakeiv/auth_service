#!/bin/bash


uvicorn src.api.server:app --reload --host 0.0.0.0 --port 8080