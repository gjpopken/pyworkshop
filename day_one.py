import requests

def main():
    languages = ["python", 'javascript', 'ruby']
    request = 'https://api.github.com/search/repositories?' + create_query(languages)

    response = requests.get(request)
    
    response_json = response.json()
    print(f'The response is this: {response_json}')


def create_query(languages, sort="stars", order="desc"):
    for lang in languages:
        pass
    return 'q=stars:>50000'

if __name__ == '__main__':
    main()