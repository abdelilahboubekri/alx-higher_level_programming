#!/usr/bin/python3
"""Defines a locked class."""


class LockedClass:
    """
    LockedClass with no class or object attribute,
    That prevents the user from dynamically creating new instance attributes,
    except if the new instance attribute is called first_name.
    """

    __slots__ = ["first_name"]
