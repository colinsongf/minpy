#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Lazy evaluation of primitive selection."""
from __future__ import absolute_import
from __future__ import print_function
from ..utils import log
from . import policy

_logger = log.get_logger(__name__, log.DEBUG)


class PrimitiveSelector(object):
    __slots__ = ['_name', '_registry', '_policy']

    def __init__(self, name, reg, plc):
        self._name = name
        self._registry = reg
        self._policy = plc

    @property
    def name(self):
        return self._name

    def __call__(self, *args, **kwargs):
        f = policy.resolve_name(self._name, self._registry, self._policy, args,
                                kwargs)
        _logger.debug('Found primitive "{}" with type {}.'.format(self._name,
                                                                  f.typestr))
        return f(*args, **kwargs)
