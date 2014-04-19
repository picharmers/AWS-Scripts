import boto

class S3Operations:
	
	s3 = None
	
	def __init__(self):
		self.s3 = boto.connect_s3()
	
	def createBucket(self, bucket_name):
		bucket = self.s3.create_bucket(bucket_name)
	
