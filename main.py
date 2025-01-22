import pandas as pd

df= pd.read_csv("hotels.csv", dtype={"id":str})
df_cards = pd.read_csv("cards.csv", dtype=str).to_dict(orient="records")

class Hotel:
    def __init__(self,hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()

    def book(self):
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv("hotels.csv", index=False)

    def availability(self):
        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        if availability == "yes":
            return True
        else:
            return False

class Reservation:
    def __init__(self,name,hotel):
        self.name = name
        self.object = hotel


    def generate(self):
        content = f"""
        Thank you for the reservation
        Here are your booking data:
        Name : {self.name}
        Hotel name : {self.object.name}
"""
        return content


class CreditCard:
    def __init__(self, number):
        self.number = number

    def validate(self,expiration,cvc,holder):
        card_data = {"number": self.number,"expiration":expiration, "cvc":cvc,
                     "holder": holder}
        if card_data in df_cards:
            return True


print(df)
hotel_id = input("enter the hotel number:")
#creating object
object = Hotel(hotel_id=hotel_id)



#condition
if object.availability():
    credit_card = CreditCard(number="1234")

    if credit_card.validate(expiration="12/26", cvc="123", holder="JOBI JOSEPH"):
        object.book()
        name = input("enter your name:")

        #creating object
        reservation_ticket = Reservation(name,object)
        print(reservation_ticket.generate())

else:
    print("hotel is not free!!")
