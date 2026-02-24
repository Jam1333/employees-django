#!/bin/bash

# Start Ollama in the background
/bin/ollama serve &

# Record Process ID
pid=$!

# Pause for Ollama to start (adjust sleep time if necessary)
sleep 5

echo "🔴 Retrieving gemma3:1b model..."
ollama pull gemma3:1b
echo "🟢 Done!"

# Wait for Ollama process to finish
wait $pid
