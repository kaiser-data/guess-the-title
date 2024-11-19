import urllib

import requests
import json


def get_the_title_summary() -> str:
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
    urllib.request.urlretrieve(url, save_as)


def main():
    return_value = get_the_title_summary()

    title = return_value["title"]

    summary = return_value["extract"]

    image_link = return_value["thumbnail"]["source"]

    download_image(image_link, "image.jpg")

    title_random = get_the_random_title()

    print(title_random)

    print(return_value)
    print(image_link)
    print(title)
    print(summary)

    categories = get_the_title_categories(title)

    for word in categories.split("Category:")[1:]:  # Categories
        print(word.split("\'")[0])


if __name__ == '__main__':
    main()
