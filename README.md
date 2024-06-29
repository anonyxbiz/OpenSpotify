# OpenSpotify

OpenSpotify is a fast and efficient reverse-engineered Spotify API, allowing unlimited access to Spotify's private API without the need for API keys. It provides access to all Spotify API routes, including private routes and data.

## Features

- Access Spotify API routes without API keys.
- Retrieve private Spotify data.
- Encrypted data handling for security.

## Installation

To install the required dependencies, use the following command:

```bash
pip install -r requirements.txt
```

## Environment Variables

Ensure you set the `safe_key` environment variable for encryption and decryption:

```bash
export safe_key=your_safe_key_here
```

## Usage

### Initialization

To initialize and use the `OpenSpotify` API, create an instance of the `Spotify` class:

```python
from openspotify import Spotify

spotify = Spotify()
```

### Retrieve Album Data

You can retrieve album data using the `get_album_data` method:

```python
album_data = await spotify.get_album_data('spotify:album:album_uri')
print(album_data)
```

### Logging

The logging functionality is provided by the `Logging` class. You can log data using the `log_data` method:

```python
await logger.log_data('Your log message here')
```

### Encryption and Decryption

To encrypt or decrypt data, use the `Safe` class:

```python
from openspotify import safe

encrypted_data = safe.tool('your_data_here', 'encrypt')
decrypted_data = safe.tool(encrypted_data, 'decrypt')
```

## Classes and Methods

### Route Class

- `get(url, headers={}, params={}, timeout=60)`: Sends a GET request.
- `post(url, headers={}, data={}, json={}, timeout=60)`: Sends a POST request.

### Logging Class

- `log_data(data, do=None)`: Logs data to the console or exits the program if `do='q'`.

### Safe Class

- `tool(og, action)`: Encrypts or decrypts data based on the `action` parameter.

### Spotify Class

- `get_album_data(album_uri)`: Retrieves data for the specified album.

## Disclaimer

```
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## Author

Anonyxbiz
