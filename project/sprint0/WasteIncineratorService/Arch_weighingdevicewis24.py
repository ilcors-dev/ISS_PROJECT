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
with Diagram('weighingdevicewis24Arch', show=False, outformat='png', graph_attr=graphattr) as diag:
  with Cluster('env'):
     sys = Custom('','./qakicons/system.png')
### see https://renenyffenegger.ch/notes/tools/Graphviz/attributes/label/HTML-like/index
     with Cluster('ctxweighingdevicewis24', graph_attr=nodeattr):
          weighingdevice=Custom('weighingdevice','./qakicons/symActorSmall.png')
     with Cluster('ctxwis24', graph_attr=nodeattr):
          wastestoragemock=Custom('wastestoragemock','./qakicons/symActorSmall.png')
     weighingdevice >> Edge( label='scaleData', **eventedgeattr, decorate='true', fontcolor='red') >> sys
diag
