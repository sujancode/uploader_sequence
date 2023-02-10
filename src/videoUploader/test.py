from videoUploader.sign_up_upload import sign_up
def main(data):
    try:
        try:
            sign_up(video_url="",title=data['title'],tags=data['tags'],username=data.get('username',""))            
        except Exception as e:
            print(e)
    except Exception as e:
        print(e)
        print("Most Probably database error")