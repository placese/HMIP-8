import pika
import os
from pika.exchange_type import ExchangeType
 
url = 'amqps://ijceahck:kpl906ISe1_aW0mHoJJkJFNKqpchLdRy@sparrow.rmq.cloudamqp.com/ijceahck'
password = 'hLUU6AI0OuWizdYd7GaCpooSI_lLJeAj'

url = os.environ.get('CLOUDAMQP_URL', 'amqps://ijceahck:hLUU6AI0OuWizdYd7GaCpooSI_lLJeAj@sparrow.rmq.cloudamqp.com/ijceahck')

params = pika.URLParameters(url)
params.socket_timeout = 5
connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue='queue_1')
channel.exchange_declare(exchange='queue_1', exchange_type=ExchangeType.direct)
channel.queue_bind(queue='queue_1', exchange='queue_1', routing_key='hello')

# try:
    # while True:
channel.basic_publish(exchange='queue_1',
                      routing_key='hello',
                      body='HumanMachine')
# except (KeyboardInterrupt, SystemExit):
connection.close()
    


