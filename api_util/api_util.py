import urllib
import requests
import json


def get_the_title_summary() -> dict[str, str]:
    """
    Fetches a random Wikipedia article summary in JSON format.

    Returns:
        dict[str, str]: A dictionary containing the title and summary of a random Wikipedia article.
        If an error occurs, a string message with the error description is returned.

    Raises:
        requests.exceptions.RequestException: For any HTTP request issues.
    """
    try:
        response = requests.get(
            "https://en.wikipedia.org/api/rest_v1/page/random/summary",
            verify=True,
            timeout=5
        )

        response.raise_for_status()  # Raises HTTPError for bad responses

        if response.status_code == 200:
            return json.loads(response.content)
        else:
            return f"Error: Fetching title from the wikipedia api"
    except requests.exceptions.RequestException as e:
        return f"Error {e}"


def get_the_title_categories(title) -> str:
    """
    Fetches the categories of a given Wikipedia article.

    Parameter:
        title (str): The title of the Wikipedia article.

    Returns:
        str: A string containing the categories of the article in JSON format.
        If an error occurs, a string message with the error description is returned.

    Raises:
        requests.exceptions.RequestException: For any HTTP request issues.
    """
    try:
        response = requests.get(
            f"https://en.wikipedia.org/w/api.php?action=query&format=json&titles={title}&prop=categories",
            verify=True,
            timeout=5
        )

        response.raise_for_status()  # Raises HTTPError for bad responses

        if response.status_code == 200:
            return str(json.loads(response.content)["query"]["pages"])
        else:
            return f"Error: Fetching title from the wikipedia api"
    except requests.exceptions.RequestException as e:
        return f"Error {e}"


def download_image(url, save_as):
    """
    Downloads an image from the specified URL and saves it to a local file.

    Parameter:
        url (str): The URL of the image to download.
        save_as (str): The local file path to save the downloaded image.

    Returns:
        None: The image is saved to the specified file location.

    Raises:
        urllib.error.URLError: If there is an issue downloading the image.
    """
    urllib.request.urlretrieve(url, save_as)
