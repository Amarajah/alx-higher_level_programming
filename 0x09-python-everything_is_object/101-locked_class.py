#!/usr/bin/python3
"""Defines a locked class."""


class LockedClass:
    """
    Prevent instantiation of any any attribute except
    first_name.
    """
    __slots__ = ["first_name"]
