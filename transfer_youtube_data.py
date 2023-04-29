import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

def authenticate_account(scope):
    flow = InstalledAppFlow.from_client_secrets_file("client_secrets.json", scope)
    return flow.run_local_server(port=0)


    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scope)

    return flow.run_console()


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


def get_playlists(youtube):
    playlists = []
    nextPageToken = None

    while True:
        request = youtube.playlists().list(
            part="snippet",
            mine=True,
            maxResults=50,
            pageToken=nextPageToken
        )
        response = request.execute()

        for item in response["items"]:
            playlists.append((item["id"], item["snippet"]["title"]))

        nextPageToken = response.get("nextPageToken")
        if nextPageToken is None:
            break

    return playlists


def get_watch_history(youtube):
    watch_history = []
    nextPageToken = None

    while True:
        request = youtube.playlistItems().list(
            part="snippet",
            playlistId="HL",  # "HL" is the watch history playlist ID
            maxResults=50,
            pageToken=nextPageToken
        )
        response = request.execute()

        for item in response["items"]:
            watch_history.append(item["snippet"]["resourceId"]["videoId"])

        nextPageToken = response.get("nextPageToken")
        if nextPageToken is None:
            break

    return watch_history


def main():
    scope = ["https://www.googleapis.com/auth/youtube.force-ssl"]
    youtube_source = googleapiclient.discovery.build("youtube", "v3", credentials=authenticate_account(scope))
    youtube_target = googleapiclient.discovery.build("youtube", "v3", credentials=authenticate_account(scope))

    source_channel_request = youtube_source.channels().list(part="snippet", mine=True)
    source_channel_id = source_channel_request.execute()["items"][0]["id"]

    subscriptions = get_subscriptions(youtube_source, source_channel_id)
    playlists = get_playlists(youtube_source)
    watch_history = get_watch_history(youtube_source)

    # Transfer subscriptions
    for channelId in subscriptions:
        youtube_target.subscriptions().insert(part="snippet", body={
            "snippet": {
                "resourceId": {
                    "kind": "youtube#channel",
                    "channelId": channelId
                }
            }
        }).execute()

    # Transfer playlists
    for playlist_id, title in playlists:
        new_playlist = youtube_target.playlists().insert(part="snippet,status", body={
            "snippet": {
                "title": title,
            },
            "status": {
                "privacyStatus": "private",
            }
        }).execute()

        new_playlist_id = new_playlist["id"]

        nextPageToken = None
        while True:
            playlist_items_request = youtube_source.playlistItems().list(
                part="snippet",
                playlistId=playlist_id,
                maxResults=50,
                pageToken=nextPageToken
            )
            playlist_items = playlist_items_request.execute()

            for item in playlist_items["items"]:
                youtube_target.playlistItems().insert(part="snippet", body={
                    "snippet": {
                        "playlistId": new_playlist_id,
                        "resourceId": item["snippet"]["resourceId"]
                    }
                }).execute()

            nextPageToken = playlist_items.get("nextPageToken")
            if nextPageToken is None:
                break

    # Note: Transferring watch history is not possible due to API limitations
    print("Subscriptions and playlists transferred successfully. Watch history cannot be transferred due to API limitations.")

if __name__ == "__main__":
    main()
