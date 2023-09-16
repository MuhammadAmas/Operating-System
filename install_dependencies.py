import subprocess


def install_dependencies():
    try:
        subprocess.check_call(["pip", "install", "tabulate", "prettytable"])
        print("Dependencies installed successfully.")
    except subprocess.CalledProcessError:
        print("Error installing dependencies.")


install_dependencies()
