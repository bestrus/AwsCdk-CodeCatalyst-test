#!/usr/bin/env python3

import aws_cdk as cdk

from aws_cdk_code_catalyst_test.aws_cdk_code_catalyst_test_stack import AwsCdkCodeCatalystTestStack


app = cdk.App()
AwsCdkCodeCatalystTestStack(app, "aws-cdk-code-catalyst-test-Renzo")

app.synth()
