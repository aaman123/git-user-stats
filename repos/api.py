# import requests

# from repos.exceptions import GitHubApiException
# from repos.models import GitHubUser

# GITHUB_API_URL = "https://api.github.com/search/users"

# def create_query(users):
#     query = ''.join(f"{user.strip()}" for user in users )
#     return query

# def get_user(users):
#     query = create_query(users)
#     parameters = {"q": query}
#     print(parameters)

#     response = requests.get(GITHUB_API_URL , params = parameters)


#     if response.status_code != 200:
#         raise GitHubApiException(response.status_code)
    
#     response_json = response.json()

#     items = response_json["items"]
#     print(items)
#     return [GitHubUser( item["id"], item["login"] , item["score"],) for item in items]






