# class GitHubApiException(Exception):

#     def __init__(self ,  status_code):
#         if status_code == 403:
#             message = "Rate limit reached , please try again after 1 minute."
#         else:
#             message =  f"Http status code is :{status_code}."


#         super().__init__("A github api exception occured" +message)

#     #