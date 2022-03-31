import pika
import os

url = os.environ.get('CLOUDAMQP_URL', 'amqps://ijceahck:hLUU6AI0OuWizdYd7GaCpooSI_lLJeAj@sparrow.rmq.cloudamqp.com/ijceahck')
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue='hello')

def callback(ch, method, properties, body):
    print(f" [x] Received {body.decode()}") # Вывод в консоль (вариант К)
    # Запись в файл (вариант Ф)
    with open('received_from_rabbitmq.txt', 'a') as f:
        f.write(f'{body.decode()}\n')

channel.basic_consume(queue='queue_1', on_message_callback=callback)

print(' [*] Waiting for messages:')
try:
    channel.start_consuming()
except KeyboardInterrupt:
    connection.close()