
# `AttributeDict` [![Build Status](https://travis-ci.com/grimen/python-attributedict.svg?branch=master)](https://travis-ci.com/grimen/python-attributedict)

*A dictionary object with attributes support.*


## Install

Install using **pip**:

```sh
$ pip install attributedict
```


## Usage

Example:

```python
from attributedict.collections import AttributeDict

data = AttributeDict({'foo': {'bar': [1, 2, 3]}})

data.foo # => `{'bar': [1, 2, 3]}}`
data.foo.bar # => `[1, 2, 3]`

data.foo = {'baz': True}
data.foo = # => `{'baz': True}`

del data.foo.baz

# and/or...

data = AttributeDict({'foo': {'bar': [1, 2, 3]}})

data['foo'] # => `{'bar': [1, 2, 3]}}`
data['foo']['bar'] # => `[1, 2, 3]`

data['foo'] = {'baz': True}
data['foo'] = # => `{'baz': True}`

del data['foo']['baz']

# instance of `dict`...

isinstance(data, dict) # => True
isinstance(data, attributedict.collections.AttributeDict) # => True

isinstance(data.__dict__, dict) # => True
isinstance(data.__dict__, attributedict.collections.AttributeDict) # => False

# no need for custom encoders...

data = AttributeDict({'foo': {'bar': [1, 2, 3]}})

json.dumps(data) # => `{"foo": {"bar": [1, 2, 3]}}`
json.dumps(data.__dict__) # => `{"foo": {"bar": [1, 2, 3]}}`

# etc.

```


## Test

Clone down source code and run:

```sh
$ make install
$ make test
```


## License

Released under the MIT license.
