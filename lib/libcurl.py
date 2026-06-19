import urllib.request

def download_file(url, save_as):
    try:
        print(f"Downloading from {url}...")
        urllib.request.urlretrieve(url, save_as)
        print(f"Success! File saved as: {save_as}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example Usage:
# download_file("https://example.com", "downloaded_image.png")
