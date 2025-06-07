from diagrams import Diagram, Cluster, Edge
from diagrams.custom import Custom
from diagrams.onprem.database import MongoDB
from diagrams.onprem.client import Users
from diagrams.onprem.compute import Server
from diagrams.onprem.analytics import Spark
from diagrams.programming.framework import React

with Diagram("River Health Monitoring System", show=False):

    camera = Custom("Image Capture", "./camera_icon.png")
    
    with Cluster("Preprocessing Layer"):
        preprocessing = Spark("Frame Extraction & Resizing")

    with Cluster("Data Processing Layer"):
        yolo = Custom("YOLOv8 Detection", "./yolo_icon.png")
        classify = Custom("Garbage Classification", "./classify_icon.png")
    
    with Cluster("Storage and Backend"):
        db = MongoDB("MongoDB")
        blockchain = Custom("Blockchain Crowdfunding", "./blockchain_icon.png")

    with Cluster("Alert System"):
        alert = Custom("Alerts & Reports", "./alert_icon.png")

    with Cluster("User Dashboard"):
        dashboard = React("User Dashboard")

    user = Users("User")

    camera >> preprocessing >> yolo >> classify >> db
    classify >> alert
    blockchain >> alert
    alert >> dashboard
    dashboard >> user
    blockchain >> user