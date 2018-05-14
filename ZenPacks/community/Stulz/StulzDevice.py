##########################################################################
# Author:               ValeruS
#
# StulzDevice object class
#
##########################################################################


from Globals import InitializeClass

from Products.ZenModel.Device import Device
from Products.ZenRelations.RelSchema import ToManyCont, ToOne
from Products.ZenModel.ZenossSecurity import ZEN_VIEW

from copy import deepcopy

class StulzDevice(Device):
    "Stulz Device"
    meta_type = portal_type = 'StulzDevice'


    _relations = Device._relations + (
        ('StulzTemperature', ToManyCont(ToOne, 'ZenPacks.community.Stulz.StulzTemperature',  'devStulzTemperature',),),
        ('StulzComponents',  ToManyCont(ToOne, 'ZenPacks.community.Stulz.StulzComponents',   'devStulzComponents',),),
        ('StulzRunTimes',    ToManyCont(ToOne, 'ZenPacks.community.Stulz.StulzRunTimes',     'devStulzRunTimes',),),
        ('StulzAlarms',      ToManyCont(ToOne, 'ZenPacks.community.Stulz.StulzAlarms',       'devStulzAlarms',),),
    )

InitializeClass(StulzDevice)
