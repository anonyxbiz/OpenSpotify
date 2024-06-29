# openspotify.py
"""
Author: Anonyxbiz
OpenSpotify - A very fast reverse engineered private spotify api, unlimited access to spotify private api, no api keys needed, no limits, access every spotify api routes, access private routes, access private data.
NB: THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

"""
from cryptography.fernet import Fernet
from os import environ
from asyncio import run, create_task, sleep
from wazing_net import route
from time import time
from httpx import AsyncClient

p = print

class Route:
    def __init__(app) -> None:
        pass
    async def get(app, url=None, headers={}, params={}, timeout=60):
        if url is None:
            return 'url is required'
        try:
            async with AsyncClient() as client:
                r = await client.get(url, headers=headers, params=params, timeout=timeout)
                return r
        except Exception as e:
            return ('request_exception', f"Error fetching {url}: {str(e)}")

    async def post(app, url=None, headers={}, data={}, json={}, timeout=60):
        if url is None:
            return 'url is required'
        try:
            async with AsyncClient() as client:
                if json != {}:
                    r = await client.post(url, headers=headers, json=json)
                else:
                    if data != {}:
                        r = await client.post(url, headers=headers, data=data)
                    else:
                        r = False
                if r:
                    return r
                
        except Exception as e:
            return ('request', f"Error fetching {url}: {str(e)}")

route = Route()

class Logging:
    def __init__(app) -> None:
        pass

    async def log_data(app, data, do=None):
        data = str(data)
        if do == 'q':
            exit(data)
        else:
            p(data)

logger = Logging()

class Safe:
    def __init__(self) -> None:
        while True:
            self.safe_key = environ.get("safe_key", False)
            if not self.safe_key:
                self.safe_key = input("Safe key not found in the environment!, Enter it below\n: ")
            if self.safe_key:
                break

    def tool(self, og: str, action: str):
        try:
            if action == "encrypt":
                data = Fernet(self.safe_key.encode()).encrypt(og.encode("utf-8")).decode('utf-8')
            elif action == "decrypt":
                data = Fernet(self.safe_key.encode()).decrypt(og.encode("utf-8")).decode('utf-8')
            
            return data
        except Exception as e:
            p(e)
            return False
        
safe = Safe()

