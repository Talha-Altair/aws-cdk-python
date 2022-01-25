import aws_cdk as core
import aws_cdk.assertions as assertions

from altair_s3_cdk.altair_s3_cdk_stack import AltairS3CdkStack

# example tests. To run these tests, uncomment this file along with the example
# resource in altair_s3_cdk/altair_s3_cdk_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = AltairS3CdkStack(app, "altair-s3-cdk")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
