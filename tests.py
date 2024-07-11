import unittest
from redis import Redis
from pydapter import RedisAdapterSingle  # Assume the class is in redis_adapter_single.py

class TestRedisAdapterSingle(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Initialize Redis connection for testing (using a test database)
        cls.redis = Redis(host='localhost', port=6379, db=15)
        cls.redis.flushdb()  # Clear the database before starting tests
        cls.adapter = RedisAdapterSingle(base_key='test', connection_string='redis://localhost:6379/15')

    def test_set_and_get_value(self):
        self.adapter.set_value('test_key', 'hello')
        result = self.adapter.get_value('test_key')
        self.assertEqual(result.decode('utf-8'), 'hello')

    def test_device_management(self):
        self.adapter.set_device('device1')
        devices = self.adapter.get_devices()
        self.assertIn('device1', devices)
        self.adapter.clear_devices(['device1'])
        devices_after_clear = self.adapter.get_devices()
        self.assertNotIn('device1', devices_after_clear)

    def test_stream_functions(self):
        data = {'field1': 'value1', 'field2': 'value2'}
        self.adapter.stream_write(data, '*', 'test_stream')
        results = self.adapter.stream_read('test_stream', '-', '+', 2)
        self.assertTrue(len(results) > 0)
        self.assertIn('value1', results[0][1].values())

    def test_hash_functions(self):
        hash_data = {'field1': 'value1', 'field2': 'value2'}
        self.adapter.set_hash('test_hash', hash_data)
        fetched_hash = self.adapter.get_hash('test_hash')
        self.assertEqual(fetched_hash[b'field1'], b'value1')

    def test_set_operations(self):
        self.adapter.set_set('test_set', 'value1')
        result = self.adapter.get_set('test_set')
        self.assertIn('value1', result)

    def test_publish_subscribe(self):
        # This test assumes presence of a subscriber client or mock
        pass  # Implement if a subscription mechanism or mock is available

    @classmethod
    def tearDownClass(cls):
        cls.redis.flushdb()  # Clean up the database after tests
        cls.redis.close()

if __name__ == '__main__':
    unittest.main()

