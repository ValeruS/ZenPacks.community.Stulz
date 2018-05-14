##########################################################################
# Author:               ValeruS
#
# StulzRunTimesMap modeler plugin
#
##########################################################################

__doc__ = """StulzRunTimesMap

Gather table information from Stulz Device.
"""

from Products.DataCollector.plugins.CollectorPlugin import SnmpPlugin, GetTableMap
from Products.DataCollector.plugins.DataMaps import ObjectMap

class StulzRunTimesMap(SnmpPlugin):
    """StulzRunTimesMap"""

    maptype = "StulzRunTimesMap"
    modname = "ZenPacks.community.Stulz.StulzRunTimes"
    relname = "StulzRunTimes"


    snmpGetTableMaps = (
        GetTableMap('StulzInfoRunTimesEntry',
                    '.1.3.6.1.4.1.29462.10',
                    {
                       '.1.1.6.1.1.393221'       : 'unitNamer',
                       '.2.1.4.1.1.1.1013'       : 'unitOnOffr',
                       '.2.1.1.4.4.3.1.1164'     : 'unitRuntimeUnit',
                       '.2.1.1.4.4.3.1.1165'     : 'unitStoptimeUnit',
                       '.2.1.1.4.4.1.1.1.1166'   : 'unitRuntimeCooling',
                       '.2.1.1.4.4.1.1.1.1167'   : 'unitRuntimeHeating',
                       '.2.1.1.4.4.1.1.1.1168'   : 'unitRuntimeHumidification',
                       '.2.1.1.4.4.1.1.1.1169'   : 'unitRuntimeDehumidification',
                       '.2.1.1.4.4.2.1.1.1.4428' : 'compr1Runtime',
                       '.2.1.1.4.4.2.5.1.6931'   : 'fan1Runtime',
                       '.2.1.1.4.4.2.3.1.1.4816' : 'elecHeating1Runtime',
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

        StulzInfoEntry = tabledata.get('StulzInfoRunTimesEntry')

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
                om.unitOnOffr = self.OnOff.get(int(om.unitOnOffr), 'unknown')
                stulzid = oid.split('.')
                om.busidr = stulzid[0]
                om.unitidr = stulzid[1]
                om.id = self.prepId(om.unitNamer)
            except (KeyError, IndexError, AttributeError, TypeError), errorInfo:
                log.warn( ' Error in StulzRunTimesMap modeler plugin %s', errorInfo)
                continue
            rm.append(om)
        return rm
