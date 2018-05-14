/*
 * Based on the configuration in ../../configure.zcml this JavaScript will only
 * be loaded when the user is looking at an ExampleDevice in the web interface.
 */

(function(){

var ZC = Ext.ns('Zenoss.component');

function render_link(ob) {
    if (ob && ob.uid) {
        return Zenoss.render.link(ob.uid);
    } else {
        return ob;
    }
}

ZC.StulzComponentsPanel = Ext.extend(ZC.ComponentGridPanel, {
    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
            componentType: 'StulzComponents',
            alias:['widget.StulzComponentsPanel'],
            sortInfo: {
                field: 'name',
                direction: 'ASC'
            },
            fields: [
                {name: 'uid'},
                {name: 'name'},
                {name: 'severity'},
                {name: 'usesMonitorAttribute'},
                {name: 'busidc'},
                {name: 'unitidc'},
                {name: 'unitOnOffc'},
                {name: 'monitor'},
                {name: 'monitored'}
            ],
            columns: [{
                id: 'severity',
                dataIndex: 'severity',
                header: _t('Events'),
                renderer: Zenoss.render.severity,
                sortable: true,
                width: 50
            },{
                id: 'busidc',
                dataIndex: 'busidc',
                header: _t('Bus ID'),
                width: 60
            },{
                id: 'unitidc',
                dataIndex: 'unitidc',
                header: _t('Unit ID'),
                width: 60
            },{
                id: 'name',
                dataIndex: 'name',
                header: _t('Unit Name'),
                width: 200
            },{
                id: 'unitOnOffc',
                flex: 1,
                dataIndex: 'unitOnOffc',
                header: _t('Unit State'),
                sortable: true,
                width: 150,
            },{
                id: 'monitored',
                dataIndex: 'monitored',
                header: _t('Monitored'),
                renderer: Zenoss.render.checkbox,
                sortable: true,
                width: 65
            }]
        });
        ZC.StulzComponentsPanel.superclass.constructor.call(this, config);
    }
});

Ext.reg('StulzComponentsPanel', ZC.StulzComponentsPanel);
ZC.registerName('StulzComponents', _t('Stulz Component'), _t('Stulz Components'));

ZC.StulzRunTimesPanel = Ext.extend(ZC.ComponentGridPanel, {
    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
            componentType: 'StulzRunTimes',
            alias:['widget.StulzRunTimesPanel'],
            sortInfo: {
                field: 'name',
                direction: 'ASC'
            },
            fields: [
                {name: 'uid'},
                {name: 'name'},
                {name: 'severity'},
                {name: 'usesMonitorAttribute'},
                {name: 'busidr'},
                {name: 'unitidr'},
                {name: 'unitOnOffr'},
                {name: 'monitor'},
                {name: 'monitored'}
            ],
            columns: [{
                id: 'severity',
                dataIndex: 'severity',
                header: _t('Events'),
                renderer: Zenoss.render.severity,
                sortable: true,
                width: 50
            },{
                id: 'busidr',
                dataIndex: 'busidr',
                header: _t('Bus ID'),
                width: 60
            },{
                id: 'unitidr',
                dataIndex: 'unitidr',
                header: _t('Unit ID'),
                width: 60
            },{
                id: 'name',
                dataIndex: 'name',
                header: _t('Unit Name'),
                width: 200
            },{
                id: 'unitOnOffr',
                flex: 1,
                dataIndex: 'unitOnOffr',
                header: _t('Unit State'),
                sortable: true,
                width: 150,
            },{
                id: 'monitored',
                dataIndex: 'monitored',
                header: _t('Monitored'),
                renderer: Zenoss.render.checkbox,
                sortable: true,
                width: 65
            }]
        });
        ZC.StulzRunTimesPanel.superclass.constructor.call(this, config);
    }
});

Ext.reg('StulzRunTimesPanel', ZC.StulzRunTimesPanel);
ZC.registerName('StulzRunTimes', _t('Stulz RunTime'), _t('Stulz RunTimes'));

ZC.StulzTemperaturePanel = Ext.extend(ZC.ComponentGridPanel, {
    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
            componentType: 'StulzTemperature',
            alias:['widget.StulzTemperaturePanel'],
            sortInfo: {
                field: 'name',
                direction: 'ASC'
            },
            fields: [
                {name: 'uid'},
                {name: 'name'},
                {name: 'severity'},
                {name: 'usesMonitorAttribute'},
                {name: 'busidt'},
                {name: 'unitidt'},
                {name: 'unitOnOfft'},
                {name: 'monitor'},
                {name: 'monitored'}
            ],
            columns: [{
                id: 'severity',
                dataIndex: 'severity',
                header: _t('Events'),
                renderer: Zenoss.render.severity,
                sortable: true,
                width: 50
            },{
                id: 'busidt',
                dataIndex: 'busidt',
                header: _t('Bus ID'),
                width: 60
            },{
                id: 'unitidt',
                dataIndex: 'unitidt',
                header: _t('Unit ID'),
                width: 60
            },{
                id: 'name',
                dataIndex: 'name',
                header: _t('Unit Name'),
                width: 200
            },{
                id: 'unitOnOfft',
                flex: 1,
                dataIndex: 'unitOnOfft',
                header: _t('Unit State'),
                sortable: true,
                width: 150,
            },{
                id: 'monitored',
                dataIndex: 'monitored',
                header: _t('Monitored'),
                renderer: Zenoss.render.checkbox,
                sortable: true,
                width: 65
            }]
        });
        ZC.StulzTemperaturePanel.superclass.constructor.call(this, config);
    }
});

Ext.reg('StulzTemperaturePanel', ZC.StulzTemperaturePanel);
ZC.registerName('StulzTemperature', _t('Stulz Temperature'), _t('Stulz Temperatures'));

ZC.StulzAlarmsPanel = Ext.extend(ZC.ComponentGridPanel, {
    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
            componentType: 'StulzAlarms',
            alias:['widget.StulzAlarmsPanel'],
            sortInfo: {
                field: 'name',
                direction: 'ASC'
            },
            fields: [
                {name: 'uid'},
                {name: 'name'},
                {name: 'severity'},
                {name: 'usesMonitorAttribute'},
                {name: 'busida'},
                {name: 'unitida'},
                {name: 'unitOnOffa'},
                {name: 'monitor'},
                {name: 'monitored'}
            ],
            columns: [{
                id: 'severity',
                dataIndex: 'severity',
                header: _t('Events'),
                renderer: Zenoss.render.severity,
                sortable: true,
                width: 50
            },{
                id: 'busida',
                dataIndex: 'busida',
                header: _t('Bus ID'),
                width: 60
            },{
                id: 'unitida',
                dataIndex: 'unitida',
                header: _t('Unit ID'),
                width: 60
            },{
                id: 'name',
                dataIndex: 'name',
                header: _t('Unit Name'),
                width: 200
            },{
                id: 'unitOnOffa',
                flex: 1,
                dataIndex: 'unitOnOffa',
                header: _t('Unit State'),
                sortable: true,
                width: 150,
            },{
                id: 'monitored',
                dataIndex: 'monitored',
                header: _t('Monitored'),
                renderer: Zenoss.render.checkbox,
                sortable: true,
                width: 65
            }]
        });
        ZC.StulzAlarmsPanel.superclass.constructor.call(this, config);
    }
});

Ext.reg('StulzAlarmsPanel', ZC.StulzAlarmsPanel);
ZC.registerName('StulzAlarms', _t('Stulz Alarm'), _t('Stulz Alarms'));

})();
