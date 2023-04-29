import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

def authenticate_account(scope):
    flow = InstalledAppFlow.from_client_secrets_file("client_secrets.json", scope)
    return flow.run_local_server(port=0, prompt='consent')

def get_subscriptions(youtube, channelId):
    subscriptions = []
    nextPageToken = None

    while True:
        request = youtube.subscriptions().list(
            part="snippet",
            channelId=channelId,
            maxResults=50,
            pageToken=nextPageToken
        )
        response = request.execute()

        for item in response["items"]:
            subscriptions.append(item["snippet"]["resourceId"]["channelId"])

        nextPageToken = response.get("nextPageToken")
        if nextPageToken is None:
            break

    return subscriptions

def main():
    scope = [
        "https://www.googleapis.com/auth/youtube.force-ssl",
        "https://www.googleapis.com/auth/youtube"
    ]
    source_credentials = authenticate_account(scope)
    target_credentials = authenticate_account(scope)
    youtube_source = googleapiclient.discovery.build("youtube", "v3", credentials=source_credentials)
    youtube_target = googleapiclient.discovery.build("youtube", "v3", credentials=target_credentials)

    source_channel_request = youtube_source.channels().list(part="snippet", mine=True)
    source_channel_id = source_channel_request.execute()["items"][0]["id"]

    subscriptions = get_subscriptions(youtube_source, source_channel_id)

    # Transfer subscriptions
    for channel_id in subscriptions:
        try:
            youtube_target.subscriptions().insert(part="snippet", body={
                
  "snippet": {
                    "resourceId": {
                        "kind": "youtube#channel",
                        "channelId": channel_id
                    }
                }
            }).execute()
        except googleapiclient.errors.HttpError as error:
            print(f"Error: {error}")
            print(f"Skipping subscription to channel ID {channel_id}")

    print("Subscriptions transferred successfully.")

if __name__ == "__main__":
    main()
