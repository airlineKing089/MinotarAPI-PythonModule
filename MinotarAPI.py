import requests
import shutil

err_connection_fail = 'Connection Failed...'

class default():
    def Steve(self):
        url = requests.get('https://minotar.net/skin/MHF_Steve')

        if url.status_code != '404':
            with open('MHF_Steve.png', 'wb') as f:
                f.write(url.content)

            shutil.move('MHF_Steve.png', 'Default_Steve.png')
        else:
            raise err_connection_fail

    def Alex(self):
        url = requests.get('https://minotar.net/skin/MHF_Alex')

        if url.status_code != '404':
            with open('MHF_Alex.png', 'wb') as f:
                f.write(url.content)

            shutil.move('MHF_Alex.png', 'Default_Alex.png')
        else:
            raise err_connection_fail

class download():
    def skin(username):
        url = requests.get(f'https://minotar.net/skin/{username}.png')
        if url.status_code != '404':
            with open('Skin.png', 'wb') as f:
                f.write(url.content)

            shutil.move('Skin.png', f'{username}(skin).png')
        else:
            raise err_connection_fail
    
    def avatar(username, size):
        url = requests.get(f'https://minotar.net/avatar/{username}/{size}.png')
        if url.status_code != '404':
            with open('Avatar.png', 'wb') as f:
                f.write(url.content)
            shutil.move('Avatar.png', f'{username}(avatar ({size})')
        else:
            raise err_connection_fail
