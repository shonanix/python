def get_host_ip():
    """
    查询本机ip地址
    :return:
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('8.8.8.8', 80))
    ip = s.getsockname()[0]
    s.close()
return ip


class KafkaMsgProducer:
    def __init__(self, server):
        self._server = server
        self.producer = None

    def connect(self):
        if self.producer is None:
            producer = KafkaProducer(bootstrap_servers=self._server)
            self.producer = producer

    def close(self):
        if self.producer is not None:
            self.producer.close()
            self.producer = None

    def send(self, topic, msg):
        if self.producer is not None:
            if not isinstance(msg, bytes):
                msg = msg.encode("utf-8")  # 将str类型转换为bytes类型
            self.producer.send(topic=topic, value=msg)
 

if __name__ == '__main__':            
    producer = KafkaMsgProducer(rf"{self.kafka_ip}:{self.kafka_port}")
    producer.connect()
    topic = "serviceheartbeat"
    msg = {
                "hostname": host,
                "ip": get_host_ip(),
                "port": port,
                "update_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S+08"),
                "flag": True
        }
    producer.send(topic=topic, msg=str(msg))
