from flask_restful import Resource
from flask_restful import request
from datetime import datetime

datas=[{'CreditCardNumber':'1234567896'},{'CreditCardNumber':'9632587412'},{'CreditCardNumber':'8523697412'}] #like DB

class ProcessPayment(Resource):
    def validation(self,details):
        card_len=len(details['CreditCardNumber'])
        if card_len==10:
            if next(filter(lambda x: x['CreditCardNumber']==details['CreditCardNumber'],datas),None) is not None:
                try:
                    expiredate = datetime.strptime(details['ExpirationDate'],"%d/%m/%Y")
                except:
                    return " Entered date is not in correct format EX:DD/MM/YYYY "

                present = datetime.now()
                if expiredate.date() > present.date():
                    if details['Amount'] >0:
                        return "done"
                    elif details['Amount']==0:
                        return "invalid amount Zero"
                    else:
                        return "invalid amount(its Negative)"
                
                else:
                    return "your card get expired"
            return "Card number not matching with DB"
        return "Invalid card number"

    def details_present(self,details):
        needed=[details['CreditCardNumber'],details['CardHolder'],details['ExpirationDate'],details['Amount']]
        for x in needed:   
            if x == "":
                return "some mandatoy field is missing"
        needed=details['SecurityCode']
        needed=str(needed)
        if len(needed)==3 or len(needed)==0 :
            out=self.validation(details)
            return out
        else:
            return "please enter valid SecurityCode"


    def CheapPaymentGateway(self):
        #CheapPaymentGateway
         return "success in CheapPaymentGateway"

    def PremiumPaymentGateway(self):
        count=0
        while count < 3:
            #- PremiumPaymentGateway 
            payment='success'#hard code
            if payment=="success":
                return "Payment success in PremiumPaymentGateway"
            else:
                count+=1
        return "Payment unsuccessfull try again"
   
    def post(self):
        data=request.get_json()
        details={"CreditCardNumber":data["CreditCardNumber"],"CardHolder":data["CardHolder"],"ExpirationDate":data["ExpirationDate"],"SecurityCode":data["SecurityCode"],"Amount":data["Amount"]}

        items=self.details_present(details)
        if items == 'done':
            if details['Amount'] <=20:
                out=self.CheapPaymentGateway()
                return out

            elif details['Amount'] >=21 and details['Amount'] <=500:
            #ExpensivePaymentGateway
                count=0
                while count < 1:
                    out=self.CheapPaymentGateway()
                    if out:
                        return "payment success in CheapPaymentGateway because ExpensivePaymentGateway is not avilable "
                    else:
                        count+=1
                        return "payment unsuccessfull"


            elif details['Amount'] > 500:
                out=self.PremiumPaymentGateway()
                return out
                #count=0
                #while count < 3:
                    #- PremiumPaymentGateway 
                    #payment='success'#hard code
                    #if payment=="success":
                        #return "Payment success in PremiumPaymentGateway"
                    #:
                        #count+=1
                #return "Payment unsuccessfull try again"
            else:
                return "some thing went wrong please try again"
        else:
            return items
