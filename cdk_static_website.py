from constructs import Construct
from cdktf import App, TerraformStack
from imports.aws import AwsProvider, S3Bucket

# example useage from Teraform CDK gitrepo https://github.com/hashicorp/terraform-cdk/blob/main/examples/python/aws/main.py
class MyStaticWebsiteStack(TerraformStack):
    def __init__(self, scope: Construct, name: str):
        super().__init__(scope, name)

        # AWS 
        AwsProvider(self, 'aws', region='us-west-2')

        # S3 bucket 
        website_bucket = S3Bucket(self, 'MyStaticWebsiteBucket',
                                  bucket='my-static-website-bucket',
                                  acl='public-read',
                                  website_index_document='index.html',
                                  website_error_document='error.html',
                                  website=True)

app = App()
MyStaticWebsiteStack(app, "my-static-website-stack")

app.synth()
