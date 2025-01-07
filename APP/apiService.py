# import requests

# class AuthAPIService:

#     def __init__(self, request, id):
#         self.request = request
#         self.id = id
#         self.api_url = "http://127.0.0.1:8000"
#         self.token = self.authenticate()

#     def authenticate(self):
#         response = requests.post(f"{self.api_url}/auth", data={'api_key': 'your_api_key'})
#         if response.status_code == 200:
#             return response.json().get('token')
#         raise Exception("Authentication failed")
    
#     def is_authenticated(self):
#         return bool(self.token)
    
#     def get_blog_info(self, id):
#         response = requests.get(f"{self.api_url}/pythonblogs/{id}/", headers={'Authorization': f'Bearer {self.token}'})
#         if response.status_code == 200:
#             return response.json()
#         raise Exception(f"Failed to fetch blog info for ID {id}")
    
#     def get_topic_content(self, id):
#         response = requests.get(f"{self.api_url}/topics/{id}/", headers={'Authorization': f'Bearer {self.token}'})
#         if response.status_code == 200:
#             return response.json()
#         raise Exception(f"Failed to fetch topic content for ID {id}")

    
    