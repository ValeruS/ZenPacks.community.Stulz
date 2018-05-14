##########################################################################
# Author:               ValeruS
#
# StulzAlarms object class
#
##########################################################################

from Globals import InitializeClass
from Products.ZenModel.DeviceComponent import DeviceComponent
from Products.ZenModel.ManagedEntity import ManagedEntity
from Products.ZenModel.ZenossSecurity import ZEN_CHANGE_DEVICE
from Products.ZenRelations.RelSchema import ToManyCont, ToOne

class StulzAlarms(DeviceComponent, ManagedEntity):
    meta_type = portal_type = "StulzAlarms"

    unitNamea                    = ""
    unitOnOffa                   = ""
    busida                       = 0
    unitida                      = 0
    generalError                 = 0
    busalarm                     = 0
    commonAlarm                  = 0
    waterDetector                = 0
    phasecheck                   = 0
    fireSmoke                    = 0

    _properties = ManagedEntity._properties + (
        {'id': 'unitNamea',                    'type': 'string', 'mode': ''},
        {'id': 'unitOnOffa',                   'type': 'string', 'mode': ''},
        {'id': 'busida',                       'type': 'int',    'mode': ''},
        {'id': 'unitida',                      'type': 'int',    'mode': ''},
        {'id': 'generalError',                 'type': 'int',    'mode': ''},
        {'id': 'busalarm',                     'type': 'int',    'mode': ''},
        {'id': 'commonAlarm',                  'type': 'int',    'mode': ''},
        {'id': 'waterDetector',                'type': 'int',    'mode': ''},
        {'id': 'phasecheck',                   'type': 'int',    'mode': ''},
        {'id': 'fireSmoke',                    'type': 'int',    'mode': ''},
    )

    _relations = ManagedEntity._relations + (
        ('devStulzAlarms', ToOne(ToManyCont, 'ZenPacks.community.Stulz.StulzDevice', 'StulzAlarms', ),),
    )

    # Defining the "perfConf" action here causes the "Graphs" display to be
    # available for components of this type.
    factory_type_information = ({
        'id'             : 'StulzAlarms',
        'meta_type'      : 'StulzAlarms',
        'description'    : """Stulz alarms info""",
        'product'        : 'Stulz',
        'immediate_view' : 'viewStulzAlarms',
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
        return self.devStulzAlarms()

InitializeClass(StulzAlarms)
