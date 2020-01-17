
from apifiles.authenticate import authenticate
from apifiles.parse import parseData
import json, requests
import itertools



class appliances(object):
    """
        appliance class object has default operations an appliance can provide, including "commit". For any appliance
        specific functions this class must be used.

        THIS CLASS CAN BE BROKEN DOWN INTO META CLASS IF NECESSARY
    """

    def __init__(self, auth, hostname, port=4712, https=True):
        self._file_names = ("proxy.pac", "proxy91.pac", "proxy93.pac") #This variable isn't necessary in this class, this acts as placeholder.
        self.auth = auth
        self.hostname = hostname
        self.port = port
        self.https = https
        self.reference = authenticate(hostname=self.hostname, port=self.port, https=self.https)



    def listAppliances(self, pagesize=10, page=1):
        """
            listAppliances method will generate a full list of appliances available depending on the primary cluster
        logged-in
        :return Full List of Appliances.
        """
        _url = self.reference.createAppendURL(string='appliances')
        _response = self.auth.get(_url, params={'pageSize': pagesize, 'page': page})
        return parseData(_response.text)

    def listAppliancesList(self, name=None, ltype=None):
        """
            listAppliancesList will generate the full list of appliances available in the cluster.
        :param name:
        :param ltype:
        :return: Full list of appliances in the active cluster.
        """
        _url = self.reference.createAppendURL(string='appliances')
        data = {}
        if ltype is not None:
            data['type'] = ltype
        if name is not None:
            data['name'] = name
        _response = self.auth.get(_url, params=data)
        return parseData(_response.text)

    def listAppliancesFileReading(self, filename, pagesize=30, page=1):
        """
            listAppliancesFileReading will read a specific file and display the file output.
        :param filename: Existing File Name
        :param pagesize: Page Size
        :param page: Page Defaults to first page
        :return: read file provided.
        """
        try:
            for id, file in itertools.product(self.BreakDownApplianceList(), self._file_names):
               _url = self.reference.createAppendURL(string='appliances/{}/files/{}'.format(id, filename))
               _response = self.auth.get(_url, params={'pageSize': pagesize, 'page': page})
               return _response.text
        except StopIteration:
            pass


    def fileDelete(self, filename):
        """
            fileDelete will delete specific file from the appliance, if it exists.
        :param filename: Name of existing file to delete.
        :return: status of operation.
        """
        for id in self.BreakDownApplianceList():
            for name in filename:
                _url = self.reference.createAppendURL(string='appliances/{}/files/{}'.format(id, name))
                _response = self.auth.delete(_url)

        for value in self._values["entry"]:
            if _response.status_code == 200:
                print("Successfully Deleted the file from", value["title"])
            else:
                print("File is not Deleted, Try Checking your inputs or Validate Manually")


    def fileUpload(self, filename, filedata):
        """
            fileUpload will upload all a file with filename and filedata provided.
        :param filename: name of the file.
        :param filedata: new file data
        :return: status of the operation
        """
        for id in self.BreakDownApplianceList():
            for name, file in zip(filename,filedata):
                _url = self.reference.createAppendURL(string='appliances/{}/files/{}'.format(id, name))
                _response = self.auth.put(_url, data=file, headers={'Content-Type': 'application/xml'})

        for value in self._values["entry"]:
            if _response.status_code == 200:
                print("Successfully Uploaded file to", value["title"])
            else:
                print("File is not Uploaded as expected, Try Checking your inputs or Validate Manually. ")
        print(input("\n" "Press ENTER to Conti.."))


    def BreakDownApplianceList(self):
        """
            BreakDownApplianceList will parse the listApplianceList data to breakdown the values that is required.
        :return: output _data with values needed.
        """
        output_dict = json.loads(json.dumps(self.listAppliancesList()))
        self._values = next(iter(output_dict.values()))
        _data = list(set([]))
        [_data.append(value["id"])for value in self._values["entry"]]
        return _data

    def commit(self):
        """
            commit is used to "Save Changes" or "Commit" to the appliances which can save changes that is
            modified or created.
        :return: status of commit operation
        """
        _url = self.reference.createAppendURL(string='commit')
        _response = self.auth.post(_url)
        return _response


















