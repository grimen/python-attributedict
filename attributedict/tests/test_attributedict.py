
# =========================================
#       DEPS
# --------------------------------------

import json

from easypackage.syspath import syspath

syspath()

from attributedict.tests import helper

import attributedict
import attributedict.collections as collections

AttributeDict = collections.AttributeDict


# =========================================
#       TEST
# --------------------------------------

class TestCase(helper.TestCase):

    def test__import(self):
        self.assertModule(collections)

        self.assertTrue(hasattr(attributedict.collections, 'AttributeDict'))
        self.assertEqual(attributedict.collections.AttributeDict, attributedict.collections.AttributeDict)

        self.assertTrue(hasattr(attributedict.collections, 'attributedict'))
        self.assertEqual(attributedict.collections.attributedict, attributedict.collections.AttributeDict)

        self.assertTrue(hasattr(attributedict.collections, 'attrdict'))
        self.assertEqual(attributedict.collections.attrdict, attributedict.collections.attrdict)

    def test_init(self):
        attr_dict = AttributeDict()

        self.assertTrue(isinstance(attr_dict, dict))
        self.assertTrue(isinstance(attr_dict, attributedict.collections.AttributeDict))
        self.assertTrue(isinstance(attr_dict.__dict__, dict))
        self.assertDeepEqual(attr_dict, {})
        self.assertDeepEqual(attr_dict.__dict__, {})

        attr_dict = AttributeDict(None)

        self.assertTrue(isinstance(attr_dict, dict))
        self.assertTrue(isinstance(attr_dict, attributedict.collections.AttributeDict))
        self.assertTrue(isinstance(attr_dict.__dict__, dict))
        self.assertDeepEqual(attr_dict, {})
        self.assertDeepEqual(attr_dict.__dict__, {})

        attr_dict = AttributeDict({})

        self.assertTrue(isinstance(attr_dict, dict))
        self.assertTrue(isinstance(attr_dict, attributedict.collections.AttributeDict))
        self.assertTrue(isinstance(attr_dict.__dict__, dict))
        self.assertDeepEqual(attr_dict, {})
        self.assertDeepEqual(attr_dict.__dict__, {})

        attr_dict = AttributeDict({'foo': None})

        self.assertTrue(isinstance(attr_dict, dict))
        self.assertTrue(isinstance(attr_dict, attributedict.collections.AttributeDict))
        self.assertTrue(isinstance(attr_dict.__dict__, dict))
        self.assertDeepEqual(attr_dict, {'foo': None})
        self.assertDeepEqual(attr_dict.__dict__, {'foo': None})

        attr_dict = AttributeDict({'foo': {}})

        self.assertTrue(isinstance(attr_dict, dict))
        self.assertTrue(isinstance(attr_dict, attributedict.collections.AttributeDict))
        self.assertTrue(isinstance(attr_dict.__dict__, dict))
        self.assertDeepEqual(attr_dict, {'foo': {}})
        self.assertDeepEqual(attr_dict.__dict__, {'foo': AttributeDict({})})

        attr_dict = AttributeDict({'foo': {'bar': [1, 2, 3]}})

        self.assertTrue(isinstance(attr_dict, dict))
        self.assertTrue(isinstance(attr_dict, attributedict.collections.AttributeDict))
        self.assertTrue(isinstance(attr_dict.__dict__, dict))
        self.assertDeepEqual(attr_dict, {'foo': {'bar': [1, 2, 3]}})
        self.assertDeepEqual(attr_dict.__dict__, {'foo': AttributeDict({'bar': [1, 2, 3]})})

    def test_update(self):
        attr_dict = AttributeDict()

        attr_dict.update()

        self.assertTrue(isinstance(attr_dict, dict))
        self.assertTrue(isinstance(attr_dict, attributedict.collections.AttributeDict))
        self.assertTrue(isinstance(attr_dict.__dict__, dict))
        self.assertTrue(isinstance(attr_dict.__dict__, dict))
        self.assertDeepEqual(attr_dict, {})
        self.assertDeepEqual(attr_dict.__dict__, {})

        with self.assertRaises(TypeError):
            attr_dict.update(None)

        attr_dict.update({})

        self.assertTrue(isinstance(attr_dict, dict))
        self.assertTrue(isinstance(attr_dict, attributedict.collections.AttributeDict))
        self.assertTrue(isinstance(attr_dict.__dict__, dict))
        self.assertDeepEqual(attr_dict, {})
        self.assertDeepEqual(attr_dict.__dict__, {})

        attr_dict.update({'foo': None})

        self.assertTrue(isinstance(attr_dict, dict))
        self.assertTrue(isinstance(attr_dict, attributedict.collections.AttributeDict))
        self.assertTrue(isinstance(attr_dict.__dict__, dict))
        self.assertDeepEqual(attr_dict, {'foo': None})
        self.assertDeepEqual(attr_dict.__dict__, {'foo': None})

        attr_dict.update({'foo': {}})

        self.assertTrue(isinstance(attr_dict, dict))
        self.assertTrue(isinstance(attr_dict, attributedict.collections.AttributeDict))
        self.assertTrue(isinstance(attr_dict.__dict__, dict))
        self.assertDeepEqual(attr_dict, {'foo': {}})
        self.assertDeepEqual(attr_dict.__dict__, {'foo': AttributeDict({})}, exclude_types = {dict, attributedict.collections.AttributeDict})

        attr_dict = AttributeDict({'foo': {'bar': [1, 2, 3]}})

        self.assertTrue(isinstance(attr_dict, dict))
        self.assertTrue(isinstance(attr_dict, attributedict.collections.AttributeDict))
        self.assertTrue(isinstance(attr_dict.__dict__, dict))
        self.assertDeepEqual(attr_dict, {'foo': {'bar': [1, 2, 3]}})
        self.assertDeepEqual(attr_dict.__dict__, {'foo': AttributeDict({'bar': [1, 2, 3]})})

    def test_keys(self):
        attr_dict = AttributeDict()

        self.assertDeepEqual(list(attr_dict.keys()), [])

        # None

        attr_dict = AttributeDict(None)

        self.assertDeepEqual(list(attr_dict.keys()), [])

        # {}

        attr_dict = AttributeDict({})

        self.assertDeepEqual(list(attr_dict.keys()), [])

        # {'foo': NONE}

        attr_dict = AttributeDict({'foo': None})

        self.assertDeepEqual(list(attr_dict.keys()), ['foo'])

        # {'foo': {'bar': [1, 2, 3]}}

        attr_dict = AttributeDict({'foo': {'bar': [1, 2, 3]}})

        self.assertDeepEqual(list(attr_dict.keys()), ['foo'])

        # {'foo': {'bar': [1, 2, 3]}, 'baz': True}

        attr_dict = AttributeDict({'foo': {'bar': [1, 2, 3]}, 'baz': True})

        self.assertDeepEqual(list(attr_dict.keys()), ['foo', 'baz'])

    def test_values(self):
        attr_dict = AttributeDict()

        self.assertDeepEqual(list(attr_dict.values()), [])

        # None

        attr_dict = AttributeDict(None)

        self.assertDeepEqual(list(attr_dict.values()), [])

        # {}

        attr_dict = AttributeDict({})

        self.assertDeepEqual(list(attr_dict.values()), [])

        # {'foo': None}

        attr_dict = AttributeDict({'foo': None})

        self.assertDeepEqual(list(attr_dict.values()), [None])

        # {'foo': {'bar': [1, 2, 3]}}

        attr_dict = AttributeDict({'foo': {'bar': [1, 2, 3]}})

        self.assertDeepEqual(list(attr_dict.values()), [{'bar': [1, 2, 3]}])

        # {'foo': {'bar': [1, 2, 3]}, 'baz': True}

        attr_dict = AttributeDict({'foo': {'bar': [1, 2, 3]}, 'baz': True})

        self.assertDeepEqual(list(attr_dict.values()), [{'bar': [1, 2, 3]}, True])

    def test_get(self):
        attr_dict = AttributeDict()

        self.assertDeepEqual(attr_dict.get('foo', 'default'), 'default')
        self.assertDeepEqual(attr_dict.get('baz', 'default'), 'default')

        # None

        attr_dict = AttributeDict(None)

        self.assertDeepEqual(attr_dict.get('foo', 'default'), 'default')
        self.assertDeepEqual(attr_dict.get('baz', 'default'), 'default')

        # {}

        attr_dict = AttributeDict({})

        self.assertDeepEqual(attr_dict.get('foo', 'default'), 'default')
        self.assertDeepEqual(attr_dict.get('baz', 'default'), 'default')

        # {'foo': None}

        attr_dict = AttributeDict({'foo': None})

        self.assertDeepEqual(attr_dict.get('foo', 'default'), None)
        self.assertDeepEqual(attr_dict.get('baz', 'default'), 'default')

        # {'foo': {'bar': [1, 2, 3]}}

        attr_dict = AttributeDict({'foo': {'bar': [1, 2, 3]}})

        self.assertDeepEqual(attr_dict.get('foo', 'default'), {'bar': [1, 2, 3]})
        self.assertDeepEqual(attr_dict.get('baz', 'default'), 'default')

        # {'foo': {'bar': [1, 2, 3]}, 'baz': True}

        attr_dict = AttributeDict({'foo': {'bar': [1, 2, 3]}, 'baz': True})

        self.assertDeepEqual(attr_dict.get('foo', 'default'), {'bar': [1, 2, 3]})
        self.assertDeepEqual(attr_dict.get('baz', 'default'), True)

    def test_pop(self):
        attr_dict = AttributeDict()

        self.assertDeepEqual(attr_dict.pop('foo', 'default'), 'default')
        self.assertDeepEqual(attr_dict.pop('baz', 'default'), 'default')

        # None

        attr_dict = AttributeDict(None)

        self.assertDeepEqual(attr_dict.pop('foo', 'default'), 'default')
        self.assertDeepEqual(attr_dict.pop('baz', 'default'), 'default')

        # {}

        attr_dict = AttributeDict({})

        self.assertDeepEqual(attr_dict.pop('foo', 'default'), 'default')
        self.assertDeepEqual(attr_dict.pop('baz', 'default'), 'default')

        # {'foo': None}

        attr_dict = AttributeDict({'foo': None})

        self.assertDeepEqual(attr_dict.pop('foo', 'default'), None)
        self.assertDeepEqual(attr_dict.pop('baz', 'default'), 'default')

        # {'foo': {'bar': [1, 2, 3]}}

        attr_dict = AttributeDict({'foo': {'bar': [1, 2, 3]}})

        self.assertDeepEqual(attr_dict.pop('foo', 'default'), {'bar': [1, 2, 3]})
        self.assertDeepEqual(attr_dict.pop('baz', 'default'), 'default')

        # {'foo': {'bar': [1, 2, 3]}, 'baz': True}

        attr_dict = AttributeDict({'foo': {'bar': [1, 2, 3]}, 'baz': True})

        self.assertDeepEqual(attr_dict.pop('foo', 'default'), {'bar': [1, 2, 3]})
        self.assertDeepEqual(attr_dict.pop('baz', 'default'), True)

    def test_setdefault(self):
        attr_dict = AttributeDict()

        self.assertDeepEqual(attr_dict.setdefault('foo', 'default'), 'default')
        self.assertDeepEqual(attr_dict.get('foo'), 'default')
        self.assertDeepEqual(attr_dict.setdefault('baz', 'default'), 'default')
        self.assertDeepEqual(attr_dict.get('baz'), 'default')

        # None

        attr_dict = AttributeDict(None)

        self.assertDeepEqual(attr_dict.setdefault('foo', 'default'), 'default')
        self.assertDeepEqual(attr_dict.get('foo'), 'default')
        self.assertDeepEqual(attr_dict.setdefault('baz', 'default'), 'default')
        self.assertDeepEqual(attr_dict.get('baz'), 'default')

        # {}

        attr_dict = AttributeDict({})

        self.assertDeepEqual(attr_dict.setdefault('foo', 'default'), 'default')
        self.assertDeepEqual(attr_dict.get('foo'), 'default')
        self.assertDeepEqual(attr_dict.setdefault('baz', 'default'), 'default')
        self.assertDeepEqual(attr_dict.get('baz'), 'default')

        # {'foo': None}

        attr_dict = AttributeDict({'foo': None})

        self.assertDeepEqual(attr_dict.setdefault('foo', 'default'), None)
        self.assertDeepEqual(attr_dict.get('foo'), None)
        self.assertDeepEqual(attr_dict.setdefault('baz', 'default'), 'default')
        self.assertDeepEqual(attr_dict.get('baz'), 'default')

        # {'foo': {'bar': [1, 2, 3]}}

        attr_dict = AttributeDict({'foo': {'bar': [1, 2, 3]}})

        self.assertDeepEqual(attr_dict.setdefault('foo', 'default'), {'bar': [1, 2, 3]})
        self.assertDeepEqual(attr_dict.get('foo'), {'bar': [1, 2, 3]})
        self.assertDeepEqual(attr_dict.setdefault('baz', 'default'), 'default')
        self.assertDeepEqual(attr_dict.get('baz'), 'default')

        # {'foo': {'bar': [1, 2, 3]}, 'baz': True}

        attr_dict = AttributeDict({'foo': {'bar': [1, 2, 3]}, 'baz': True})

        self.assertDeepEqual(attr_dict.setdefault('foo', 'default'), {'bar': [1, 2, 3]})
        self.assertDeepEqual(attr_dict.get('foo'), {'bar': [1, 2, 3]})
        self.assertDeepEqual(attr_dict.setdefault('baz', 'default'), True)
        self.assertDeepEqual(attr_dict.get('baz'), True)

    def test_copy(self):
        attr_dict = AttributeDict()

        self.assertDeepEqual(attr_dict.copy(), {})
        self.assertDeepEqual(type(attr_dict.copy()), attributedict.collections.AttributeDict)

        # None

        attr_dict = AttributeDict(None)

        self.assertDeepEqual(attr_dict.copy(), {})

        # {}

        attr_dict = AttributeDict({})

        self.assertDeepEqual(attr_dict.copy(), {})

        # {'foo': None}

        attr_dict = AttributeDict({'foo': None})

        self.assertDeepEqual(attr_dict.copy(), {'foo': None})

        # {'foo': {'bar': [1, 2, 3]}}

        attr_dict = AttributeDict({'foo': {'bar': [1, 2, 3]}})

        self.assertDeepEqual(attr_dict.copy(), {'foo': {'bar': [1, 2, 3]}})

        # {'foo': {'bar': [1, 2, 3]}, 'baz': True}

        attr_dict = AttributeDict({'foo': {'bar': [1, 2, 3]}, 'baz': True})

        self.assertDeepEqual(attr_dict.copy(), {'foo': {'bar': [1, 2, 3]}, 'baz': True})

    def test_get_item(self):
        attr_dict = AttributeDict()

        with self.assertRaises(KeyError):
            attr_dict['foo']

        with self.assertRaises(KeyError):
            attr_dict['foo']['bar']

        with self.assertRaises(KeyError):
            attr_dict['baz']

        # None

        attr_dict = AttributeDict(None)

        with self.assertRaises(KeyError):
            attr_dict['foo']

        with self.assertRaises(KeyError):
            attr_dict['foo']['bar']

        with self.assertRaises(KeyError):
            attr_dict['baz']

        # {}

        attr_dict = AttributeDict({})

        with self.assertRaises(KeyError):
            attr_dict['foo']

        with self.assertRaises(KeyError):
            attr_dict['foo']['bar']

        with self.assertRaises(KeyError):
            attr_dict['baz']

        # {'foo': None}

        attr_dict = AttributeDict({'foo': None})

        self.assertDeepEqual(attr_dict['foo'], None)

        with self.assertRaises(TypeError):
            attr_dict['foo']['bar']

        with self.assertRaises(KeyError):
            attr_dict['baz']

        # {'foo': {'bar': [1, 2, 3]}}

        attr_dict = AttributeDict({'foo': {'bar': [1, 2, 3]}})

        self.assertDeepEqual(attr_dict['foo'], {'bar': [1, 2, 3]})
        self.assertDeepEqual(attr_dict['foo']['bar'], [1, 2, 3])

        with self.assertRaises(KeyError):
            attr_dict['baz']

        # {'foo': {'bar': [1, 2, 3]}, 'baz': True}

        attr_dict = AttributeDict({'foo': {'bar': [1, 2, 3]}, 'baz': True})

        self.assertDeepEqual(attr_dict['foo'], {'bar': [1, 2, 3]})
        self.assertDeepEqual(attr_dict['foo']['bar'], [1, 2, 3])
        self.assertDeepEqual(attr_dict['baz'], True)

    def test_set_item(self):
        attr_dict = AttributeDict()

        with self.assertRaises(KeyError):
            attr_dict['foo']

        with self.assertRaises(KeyError):
            attr_dict['foo']['bar']

        attr_dict['foo'] = None

        self.assertDeepEqual(attr_dict['foo'], None)

        with self.assertRaises(TypeError):
            attr_dict['foo']['bar']

        with self.assertRaises(KeyError):
            attr_dict['baz']

        # None

        attr_dict = AttributeDict(None)

        with self.assertRaises(KeyError):
            attr_dict['foo']

        with self.assertRaises(KeyError):
            attr_dict['foo']['bar']

        attr_dict['foo'] = None

        self.assertDeepEqual(attr_dict['foo'], None)

        with self.assertRaises(TypeError):
            attr_dict['foo']['bar']

        with self.assertRaises(KeyError):
            attr_dict['baz']

        # {}

        attr_dict = AttributeDict({})

        with self.assertRaises(KeyError):
            attr_dict['foo']

        with self.assertRaises(KeyError):
            attr_dict['foo']['bar']

        attr_dict['foo'] = None

        self.assertDeepEqual(attr_dict['foo'], None)

        with self.assertRaises(TypeError):
            attr_dict['foo']['bar']

        with self.assertRaises(KeyError):
            attr_dict['baz']

        # {'foo': None}

        attr_dict = AttributeDict({'foo': None})

        self.assertDeepEqual(attr_dict['foo'], None)

        attr_dict['foo'] = {}

        self.assertDeepEqual(attr_dict['foo'], {})

        with self.assertRaises(KeyError):
            attr_dict['foo']['bar']

        with self.assertRaises(KeyError):
            attr_dict['baz']

        # {'foo': {'bar': [1, 2, 3]}}

        attr_dict = AttributeDict({'foo': {'bar': [1, 2, 3]}})

        self.assertDeepEqual(attr_dict['foo'], {'bar': [1, 2, 3]})

        attr_dict['foo'] = {}

        self.assertDeepEqual(attr_dict['foo'], {})

        with self.assertRaises(KeyError):
            attr_dict['foo']['bar']

        with self.assertRaises(KeyError):
            attr_dict['baz']

        # {'foo': {'bar': [1, 2, 3]}, 'baz': True}

        attr_dict = AttributeDict({'foo': {'bar': [1, 2, 3]}, 'baz': True})

        self.assertDeepEqual(attr_dict['foo'], {'bar': [1, 2, 3]})
        self.assertDeepEqual(attr_dict['baz'], True)

        attr_dict['foo'] = {}
        attr_dict['baz'] = {}

        self.assertDeepEqual(attr_dict['foo'], {})

        with self.assertRaises(KeyError):
            attr_dict['foo']['bar']

        self.assertDeepEqual(attr_dict['baz'], {})

    def test_del_item(self):
        attr_dict = AttributeDict()

        with self.assertRaises(KeyError):
            del attr_dict['foo']

        attr_dict['foo'] = True

        self.assertDeepEqual(attr_dict['foo'], True)

        del attr_dict['foo']

        with self.assertRaises(KeyError):
            attr_dict['foo']

        with self.assertRaises(KeyError):
            attr_dict['foo']['bar']

        with self.assertRaises(Exception):
            attr_dict['baz']

        # None

        attr_dict = AttributeDict(None)

        with self.assertRaises(KeyError):
            del attr_dict['foo']

        attr_dict['foo'] = True

        self.assertDeepEqual(attr_dict['foo'], True)

        del attr_dict['foo']

        with self.assertRaises(KeyError):
            attr_dict['foo']

        with self.assertRaises(KeyError):
            attr_dict['foo']['bar']

        with self.assertRaises(Exception):
            attr_dict['baz']

        # {}

        attr_dict = AttributeDict({})

        with self.assertRaises(KeyError):
            del attr_dict['foo']

        attr_dict['foo'] = True

        self.assertDeepEqual(attr_dict['foo'], True)

        del attr_dict['foo']

        with self.assertRaises(KeyError):
            attr_dict['foo']

        with self.assertRaises(KeyError):
            attr_dict['foo']['bar']

        with self.assertRaises(Exception):
            attr_dict['baz']

        # {'foo': None}

        attr_dict = AttributeDict({'foo': None})

        del attr_dict['foo']

        attr_dict['foo'] = True

        self.assertDeepEqual(attr_dict['foo'], True)

        del attr_dict['foo']

        with self.assertRaises(KeyError):
            attr_dict['foo']

        with self.assertRaises(KeyError):
            attr_dict['foo']['bar']

        with self.assertRaises(Exception):
            attr_dict['baz']

        # {'foo': {'bar': [1, 2, 3]}}

        attr_dict = AttributeDict({'foo': {'bar': [1, 2, 3]}})

        del attr_dict['foo']

        attr_dict['foo'] = True

        self.assertDeepEqual(attr_dict['foo'], True)

        del attr_dict['foo']

        with self.assertRaises(KeyError):
            attr_dict['foo']

        with self.assertRaises(KeyError):
            attr_dict['foo']['bar']

        with self.assertRaises(Exception):
            attr_dict['baz']

        # {'foo': {'bar': [1, 2, 3]}, 'baz': True}

        attr_dict = AttributeDict({'foo': {'bar': [1, 2, 3]}, 'baz': True})

        del attr_dict['foo']

        attr_dict['foo'] = True

        self.assertDeepEqual(attr_dict['foo'], True)

        del attr_dict['foo']

        with self.assertRaises(KeyError):
            attr_dict['foo']

        with self.assertRaises(KeyError):
            attr_dict['foo']['bar']

        self.assertDeepEqual(attr_dict['baz'], True)

    def test_get_attribute(self):
        attr_dict = AttributeDict()

        with self.assertRaises(AttributeError):
            attr_dict.foo

        with self.assertRaises(AttributeError):
            attr_dict.foo.bar

        with self.assertRaises(AttributeError):
            attr_dict.baz

        # None

        attr_dict = AttributeDict(None)

        with self.assertRaises(AttributeError):
            attr_dict.foo

        with self.assertRaises(AttributeError):
            attr_dict.foo.bar

        with self.assertRaises(AttributeError):
            attr_dict.baz

        # {}

        attr_dict = AttributeDict({})

        with self.assertRaises(AttributeError):
            attr_dict.foo

        with self.assertRaises(AttributeError):
            attr_dict.foo.bar

        with self.assertRaises(AttributeError):
            attr_dict.baz

        # {'foo': None}

        attr_dict = AttributeDict({'foo': None})

        self.assertDeepEqual(attr_dict.foo, None)

        with self.assertRaises(AttributeError):
            attr_dict.foo.bar

        with self.assertRaises(AttributeError):
            attr_dict.baz

        # {'foo': {'bar': [1, 2, 3]}}

        attr_dict = AttributeDict({'foo': {'bar': [1, 2, 3]}})

        self.assertDeepEqual(attr_dict.foo, {'bar': [1, 2, 3]})
        self.assertDeepEqual(attr_dict.foo.bar, [1, 2, 3])

        with self.assertRaises(AttributeError):
            attr_dict.baz

        # {'foo': {'bar': [1, 2, 3]}, 'baz': True}

        attr_dict = AttributeDict({'foo': {'bar': [1, 2, 3]}, 'baz': True})

        self.assertDeepEqual(attr_dict.foo, {'bar': [1, 2, 3]})
        self.assertDeepEqual(attr_dict.foo.bar, [1, 2, 3])
        self.assertDeepEqual(attr_dict.baz, True)

    def test_set_attribute(self):
        attr_dict = AttributeDict()

        with self.assertRaises(KeyError):
            attr_dict['foo']

        with self.assertRaises(KeyError):
            attr_dict['foo']['bar']

        attr_dict.foo = None

        self.assertDeepEqual(attr_dict['foo'], None)

        with self.assertRaises(TypeError):
            attr_dict['foo']['bar']

        with self.assertRaises(KeyError):
            attr_dict['baz']

        # None

        attr_dict = AttributeDict(None)

        with self.assertRaises(KeyError):
            attr_dict['foo']

        with self.assertRaises(KeyError):
            attr_dict['foo']['bar']

        attr_dict.foo = None

        self.assertDeepEqual(attr_dict['foo'], None)

        with self.assertRaises(TypeError):
            attr_dict['foo']['bar']

        with self.assertRaises(KeyError):
            attr_dict['baz']

        # {}

        attr_dict = AttributeDict({})

        with self.assertRaises(KeyError):
            attr_dict['foo']

        with self.assertRaises(KeyError):
            attr_dict['foo']['bar']

        attr_dict.foo = None

        self.assertDeepEqual(attr_dict['foo'], None)

        with self.assertRaises(TypeError):
            attr_dict['foo']['bar']

        with self.assertRaises(KeyError):
            attr_dict['baz']

        # {'foo': None}

        attr_dict = AttributeDict({'foo': None})

        self.assertDeepEqual(attr_dict['foo'], None)

        attr_dict.foo = {}

        self.assertDeepEqual(attr_dict['foo'], {})

        with self.assertRaises(KeyError):
            attr_dict['foo']['bar']

        with self.assertRaises(KeyError):
            attr_dict['baz']

        # {'foo': {'bar': [1, 2, 3]}}

        attr_dict = AttributeDict({'foo': {'bar': [1, 2, 3]}})

        self.assertDeepEqual(attr_dict['foo'], {'bar': [1, 2, 3]})

        attr_dict.foo = {}

        self.assertDeepEqual(attr_dict['foo'], {})

        with self.assertRaises(KeyError):
            attr_dict['foo']['bar']

        with self.assertRaises(KeyError):
            attr_dict['baz']

        # {'foo': {'bar': [1, 2, 3]}, 'baz': True}

        attr_dict = AttributeDict({'foo': {'bar': [1, 2, 3]}, 'baz': True})

        self.assertDeepEqual(attr_dict['foo'], {'bar': [1, 2, 3]})
        self.assertDeepEqual(attr_dict['baz'], True)

        attr_dict.foo = {}
        attr_dict.baz = {}

        self.assertDeepEqual(attr_dict['foo'], {})

        with self.assertRaises(KeyError):
            attr_dict['foo']['bar']

        self.assertDeepEqual(attr_dict['baz'], {})

    def test_del_attribute(self):
        attr_dict = AttributeDict()

        with self.assertRaises(KeyError):
            del attr_dict['foo']

        attr_dict['foo'] = True

        self.assertDeepEqual(attr_dict['foo'], True)

        del attr_dict['foo']

        with self.assertRaises(KeyError):
            attr_dict['foo']

        with self.assertRaises(KeyError):
            attr_dict['foo']['bar']

        with self.assertRaises(KeyError):
            attr_dict['baz']

        # None

        attr_dict = AttributeDict(None)

        with self.assertRaises(AttributeError):
            del attr_dict.foo

        attr_dict['foo'] = True

        self.assertDeepEqual(attr_dict['foo'], True)

        del attr_dict.foo

        with self.assertRaises(KeyError):
            attr_dict['foo']

        with self.assertRaises(KeyError):
            attr_dict['foo']['bar']

        with self.assertRaises(KeyError):
            attr_dict['baz']

        # {}

        attr_dict = AttributeDict({})

        with self.assertRaises(AttributeError):
            del attr_dict.foo

        attr_dict['foo'] = True

        self.assertDeepEqual(attr_dict['foo'], True)

        del attr_dict.foo

        with self.assertRaises(KeyError):
            attr_dict['foo']

        with self.assertRaises(KeyError):
            attr_dict['foo']['bar']

        with self.assertRaises(KeyError):
            attr_dict['baz']

        # {'foo': None}

        attr_dict = AttributeDict({'foo': None})

        del attr_dict.foo

        attr_dict['foo'] = True

        self.assertDeepEqual(attr_dict['foo'], True)

        del attr_dict.foo

        with self.assertRaises(KeyError):
            attr_dict['foo']

        with self.assertRaises(KeyError):
            attr_dict['foo']['bar']

        with self.assertRaises(KeyError):
            attr_dict['baz']

        # {'foo': {'bar': [1, 2, 3]}}

        attr_dict = AttributeDict({'foo': {'bar': [1, 2, 3]}})

        del attr_dict.foo

        attr_dict['foo'] = True

        self.assertDeepEqual(attr_dict['foo'], True)

        del attr_dict.foo

        with self.assertRaises(KeyError):
            attr_dict['foo']

        with self.assertRaises(KeyError):
            attr_dict['foo']['bar']

        with self.assertRaises(KeyError):
            attr_dict['baz']

        # {'foo': {'bar': [1, 2, 3]}, 'baz': True}

        attr_dict = AttributeDict({'foo': {'bar': [1, 2, 3]}, 'baz': True})

        del attr_dict.foo

        attr_dict['foo'] = True

        self.assertDeepEqual(attr_dict['foo'], True)

        del attr_dict.foo

        with self.assertRaises(KeyError):
            attr_dict['foo']

        with self.assertRaises(KeyError):
            attr_dict['foo']['bar']

        self.assertDeepEqual(attr_dict['baz'], True)

    def test_str(self):
        attr_dict = AttributeDict()

        self.assertEqual(str(attr_dict), "{}")

        # None

        attr_dict = AttributeDict(None)

        self.assertEqual(str(attr_dict), "{}")

        # {}

        attr_dict = AttributeDict({})

        self.assertEqual(str(attr_dict), "{}")

        # {'foo': NONE}

        attr_dict = AttributeDict({'foo': None})

        self.assertEqual(str(attr_dict), "{'foo': None}")

        # {'foo': {'bar': [1, 2, 3]}}

        attr_dict = AttributeDict({'foo': {'bar': [1, 2, 3]}})

        self.assertEqual(str(attr_dict), "{'foo': {'bar': [1, 2, 3]}}")

        # {'foo': {'bar': [1, 2, 3]}, 'baz': True}

        attr_dict = AttributeDict({'foo': {'bar': [1, 2, 3]}, 'baz': True})

        self.assertEqual(str(attr_dict), "{'foo': {'bar': [1, 2, 3]}, 'baz': True}")

    def test_repr(self):
        attr_dict = AttributeDict()

        self.assertEqual(repr(attr_dict), "{}")

        # None

        attr_dict = AttributeDict(None)

        self.assertEqual(repr(attr_dict), "{}")

        # {}

        attr_dict = AttributeDict({})

        self.assertEqual(repr(attr_dict), "{}")

        # {'foo': NONE}

        attr_dict = AttributeDict({'foo': None})

        self.assertEqual(repr(attr_dict), "{'foo': None}")

        # {'foo': {'bar': [1, 2, 3]}}

        attr_dict = AttributeDict({'foo': {'bar': [1, 2, 3]}})

        self.assertEqual(repr(attr_dict), "{'foo': {'bar': [1, 2, 3]}}")

        # {'foo': {'bar': [1, 2, 3]}, 'baz': True}

        attr_dict = AttributeDict({'foo': {'bar': [1, 2, 3]}, 'baz': True})

        self.assertEqual(repr(attr_dict), "{'foo': {'bar': [1, 2, 3]}, 'baz': True}")

    def test_dir(self):
        attr_dict = AttributeDict()

        with self.assertNotRaises(Exception):
            dir(attr_dict)

    def test_init_encode(self):
        attr_dict = AttributeDict()

        self.assertDeepEqual(helper.json_encode(attr_dict), '{}')
        # self.assertDeepEqual(helper.json_encode(attr_dict.__dict__), '{}')

        attr_dict = AttributeDict(None)

        self.assertDeepEqual(helper.json_encode(attr_dict), '{}')
        # self.assertDeepEqual(helper.json_encode(attr_dict.__dict__), '{}')

        attr_dict = AttributeDict({})

        self.assertDeepEqual(helper.json_encode(attr_dict), '{}')
        # self.assertDeepEqual(helper.json_encode(attr_dict.__dict__), '{}')

        attr_dict = AttributeDict({'foo': None})

        self.assertDeepEqual(helper.json_encode(attr_dict), '{"foo":null}')
        # self.assertDeepEqual(helper.json_encode(attr_dict.__dict__), '{"foo":null}')

        attr_dict = AttributeDict({'foo': {}})

        self.assertDeepEqual(helper.json_encode(attr_dict), '{"foo":{}}')
        # self.assertDeepEqual(helper.json_encode(attr_dict.__dict__), '{"foo":{}}')

        attr_dict = AttributeDict({'foo': {'bar': [1, 2, 3]}})

        self.assertDeepEqual(helper.json_encode(attr_dict), '{"foo":{"bar":[1,2,3]}}')
        # self.assertDeepEqual(helper.json_encode(attr_dict.__dict__), '{"foo":{"bar":[1,2,3]}}')

    def test_key_encode(self):
        attr_dict = AttributeDict()

        attr_dict['foo'] = None

        self.assertDeepEqual(helper.json_encode(attr_dict), '{"foo":null}')
        self.assertDeepEqual(helper.json_encode(attr_dict.__dict__), '{"foo":null}')

        attr_dict['foo'] = {}

        self.assertDeepEqual(helper.json_encode(attr_dict), '{"foo":{}}')
        self.assertDeepEqual(helper.json_encode(attr_dict.__dict__), '{"foo":{}}')

        attr_dict['foo'] = {'bar': [1, 2, 3]}

        self.assertDeepEqual(helper.json_encode(attr_dict), '{"foo":{"bar":[1,2,3]}}')
        self.assertDeepEqual(helper.json_encode(attr_dict.__dict__), '{"foo":{"bar":[1,2,3]}}')

        attr_dict['foo']['bar'] = [3, 2, 1]

        self.assertDeepEqual(helper.json_encode(attr_dict), '{"foo":{"bar":[3,2,1]}}')
        self.assertDeepEqual(helper.json_encode(attr_dict.__dict__), '{"foo":{"bar":[3,2,1]}}')

        attr_dict['baz'] = True

        self.assertDeepEqual(helper.json_encode(attr_dict), '{"foo":{"bar":[1,2,3]},"baz":true}')
        self.assertDeepEqual(helper.json_encode(attr_dict.__dict__), '{"foo":{"bar":[1,2,3]},"baz":true}')

        del attr_dict['baz']

        self.assertDeepEqual(helper.json_encode(attr_dict), '{"foo":{"bar":[1,2,3]}}')
        self.assertDeepEqual(helper.json_encode(attr_dict.__dict__), '{"foo":{"bar":[1,2,3]}}')

    def test_key_encode(self):
        attr_dict = AttributeDict()

        attr_dict.foo = None

        self.assertDeepEqual(helper.json_encode(attr_dict), '{"foo":null}')
        self.assertDeepEqual(helper.json_encode(attr_dict.__dict__), '{"foo":null}')

        attr_dict.foo = {}

        self.assertDeepEqual(helper.json_encode(attr_dict), '{"foo":{}}')
        self.assertDeepEqual(helper.json_encode(attr_dict.__dict__), '{"foo":{}}')

        attr_dict.foo = {'bar': [1, 2, 3]}

        self.assertDeepEqual(helper.json_encode(attr_dict), '{"foo":{"bar":[1,2,3]}}')
        self.assertDeepEqual(helper.json_encode(attr_dict.__dict__), '{"foo":{"bar":[1,2,3]}}')

        attr_dict.foo.bar = [3, 2, 1]

        self.assertDeepEqual(helper.json_encode(attr_dict), '{"foo":{"bar":[3,2,1]}}')
        self.assertDeepEqual(helper.json_encode(attr_dict.__dict__), '{"foo":{"bar":[3,2,1]}}')

        attr_dict.baz = True

        self.assertDeepEqual(helper.json_encode(attr_dict), '{"foo":{"bar":[3,2,1]},"baz":true}')
        self.assertDeepEqual(helper.json_encode(attr_dict.__dict__), '{"foo":{"bar":[3,2,1]},"baz":true}')

        del attr_dict.baz

        self.assertDeepEqual(helper.json_encode(attr_dict), '{"foo":{"bar":[3,2,1]}}')
        self.assertDeepEqual(helper.json_encode(attr_dict.__dict__), '{"foo":{"bar":[3,2,1]}}')


    def test_fromkeys(self):
        with self.assertRaises(TypeError):
            AttributeDict().fromkeys()

        attr_dict = AttributeDict().fromkeys([])

        self.assertDeepEqual(attr_dict, {})

        attr_dict = AttributeDict().fromkeys(['foo'])

        self.assertDeepEqual(attr_dict, {'foo': None})

        attr_dict = AttributeDict().fromkeys(['foo'], 'default')

        self.assertDeepEqual(attr_dict, {'foo': 'default'})

        attr_dict = AttributeDict().fromkeys(['foo', 'bar'])

        self.assertDeepEqual(attr_dict, {'foo': None, 'bar': None})

        attr_dict = AttributeDict().fromkeys(['foo', 'bar'], 'default')

        self.assertDeepEqual(attr_dict, {'foo': 'default', 'bar': 'default'})


# =========================================
#       MAIN
# --------------------------------------

if __name__ == '__main__':
    helper.run(TestCase)
