#!/usr/bin/env python3

import aws_cdk as cdk

from cdkgettingstarted.cdkgettingstarted_stack import CdkgettingstartedStack


app = cdk.App()
CdkgettingstartedStack(app, "CdkgettingstartedStack")

app.synth()
