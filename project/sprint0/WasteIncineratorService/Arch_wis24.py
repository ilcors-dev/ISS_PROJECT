### conda install diagrams
from diagrams import Cluster, Diagram, Edge
from diagrams.custom import Custom
import os
os.environ['PATH'] += os.pathsep + 'C:/Program Files/Graphviz/bin/'

graphattr = {     #https://www.graphviz.org/doc/info/attrs.html
    'fontsize': '22',
}

nodeattr = {   
    'fontsize': '22',
    'bgcolor': 'lightyellow'
}

eventedgeattr = {
    'color': 'red',
    'style': 'dotted'
}
evattr = {
    'color': 'darkgreen',
    'style': 'dotted'
}
with Diagram('wis24Arch', show=False, outformat='png', graph_attr=graphattr) as diag:
  with Cluster('env'):
     sys = Custom('','./qakicons/system.png')
### see https://renenyffenegger.ch/notes/tools/Graphviz/attributes/label/HTML-like/index
     with Cluster('ctxwis24', graph_attr=nodeattr):
          wis=Custom('wis','./qakicons/symActorSmall.png')
          oprobot=Custom('oprobot','./qakicons/symActorSmall.png')
          incinerator=Custom('incinerator','./qakicons/symActorSmall.png')
          monitoringdeviceobserver=Custom('monitoringdeviceobserver','./qakicons/symActorSmall.png')
          weighingdeviceobserver=Custom('weighingdeviceobserver','./qakicons/symActorSmall.png')
          wastestoragemock=Custom('wastestoragemock','./qakicons/symActorSmall.png')
          ashstoragemock=Custom('ashstoragemock','./qakicons/symActorSmall.png')
     with Cluster('ctxbasicrobot', graph_attr=nodeattr):
          basicrobot=Custom('basicrobot(ext)','./qakicons/externalQActor.png')
     sys >> Edge( label='burning', **evattr, decorate='true', fontcolor='darkgreen') >> wis
     sys >> Edge( label='finishedBurning', **evattr, decorate='true', fontcolor='darkgreen') >> wis
     incinerator >> Edge( label='burning', **eventedgeattr, decorate='true', fontcolor='red') >> sys
     incinerator >> Edge( label='finishedBurning', **eventedgeattr, decorate='true', fontcolor='red') >> sys
     sys >> Edge( label='sonarData', **evattr, decorate='true', fontcolor='darkgreen') >> monitoringdeviceobserver
     sys >> Edge( label='reports', **evattr, decorate='true', fontcolor='darkgreen') >> weighingdeviceobserver
     oprobot >> Edge(color='magenta', style='solid', decorate='true', label='<engage &nbsp; >',  fontcolor='magenta') >> basicrobot
     monitoringdeviceobserver >> Edge(color='blue', style='solid',  decorate='true', label='<ashMeasurement &nbsp; >',  fontcolor='blue') >> wis
     oprobot >> Edge(color='blue', style='solid',  decorate='true', label='<inhome &nbsp; endburnindeposit &nbsp; endashdeposit &nbsp; >',  fontcolor='blue') >> wis
     weighingdeviceobserver >> Edge(color='blue', style='solid',  decorate='true', label='<rpInWaste &nbsp; >',  fontcolor='blue') >> wis
     wis >> Edge(color='blue', style='solid',  decorate='true', label='<getash &nbsp; getrp &nbsp; gohome &nbsp; >',  fontcolor='blue') >> oprobot
diag
