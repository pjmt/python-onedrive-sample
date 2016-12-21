from __future__ import unicode_literals

import onedrivesdk
from onedrivesdk.helpers import GetAuthCodeServer

def main():
    redirect_uri="http://localhost:8080/"
    client_secret = "BqaTYqI0XI7wDKcnJ5i3MvLwGcVsaMVM"

    client = onedrivesdk.get_default_client(client_id='00000000481695BB', scopes=['wl.signin', 'wl.offline_access', 'onedrive.readwrite'])
    auth_url = client.auth_provider.get_auth_url(redirect_uri)

    code = GetAuthCodeServer.get_auth_code(auth_url, redirect_uri)

    client.auth_provider.authenticate(code, redirect_uri, client_secret)

    root = client.item(id="root").get()

    listItemsInFolder(client, root)


def listItemsInFolder(client, folder):
    folder_name = folder.name + "/"

    items = client.item(id=folder.id).children.get()

    for item in items:
        if item.folder is None:
            print(folder_name + item.name)
        else:
            listItemsInFolder(client, item)

if __name__ == "__main__":
    main()