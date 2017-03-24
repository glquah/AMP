#
#   Cisco Network Services Orchestrator(NSO) Wrapper API
#       v.01
#
#   Joel Fernandez(joelfern@cisco.com)
#       Feb 2017
#
#       This class provides methods to facilitates
#       access to the Network Services Orchestrator API.
#
#   REQUIREMENTS:
#       Python requests library (issue the 'pip install requests' command in shell or cmd)
#
#   WARNING:
#       This script is meant for educational purposes only.
#       Any use of these scripts and tools is at
#       your own risk. There is no guarantee that
#       they have been through thorough testing in a
#       comparable environment and we are not
#       responsible for any damage or data loss
#       incurred with their use.
#
#   INFORMATION:
#       If you have further questions about this API and script, please contact GVE. Here are the contact details:
#           For internal Cisco gve-programmability@cisco.com
#           For Cisco partners, open a case at www.cisco.com/go/ph

# IP & ADMIN ONLY USED WHEN DCLOUD IS WORKING
import requests

#host = '198.18.134.28:8080'
host = 'api.apjc.amp.cisco.com'
username = '8a2a49f003566ed3fb0b'
password = '5d97572a-675f-40b6-a98c-2ba67b8e2c92'

#username = 'badc2e9d062af26be4ad'
#password = 'ff7924e3-6e14-404e-b289-d5628b7de7ca'
#username = 'admin'
#password = 'admin'

