##########################################################################
# Author:               ValeruS
#
# StulzComponents object class
#
##########################################################################

from Globals import InitializeClass
from Products.ZenModel.DeviceComponent import DeviceComponent
from Products.ZenModel.ManagedEntity import ManagedEntity
from Products.ZenModel.ZenossSecurity import ZEN_CHANGE_DEVICE
from Products.ZenRelations.RelSchema import ToManyCont, ToOne

class StulzComponents(DeviceComponent, ManagedEntity):
    meta_type = portal_type = "StulzComponents"

    unitNamec                   = ""
    unitOnOffc                  = ""
    busidc                      = 0
    unitidc                     = 0
    compr1Running               = 0
    elecHeating1Running         = 0
    humidifier1Running          = 0
    fan1Running                 = 0
    fan1Speed                   = 0
    louver1Open                 = 0

    _properties = ManagedEntity._properties + (
        {'id': 'unitNamec',                 'type': 'string', 'mode': ''},
        {'id': 'unitOnOffc',                'type': 'string', 'mode': ''},
        {'id': 'busidc',                    'type': 'int',    'mode': ''},
        {'id': 'unitidc',                   'type': 'int',    'mode': ''},
        {'id': 'compr1Running',             'type': 'int',    'mode': ''},
        {'id': 'elecHeating1Running',       'type': 'int',    'mode': ''},
        {'id': 'humidifier1Running',        'type': 'int',    'mode': ''},
        {'id': 'fan1Running',               'type': 'int',    'mode': ''},
        {'id': 'fan1Speed',                 'type': 'int',    'mode': ''},
        {'id': 'louver1Open',               'type': 'int',    'mode': ''},
    )

    _relations = ManagedEntity._relations + (
        ('devStulzComponents', ToOne(ToManyCont, 'ZenPacks.community.Stulz.StulzDevice', 'StulzComponents', ),),
    )

    # Defining the "perfConf" action here causes the "Graphs" display to be
    # available for components of this type.
    factory_type_information = ({
        'id'             : 'StulzComponents',
        'meta_type'      : 'StulzComponents',
        'description'    : """Stulz components info""",
        'product'        : 'Stulz',
        'immediate_view' : 'viewStulzComponents',
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
        return self.devStulzComponents()

InitializeClass(StulzComponents)
