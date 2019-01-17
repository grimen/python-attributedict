
# =========================================
#       DEPS
# --------------------------------------

from os import path

import rootpath

rootpath.append()

from attributedict.tests import helper

# =========================================
#       RUN
# --------------------------------------

suite = helper.suite(path.abspath(path.dirname(__file__)))

helper.run(suite)