class Wrapper_API(object) :
    """
    This class is used to interact with the NSO API
    """
    def __init__(self):
        self.host = host
        self.username = username
        self.password = password

    def send_api_request(self, phrase):
        """
        Sends a request to the API for retrieving data.
        """
        url = 'http://' + host + '/v1' + '/' + phrase
        headers = {'Content-Type': 'application/json',
                   'Accept': 'application/json',
                   'Accept-Encoding': 'application/gzip'
                   }
        response = requests.get(url, auth=(username, password),
                                headers=headers, verify=False)
        return response.text

    def getComputers(self):
        """
        Retrieves a list of computers
        """
        computersURL = '/computers'
        apiRequest = Wrapper_API()
        apiResponse = apiRequest.send_api_request(computersURL)
        return apiResponse

    def getComputersbyGuid(self):
        """
        Retrieves a list of computers with given connector_guid
        """
        computersURL = '/computers/7a6d95ee-bc44-4039-b317-728ed5690481'
        apiRequest = Wrapper_API()
        apiResponse = apiRequest.send_api_request(computersURL)
        return apiResponse

    def getComputerstrajectory(self):
        """
        Retrieves specific computer's trajectory with given connector_guid
        """
        computersURL = '/computers/7a6d95ee-bc44-4039-b317-728ed5690481/trajectory'
        apiRequest = Wrapper_API()
        apiResponse = apiRequest.send_api_request(computersURL)
        return apiResponse

    def getComputerActivity1(self):
        """
        Retrieves a list of computers that has observed files with given file name
        """
        computersURL = '/computers/activity?q=SearchProtocolHost.exe&limit=5'
        apiRequest = Wrapper_API()
        apiResponse = apiRequest.send_api_request(computersURL)
        return apiResponse

    def getComputerActivity2(self):
        """
        Retrieves a list of computers that has observed files with given SHA-256 value
        """
        computersURL = '/computers/activity?q=814a37d89a79aa3975308e723bc1a3a67360323b7e3584de00896fe7c59bbb8e&offset=0&limit=5'
        apiRequest = Wrapper_API()
        apiResponse = apiRequest.send_api_request(computersURL)
        return apiResponse

    def getEvent1(self):
        """
        Retrieves a list of event sorted in descending order by timestamp
        """
        computersURL = '/events?limit=2'
        apiRequest = Wrapper_API()
        apiResponse = apiRequest.send_api_request(computersURL)
        return apiResponse

    def getEvent2(self):
        """
        Retrieves a list of event filtered by connector guid
        """
        computersURL = '/events?connector_guid[]=0f49fe9a-ac1b-4a8f-a557-f2078434634b&limit=1'
        apiRequest = Wrapper_API()
        apiResponse = apiRequest.send_api_request(computersURL)
        return apiResponse

    def getEvent3(self):
        """
        Retrieves a list of event filtered by group guid
        """
        computersURL = '/events?group_guid[]=b077d6bc-bbdf-42f7-8838-a06053fbd98a&limit=1'
        apiRequest = Wrapper_API()
        apiResponse = apiRequest.send_api_request(computersURL)
        return apiResponse

    def getEvent4(self):
        """
        Retrieves a list of event filtered by detection_SHA256
        """
        computersURL = '/events?detection_sha256=3372c1edab46837f1e973164fa2d726c5c5e17bcb888828ccd7c4dfcc234a370&limit=1'
        apiRequest = Wrapper_API()
        apiResponse = apiRequest.send_api_request(computersURL)
        return apiResponse

    def getEvent5(self):
        """
        Retrieves a list of event filtered by application_SHA256
        """
        computersURL = '/events?application_sha256=3372c1edab46837f1e973164fa2d726c5c5e17bcb888828ccd7c4dfcc234a370&limit=1'
        apiRequest = Wrapper_API()
        apiResponse = apiRequest.send_api_request(computersURL)
        return apiResponse

    def getEvent6(self):
        """
        Retrieves a list of event filtered by detection_SHA256 and application_SHA256
        """
        computersURL = '/events?detection_sha256=3372c1edab46837f1e973164fa2d726c5c5e17bcb888828ccd7c4dfcc234a370&application_sha256=3372c1edab46837f1e973164fa2d726c5c5e17bcb888828ccd7c4dfcc234a370&limit=1'
        apiRequest = Wrapper_API()
        apiResponse = apiRequest.send_api_request(computersURL)
        return apiResponse

    def getEvent7(self):
        """
        Retrieves a list of event newer than a given timestamp
        """
        computersURL = '/events?start_date=2015-10-01T00%3A00%3A00%2B00%3A00&offset=10&limit=10'
        apiRequest = Wrapper_API()
        apiResponse = apiRequest.send_api_request(computersURL)
        return apiResponse

    def getEventTypes(self):
        """
        Retrieves a list of event
        """
        computersURL = '/event_types'
        apiRequest = Wrapper_API()
        apiResponse = apiRequest.send_api_request(computersURL)
        return apiResponse

    def getApplicationsBlockingList(self):
        """
        Retrieves a list of application_blocking file_lists
        """
        computersURL = '/event_types'
        apiRequest = Wrapper_API()
        apiResponse = apiRequest.send_api_request(computersURL)
        return apiResponse

    def getApplicationsBlockingList(self):
        """
        Retrieves a list of application_blocking file_lists
        """
        computersURL = '/file_lists/application_blocking?limit=3&offset=2'
        apiRequest = Wrapper_API()
        apiResponse = apiRequest.send_api_request(computersURL)
        return apiResponse

    def getApplicationsBlockingbyName(self):
        """
        Retrieves a list of application_blocking file_lists filtered by name
        """
        computersURL = '/file_lists/application_blocking?name[]=Sample%20Application%20Blocking%20List&limit=10'
        apiRequest = Wrapper_API()
        apiResponse = apiRequest.send_api_request(computersURL)
        return apiResponse

    def getApplicationsBlockingbyGuid(self):
        """
        Retrieves a list of application_blocking file_lists with given file_list_guid
        """
        computersURL = '/file_lists/e773a9eb-296c-40df-98d8-bed46322589d'
        apiRequest = Wrapper_API()
        apiResponse = apiRequest.send_api_request(computersURL)
        return apiResponse

    def getCustomDetectionbyGuid(self):
        """
        Retrieves simple_custom_detection file list with given file_list_guid
        """
        computersURL = '/file_lists/03097bae-53f9-44b1-a0e5-d23b1f33a94a'
        apiRequest = Wrapper_API()
        apiResponse = apiRequest.send_api_request(computersURL)
        return apiResponse

    def getFileListItem1(self):
        """
        Retrieves a list of file items associated with a specific file list with given file_list_guid
        """
        computersURL = '/file_lists/e773a9eb-296c-40df-98d8-bed46322589d/files?limit=3&offset=2'
        apiRequest = Wrapper_API()
        apiResponse = apiRequest.send_api_request(computersURL)
        return apiResponse

    def getFileListItem2(self):
        """
        Retrieves a list of file items with a given SHA-256 and associated with file list for given file_list_guid
        """
        computersURL = '/file_lists/e773a9eb-296c-40df-98d8-bed46322589d/files/9e1ec8b43a88e68767fd8fed2f38e7984357b3f4186d0f907e62f8b6c9ff56ad'
        apiRequest = Wrapper_API()
        apiResponse = apiRequest.send_api_request(computersURL)
        return apiResponse

    def getGroups(self):
        """
        Retrieves a list of group
        """
        computersURL = '/groups'
        apiRequest = Wrapper_API()
        apiResponse = apiRequest.send_api_request(computersURL)
        return apiResponse

    def getGroupsbyGuid(self):
        """
        Retrieves a list group with given group_guid
        """
        computersURL = '/groups/b077d6bc-bbdf-42f7-8838-a06053fbd98a'
        apiRequest = Wrapper_API()
        apiResponse = apiRequest.send_api_request(computersURL)
        return apiResponse

    def getPolicy(self):
        """
        Retrieves a list of policy
        """
        computersURL = '/policies?limit=3&offset=2'
        apiRequest = Wrapper_API()
        apiResponse = apiRequest.send_api_request(computersURL)
        return apiResponse

    def getPolicybyGuid(self):
        """
        Retrieves a list of policy for given policy_guid
        """
        computersURL = '/policies/89912c9e-8dbd-4c2b-a1d8-dee8a0c2bb29'
        apiRequest = Wrapper_API()
        apiResponse = apiRequest.send_api_request(computersURL)
        return apiResponse

    def getVersion(self):
        """
        Retrieves a list of event
        """
        computersURL = '/version'
        apiRequest = Wrapper_API()
        apiResponse = apiRequest.send_api_request(computersURL)
        return apiResponse

