$#!/bin/bash
MY_PORT=5000;
uvicorn main:app --reload --port $MY_PORT --host 0.0.0.0
