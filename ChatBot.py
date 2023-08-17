import transformers
from CodeGenerator import CodeGenerator
from GitHandler import GitHandler
from DeploymentHandler import DeploymentHandler
from UIHandler import UIHandler

class ChatBot:
    def __init__(self):
        self.code_generator = CodeGenerator()
        self.git_handler = GitHandler()
        self.deployment_handler = DeploymentHandler()
        self.ui_handler = UIHandler()

    def start(self):
        while True:
            user_input = self.ui_handler.get_user_input()
            response = self.process_input(user_input)
            self.ui_handler.display_message(response)

    def process_input(self, input_text):
        if 'code' in input_text:
            return self.code_generator.generate_code(input_text)
        elif 'git' in input_text:
            if 'clone' in input_text:
                repo_url = input_text.split(' ')[-1]
                return self.git_handler.clone_repository(repo_url)
            elif 'commit' in input_text:
                commit_message = ' '.join(input_text.split(' ')[1:])
                return self.git_handler.commit_changes('.', commit_message)
            elif 'push' in input_text:
                return self.git_handler.push_changes('.')
        elif 'deploy' in input_text:
            app_path = input_text.split(' ')[-1]
            return self.deployment_handler.deploy_application(app_path)
        elif 'restart' in input_text:
            app_name = input_text.split(' ')[-1]
            return self.deployment_handler.restart_application(app_name)
        else:
            return "I'm sorry, I didn't understand that. Could you please rephrase?"