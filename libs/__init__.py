from redis import Redis


config = {
    'host': '10.0.0.48',
    'password': '123',
    'port': 6379,
    'db': '9',
    'decode_responses': True
}

rd_client = Redis(**config)

if __name__ == '__main__':
    rd_client.keys('*')
