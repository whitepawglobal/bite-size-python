from pydantic import BaseModel, HttpUrl

class MyModel(BaseModel):
    url: HttpUrl

if __name__ == "__main__":

    urls = ["https://example.com/path?query=123", "ftp://example.com", "random_text", "http://random.text", "http://random.com"]

    for url in urls:
        # Invalid example
        try:

            invalid_model = MyModel(url=url)

        except ValueError as e:

            print(f"{url} invalid")