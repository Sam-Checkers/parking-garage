class parking_garage():
    
    tickets = 10
    parkingSpaces = 10
    payment = []
    currentTicket = {'ticket status: paid'}
    enter =[]
    
    def takeTicket(self):
        enter = input('take ticket? Y/N')
        self.enter.append(enter)
        if enter.lower() == 'y' and self.tickets !=0:
            self.tickets = self.tickets - 1
            self.parkingSpaces = self.parkingSpaces - 1
            self.currentTicket = False

        if self.tickets == 0:
            print('Sorry. No available spaces')
            self.currentTicket = False
        if enter.lower() == 'n':
            print('Then why are you here?')
            self.currentTicket = False

    
    def payForParking(self):
        if self.enter == ['y'] or self.enter == ['Y']:
            fee = input('To pay now, insert $5.00 Y/N')
            if fee.lower() == 'y':
                self.payment.append(5)
                self.currentTicket = True
                print('Ticket paid. 15 minutes available')
            if fee.lower() == 'n':
                self.currentTicket = False
        else:
            print('No ticket, no entry')
            
    def leaveGarage(self):
        if self.enter == ['y'] or self.enter == ['Y']:
            if self.currentTicket == True:
                print('Thank you, have a nice day!')
                self.tickets = self.tickets +1
                self.parkingSpaces = self.parkingSpaces + 1
            if self.currentTicket == False:
                fee = input('insert $5.00 Y/N')
                if fee.lower() == 'y':
                    self.payment.append(5)
                    self.currentTicket = True
                    print('Thank you, have a nice day!')
                if fee.lower() == 'n':
                    print("Come back when you can afford it.")

garage = parking_garage()
garage.takeTicket()
garage.payForParking()
garage.leaveGarage()