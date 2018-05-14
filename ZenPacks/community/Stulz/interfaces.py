##########################################################################
# Author:               ValeruS
#
# interfaces.py for Stulz ZenPack
#
################################################################################

from Products.Zuul.form import schema
from Products.Zuul.interfaces.device import IDeviceInfo
from Products.Zuul.interfaces.component import IComponentInfo
from Products.Zuul.utils import ZuulMessageFactory as _t

from Products.ZenModel.ZVersion import VERSION as ZENOSS_VERSION
from Products.ZenUtils.Version import Version

if Version.parse('Zenoss %s' % ZENOSS_VERSION) >= Version.parse('Zenoss 4'):
    SingleLineText = schema.TextLine
    MultiLineText = schema.Text
else:
    SingleLineText = schema.Text
    MultiLineText = schema.TextLine


class IStulzTemperatureInfo(IComponentInfo):
    unitNamet                    = SingleLineText(title=_t(u"Unit Name"))
    unitOnOfft                   = SingleLineText(title=_t(u"Unit On/Off"))
    busidt                       = SingleLineText(title=_t(u"Bus ID"))
    unitidt                      = SingleLineText(title=_t(u"Unit ID"))
    unitAirTemperature           = SingleLineText(title=_t(u"Unit Temperature"))
    unitReturnAirTemperature     = SingleLineText(title=_t(u"Return Temperature"))
    unitHumidity                 = SingleLineText(title=_t(u"Unit Humidity"))
    unitReturnAirHumidity        = SingleLineText(title=_t(u"Return Humidity"))

class IStulzComponentsInfo(IComponentInfo):
    unitNamec                    = SingleLineText(title=_t(u"Unit ID"))
    unitOnOffc                   = SingleLineText(title=_t(u"Unit On/Off"))
    busidc                       = SingleLineText(title=_t(u"Bus ID"))
    unitidc                      = SingleLineText(title=_t(u"Unit ID"))
    compr1Running                = SingleLineText(title=_t(u"Compressor Running"))
    elecHeating1Running          = SingleLineText(title=_t(u"Heating Running"))
    humidifier1Running           = SingleLineText(title=_t(u"Humidifier Running"))
    fan1Running                  = SingleLineText(title=_t(u"Fun Running"))
    fan1Speed                    = SingleLineText(title=_t(u"Fun Speed"))
    louver1Open                  = SingleLineText(title=_t(u"Louver"))

class IStulzRunTimesInfo(IComponentInfo):
    unitNamer                    = SingleLineText(title=_t(u"Unit ID"))
    unitOnOffr                   = SingleLineText(title=_t(u"Unit On/Off"))
    busidr                       = SingleLineText(title=_t(u"Bus ID"))
    unitidr                      = SingleLineText(title=_t(u"Unit ID"))
    unitRuntimeUnit              = SingleLineText(title=_t(u"Unit Run Time"))
    unitStoptimeUnit             = SingleLineText(title=_t(u"Unit Stop Time"))
    unitRuntimeCooling           = SingleLineText(title=_t(u"Run Time Cooling"))
    unitRuntimeHeating           = SingleLineText(title=_t(u"Run Time Heating"))
    unitRuntimeHumidification    = SingleLineText(title=_t(u"Run Time Humidification"))
    unitRuntimeDehumidification  = SingleLineText(title=_t(u"Run Time Dehumidification"))
    compr1Runtime                = SingleLineText(title=_t(u"Run Time Compressor"))
    fan1Runtime                  = SingleLineText(title=_t(u"Run Time Fan"))
    elecHeating1Runtime          = SingleLineText(title=_t(u"Run Time ElecHeating"))

class IStulzAlarmsInfo(IComponentInfo):
    unitNamea                    = SingleLineText(title=_t(u"Unit ID"))
    unitOnOffa                   = SingleLineText(title=_t(u"Unit On/Off"))
    busida                       = SingleLineText(title=_t(u"Bus ID"))
    unitida                      = SingleLineText(title=_t(u"Unit ID"))
    generalError                 = SingleLineText(title=_t(u"General Error"))
    busalarm                     = SingleLineText(title=_t(u"Bus Alarm"))
    commonAlarm                  = SingleLineText(title=_t(u"Common Alarm"))
    waterDetector                = SingleLineText(title=_t(u"Water Detector"))
    phasecheck                   = SingleLineText(title=_t(u"Phase Check"))
    fireSmoke                    = SingleLineText(title=_t(u"Fire Smoke"))
