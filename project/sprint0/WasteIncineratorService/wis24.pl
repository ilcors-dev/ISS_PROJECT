%====================================================================================
% wis24 description   
%====================================================================================
request( engage, engage(OWNER,STEPTIME) ).
dispatch( getrp, getrp(MOVE) ).
dispatch( endburnindeposit, endburnindeposit(WEIGHRP) ).
dispatch( gohome, gohome(X,Y) ).
dispatch( getash, getash(MOVE) ).
dispatch( endashdeposit, endashdeposit(WEIGHASH) ).
%====================================================================================
context(ctxwis24, "localhost",  "TCP", "8120").
context(ctxbasicrobot, "127.0.0.1",  "TCP", "8020").
 qactor( basicrobot, ctxbasicrobot, "external").
  qactor( wis, ctxwis24, "it.unibo.wis.Wis").
 static(wis).
  qactor( oprobot, ctxwis24, "it.unibo.oprobot.Oprobot").
 static(oprobot).
  qactor( incinerator, ctxwis24, "it.unibo.incinerator.Incinerator").
 static(incinerator).
  qactor( monitoringdevice, ctxwis24, "it.unibo.monitoringdevice.Monitoringdevice").
 static(monitoringdevice).
  qactor( warningdevice, ctxwis24, "it.unibo.warningdevice.Warningdevice").
 static(warningdevice).
  qactor( weighingdevice, ctxwis24, "it.unibo.weighingdevice.Weighingdevice").
 static(weighingdevice).
  qactor( wastestoragemock, ctxwis24, "it.unibo.wastestoragemock.Wastestoragemock").
 static(wastestoragemock).
  qactor( ashstoragemock, ctxwis24, "it.unibo.ashstoragemock.Ashstoragemock").
 static(ashstoragemock).
