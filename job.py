class Job:
    def __init__(self, title="", company="", date="", link="", location=""):
        self.title = title
        self.company = company
        self.date = date
        self.link = link
        self.location = location

    def setTitle(self, title):
        if(title != None):
            self.title = title

    def setCompany(self, company):
        if(company != None):
            self.company = company

    def setDate(self, date):
        if(date != None):
            self.date = date

    def setLink(self, link):
        if(link != None):
            self.link = link

    def setLocation(self, location):
        if(location != None):
            self.location = location
