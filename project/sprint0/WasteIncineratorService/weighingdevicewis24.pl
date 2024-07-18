%====================================================================================
% weighingdevicewis24 description   
%====================================================================================
event( scaleData, weight(W) ).
%====================================================================================
context(ctxweighingdevicewis24, "localhost",  "TCP", "8130").
context(ctxwis24, "IPTOINSERT",  "TCP", "8120").
 qactor( weighingdevice, ctxweighingdevicewis24, "it.unibo.weighingdevice.Weighingdevice").
 static(weighingdevice).
  qactor( wastestoragemock, ctxwis24, "it.unibo.wastestoragemock.Wastestoragemock").
 static(wastestoragemock).
