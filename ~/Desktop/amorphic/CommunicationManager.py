import pika

class CommunicationManager:

    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        self.channel = self.connection.channel()

    def send_message(self, queue, message):
        self.channel.queue_declare(queue=queue)
        self.channel.basic_publish(exchange='', routing_key=queue, body=message)
        print(f'Sent: {message}')

    def receive_message(self, queue):
        def callback(ch, method, properties, body):
            print(f'Received: {body}')

        self.channel.queue_declare(queue=queue)
        self.channel.basic_consume(queue=queue, on_message_callback=callback, auto_ack=True)
        self.channel.start_consuming()