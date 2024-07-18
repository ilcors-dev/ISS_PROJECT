%====================================================================================
% monitoringdevicewis24 description   
%====================================================================================
event( sonarData, distance(D) ).
%====================================================================================
context(ctxmonitoringdevice24, "localhost",  "TCP", "8128").
context(ctxwis24, "IPTOINSERT",  "TCP", "8120").
 qactor( monitoringdevice, ctxmonitoringdevice24, "it.unibo.monitoringdevice.Monitoringdevice").
 static(monitoringdevice).
