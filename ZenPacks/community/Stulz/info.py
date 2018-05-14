##########################################################################
# Author:               ValeruS
#
# info.py for Stulz ZenPack
#
################################################################################

from zope.interface import implements
from Products.Zuul.infos import ProxyProperty
from Products.Zuul.infos.device import DeviceInfo
from Products.Zuul.infos.component import ComponentInfo
from Products.Zuul.decorators import info

from ZenPacks.community.Stulz import interfaces


class StulzTemperatureInfo(ComponentInfo):
    implements(interfaces.IStulzTemperatureInfo)
    unitNamet                    = ProxyProperty("unitNamet")
    unitOnOfft                   = ProxyProperty("unitOnOfft")
    busidt                       = ProxyProperty("busidt")
    unitidt                      = ProxyProperty("unitidt")
    unitAirTemperature           = ProxyProperty("unitAirTemperature")
    unitReturnAirTemperature     = ProxyProperty("unitReturnAirTemperature")
    unitHumidity                 = ProxyProperty("unitHumidity")
    unitReturnAirHumidity        = ProxyProperty("unitReturnAirHumidity")
    limitAirTempHigh             = ProxyProperty("limitAirTempHigh")

class StulzComponentsInfo(ComponentInfo):
    implements(interfaces.IStulzComponentsInfo)
    unitNamec                    = ProxyProperty("unitNamec")
    unitOnOffc                   = ProxyProperty("unitOnOffc")
    busidc                       = ProxyProperty("busidc")
    unitidc                      = ProxyProperty("unitidc")
    compr1Running                = ProxyProperty("compr1Running")
    elecHeating1Running          = ProxyProperty("elecHeating1Running")
    humidifier1Running           = ProxyProperty("humidifier1Running")
    fan1Running                  = ProxyProperty("fan1Running")
    fan1Speed                    = ProxyProperty("fan1Speed")
    louver1Open                  = ProxyProperty("louver1Open")

class StulzRunTimesInfo(ComponentInfo):
    implements(interfaces.IStulzRunTimesInfo)
    unitNamer                    = ProxyProperty("unitNamer")
    unitOnOffr                   = ProxyProperty("unitOnOffr")
    busidr                       = ProxyProperty("busidr")
    unitidr                      = ProxyProperty("unitidr")
    unitRuntimeUnit              = ProxyProperty("unitRuntimeUnit")
    unitStoptimeUnit             = ProxyProperty("unitStoptimeUnit")
    unitRuntimeCooling           = ProxyProperty("unitRuntimeCooling")
    unitRuntimeHeating           = ProxyProperty("unitRuntimeHeating")
    unitRuntimeHumidification    = ProxyProperty("unitRuntimeHumidification")
    unitRuntimeDehumidification  = ProxyProperty("unitRuntimeDehumidification")
    compr1Runtime                = ProxyProperty("compr1Runtime")
    fan1Runtime                  = ProxyProperty("fan1Runtime")
    elecHeating1Runtime          = ProxyProperty("elecHeating1Runtime")

class StulzAlarmsInfo(ComponentInfo):
    implements(interfaces.IStulzAlarmsInfo)
    unitNamea                    = ProxyProperty("unitNamea")
    unitOnOffa                   = ProxyProperty("unitOnOffa")
    busida                       = ProxyProperty("busida")
    unitida                      = ProxyProperty("unitida")
    generalError                 = ProxyProperty("generalError")
    busalarm                     = ProxyProperty("busalarm")
    commonAlarm                  = ProxyProperty("commonAlarm")
    waterDetector                = ProxyProperty("waterDetector")
    phasecheck                   = ProxyProperty("phasecheck")
    fireSmoke                    = ProxyProperty("fireSmoke")
