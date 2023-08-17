import subprocess

class GitHandler:
    def __init__(self):
        pass

    def clone_repository(self, repo_url):
        try:
            subprocess.check_output(['git', 'clone', repo_url])
            return "Repository cloned successfully."
        except subprocess.CalledProcessError as e:
            return str(e)

    def commit_changes(self, repo_path, commit_message):
        try:
            subprocess.check_output(['git', '-C', repo_path, 'add', '.'])
            subprocess.check_output(['git', '-C', repo_path, 'commit', '-m', commit_message])
            return "Changes committed successfully."
        except subprocess.CalledProcessError as e:
            return str(e)

    def push_changes(self, repo_path):
        try:
            subprocess.check_output(['git', '-C', repo_path, 'push'])
            return "Changes pushed successfully."
        except subprocess.CalledProcessError as e:
            return str(e)