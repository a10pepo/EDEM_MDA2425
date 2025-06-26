import subprocess

def run_script(script_name):
    print(f"Ejecutando {script_name}...")
    result = subprocess.run(["python", script_name], capture_output=True, text=True)
    
    if result.returncode == 0:
        print(f"✅ {script_name} ejecutado con éxito")
        print(result.stdout)
    else:
        print(f"❌ Error al ejecutar {script_name}")
        print(result.stderr)

if __name__ == "__main__":
    scripts = ["test.py", "test_redshift.py", "redshift_etl.py"]
    for script in scripts:
        run_script(script)