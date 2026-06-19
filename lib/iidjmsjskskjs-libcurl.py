import urllib.request
import urllib.error

def check_websites(url_list):
    for url in url_list:
        # Add http if missing
        if not url.startswith("http"):
            url = "http://" + url
            
        try:
            # Send request with a 5-second timeout limit
            response = urllib.request.urlopen(url, timeout=5)
            print(f"[ONLINE] {url} - Status Code: {response.getcode()}")
        except urllib.error.HTTPError as e:
            print(f"[ERROR]  {url} - HTTP Error Code: {e.code}")
        except urllib.error.URLError as e:
            print(f"[OFFLINE] {url} - Cannot reach server. Reason: {e.reason}")
        except Exception as e:
            print(f"[FAILED] {url} - Error: {e}")

# Example Usage:
# check_websites(["google.com", "github.com", "this-is-a-fake-site.xyz"])
