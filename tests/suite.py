# pyCI
# Copyright (C) 2014  Torsten Braun
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

import unittest
import sys
import os
sys.path.insert(0, os.path.abspath('..'))


from tests.pyCI.html.helper import test_badges
from tests.pyCI.util import test_slug, test_config, test_log, test_db


all_tests = unittest.TestSuite([
    test_badges.suite(),
    test_slug.suite(),
    test_config.suite(),
    test_log.suite(),
    test_db.suite(),
])


if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2, stream=sys.stdout)
    result = runner.run(all_tests)

    if len(result.errors) > 0 or len(result.failures) > 0:
        sys.exit(-1)
