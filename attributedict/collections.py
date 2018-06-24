
# =========================================
#       DEPS
# --------------------------------------

import collections

from easypackage.syspath import syspath

syspath()

import attributedict.compat as compat


# =========================================
#       CLASSES
# --------------------------------------

class AttributeDict(dict):

    """
    :class:`~attributedict.collections.AttributeDict` is a seamlessly extended dictionary object (subclass of `dict`),
    with access to additional attribute get/set/delete of key/values.

    @example:

        data = AttributeDict({'foo': {'bar': [1, 2, 3]}})

        data.foo # => `{'bar': [1, 2, 3]}}`
        data.foo.bar # => `[1, 2, 3]`

        data.foo = {'baz': True}
        data.foo = # => `{'baz': True}`

        del data.foo

    """

    # def __init__(self, entries = {}):
    #     entries = entries or {}

    #     dict.__init__(self, entries)

    #     self.update(entries)

    def __init__(self, entries = {}):
        entries = entries or {}

        # dict.__init__(self, entries)
        super(AttributeDict, self).__init__(entries)

        self.update(entries)

    def _refresh(self):
        # HACK
        #
        # to make object encoding (e.g. `json` work), call `dict` constructor with updated data.
        #
        # it is terrible language design that this is the only way. >:/
        #
        # @see https://stackoverflow.com/questions/23088565/make-a-custom-class-json-serializable
        # @see https://stackoverflow.com/questions/2144988/python-multiple-calls-to-init-on-the-same-instance
        #
        # print('_refresh')
        dict.__init__(self, self.__dict__)

    def update(self, entries = {}, *args, **kwargs):
        """
        Update dictionary.

        @example:

            object.update({'foo': {'bar': 1}})

        """
        for key, value in dict(entries, *args, **kwargs).items():
            if isinstance(value, dict):
                self.__dict__[key] = AttributeDict(value)
            else:
                self.__dict__[key] = value

        self._refresh()

    def keys(self):
        return self.__dict__.keys()

    def values(self):
        return self.__dict__.values()

    def items(self, *args, **kwargs):
        return self.__dict__.items(*args, **kwargs)

    def iteritems(self, *args, **kwargs):
        self.__dict__.items(*args, **kwargs)

    def iterkeys(self, *args, **kwargs):
        self.__dict__.iterkeys(*args, **kwargs)

    def itervalues(self, *args, **kwargs):
        self.__dict__.itervalues(*args, **kwargs)

    def get(self, key, default = None):
        result = self.__dict__.get(key, default)

        return result

    def pop(self, key, value = None):
        result = self.__dict__.pop(key, value)

        self._refresh()

        return result

    def copy(self):
        return type(self)(self)

    def setdefault(self, key, default = None):
        result = self.__dict__.setdefault(key, default)

        self._refresh()

        return result

    def __getitem__(self, key):
        """
        Provides `dict` style property access to dictionary key-values.

        @example:

            value = object['key']

        """
        result = self.__dict__.__getitem__(key)

        self._refresh()

        return result

    def __setitem__(self, key, value):
        """
        Provides `dict` style property assignment to dictionary key-values.

        @example:

            object['key'] = value

        """
        if isinstance(value, dict):
            value = AttributeDict(value)

        result = self.__dict__.__setitem__(key, value)

        self._refresh()

        return result

    def __delitem__(self, key):
        """
        Provides `dict` style property deletion to dictionary key-values.

        @example:

            del object['key']

        """
        result = self.__dict__.__delitem__(key)

        self._refresh()

        return result

    def __getattr__(self, key):
        """
        Provides `object` style attribute access to dictionary key-values.

        @example:

            value = object.key

        """
        try:
            return self.__getitem__(key)

        except Exception as error:
            raise AttributeError(error)

    def __setattr__(self, key, value):
        """
        Provides `object` style attribute assignment to dictionary key-values.

        @example:

            object.key = value

        """
        try:
            return self.__setitem__(key, value)

        except Exception as error:
            raise AttributeError(error)

    def __delattr__(self, key):
        """
        Provides `object` style attribute deletion to dictionary key-values.

        @example:

            del object.key

        """
        try:
            return self.__delitem__(key)

        except Exception as error:
            raise AttributeError(error)

    def __str__(self):
        """
        String value of the dictionary instance.
        """
        return str(self.__dict__)

    def __repr__(self):
        """
        String representation of the dictionary instance.
        """
        return repr(self.__dict__)

    def __dir__(self):
        return dir(type(self)) + list(self.__dict__.keys())

    def __iter__(self):
        """
        Iterate over dictionary key/values.
        """
        return iter(self.__dict__.keys())

    def __len__(self):
        """
        Get number of items.
        """
        return len(self.__dict__.keys())

    def __contains__(self, key):
        """
        Check if key exists.
        """
        return self.__dict__.__contains__(key)

    def __reduce__(self):
        """
        Return state information for pickling.
        """
        return self.__dict__.__contains__(key)

    def __eq__(self, other):
        """
        Check dictionary is equal to another provided dictionary.
        """
        return self.__dict__.__eq__(other)

    def __ne__(self, other):
        """
        Check dictionary is inequal to another provided dictionary.
        """
        return self.__dict__.__ne__(other)

    @classmethod
    def fromkeys(klass, keys, value = None):
        return AttributeDict(dict.fromkeys((key for key in keys), value))


# =========================================
#       ALIASES
# --------------------------------------

attributedict = AttributeDict
attrdict = AttributeDict


# =========================================
#       MAIN
# --------------------------------------

if __name__ == '__main__':

    from easypackage.utils.banner import banner

    with banner(__file__):
        data = {
            'a': {
                'b': {
                    'c': [1, 2, 3]
                }
            }
        }

        object = AttributeDict(data)

        print('object = AttributeDict({0})\n'.format(data))

        print('object\n\n\t{0}\n'.format(object))
        print('object.a\n\n\t{0}\n'.format(object.a))
        print('object.a.b\n\n\t{0}\n'.format(object.a.b))
        print('object.a.b.c\n\n\t{0}\n'.format(object.a.b.c))
