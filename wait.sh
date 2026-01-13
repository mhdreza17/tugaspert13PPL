#!/bin/sh
echo "Waiting for Selenium Hub..."
for i in $(seq 1 30); do
  if curl -s http://localhost:4444/wd/hub/status | grep -q "ready"; then
    echo "Selenium Hub is ready!"
    exit 0
  fi
  sleep 2
done
echo "Selenium Hub not ready (timeout)"
exit 1
