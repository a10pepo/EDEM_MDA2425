#!/bin/bash

export PATH=/usr/local/bin:/usr/bin:/bin
export PYTHONPATH=/app

echo "PROJECT_ID=$PROJECT_ID"
echo "POSTGRES_IP=$POSTGRES_IP"
echo "GOOGLE_APPLICATION_CREDENTIALS=$GOOGLE_APPLICATION_CREDENTIALS"

PYTHON_BIN="/usr/local/bin/python"

echo "[$(date)] Running analytical_layer.el_delivery.main..."
$PYTHON_BIN -m analytical_layer.el_delivery.main

echo "[$(date)] Running analytical_layer.el_orders.main..."
$PYTHON_BIN -m analytical_layer.el_orders.main
