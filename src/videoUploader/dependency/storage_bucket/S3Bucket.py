

class S3Bucket:
    def __init__(self,client,getFiles) -> None:
        self.s3Client=client
        self.getFiles=getFiles
    

    def upload_multiple_files(
            self,
            bucket_name,
            path,
            file_type,
            user_id,
            process_id,

        ):
        files=self.getFiles(path=f'{path}/*.{file_type}')
        print(files)
        for file in files:
            print(file)
            file_name=file.split("/")[-1]
            self.upload_file(path=file,bucket_name=bucket_name,upload_location=f"{user_id}/process/{process_id}/{file_type}/{file_name}")

    def upload_file(self,path,bucket_name,upload_location):
        self.s3Client.upload_file(path,bucket_name,upload_location)
        