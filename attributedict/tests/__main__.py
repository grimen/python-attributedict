
# =========================================
#       DEPS
# --------------------------------------

from os import path

from easypackage.syspath import syspath

syspath()

from attributedict.tests import helper

# =========================================
#       RUN
# --------------------------------------

suite = helper.suite(path.abspath(path.dirname(__file__)))

helper.run(suite)