class Spotify:
    def __init__(app) -> None:
        app.readiness = False
        app.device_id = 'gAAAAABmfydbcT4PsJfFBKB4eNvA-v6qwBDKi2t-6AILcBek0hLXY395Xhl9bmaf2i-cJ-Cp7gh2D_62kZKfI0cEXNxaTRINSLjs2QMf5Na6oPLE6aPwmXpHaCo3KoT_UioCwBzgh-od'
        app.gAAAAABmf0W0H = False
        app.os_version = 'gAAAAABmfyeU-kF0BzzdvVZ_jOuhjmldXVA6l2jdE7aJg7zKN_E73ZUL0zfjRxXSKo4sXu2E4AzpU7vBpJcJw06fcpmHGkLBAQ=='
        app.os = 'gAAAAABmfyep5gPr-J0aj3etzZuvKmCEzySt8gxi3C9ApTHNH8JeuIhRMJ2kuIkg2hnj_gMOc3yD5yfds66wT8uR0xeLnVRGpg=='
        app.device_model = 'gAAAAABmfye8lZln_cKiwKH0CJp2GKx_QkYjujuU1GYwN6GYUFA6LT-uSAT2JwooWrDl_gtgNZ4EHq32Cua2LGiQkO5hiGNmsA=='
        app.device_brand = 'gAAAAABmfyfJAI-b2ahhIK9eNoTBGqyCftyrIXObVFsRpQIpjHI7DDFqJq1_71vASmDGf2VtgwFk8TtWM48JNaDRbBqv7K75gg=='
        app.device_type = 'gAAAAABmfyfY73jHOpT3PRyI7iPBBOUVz-4NJDZXSeWzoqX8Q7XGgBDQr-5invjqZg3-ihaqoiIPStQy2ipi7vKwL2gQjyOVcw=='
        app.client_version = 'gAAAAABmfyfn9SJkpRuovnMgj1J4ckoQkofbI4Cyk0Y5XzeC3QlQhpT_-3ZGh8xomnais3imX5SICVO726WXs6gTE805RA1YZjRFBOvHubMkUKvQGfIze3g='
        app.params = 'gAAAAABmfzqLx83HzurlaPN4w4YLc9uNoIgoF28iii3a-oI_v7LbNx60fWQSBSW50m16r1vUMdP6PodU4oe5ofPvJJtqLZa5pJ3TqzgPZkwaRMoyWU_vf8FLuRf-F6BMTEjMKeEmJUCxtTlRu3oybeo4GpS3XQ2O3T0Bvoo3PcriHYex8d2YWK-BhiaiUJONzqs1dqbAovMXyINDKulUPV-9IdO6yNLXMNjuELCX9o2ZHo5ZPEImAGxadQr8FK8lvoqiyTKFsQXuKz9RbUNduiQAoDLXZGOrGze3NCWH8HXX0YSrI9Ml8TYLdvSrMIysoGLqLScx1Ph0HjM2qJoM2IwB2Nu3JXpmKMQZkF762uMxAuSzKiceB9-gftBLpRAFPWUAsm4puZZQMbffQpxlvllNADEDjV5b_0xYw59zu4UPoeJWP-bpx1CNUzVV31nM1VauUGH_co382DN4kL0wZB6b6pgUEQze9KfnPBsXAoRNu3TTfp0QTbxBaoIJMl8FE0ru_D488IEI'
        app.get_album_data_url = safe.tool('gAAAAABmf0C7cfu-UQtf2iQTDgvUsypWhW_a8hMJiMReIvOhYvH2_vfiotDGufY96p9zxlOmlzdyo1G-ASx8Ss5lpFe_A2Nu0NUftGn4ce2p90WKzmVuH-1DFMTaCm3-7F2qBMw3cjNxL2B8tyfozDVXkdeby84bOw==', "decrypt")
        app.set_app_url = safe.tool('gAAAAABmfyxtYNrRIVAd9ev70heOKybqiKmwD1Q-IS8wRlsUb0fqU4-jAgV9JaEDmRndbSd1VfAk3NLwDD913bcSU7IhUknlUpLnNhu3esckBg56Njgmu8o=', "decrypt")

        keys = safe.tool(app.params, "decrypt").strip().split('<{')[1].split('}>')[0].strip().split("key>'")
        for i, x in enumerate(keys):
            if x == '' or x == ' ' or x == '\n':
                del keys[i]
            else:
                keys[i] == x.strip()

        app.params = {}
        for key in keys:
            dict_key = key.split("'<:")[0].strip()
            dict_value = key.split("'<:")[1].strip().split("values>")[1].split(",<")[0].strip()

            app.params.update({dict_key: dict_value})
        app.headers = {
            'accept': 'application/json',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'no-cache',
            'content-type': 'application/json',
            'origin': safe.tool('gAAAAABmf0IMyHZsMDKg6HBf-LMFq7rvvstUMH3FXee6HfwhwD6bIAsuTitDKgJpAPfAAyDAdDCqVzp-FR5Wy1bPsz5TKz179Xm7rjH9_IgX9pLwvW-nBCQ=', "decrypt"),
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': safe.tool('gAAAAABmf0IqM6orK71nEqVk_Pr5gSSVETZFYlCghjI1VcfcQj47LO5Nwv8v8erJxhI1Ls7ijgW9vwC4vYUIsmJWp7nDKTbELW1cE2myGZyoJyNHZ8I-9eA=', "decrypt"),
            'sec-ch-ua': safe.tool('gAAAAABmf0MHQymDwWook1WGlz8XJTlRhR-npJ41IlgAg70J9U1OLSLQVNOuJpiRSOEu9CnWT6taZJqpOVsr3kkSfx_mnajOeXQSgUOUJnoaw3CqtE-J0LEdpM1KWXwCXmQd9SHsW-CPUXdrzjNaLdx9ClPZxpLntXw6yMxlzNcZ3HFCBsSLU4w=', "decrypt"),
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': safe.tool('gAAAAABmf0KY4pw6kL8GXEP-8qibwfO4ailjYFiVZ7iGR3is14GfHgc-QAflr6rua2LvE_zJBXtLIoi_NlcNFbZVbu6hfx-zHg==', "decrypt"),
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': safe.tool('gAAAAABmf0K-1s4IZWH3snwLOWNhZqrS0tICSFh-8CWSTL-Q0bFXw59iffTl0lblJ9OzCemfK9Yh3BAdqXgwnU969jngiCWYBRl1Q4knim6zbqBdKWqnFxNosV6cCfIaewlChB6ico17matfsmHXi5Ie6pnoynDYlA2ZAhookAMlvEprYmNCO3UHEsi4jeIpfdVMNpuyThGzl7RrArI_xIH0HUunn-DKug==', "decrypt"),
        }

    async def update_headers(app, headers, update_target):
        new_keys = []
        try:
            for key, value in update_target.items():
                new_keys.append(key)

            key_count = 0
            for key, value in headers.items():
                if key in new_keys:
                    update_target[key] = value
                else:
                    update_target.update({key: value})
                key_count += 1
            return 'ok'
        except Exception as e:
            await logger.log_data(e, 'q')

    async def set_collected_creds(app):
        app.u_headers = {
            safe.tool("gAAAAABmf0RY8kwDtqS5mnv0kpJT4AZ8R6Fu-lvAPm8JLXYx7srPmJUVpJDPLjV3JaIC53PG3TF8Vo7QCkIL8gDHVm6Z2ZJ4Bg==", "decrypt"): f'{safe.tool("gAAAAABmf0SdlZVGHMJdqehziz_UCBKyvTXjSMSB3-9qmwajs2nbDBe7Hri1RSW2Qmw-Ka1FtuMn9YcHr_XzMJRqbWwZjKS2Lw==", "decrypt")} {app.gAAAAABmf0WVQ}',
            safe.tool("gAAAAABmf0Tu2DTBhd3yH4ABrpKZOFwTmGxmfPYAQPNKklw_9DS_EznIROxYYMT9n-OlTLUA3sczJPmCnU4sTC-HxEeaxn6qIg==", "decrypt"): app.important_grant[safe.tool("gAAAAABmf0UxxHn4DBPiD0elHw98BLS0rHgdWqQHlXcBR07oA75LoTpMltE3dA7RiO3Bu78lLAOJKD7nylUbRlpJoMaZ0ckmKg==", "decrypt")]
        }
        if await app.update_headers(app.u_headers, app.headers):
            return 'ok'

    async def set_creds(app):
        app.gAAAAABmf0WVQ = app.r.split(safe.tool("gAAAAABmf0WVQanoY7XmhkhNrelnBkfMbaO2WyRM1q9AB1TNqCbAARe56S45iIHbAudJEqGnD9fWHB4c4Uwvat6bPEQGVMxuOg==", "decrypt"))[1].split('",')[0]
        app.gAAAAABmf0W0H = app.r.split(safe.tool("gAAAAABmf0W0HpDfvQNwVhtQsFUTtGll3k3Ju6WBNHb1iGlHUmlEXl1JPEQgcISNKmJq05IrIca_GbWAlbZaEbs21IVrHiH40Q==", "decrypt"))[1].split('"')[0]

        if app.gAAAAABmf0WVQ and app.gAAAAABmf0W0H:
            await app.generate_important_stuff()

    async def generate_important_stuff(app):
        json_data = {
            safe.tool("gAAAAABmf0e441RYkp4XDjaLZvyDNbNc9796KFaO8s56rmIBRq89aGFK-1YUccyH-TDjcTDxXhopvczxDYDmbhskjZ7N0xSjcg==", "decrypt"): {
                safe.tool("gAAAAABmf0a98dnBrTLpiKT5s8m6CKZUYQzQKrNvXZpEAWqx8rqjHKzOHX8j4Z98zdMGeKEQHdzhI1YYeBaNlAruZw6C6L44hQ==", "decrypt"): safe.tool(app.client_version, "decrypt"),
                safe.tool("gAAAAABmf0bdbAiOzpdLOzUaYGlKXgHZ2K4zssjEvPNZcRriuMGNTGNIehIbeyF_esSrk_JUutpyXPHyhQ-SJg02iIF5bec3vw==", "decrypt"): app.gAAAAABmf0W0H,
                safe.tool("gAAAAABmf0gURSovYloI8Td_E6W5rSfF2dl1z7zoqAlUpfrhVBTM23bSArj9CykN__z3x6J_tmdnKpqhrLza6oNjJ2QcI5vVtQ==", "decrypt"): {
                    safe.tool("gAAAAABmf0diRNNWH-SHPhU31yfnS4JKZUdNf8Ymai1LAt81EdNjWhYzTJ9PVdHUfvgGX7ksnDfXnBCcWy2G1ZjMr4kEjUmHFw==", "decrypt"): safe.tool(app.device_brand, "decrypt"),
                    safe.tool("gAAAAABmf0d2520ykbSVq6iD8mBzAG3NCOzSUoWKopVaYPpxLUIgdPIu8NYf3en0hn1W5AUR9-YHL1_hhc2ja26l4pzjnpS9vQ==", "decrypt"): safe.tool(app.device_model, "decrypt"),
                    safe.tool("gAAAAABmf0eJOlAMEyY-O5BqhsV-DOW3rgHiv9zz2D-tfhsKT7VBZKAVXy1fLNexuon9fUclMNXDJLQC0iE8AhfKb8jsFNntrA==", "decrypt"): safe.tool(app.os, "decrypt"),
                    safe.tool("gAAAAABmf0eXC0z-0w7KBsEAyvh3M1e9Q9ysKyHKOKxBs4uGcEh-av6lYlVaaOGUUovRDS4e9qQpD5D75jOFuHIc-AjsBeMrTQ==", "decrypt"): safe.tool(app.os_version, "decrypt"),
                    safe.tool("gAAAAABmf0ej03TdlYWtR3rvEwl7igSPYF0XyAxjy3MRwFn_4k3bPiBI9lek7wA7_Ifw6ayhCDYD1JuHu8VrLwt22QBWv0Ojcg==", "decrypt"): safe.tool(app.device_id, "decrypt"),
                    safe.tool("gAAAAABmf0etnFuuYxqwyg-LoCPsB8_fbGhAk-TPUNlGR6gDnPwow8sktN11KLlLvwXw7P-lbyJH2U0i4knzkPgQzd0qOfuI7Q==", "decrypt"): safe.tool(app.device_type, "decrypt"),
                },
            },
        }
        try:
            r = await route.post(safe.tool('gAAAAABmfyqQU0mqfvrAysPi9dpA0hN2AarP4y8-QzqGYNWQY4PngzUrp7kH93idAxvynO__GsH3-2nDOBj2L8OR6_lEE8wmcE7FjW6I7jxZUcpu-FRkDFYKcdv4VepuT8bZzmV0i5XW', "decrypt"), headers=app.headers, json=json_data)
            
            if r.status_code < 300:
                if r.json().get(safe.tool('gAAAAABmfyv4wwCdR2XDdAC-jci0iw0lYCzUKjxpaQ1RNf2qkt2_dqNfiYeussMqFhmI3obr_T7hY7gVu5yUNxYANkuVorM0AQ==', "decrypt"), False):
                    app.important_grant = r.json().get(safe.tool('gAAAAABmfyxBunBWPHVzAZABa2Ct0GETTzWQdFqJ5s_Cbq0QCTQBftRMfPVejKeCDPUkuBP3md3ZZzfzwGpImKkaPTYPatj7lw==', "decrypt"))
                else:
                    return False

            if await app.set_collected_creds():
                app.readiness = 'ready'
            return 'ok'

        except Exception as e:
            await logger.log_data(e)

    async def set_app(app):
        r = await route.get(app.set_app_url)
        if r.status_code < 300:
            app.r = str(r.text)
            create_task(app.set_creds())
            while not app.readiness:
                await sleep(0.1)
            return 'ok'
        else:
            await logger.log_data("Something went wrong")

    async def generate_album_info(app):
        if not app.album_info.get('data', False):
            return False
        albumUnion = app.album_info['data']['albumUnion']
        app.album_info = {
            "copyright": albumUnion['copyright']['items'][0]['text'],
            "record_label": albumUnion['label'],
            "name": albumUnion['name'],
            "playability": albumUnion['playability'],
            "artists": albumUnion['artists'],
            "coverArt": albumUnion['coverArt'],
            "playcount": str(albumUnion).split('playcount')[1].split("': '")[1].split("',")[0]
        }

        return 'ok'

    async def get_album_data(app, album_uri):
        app.album_info = None
        while True:
            app.album_info = None
            if not app.readiness:
                if not await app.set_app():
                    await logger.log_data("Something went wrong")
                    return False
            app.params['variables'] = str(app.params['variables']).replace('spotify:album:album_uri', str(album_uri))
            
            try:
                r = await route.get(app.get_album_data_url, params=app.params, headers=app.headers)

                if r.status_code < 300:
                    app.album_info = r.json()
                    if await app.generate_album_info():
                        app.album_info.update({'uri': album_uri})
                        return app.album_info
                    else:
                        await logger.log_data('Something went wrong while generating album info')
                        return False
                    
                elif r.status_code == 401:
                    # Invalid Bearer token, so reset it.
                    app.readiness = False
                else:
                    await logger.log_data('Something went wrong while generating album info')
                    app.readiness = False
                    return False
                
            except Exception as e:
                await logger.log_data(e)
                app.readiness = False
                return False

class Playground:
    def __init__(app) -> None:
        app.spotify = Spotify()

    async def playground(app, uri = None):
        while True:
            if not uri:
                album_uri = input('album_uri: ')
            else:
                album_uri = uri
            if album_uri == '' or album_uri == ' ':
                break

            start_time = time()
            album_info = await app.spotify.get_album_data(album_uri)
            if album_info:
                duration = float(time()) - float(start_time)
                p(album_info)
                p(f'Processed in: {duration} Seconds')
            else:
                p('Something went wrong.')
            
if __name__ == "__main__":
    run(Playground().playground())
