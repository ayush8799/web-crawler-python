import requests
from urllib3.util.retry import Retry

def retry_requests(retries=3, backoff_factor=0.5):
  """
  Function to create a Requests session with retry logic.

  Args:
      retries: Number of retries to attempt (default: 3).
      backoff_factor: Exponential backoff factor for delays between retries (default: 0.5).

  Returns:
      A Requests session object with retry capabilities.
  """
  session = requests.Session()
  retry_strategy = Retry(
      total=retries,
      backoff_factor=backoff_factor,
      status_forcelist=[429, 403, 500, 502, 503, 504]  # Retry on specific status codes
  )
  adapter = requests.adapters.HTTPAdapter(max_retries=retry_strategy)
  session.mount('http://', adapter)
  session.mount('https://', adapter)
  return session
