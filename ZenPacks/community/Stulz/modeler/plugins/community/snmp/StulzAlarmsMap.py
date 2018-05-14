##########################################################################
# Author:               ValeruS
#
# StulzAlarmsMap modeler plugin
#
##########################################################################

__doc__ = """StulzAlarmsMap

Gather table information from Stulz Device.
"""

from Products.DataCollector.plugins.CollectorPlugin import SnmpPlugin, GetTableMap
from Products.DataCollector.plugins.DataMaps import ObjectMap

class StulzAlarmsMap(SnmpPlugin):
    """StulzAlarmsMap"""

    maptype = "StulzAlarmsMap"
    modname = "ZenPacks.community.Stulz.StulzAlarms"
    relname = "StulzAlarms"


    snmpGetTableMaps = (
        GetTableMap('StulzInfoComponentsEntry',
                    '.1.3.6.1.4.1.29462.10',
                    {
                       '.1.1.6.1.1.393221'     : 'unitNamea',
                       '.2.1.4.1.1.1.1013'     : 'unitOnOffa',
                       '.2.1.4.2.1.1.8'        : 'generalError',
                       '.2.1.4.1.1.1.10'       : 'busalarm',
                       '.2.1.4.4.1.1.1.1010'   : 'commonAlarm',
                       '.2.1.4.4.1.1.1.8505'   : 'waterDetector',
                       '.2.1.4.4.1.1.1.8506'   : 'phasecheck',
                       '.2.1.4.4.1.1.1.8507'   : 'fireSmoke',
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

        StulzInfoEntry = tabledata.get('StulzInfoComponentsEntry')

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
                om.unitOnOffa = self.OnOff.get(int(om.unitOnOffa), 'unknown')
                stulzid = oid.split('.')
                om.busida = stulzid[0]
                om.unitida = stulzid[1]
                om.id = self.prepId(om.unitNamea)
            except (KeyError, IndexError, AttributeError, TypeError), errorInfo:
                log.warn( ' Error in StulzAlarmsMap modeler plugin %s', errorInfo)
                continue
            rm.append(om)
        return rm
