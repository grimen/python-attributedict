
# =========================================
#       DEPS
# --------------------------------------

import json

import rootpath

rootpath.append()

from attributedict.tests import helper

import attributedict
import attributedict.collections as collections

AttributeDict = collections.AttributeDict

class CustomAttributeDict(AttributeDict):
    pass


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
        for _AttributeDict in [AttributeDict, CustomAttributeDict]:
            attr_dict = _AttributeDict()

            self.assertTrue(isinstance(attr_dict, dict))
            self.assertTrue(isinstance(attr_dict, attributedict.collections.AttributeDict))
            self.assertTrue(isinstance(attr_dict.__dict__, dict))
            self.assertDeepEqual(attr_dict, {})
            self.assertDeepEqual(attr_dict.__dict__, {})

            attr_dict = _AttributeDict(None)

            self.assertTrue(isinstance(attr_dict, dict))
            self.assertTrue(isinstance(attr_dict, attributedict.collections.AttributeDict))
            self.assertTrue(isinstance(attr_dict.__dict__, dict))
            self.assertDeepEqual(attr_dict, {})
            self.assertDeepEqual(attr_dict.__dict__, {})

            attr_dict = _AttributeDict({})

            self.assertTrue(isinstance(attr_dict, dict))
            self.assertTrue(isinstance(attr_dict, attributedict.collections.AttributeDict))
            self.assertTrue(isinstance(attr_dict.__dict__, dict))
            self.assertDeepEqual(attr_dict, {})
            self.assertDeepEqual(attr_dict.__dict__, {})

            attr_dict = _AttributeDict({'foo': None, '__reserved': True})

            self.assertTrue(isinstance(attr_dict, dict))
            self.assertTrue(isinstance(attr_dict, attributedict.collections.AttributeDict))
            self.assertTrue(isinstance(attr_dict.__dict__, dict))
            self.assertDeepEqual(attr_dict, {'foo': None})
            self.assertDeepEqual(attr_dict.__dict__, {'foo': None})

            attr_dict = _AttributeDict({'foo': {}, '__reserved': True})

            self.assertTrue(isinstance(attr_dict, dict))
            self.assertTrue(isinstance(attr_dict, attributedict.collections.AttributeDict))
            self.assertTrue(isinstance(attr_dict.__dict__, dict))
            self.assertDeepEqual(attr_dict, {'foo': {}})
            self.assertDeepEqual(attr_dict.__dict__, {'foo': _AttributeDict({})})

            attr_dict = _AttributeDict({'foo': {'bar': [1, 2, 3]}, '__reserved': True})

            self.assertTrue(isinstance(attr_dict, dict))
            self.assertTrue(isinstance(attr_dict, attributedict.collections.AttributeDict))
            self.assertTrue(isinstance(attr_dict.__dict__, dict))
            self.assertDeepEqual(attr_dict, {'foo': {'bar': [1, 2, 3]}})
            self.assertDeepEqual(attr_dict.__dict__, {'foo': _AttributeDict({'bar': [1, 2, 3]})})

    def test_update(self):
        for _AttributeDict in [AttributeDict, CustomAttributeDict]:
            attr_dict = _AttributeDict()

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

            attr_dict.update({'foo': None, '__reserved': True})

            self.assertTrue(isinstance(attr_dict, dict))
            self.assertTrue(isinstance(attr_dict, attributedict.collections.AttributeDict))
            self.assertTrue(isinstance(attr_dict.__dict__, dict))
            self.assertDeepEqual(attr_dict, {'foo': None})
            self.assertDeepEqual(attr_dict.__dict__, {'foo': None})

            attr_dict.update({'foo': {}, '__reserved': True})

            self.assertTrue(isinstance(attr_dict, dict))
            self.assertTrue(isinstance(attr_dict, attributedict.collections.AttributeDict))
            self.assertTrue(isinstance(attr_dict.__dict__, dict))
            self.assertDeepEqual(attr_dict, {'foo': {}})
            self.assertDeepEqual(attr_dict.__dict__, {'foo': AttributeDict({})}, exclude_types = {dict, attributedict.collections.AttributeDict})

            attr_dict = _AttributeDict({'foo': {'bar': [1, 2, 3]}, '__reserved': True})

            self.assertTrue(isinstance(attr_dict, dict))
            self.assertTrue(isinstance(attr_dict, attributedict.collections.AttributeDict))
            self.assertTrue(isinstance(attr_dict.__dict__, dict))
            self.assertDeepEqual(attr_dict, {'foo': {'bar': [1, 2, 3]}})
            self.assertDeepEqual(attr_dict.__dict__, {'foo': AttributeDict({'bar': [1, 2, 3]})})

    def test_keys(self):
        for _AttributeDict in [AttributeDict, CustomAttributeDict]:
            attr_dict = _AttributeDict()

            self.assertDeepEqual(list(attr_dict.keys()), [])

            # None

            attr_dict = _AttributeDict(None)

            self.assertDeepEqual(list(attr_dict.keys()), [])

            # {}

            attr_dict = _AttributeDict({})

            self.assertDeepEqual(list(attr_dict.keys()), [])

            # {'foo': NONE}

            attr_dict = _AttributeDict({'foo': None, '__reserved': True})

            self.assertDeepEqual(list(attr_dict.keys()), ['foo'])

            # {'foo': {'bar': [1, 2, 3]}}

            attr_dict = _AttributeDict({'foo': {'bar': [1, 2, 3]}, '__reserved': True})

            self.assertDeepEqual(list(attr_dict.keys()), ['foo'])

            # {'foo': {'bar': [1, 2, 3]}, 'baz': True}

            attr_dict = _AttributeDict({'foo': {'bar': [1, 2, 3]}, 'baz': True, '__reserved': True})

            self.assertDeepEqual(list(attr_dict.keys()), ['foo', 'baz'])

    def test_values(self):
        for _AttributeDict in [AttributeDict, CustomAttributeDict]:
            attr_dict = _AttributeDict()

            self.assertDeepEqual(list(attr_dict.values()), [])

            # None

            attr_dict = _AttributeDict(None)

            self.assertDeepEqual(list(attr_dict.values()), [])

            # {}

            attr_dict = _AttributeDict({})

            self.assertDeepEqual(list(attr_dict.values()), [])

            # {'foo': None}

            attr_dict = _AttributeDict({'foo': None, '__reserved': True})

            self.assertDeepEqual(list(attr_dict.values()), [None])

            # {'foo': {'bar': [1, 2, 3]}}

            attr_dict = _AttributeDict({'foo': {'bar': [1, 2, 3]}, '__reserved': True})

            self.assertDeepEqual(list(attr_dict.values()), [{'bar': [1, 2, 3]}])

            # {'foo': {'bar': [1, 2, 3]}, 'baz': True}

            attr_dict = _AttributeDict({'foo': {'bar': [1, 2, 3]}, 'baz': True, '__reserved': True})

            self.assertDeepEqual(list(attr_dict.values()), [{'bar': [1, 2, 3]}, True])

    def test_get(self):
        for _AttributeDict in [AttributeDict, CustomAttributeDict]:
            attr_dict = _AttributeDict()

            self.assertDeepEqual(attr_dict.get('foo', 'default'), 'default')
            self.assertDeepEqual(attr_dict.get('baz', 'default'), 'default')

            # None

            attr_dict = _AttributeDict(None)

            self.assertDeepEqual(attr_dict.get('foo', 'default'), 'default')
            self.assertDeepEqual(attr_dict.get('baz', 'default'), 'default')

            # {}

            attr_dict = _AttributeDict({})

            self.assertDeepEqual(attr_dict.get('foo', 'default'), 'default')
            self.assertDeepEqual(attr_dict.get('baz', 'default'), 'default')

            # {'foo': None}

            attr_dict = _AttributeDict({'foo': None, '__reserved': True})

            self.assertDeepEqual(attr_dict.get('foo', 'default'), None)
            self.assertDeepEqual(attr_dict.get('baz', 'default'), 'default')

            # {'foo': {'bar': [1, 2, 3]}}

            attr_dict = _AttributeDict({'foo': {'bar': [1, 2, 3]}, '__reserved': True})

            self.assertDeepEqual(attr_dict.get('foo', 'default'), {'bar': [1, 2, 3]})
            self.assertDeepEqual(attr_dict.get('baz', 'default'), 'default')

            # {'foo': {'bar': [1, 2, 3]}, 'baz': True}

            attr_dict = _AttributeDict({'foo': {'bar': [1, 2, 3]}, 'baz': True, '__reserved': True})

            self.assertDeepEqual(attr_dict.get('foo', 'default'), {'bar': [1, 2, 3]})
            self.assertDeepEqual(attr_dict.get('baz', 'default'), True)

    def test_pop(self):
        for _AttributeDict in [AttributeDict, CustomAttributeDict]:
            attr_dict = _AttributeDict()

            self.assertDeepEqual(attr_dict.pop('foo', 'default'), 'default')
            self.assertDeepEqual(attr_dict.pop('baz', 'default'), 'default')

            # None

            attr_dict = _AttributeDict(None)

            self.assertDeepEqual(attr_dict.pop('foo', 'default'), 'default')
            self.assertDeepEqual(attr_dict.pop('baz', 'default'), 'default')

            # {}

            attr_dict = _AttributeDict({})

            self.assertDeepEqual(attr_dict.pop('foo', 'default'), 'default')
            self.assertDeepEqual(attr_dict.pop('baz', 'default'), 'default')

            # {'foo': None}

            attr_dict = _AttributeDict({'foo': None, '__reserved': True})

            self.assertDeepEqual(attr_dict.pop('foo', 'default'), None)
            self.assertDeepEqual(attr_dict.pop('baz', 'default'), 'default')

            # {'foo': {'bar': [1, 2, 3]}}

            attr_dict = _AttributeDict({'foo': {'bar': [1, 2, 3]}, '__reserved': True})

            self.assertDeepEqual(attr_dict.pop('foo', 'default'), {'bar': [1, 2, 3]})
            self.assertDeepEqual(attr_dict.pop('baz', 'default'), 'default')

            # {'foo': {'bar': [1, 2, 3]}, 'baz': True}

            attr_dict = _AttributeDict({'foo': {'bar': [1, 2, 3]}, 'baz': True, '__reserved': True})

            self.assertDeepEqual(attr_dict.pop('foo', 'default'), {'bar': [1, 2, 3]})
            self.assertDeepEqual(attr_dict.pop('baz', 'default'), True)

    def test_setdefault(self):
        for _AttributeDict in [AttributeDict, CustomAttributeDict]:
            attr_dict = _AttributeDict()

            self.assertDeepEqual(attr_dict.setdefault('foo', 'default'), 'default')
            self.assertDeepEqual(attr_dict.get('foo'), 'default')
            self.assertDeepEqual(attr_dict.setdefault('baz', 'default'), 'default')
            self.assertDeepEqual(attr_dict.get('baz'), 'default')

            # None

            attr_dict = _AttributeDict(None)

            self.assertDeepEqual(attr_dict.setdefault('foo', 'default'), 'default')
            self.assertDeepEqual(attr_dict.get('foo'), 'default')
            self.assertDeepEqual(attr_dict.setdefault('baz', 'default'), 'default')
            self.assertDeepEqual(attr_dict.get('baz'), 'default')

            # {}

            attr_dict = _AttributeDict({})

            self.assertDeepEqual(attr_dict.setdefault('foo', 'default'), 'default')
            self.assertDeepEqual(attr_dict.get('foo'), 'default')
            self.assertDeepEqual(attr_dict.setdefault('baz', 'default'), 'default')
            self.assertDeepEqual(attr_dict.get('baz'), 'default')

            # {'foo': None}

            attr_dict = _AttributeDict({'foo': None, '__reserved': True})

            self.assertDeepEqual(attr_dict.setdefault('foo', 'default'), None)
            self.assertDeepEqual(attr_dict.get('foo'), None)
            self.assertDeepEqual(attr_dict.setdefault('baz', 'default'), 'default')
            self.assertDeepEqual(attr_dict.get('baz'), 'default')

            # {'foo': {'bar': [1, 2, 3]}}

            attr_dict = _AttributeDict({'foo': {'bar': [1, 2, 3]}, '__reserved': True})

            self.assertDeepEqual(attr_dict.setdefault('foo', 'default'), {'bar': [1, 2, 3]})
            self.assertDeepEqual(attr_dict.get('foo'), {'bar': [1, 2, 3]})
            self.assertDeepEqual(attr_dict.setdefault('baz', 'default'), 'default')
            self.assertDeepEqual(attr_dict.get('baz'), 'default')

            # {'foo': {'bar': [1, 2, 3]}, 'baz': True}

            attr_dict = _AttributeDict({'foo': {'bar': [1, 2, 3]}, 'baz': True, '__reserved': True})

            self.assertDeepEqual(attr_dict.setdefault('foo', 'default'), {'bar': [1, 2, 3]})
            self.assertDeepEqual(attr_dict.get('foo'), {'bar': [1, 2, 3]})
            self.assertDeepEqual(attr_dict.setdefault('baz', 'default'), True)
            self.assertDeepEqual(attr_dict.get('baz'), True)

    def test_copy(self):
        attr_dict = AttributeDict()

        self.assertDeepEqual(attr_dict.copy(), {})
        self.assertDeepEqual(type(attr_dict.copy()), attributedict.collections.AttributeDict)

        attr_dict = CustomAttributeDict()

        self.assertDeepEqual(attr_dict.copy(), {})
        self.assertDeepEqual(type(attr_dict.copy()), CustomAttributeDict)

        for _AttributeDict in [AttributeDict, CustomAttributeDict]:

            # None

            attr_dict = _AttributeDict(None)

            self.assertDeepEqual(attr_dict.copy(), {})

            # {}

            attr_dict = _AttributeDict({})

            self.assertDeepEqual(attr_dict.copy(), {})

            # {'foo': None}

            attr_dict = _AttributeDict({'foo': None, '__reserved': True})

            self.assertDeepEqual(attr_dict.copy(), {'foo': None})

            # {'foo': {'bar': [1, 2, 3]}}

            attr_dict = _AttributeDict({'foo': {'bar': [1, 2, 3]}, '__reserved': True})

            self.assertDeepEqual(attr_dict.copy(), {'foo': {'bar': [1, 2, 3]}})

            # {'foo': {'bar': [1, 2, 3]}, 'baz': True}

            attr_dict = _AttributeDict({'foo': {'bar': [1, 2, 3]}, 'baz': True, '__reserved': True})

            self.assertDeepEqual(attr_dict.copy(), {'foo': {'bar': [1, 2, 3]}, 'baz': True})

    def test_get_item(self):
        for _AttributeDict in [AttributeDict, CustomAttributeDict]:
            attr_dict = _AttributeDict()

            with self.assertRaises(KeyError):
                attr_dict['foo']

            with self.assertRaises(KeyError):
                attr_dict['foo']['bar']

            with self.assertRaises(KeyError):
                attr_dict['baz']

            # None

            attr_dict = _AttributeDict(None)

            with self.assertRaises(KeyError):
                attr_dict['foo']

            with self.assertRaises(KeyError):
                attr_dict['foo']['bar']

            with self.assertRaises(KeyError):
                attr_dict['baz']

            # {}

            attr_dict = _AttributeDict({})

            with self.assertRaises(KeyError):
                attr_dict['foo']

            with self.assertRaises(KeyError):
                attr_dict['foo']['bar']

            with self.assertRaises(KeyError):
                attr_dict['baz']

            # {'foo': None}

            attr_dict = _AttributeDict({'foo': None, '__reserved': True})

            self.assertDeepEqual(attr_dict['foo'], None)

            with self.assertRaises(TypeError):
                attr_dict['foo']['bar']

            with self.assertRaises(KeyError):
                attr_dict['baz']

            # {'foo': {'bar': [1, 2, 3]}}

            attr_dict = _AttributeDict({'foo': {'bar': [1, 2, 3]}, '__reserved': True})

            self.assertDeepEqual(attr_dict['foo'], {'bar': [1, 2, 3]})
            self.assertDeepEqual(attr_dict['foo']['bar'], [1, 2, 3])

            with self.assertRaises(KeyError):
                attr_dict['baz']

            # {'foo': {'bar': [1, 2, 3]}, 'baz': True}

            attr_dict = _AttributeDict({'foo': {'bar': [1, 2, 3]}, 'baz': True, '__reserved': True})

            self.assertDeepEqual(attr_dict['foo'], {'bar': [1, 2, 3]})
            self.assertDeepEqual(attr_dict['foo']['bar'], [1, 2, 3])
            self.assertDeepEqual(attr_dict['baz'], True)

    def test_set_item(self):
        for _AttributeDict in [AttributeDict, CustomAttributeDict]:
            attr_dict = _AttributeDict()

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

            attr_dict = _AttributeDict(None)

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

            attr_dict = _AttributeDict({})

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

            attr_dict = _AttributeDict({'foo': None, '__reserved': True})

            self.assertDeepEqual(attr_dict['foo'], None)

            attr_dict['foo'] = {}

            self.assertDeepEqual(attr_dict['foo'], {})

            with self.assertRaises(KeyError):
                attr_dict['foo']['bar']

            with self.assertRaises(KeyError):
                attr_dict['baz']

            # {'foo': {'bar': [1, 2, 3]}}

            attr_dict = _AttributeDict({'foo': {'bar': [1, 2, 3]}, '__reserved': True})

            self.assertDeepEqual(attr_dict['foo'], {'bar': [1, 2, 3]})

            attr_dict['foo'] = {}

            self.assertDeepEqual(attr_dict['foo'], {})

            with self.assertRaises(KeyError):
                attr_dict['foo']['bar']

            with self.assertRaises(KeyError):
                attr_dict['baz']

            # {'foo': {'bar': [1, 2, 3]}, 'baz': True}

            attr_dict = _AttributeDict({'foo': {'bar': [1, 2, 3]}, 'baz': True, '__reserved': True})

            self.assertDeepEqual(attr_dict['foo'], {'bar': [1, 2, 3]})
            self.assertDeepEqual(attr_dict['baz'], True)

            attr_dict['foo'] = {}
            attr_dict['baz'] = {}

            self.assertDeepEqual(attr_dict['foo'], {})

            with self.assertRaises(KeyError):
                attr_dict['foo']['bar']

            self.assertDeepEqual(attr_dict['baz'], {})

    def test_del_item(self):
        for _AttributeDict in [AttributeDict, CustomAttributeDict]:
            attr_dict = _AttributeDict()

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

            attr_dict = _AttributeDict(None)

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

            attr_dict = _AttributeDict({})

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

            attr_dict = _AttributeDict({'foo': None, '__reserved': True})

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

            attr_dict = _AttributeDict({'foo': {'bar': [1, 2, 3]}, '__reserved': True})

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

            attr_dict = _AttributeDict({'foo': {'bar': [1, 2, 3]}, 'baz': True, '__reserved': True})

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
        for _AttributeDict in [AttributeDict, CustomAttributeDict]:
            attr_dict = _AttributeDict()

            with self.assertRaises(AttributeError):
                attr_dict.foo

            with self.assertRaises(AttributeError):
                attr_dict.foo.bar

            with self.assertRaises(AttributeError):
                attr_dict.baz

            # None

            attr_dict = _AttributeDict(None)

            with self.assertRaises(AttributeError):
                attr_dict.foo

            with self.assertRaises(AttributeError):
                attr_dict.foo.bar

            with self.assertRaises(AttributeError):
                attr_dict.baz

            # {}

            attr_dict = _AttributeDict({})

            with self.assertRaises(AttributeError):
                attr_dict.foo

            with self.assertRaises(AttributeError):
                attr_dict.foo.bar

            with self.assertRaises(AttributeError):
                attr_dict.baz

            # {'foo': None}

            attr_dict = _AttributeDict({'foo': None, '__reserved': True})

            self.assertDeepEqual(attr_dict.foo, None)

            with self.assertRaises(AttributeError):
                attr_dict.foo.bar

            with self.assertRaises(AttributeError):
                attr_dict.baz

            # {'foo': {'bar': [1, 2, 3]}}

            attr_dict = _AttributeDict({'foo': {'bar': [1, 2, 3]}, '__reserved': True})

            self.assertDeepEqual(attr_dict.foo, {'bar': [1, 2, 3]})
            self.assertDeepEqual(attr_dict.foo.bar, [1, 2, 3])

            with self.assertRaises(AttributeError):
                attr_dict.baz

            # {'foo': {'bar': [1, 2, 3]}, 'baz': True}

            attr_dict = _AttributeDict({'foo': {'bar': [1, 2, 3]}, 'baz': True, '__reserved': True})

            self.assertDeepEqual(attr_dict.foo, {'bar': [1, 2, 3]})
            self.assertDeepEqual(attr_dict.foo.bar, [1, 2, 3])
            self.assertDeepEqual(attr_dict.baz, True)

    def test_set_attribute(self):
        for _AttributeDict in [AttributeDict, CustomAttributeDict]:
            attr_dict = _AttributeDict()

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

            attr_dict = _AttributeDict(None)

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

            attr_dict = _AttributeDict({})

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

            attr_dict = _AttributeDict({'foo': None, '__reserved': True})

            self.assertDeepEqual(attr_dict['foo'], None)

            attr_dict.foo = {}

            self.assertDeepEqual(attr_dict['foo'], {})

            with self.assertRaises(KeyError):
                attr_dict['foo']['bar']

            with self.assertRaises(KeyError):
                attr_dict['baz']

            # {'foo': {'bar': [1, 2, 3]}}

            attr_dict = _AttributeDict({'foo': {'bar': [1, 2, 3]}, '__reserved': True})

            self.assertDeepEqual(attr_dict['foo'], {'bar': [1, 2, 3]})

            attr_dict.foo = {}

            self.assertDeepEqual(attr_dict['foo'], {})

            with self.assertRaises(KeyError):
                attr_dict['foo']['bar']

            with self.assertRaises(KeyError):
                attr_dict['baz']

            # {'foo': {'bar': [1, 2, 3]}, 'baz': True}

            attr_dict = _AttributeDict({'foo': {'bar': [1, 2, 3]}, 'baz': True, '__reserved': True})

            self.assertDeepEqual(attr_dict['foo'], {'bar': [1, 2, 3]})
            self.assertDeepEqual(attr_dict['baz'], True)

            attr_dict.foo = {}
            attr_dict.baz = {}

            self.assertDeepEqual(attr_dict['foo'], {})

            with self.assertRaises(KeyError):
                attr_dict['foo']['bar']

            self.assertDeepEqual(attr_dict['baz'], {})

    def test_del_attribute(self):
        for _AttributeDict in [AttributeDict, CustomAttributeDict]:
            attr_dict = _AttributeDict()

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

            attr_dict = _AttributeDict(None)

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

            attr_dict = _AttributeDict({})

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

            attr_dict = _AttributeDict({'foo': None, '__reserved': True})

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

            attr_dict = _AttributeDict({'foo': {'bar': [1, 2, 3]}, '__reserved': True})

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

            attr_dict = _AttributeDict({'foo': {'bar': [1, 2, 3]}, 'baz': True, '__reserved': True})

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
        for _AttributeDict in [AttributeDict, CustomAttributeDict]:
            attr_dict = _AttributeDict()

            self.assertEqual(str(attr_dict), "{}")

            # None

            attr_dict = _AttributeDict(None)

            self.assertEqual(str(attr_dict), "{}")

            # {}

            attr_dict = _AttributeDict({})

            self.assertEqual(str(attr_dict), "{}")

            # {'foo': NONE}

            attr_dict = _AttributeDict({'foo': None, '__reserved': True})

            self.assertEqual(str(attr_dict), "{'foo': None}")

            # {'foo': {'bar': [1, 2, 3]}}

            attr_dict = _AttributeDict({'foo': {'bar': [1, 2, 3]}, '__reserved': True})

            self.assertEqual(str(attr_dict), "{'foo': {'bar': [1, 2, 3]}}")

            # {'foo': {'bar': [1, 2, 3]}, 'baz': True}

            attr_dict = _AttributeDict({'foo': {'bar': [1, 2, 3]}, 'baz': True, '__reserved': True})

            self.assertEqual(str(attr_dict), "{'foo': {'bar': [1, 2, 3]}, 'baz': True}")

    def test_repr(self):
        for _AttributeDict in [AttributeDict, CustomAttributeDict]:
            attr_dict = _AttributeDict()

            self.assertEqual(repr(attr_dict), "{}")

            # None

            attr_dict = _AttributeDict(None)

            self.assertEqual(repr(attr_dict), "{}")

            # {}

            attr_dict = _AttributeDict({})

            self.assertEqual(repr(attr_dict), "{}")

            # {'foo': NONE}

            attr_dict = _AttributeDict({'foo': None, '__reserved': True})

            self.assertEqual(repr(attr_dict), "{'foo': None}")

            # {'foo': {'bar': [1, 2, 3]}}

            attr_dict = _AttributeDict({'foo': {'bar': [1, 2, 3]}, '__reserved': True})

            self.assertEqual(repr(attr_dict), "{'foo': {'bar': [1, 2, 3]}}")

            # {'foo': {'bar': [1, 2, 3]}, 'baz': True}

            attr_dict = _AttributeDict({'foo': {'bar': [1, 2, 3]}, 'baz': True, '__reserved': True})

            self.assertEqual(repr(attr_dict), "{'foo': {'bar': [1, 2, 3]}, 'baz': True}")

    def test_dir(self):
        for _AttributeDict in [AttributeDict, CustomAttributeDict]:
            attr_dict = _AttributeDict()

            with self.assertNotRaises(Exception):
                dir(attr_dict)

    def test_init_encode(self):
        for _AttributeDict in [AttributeDict, CustomAttributeDict]:
            attr_dict = _AttributeDict()

            self.assertDeepEqual(helper.json_encode(attr_dict), '{}')
            # self.assertDeepEqual(helper.json_encode(attr_dict.__dict__), '{}')

            attr_dict = _AttributeDict(None)

            self.assertDeepEqual(helper.json_encode(attr_dict), '{}')
            # self.assertDeepEqual(helper.json_encode(attr_dict.__dict__), '{}')

            attr_dict = _AttributeDict({})

            self.assertDeepEqual(helper.json_encode(attr_dict), '{}')
            # self.assertDeepEqual(helper.json_encode(attr_dict.__dict__), '{}')

            attr_dict = _AttributeDict({'foo': None, '__reserved': True})

            self.assertDeepEqual(helper.json_encode(attr_dict), '{"foo":null}')
            # self.assertDeepEqual(helper.json_encode(attr_dict.__dict__), '{"foo":null}')

            attr_dict = _AttributeDict({'foo': {}, '__reserved': True})

            self.assertDeepEqual(helper.json_encode(attr_dict), '{"foo":{}}')
            # self.assertDeepEqual(helper.json_encode(attr_dict.__dict__), '{"foo":{}}')

            attr_dict = _AttributeDict({'foo': {'bar': [1, 2, 3]}, '__reserved': True})

            self.assertDeepEqual(helper.json_encode(attr_dict), '{"foo":{"bar":[1,2,3]}}')
            # self.assertDeepEqual(helper.json_encode(attr_dict.__dict__), '{"foo":{"bar":[1,2,3]}}')

    def test_key_encode(self):
        for _AttributeDict in [AttributeDict, CustomAttributeDict]:
            attr_dict = _AttributeDict()

            attr_dict['foo'] = None

            self.assertDeepEqual(helper.json_encode(attr_dict), '{"foo":null}')
            self.assertDeepEqual(helper.json_encode(attr_dict.__dict__), '{"foo":null}')

            attr_dict['foo'] = {}

            self.assertDeepEqual(helper.json_encode(attr_dict), '{"foo":{}}')
            self.assertDeepEqual(helper.json_encode(attr_dict.__dict__), '{"foo":{}}')

            attr_dict['foo'] = {'bar': [1, 2, 3], '__reserved': True}

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
        for _AttributeDict in [AttributeDict, CustomAttributeDict]:
            attr_dict = _AttributeDict()

            attr_dict.foo = None

            self.assertDeepEqual(helper.json_encode(attr_dict), '{"foo":null}')
            self.assertDeepEqual(helper.json_encode(attr_dict.__dict__), '{"foo":null}')

            attr_dict.foo = {}

            self.assertDeepEqual(helper.json_encode(attr_dict), '{"foo":{}}')
            self.assertDeepEqual(helper.json_encode(attr_dict.__dict__), '{"foo":{}}')

            attr_dict.foo = {'bar': [1, 2, 3], '__reserved': True}

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
        for _AttributeDict in [AttributeDict, CustomAttributeDict]:
            with self.assertRaises(TypeError):
                _AttributeDict().fromkeys()

            attr_dict = _AttributeDict().fromkeys([])

            self.assertDeepEqual(attr_dict, {})

            attr_dict = _AttributeDict().fromkeys(['foo'])

            self.assertDeepEqual(attr_dict, {'foo': None})

            attr_dict = _AttributeDict().fromkeys(['foo'], 'default')

            self.assertDeepEqual(attr_dict, {'foo': 'default'})

            attr_dict = _AttributeDict().fromkeys(['foo', 'bar'])

            self.assertDeepEqual(attr_dict, {'foo': None, 'bar': None})

            attr_dict = _AttributeDict().fromkeys(['foo', 'bar'], 'default')

            self.assertDeepEqual(attr_dict, {'foo': 'default', 'bar': 'default'})

    def test_to_dict(self):
        for _AttributeDict in [AttributeDict, CustomAttributeDict]:
            native_dict = _AttributeDict().to_dict()

            self.assertTrue(isinstance(native_dict, dict))
            self.assertDeepEqual(native_dict, {})

            native_dict = _AttributeDict(None).to_dict()

            self.assertTrue(isinstance(native_dict, dict))
            self.assertDeepEqual(native_dict, {})

            native_dict = _AttributeDict({}).to_dict()

            self.assertTrue(isinstance(native_dict, dict))
            self.assertDeepEqual(native_dict, {})

            native_dict = {'foo': {'bar': 'baz'}}
            native_dict = _AttributeDict(native_dict).to_dict()

            self.assertTrue(isinstance(native_dict, dict))
            self.assertDeepEqual(native_dict, {'foo': {'bar': 'baz'}})

            attr_dict = _AttributeDict({'foo': {'bar': 'baz'}})
            native_dict = _AttributeDict(attr_dict).to_dict()

            self.assertTrue(isinstance(attr_dict, _AttributeDict))
            self.assertTrue(isinstance(native_dict, dict))
            self.assertDeepEqual(native_dict, {'foo': {'bar': 'baz'}})

    def test_class_to_dict(self):
        for _AttributeDict in [AttributeDict, CustomAttributeDict]:
            native_dict = _AttributeDict.dict()

            self.assertTrue(isinstance(native_dict, dict))
            self.assertDeepEqual(native_dict, {})

            native_dict = _AttributeDict.dict(None)

            self.assertTrue(not isinstance(native_dict, dict))
            self.assertDeepEqual(native_dict, None)

            native_dict = _AttributeDict.dict({})

            self.assertTrue(isinstance(native_dict, dict))
            self.assertDeepEqual(native_dict, {})

            native_dict = {'foo': {'bar': 'baz'}}
            native_dict = _AttributeDict.dict(native_dict)

            self.assertTrue(isinstance(native_dict, dict))
            self.assertDeepEqual(native_dict, {'foo': {'bar': 'baz'}})

            attr_dict = _AttributeDict({'foo': {'bar': 'baz'}})
            native_dict = _AttributeDict.dict(attr_dict)

            self.assertTrue(isinstance(attr_dict, _AttributeDict))
            self.assertTrue(isinstance(native_dict, dict))
            self.assertDeepEqual(native_dict, {'foo': {'bar': 'baz'}})


# =========================================
#       MAIN
# --------------------------------------

if __name__ == '__main__':
    helper.run(TestCase)
