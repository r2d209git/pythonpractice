#diagrams python package를 이용해서 alerting_workflow.png 파일과 같은 AWS cloud cluster, node diagram 작성
from diagrams import Diagram, Cluster

from diagrams.aws.compute import Lambda
from diagrams.aws.integration import SNS, Eventbridge
from diagrams.aws.management import Cloudwatch
from diagrams.aws.storage import S3
from diagrams.onprem.queue import ActiveMQ

with Diagram("Alerting Workflow", show=True):
    with Cluster('main account'):
        topic = SNS('SNS Topic')

        with Cluster('Lamda'):
            l = Lambda('processor')
            topic >> l
            S3('lamda source') - l

        cl = Cloudwatch('Cloudwatch')
        l >> cl

        event = Eventbridge('Cloudwatch\nevent rule')
        cl >> event

    with Cluster('Event Bus'):
        event_bus = ActiveMQ('bus')
        event >> event_bus
