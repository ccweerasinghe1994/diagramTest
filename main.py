from diagrams import Diagram
from diagrams.aws.compute import EC2

graph_attr = {
    "fontsize": "45",
    "fontname": "Courier New bold",
    "label": "Home",
    "beautify": "true"
}

with Diagram("Simple Diagram", graph_attr=graph_attr):
    EC2("WEB")
