class ClockTime:
    def __init__(self):
        self.attributes=0
        self.hours=0
        self.minutes=0
        self.seconds=0

    # set hours in 24 format
    def setHours(self):
        inputedHours=int(input("Input hours in 24hr format: "))
        if inputedHours<0 or inputedHours>24:
            print("Invalid input, input again")
            self.setHours()
        elif inputedHours==24:
            inputedHours=0
        else:
            self.hours=inputedHours

    # set minutes
    def setMinutes(self):
        inputedMinutes=int(input("Input minutes: "))
        if inputedMinutes<0 or inputedMinutes>59:
            print("Invalid input, input again")
            self.setMinutes()
        else:
            self.minutes=inputedMinutes

    # set seconds
    def setSeconds(self):
        inputedSeconds=int(input("Input seconds: "))
        if inputedSeconds<0 or inputedSeconds>59:
            print("Invalid input, input again")
            self.setSeconds()
        else:
            self.seconds=inputedSeconds

    # setTime method to call the rest of the set methods
    def setTime(self):
        self.setHours()
        self.setMinutes()
        self.setSeconds()

    # display set values
    def showTime(self):
        print(f"Time is {self.hours}:{self.minutes}:{self.seconds}")

# create an object for clockTime class
ct=ClockTime()
ct.setTime()
ct.showTime()



