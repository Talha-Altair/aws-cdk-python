import os

import aws_cdk as cdk

from altair_s3_cdk.altair_s3_cdk_stack import AltairS3CdkStack

app = cdk.App()

AltairS3CdkStack(app, "AltairS3CdkStack")

app.synth()
