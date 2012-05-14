# -*- coding: utf-8 -*-

from shove._compat import unittest


class TestSimpleCache(unittest.TestCase):

    initstring = 'simple://'

    def setUp(self):
        from shove.cache.core import SimpleCache
        self.cache = SimpleCache(self.initstring)

    def tearDown(self):
        self.cache = None

    def test_getitem(self):
        self.cache['test'] = 'test'
        self.assertEqual(self.cache['test'], 'test')

    def test_setitem(self):
        self.cache['test'] = 'test'
        self.assertEqual(self.cache['test'], 'test')

    def test_delitem(self):
        self.cache['test'] = 'test'
        del self.cache['test']
        self.assertEqual('test' in self.cache, False)

    def test_get(self):
        self.assertEqual(self.cache.get('min'), None)

    def test_timeout(self):
        import time
        from shove.cache.core import SimpleCache
        cache = SimpleCache(self.initstring, timeout=1)
        cache['test'] = 'test'
        time.sleep(1)

        def tmp():
            cache['test']
        self.assertRaises(KeyError, tmp)

    def test_cull(self):
        from shove.cache.core import SimpleCache
        cache = SimpleCache(self.initstring, max_entries=1)
        cache['test'] = 'test'
        cache['test2'] = 'test'
        cache['test2'] = 'test'
        self.assertEquals(len(cache), 1)


class TestMemoryCache(unittest.TestCase):

    initstring = 'memory://'

    def setUp(self):
        from shove.cache.core import MemoryCache
        self.cache = MemoryCache(self.initstring)

    def tearDown(self):
        self.cache = None

    def test_getitem(self):
        self.cache['test'] = 'test'
        self.assertEqual(self.cache['test'], 'test')

    def test_setitem(self):
        self.cache['test'] = 'test'
        self.assertEqual(self.cache['test'], 'test')

    def test_delitem(self):
        self.cache['test'] = 'test'
        del self.cache['test']
        self.assertEqual('test' in self.cache, False)

    def test_get(self):
        self.assertEqual(self.cache.get('min'), None)

    def test_timeout(self):
        import time
        from shove.cache.core import MemoryCache
        cache = MemoryCache(self.initstring, timeout=1)
        cache['test'] = 'test'
        time.sleep(1)

        def tmp():
            cache['test']
        self.assertRaises(KeyError, tmp)

    def test_cull(self):
        from shove.cache.core import MemoryCache
        cache = MemoryCache(self.initstring, max_entries=1)
        cache['test'] = 'test'
        cache['test2'] = 'test'
        cache['test2'] = 'test'
        self.assertEquals(len(cache), 1)


class TestFileCache(unittest.TestCase):

    initstring = 'file://test'

    def setUp(self):
        from shove.cache.core import FileCache
        self.cache = FileCache(self.initstring)

    def tearDown(self):
        import os
        self.cache = None
        for x in os.listdir('test'):
            os.remove(os.path.join('test', x))
        os.rmdir('test')

    def test_getitem(self):
        self.cache['test'] = 'test'
        self.assertEqual(self.cache['test'], 'test')

    def test_setitem(self):
        self.cache['test'] = 'test'
        self.assertEqual(self.cache['test'], 'test')

    def test_delitem(self):
        self.cache['test'] = 'test'
        del self.cache['test']
        self.assertEqual('test' in self.cache, False)

    def test_get(self):
        self.assertEqual(self.cache.get('min'), None)

    def test_timeout(self):
        import time
        from shove.cache.core import FileCache
        cache = FileCache(self.initstring, timeout=1)
        cache['test'] = 'test'
        time.sleep(2)

        def tmp():
            cache['test']
        self.assertRaises(KeyError, tmp)

    def test_cull(self):
        from shove.cache.core import FileCache
        cache = FileCache(self.initstring, max_entries=1)
        cache['test'] = 'test'
        cache['test2'] = 'test'
        num = len(cache)
        self.assertEquals(num, 1)


if __name__ == '__main__':
    unittest.main()