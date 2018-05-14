##########################################################################
# Author:               ValeruS
#
# StulzTemperature object class
#
##########################################################################

from Globals import InitializeClass
from Products.ZenModel.DeviceComponent import DeviceComponent
from Products.ZenModel.ManagedEntity import ManagedEntity
from Products.ZenModel.ZenossSecurity import ZEN_CHANGE_DEVICE
from Products.ZenRelations.RelSchema import ToManyCont, ToOne

class StulzTemperature(DeviceComponent, ManagedEntity):
    meta_type = portal_type = "StulzTemperature"

    unitNamet                   = ""
    unitOnOfft                  = ""
    busidt                      = 0
    unitidt                     = 0
    unitAirTemperature          = 0
    unitReturnAirTemperature    = 0
    unitHumidity                = 0
    unitReturnAirHumidity       = 0
    limitAirTempHigh            = 0

    _properties = ManagedEntity._properties + (
        {'id': 'unitNamet',                 'type': 'string', 'mode': ''},
        {'id': 'unitOnOfft',                'type': 'string', 'mode': ''},
        {'id': 'busidt',                    'type': 'int',    'mode': ''},
        {'id': 'unitidt',                   'type': 'int',    'mode': ''},
        {'id': 'unitAirTemperature',        'type': 'int',    'mode': ''},
        {'id': 'unitReturnAirTemperature',  'type': 'int',    'mode': ''},
        {'id': 'unitHumidity',              'type': 'int',    'mode': ''},
        {'id': 'unitReturnAirHumidity',     'type': 'int',    'mode': ''},
        {'id': 'limitAirTempHigh',          'type': 'int',    'mode': ''},
    )

    _relations = ManagedEntity._relations + (
        ('devStulzTemperature', ToOne(ToManyCont, 'ZenPacks.community.Stulz.StulzDevice', 'StulzTemperature', ),),
    )

    # Defining the "perfConf" action here causes the "Graphs" display to be
    # available for components of this type.
    factory_type_information = ({
        'id'             : 'StulzTemperature',
        'meta_type'      : 'StulzTemperature',
        'description'    : """Stulz temperature info""",
        'product'        : 'Stulz',
        'immediate_view' : 'viewStulzTemperature',
        'actions'        : 
        (
           {'id'            : 'perfConf',
            'name'          : 'Template',
            'action'        : 'objTemplates',
            'permissions'   : (ZEN_CHANGE_DEVICE,),
           },
        ),
    },)


    # Custom components must always implement the device method. The method
    # should return the device object that contains the component.
    def device(self):
        return self.devStulzTemperature()

InitializeClass(StulzTemperature)
