#!/bin/bash

echo "MUSE - Run Script"
echo "=================="

if [ "$1" == "dev" ]; then
    echo "Starting development environment..."
    docker-compose up -d
    echo "API running at http://localhost:8000"
    echo "API docs at http://localhost:8000/docs"
elif [ "$1" == "stop" ]; then
    echo "Stopping containers..."
    docker-compose down
elif [ "$1" == "logs" ]; then
    echo "Showing logs..."
    docker-compose logs -f
elif [ "$1" == "restart" ]; then
    echo "Restarting containers..."
    docker-compose restart
else
    echo "Usage: ./scripts/run.sh [dev|stop|logs|restart]"
fi
