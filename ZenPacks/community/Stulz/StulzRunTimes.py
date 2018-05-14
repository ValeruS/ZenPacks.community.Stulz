##########################################################################
# Author:               ValeruS
#
# StulzRunTimes object class
#
##########################################################################

from Globals import InitializeClass
from Products.ZenModel.DeviceComponent import DeviceComponent
from Products.ZenModel.ManagedEntity import ManagedEntity
from Products.ZenModel.ZenossSecurity import ZEN_CHANGE_DEVICE
from Products.ZenRelations.RelSchema import ToManyCont, ToOne

class StulzRunTimes(DeviceComponent, ManagedEntity):
    meta_type = portal_type = "StulzRunTimes"

    unitNamer                    = ""
    unitOnOffr                   = ""
    busidr                       = 0
    unitidr                      = 0
    unitRuntimeUnit              = 0
    unitStoptimeUnit             = 0
    unitRuntimeCooling           = 0
    unitRuntimeHeating           = 0
    unitRuntimeHumidification    = 0
    unitRuntimeDehumidification  = 0
    compr1Runtime                = 0
    fan1Runtime                  = 0
    elecHeating1Runtime          = 0

    _properties = ManagedEntity._properties + (
        {'id': 'unitNamer',                    'type': 'string', 'mode': ''},
        {'id': 'unitOnOffr',                   'type': 'string', 'mode': ''},
        {'id': 'busidr',                       'type': 'int',    'mode': ''},
        {'id': 'unitidr',                      'type': 'int',    'mode': ''},
        {'id': 'unitRuntimeUnit',              'type': 'int',    'mode': ''},
        {'id': 'unitStoptimeUnit',             'type': 'int',    'mode': ''},
        {'id': 'unitRuntimeCooling',           'type': 'int',    'mode': ''},
        {'id': 'unitRuntimeHeating',           'type': 'int',    'mode': ''},
        {'id': 'unitRuntimeHumidification',    'type': 'int',    'mode': ''},
        {'id': 'unitRuntimeDehumidification',  'type': 'int',    'mode': ''},
        {'id': 'compr1Runtime',                'type': 'int',    'mode': ''},
        {'id': 'fan1Runtime',                  'type': 'int',    'mode': ''},
        {'id': 'elecHeating1Runtime',          'type': 'int',    'mode': ''},
    )

    _relations = ManagedEntity._relations + (
        ('devStulzRunTimes', ToOne(ToManyCont, 'ZenPacks.community.Stulz.StulzDevice', 'StulzRunTimes', ),),
    )

    # Defining the "perfConf" action here causes the "Graphs" display to be
    # available for components of this type.
    factory_type_information = ({
        'id'             : 'StulzRunTimes',
        'meta_type'      : 'StulzRunTimes',
        'description'    : """Stulz run times info""",
        'product'        : 'Stulz',
        'immediate_view' : 'viewStulzRunTimes',
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
        return self.devStulzRunTimes()

InitializeClass(StulzRunTimes)
