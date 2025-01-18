
set -e 


echo "Ejecutando ahorcado.py..."
python ahorcado.py

# Mantener el contenedor activo después de ejecutar los scripts
tail -f /dev/null