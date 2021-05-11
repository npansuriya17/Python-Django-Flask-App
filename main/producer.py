import pika, json

params = pika.URLParameters('amqps://dhjfkjnk:27zj5yp9OGMVMYzWzHS-qrCvSLxABvBv@baboon.rmq.cloudamqp.com/dhjfkjnk')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='admin', body=json.dumps(body), properties=properties)
