import os
from jupyter_server.auth import passwd

# Function to change the Jupyter password
def change_jupyter_password(new_password):
    hashed_password = passwd(new_password)
    config_file = '/root/.jupyter/jupyter_server_config.py'

    with open(config_file, 'r') as file:
        lines = file.readlines()

    with open(config_file, 'w') as file:
        for line in lines:
            if line.startswith("c.ServerApp.password"):
                file.write(f"c.ServerApp.password = u'{hashed_password}'\n")
            else:
                file.write(line)

    print("Password changed successfully. Restarting Jupyter server...")

    # Restart the Jupyter server
    os.system("supervisorctl restart jupyterlab")

# Input prompt for the new password
new_password = input("Enter new Jupyter password: ")
change_jupyter_password(new_password)
