'''
Strategy design pattern : is a behavioral design pattern that lets you define a family of algorithms,
put each of them into a separate class, and make their objects interchangeable.
'''
import string
import random
from typing import List
from abc import ABC, abstractmethod
class SupportTicket:

    def __init__(self, customer, issue):
        self.id = generate_id()
        self.customer = customer
        self.issue = issue

def generate_id(length=8):
    # helper function for generating an id
    return ''.join(random.choices(string.ascii_uppercase, k=length))

class TicketOrderingStrategy(ABC):#Our strategy class
    @abstractmethod
    def ordering(self, list: List[SupportTicket]) -> List[SupportTicket]: #ordering method 
        pass


class FIFOOrdering(TicketOrderingStrategy): #Inherit from our strategy class
    def ordering(self, list: List[SupportTicket]) -> List[SupportTicket]: #ordering method 
        return list.copy() #Return a copy from original list woth first in first out 

class FILOOrdering(TicketOrderingStrategy): #Inherit from our strategy class
    def ordering(self, list: List[SupportTicket]) -> List[SupportTicket]: #ordering method 
        list_copy = list.copy
        list.copy.reverse() #reverse the original list to make it first in last put
        return list_copy 

class RANDOMOrdering(TicketOrderingStrategy): #Inherit from our strategy class
    def ordering(self, list: List[SupportTicket]) -> List[SupportTicket]: #ordering method 
        list_copy = list.copy()
        random.shuffle(list_copy)
        return list_copy #Return a copy from original list with random ordering 



class CustomerSupport:

    def __init__(self, processing_strategy: TicketOrderingStrategy): # Change the str ordering to a class strategy
        self.tickets = []
        self.processing_strategy = processing_strategy

    def create_ticket(self, customer, issue):
        self.tickets.append(SupportTicket(customer, issue))

    def process_tickets(self, processing_strategy: TicketOrderingStrategy):
        # if it's empty, don't do anything
        if len(self.tickets) == 0:
            print("There are no tickets to process. Well done!")
            return
        
        ticket_list = processing_strategy.ordering(self.tickets) #Use our strategy class

        for ticket in ticket_list:
            self.process_ticket(ticket)
        
        

    def process_ticket(self, ticket: SupportTicket):
        print("==================================")
        print(f"Processing ticket id: {ticket.id}")
        print(f"Customer: {ticket.customer}")
        print(f"Issue: {ticket.issue}")
        print("==================================")


# create the application
app = CustomerSupport("filo")

# register a few tickets
app.create_ticket("Yussef raouf", "My computer need fix")
app.create_ticket("Raouf", "I can't upload any videos, please help.")
app.create_ticket("John doee", "VSCode doesn't automatically solve my bugs.")

# process the tickets
app.process_tickets(RANDOMOrdering())