# SPDX-Copyright: 2019 Free Software Foundation Europe e.V.
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""All tests for reuse._comment.

A lot of SPDX tags are explicitly wrong in this module, and replaced with the
tags REUSE-Copyright and REUSE-License-Identifier. This makes it easier for the
project itself to remain REUSE compliant.
"""

from inspect import cleandoc

from reuse._comment import create_comment, parse_comment


def test_create_comment_python():
    """Create a simple Python comment."""
    text = cleandoc(
        """
        REUSE-Copyright: Mary Sue

        REUSE-License-Identifier: GPL-3.0-or-later
        """
    )

    expected = cleandoc(
        """
        # REUSE-Copyright: Mary Sue
        #
        # REUSE-License-Identifier: GPL-3.0-or-later
        """
    )

    assert create_comment(text) == expected


def test_parse_comment_python():
    """Parse a simple Python comment."""
    text = cleandoc(
        """
        # REUSE-Copyright: Mary Sue
        #
        # REUSE-License-Identifier: GPL-3.0-or-later
        """
    )

    expected = cleandoc(
        """
        REUSE-Copyright: Mary Sue

        REUSE-License-Identifier: GPL-3.0-or-later
        """
    )

    assert parse_comment(text) == expected
