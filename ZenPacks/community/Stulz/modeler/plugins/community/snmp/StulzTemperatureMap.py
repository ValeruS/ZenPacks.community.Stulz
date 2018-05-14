##########################################################################
# Author:               ValeruS
#
# StulzTemperatureMap modeler plugin
#
##########################################################################

__doc__ = """StulzTemperatureMap

Gather table information from Stulz Device.
"""

from Products.DataCollector.plugins.CollectorPlugin import SnmpPlugin, GetTableMap
from Products.DataCollector.plugins.DataMaps import ObjectMap

class StulzTemperatureMap(SnmpPlugin):
    """StulzTemperatureMap"""

    maptype = "StulzTemperatureMap"
    modname = "ZenPacks.community.Stulz.StulzTemperature"
    relname = "StulzTemperature"


    snmpGetTableMaps = (
        GetTableMap('StulzInfoValuesEntry',
                    '.1.3.6.1.4.1.29462.10',
                    {
                       '.1.1.6.1.1.393221'     : 'unitNamet',
                       '.2.1.4.1.1.1.1013'     : 'unitOnOfft',
                       '.2.1.1.1.1.1.1.1.1170' : 'unitAirTemperature',
                       '.2.1.1.1.1.1.1.1.1192' : 'unitReturnAirTemperature',
                       '.2.1.1.1.1.2.1.1.1171' : 'unitHumidity',
                       '.2.1.1.1.1.2.1.1.1194' : 'unitReturnAirHumidity',
                       '.2.1.2.1.1.1.1.1.2239' : 'limitAirTempHigh',
                    }
        ),
    )

    OnOff   = {1:'On',0:'Off',}

    def process(self, device, results, log):
        """collect snmp information from this device"""
        log.info('processing %s for device %s', self.name(), device.id)
        getdata, tabledata = results
#        log.info( "Table = %s", tabledata )
        rm = self.relMap()

        StulzInfoEntry = tabledata.get('StulzInfoValuesEntry')

# If no data supplied then simply return
        if not StulzInfoEntry:
            log.warn( 'No SNMP response from %s for the %s plugin', device.id, self.name() )
            log.warn( "Data= %s", tabledata )
            return

        StulzEntry = {}
        for key in StulzInfoEntry:
            if (key[:1] == "1" or key[:1] == "2") and len(key) == 3:
               dict1 = StulzInfoEntry[key]
               dict2 = StulzInfoEntry[key+".1"]
               dict1.update(dict2)
               StulzEntry[key+".1"] = dict1

        for oid, data in StulzEntry.items():
            try:
                om = self.objectMap(data)
                om.snmpindex = oid.strip('.')
                om.unitOnOfft = self.OnOff.get(int(om.unitOnOfft), 'unknown')
                stulzid = oid.split('.')
                om.busidt = stulzid[0]
                om.unitidt = stulzid[1]
                om.id = self.prepId(om.unitNamet)
            except (KeyError, IndexError, AttributeError, TypeError), errorInfo:
                log.warn( ' Error in StulzTemperatureMap modeler plugin %s', errorInfo)
                continue
            rm.append(om)
        return rm
