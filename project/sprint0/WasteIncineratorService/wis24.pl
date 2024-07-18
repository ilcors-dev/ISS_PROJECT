%====================================================================================
% wis24 description   
%====================================================================================
request( engage, engage(OWNER,STEPTIME) ).
dispatch( getrp, getrp(X,Y) ).
dispatch( endburnindeposit, endburnindeposit(WEIGHRP) ).
dispatch( gohome, gohome(X,Y) ).
dispatch( inhome, inhome(STATUS) ).
dispatch( getash, getash(X,Y) ).
dispatch( endashdeposit, endashdeposit(WEIGHASH) ).
dispatch( startIncinerator, startIncinerator(BTIME) ).
event( sonarData, distance(D) ).
dispatch( ashMeasurement, ashMeasurement(rpCount) ).
event( burning, burning(START_TIME) ).
event( finishedBurning, finishedBurning(TIME_ELAPSED) ).
event( reports, reports(WEIGHRP) ).
dispatch( rpInWaste, rpInWaste(RPCOUNT) ).
dispatch( sonarstart, sonarstart(X) ).
dispatch( sonarstop, sonarstop(X) ).
event( sonardata, distance(D) ).
dispatch( doread, doread(X) ).
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
  qactor( monitoringdeviceobserver, ctxwis24, "it.unibo.monitoringdeviceobserver.Monitoringdeviceobserver").
 static(monitoringdeviceobserver).
  qactor( weighingdeviceobserver, ctxwis24, "it.unibo.weighingdeviceobserver.Weighingdeviceobserver").
 static(weighingdeviceobserver).
  qactor( wastestoragemock, ctxwis24, "it.unibo.wastestoragemock.Wastestoragemock").
 static(wastestoragemock).
  qactor( ashstoragemock, ctxwis24, "it.unibo.ashstoragemock.Ashstoragemock").
 static(ashstoragemock).
