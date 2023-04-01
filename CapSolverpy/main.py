import requests, time



class CapSolver:
    def __init__(self, ClientKey):
        self.base_url = "https://api.capsolver.com"
        self.headers = {"Content-Type": "Application/json"}
        self.clientKey = ClientKey


    def __ApiPost__(self, TaskEndpoint: str, Task: object):
        Task.update({"clientKey": self.clientKey})
        response = requests.post(f"{self.base_url}/{TaskEndpoint}", json=Task, headers=self.headers).json()
        if not hasattr(response, "errorId") or response["errorID"] == 0:
            return response
        else:
            raise(Exception)


    def __CreateTask__(self, Task: object):
        return self.__ApiPost__("createTask", Task)


    def __Task__(self, TaskId: str):
        return self.__ApiPost__("getTaskResult", {"taskId": TaskId})


    def __GetResult__(self, TaskId: str, Sleep, response: dict):
        while response["status"] != "ready":
            response = self.__Task__(TaskId)
            time.sleep(Sleep)
        if not hasattr(response, "errorId") or response["errorID"] == 0:
            return response
        else:
            return None


    def __RetrieveToken__(self, TaskId: str, Sleep, response: dict):
        try:
           return self.__GetResult__(TaskId, Sleep, response)["solution"]["gRecaptchaResponse"]
        except:
            return self.__GetResult__(TaskId, Sleep, response)["solution"]["token"]
    

    def solve(self, Task: object):
        response = self.__CreateTask__(Task)
        return self.__RetrieveToken__(response["taskId"], 5, response) if response !=None else None
