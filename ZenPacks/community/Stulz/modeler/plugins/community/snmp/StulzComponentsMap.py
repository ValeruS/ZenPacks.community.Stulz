##########################################################################
# Author:               ValeruS
#
# StulzComponentsMap modeler plugin
#
##########################################################################

__doc__ = """StulzComponentsMap

Gather table information from Stulz Device.
"""

from Products.DataCollector.plugins.CollectorPlugin import SnmpPlugin, GetTableMap
from Products.DataCollector.plugins.DataMaps import ObjectMap

class StulzComponentsMap(SnmpPlugin):
    """StulzComponentsMap"""

    maptype = "StulzComponentsMap"
    modname = "ZenPacks.community.Stulz.StulzComponents"
    relname = "StulzComponents"


    snmpGetTableMaps = (
        GetTableMap('StulzInfoComponentsEntry',
                    '.1.3.6.1.4.1.29462.10',
                    {
                       '.1.1.6.1.1.393221'     : 'unitNamec',
                       '.2.1.4.1.1.1.1013'     : 'unitOnOffc',
                       '.2.1.1.2.1.1.1.1.4403' : 'compr1Running',
                       '.2.1.1.2.2.1.1.1.4803' : 'elecHeating1Running',
                       '.2.1.1.2.3.1.1.6402'   : 'humidifier1Running',
                       '.2.1.1.2.4.1.1.6902'   : 'fan1Running',
                       '.2.1.1.2.4.1.1.6932'   : 'fan1Speed',
                       '.2.1.1.2.4.1.1.7202'   : 'louver1Open',
                    }
        ),
    )

    OnOff   = {1:'On',0:'Off',}
    Run     = {1:'Yes',0:'No',}
    Open    = {1:'Open',0:'Close',}

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
                om.compr1Running = self.Run.get(int(om.compr1Running), 'unknown')
                om.elecHeating1Running = self.Run.get(int(om.elecHeating1Running), 'unknown')
                om.humidifier1Running = self.Run.get(int(om.humidifier1Running), 'unknown')
                om.fan1Running = self.Run.get(int(om.fan1Running), 'unknown')
                om.unitOnOffc = self.OnOff.get(int(om.unitOnOffc), 'unknown')
                om.louver1Open = self.Open.get(int(om.louver1Open), 'unknown')
                stulzid = oid.split('.')
                om.busidc = stulzid[0]
                om.unitidc = stulzid[1]
                om.id = self.prepId(om.unitNamec)
            except (KeyError, IndexError, AttributeError, TypeError), errorInfo:
                log.warn( ' Error in StulzComponentsMap modeler plugin %s', errorInfo)
                continue
            rm.append(om)
        return rm
