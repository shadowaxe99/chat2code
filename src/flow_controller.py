class FlowController:
    def __init__(self):
        # Initialize the flow controller
        self.flow_status = 'stopped'

    def start_flow(self):
        # Start the flow
        self.flow_status = 'started'
        print('Flow started')

    def stop_flow(self):
        # Stop the flow
        self.flow_status = 'stopped'
        print('Flow stopped')

    def get_flow_status(self):
        # Get the flow status
        return self.flow_status