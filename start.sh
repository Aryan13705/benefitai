#!/bin/bash
# BenefitAI — Start both backend and frontend servers
# Usage: bash start.sh

cd "$(dirname "$0")"   # always run from project root

echo "🚀 Starting BenefitAI..."
echo ""

# Kill anything already on ports 5002 and 3000
lsof -ti :5002 | xargs kill -9 2>/dev/null
lsof -ti :3000 | xargs kill -9 2>/dev/null
sleep 0.5

# Activate venv if present
if [ -f "venv/bin/activate" ]; then
  source venv/bin/activate
fi

# Start backend
echo "✅ Backend  → http://127.0.0.1:5002"
if [ -f "venv/bin/python3" ]; then
  venv/bin/python3 backend/app.py &
else
  python3 backend/app.py &
fi
BACKEND_PID=$!

# Wait for backend to be ready
sleep 2

# Start frontend
echo "✅ Frontend → http://localhost:3000"
(cd frontend && python3 -m http.server 3000) &
FRONTEND_PID=$!

echo ""
echo "Open your browser at: http://localhost:3000"
echo "Press Ctrl+C to stop both servers."

# Open browser automatically on macOS
if [[ "$OSTYPE" == "darwin"* ]]; then
  open http://localhost:3000
fi

# Wait for either to exit
wait $BACKEND_PID $FRONTEND_PID
