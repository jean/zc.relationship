##############################################################################
#
# Copyright (c) 2004 Zope Corporation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""intid-based containers

$Id$
"""
from zope import interface, component
from BTrees import IOBTree, OOBTree, OIBTree, IIBTree

from zope.app.intid.interfaces import IIntIds

from zc.relationship import interfaces, shared

def Container():
    res = shared.Container()
    interface.alsoProvides(res, interfaces.IIntIdRelationshipContainer)
    return res
