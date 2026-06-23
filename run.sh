#!/bin/bash

echo "Starting backend"
uvicorn src.main:app --reload &
BACKEND_PID=$!

echo "Starting frontend"
cd src/frontend
npm run dev &
FRONTEND_PID=$!

wait $BACKEND_PID $FRONTEND_PID