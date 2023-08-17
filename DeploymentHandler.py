import subprocess

class DeploymentHandler:
    def __init__(self):
        pass

    def deploy_application(self, app_path):
        try:
            subprocess.check_output(['deploy', app_path])
            return "Application deployed successfully."
        except subprocess.CalledProcessError as e:
            return str(e)

    def restart_application(self, app_name):
        try:
            subprocess.check_output(['restart', app_name])
            return "Application restarted successfully."
        except subprocess.CalledProcessError as e:
            return str(e)