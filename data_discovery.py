import re
import csv

#List to store matched data
matched_pan=[]
matched_aadhar=[]
matched_mobile=[]
matched_email=[]
matched_passport=[]
matched_driving=[]
matched_voterid=[]
matched_cvv=[]
                                    #pattern recovery form Sample data


#pattern for recorganizing CVV
cvv_pattern=re.compile(r'^\d{3,4}$')


#pattern for recorganizing Voter ID
voterid_pattern=re.compile(r'[A-Z]{3}\d{7}')

#pattern for recorganizing Passport
driving_pattern=re.compile(r'[A-Z]{2}-?\d{13}')


#pattern for recorganizing Passport
passport_pattern=re.compile(r'[A-Z]\d{7}')


#pattern for recorganizing mobile nubers
mobile_pattern = re.compile(r'\+91+\s[6-9][0-9]{9}')

#pattern for recorganizing aadhar number
aadhar_pattern=re.compile(r'\d{4}\s\d{4}\s\d{4}')

#Pattern for recorganizing PAN Number
pan_pattern=re.compile(r'[A-Z]{5}\d{4}[A-Z]')

#pattern for recorganizing email
email_pattern= re.compile(r'[A-Za-z.+_-]+@[A-Za-z-.]+\.[A-Za-z0-9-.]+')

#Pattern for recorganizing full name

full_name_pattern=re.compile(r'[A-z][a-z]+\s[A-z][a-z]+')


                            #FINDING DATA FROM THE TEXT FILE(MOBILE N.O, EMAIL)


with open('india_pii_data_sample.txt','r') as data_input:
    contents=data_input.read()
    
    #finding mobile number
    mobile_matches= mobile_pattern.findall(contents)

    for match in mobile_matches:
        matched_mobile.append(match)
    print("Mobile Numbers:",matched_mobile)
    print("\n")

    #finding email
    email_matches=email_pattern.findall(contents)

    for match in email_matches:
        matched_email.append(match)
    print("MATCHED EMAILS:",matched_email)
    print("\n")


                                         #  FINDING DATA FROM CSV(PAN, AADHAR,DRIVING LISCENCE, VOTERID, CVV)

with open('sample_data.csv','r') as csv_data:
    csv_reader=csv.reader(csv_data)

                                
    for row in csv_reader:
        for cell in row:

            #Findining pan number
            if pan_pattern.match(cell):
                
                matched_pan.append(cell)#Storing them into lists
            #Finding Aadhar number
            elif aadhar_pattern.match(cell):

                matched_aadhar.append(cell) #Storing them into lists


            #Finding Aadhar number
            elif passport_pattern.match(cell):
                
                matched_passport.append(cell) #Storing them into lists

            #Finding Driving Liscence
            elif driving_pattern.match(cell):
                matched_driving.append(cell)

            #Findding Voterid
            elif voterid_pattern.match(cell):
                matched_voterid.append(cell)
            
            #Findding CVV
            elif cvv_pattern.match(cell):
                matched_cvv.append(cell)

            

#Printing matched content
    print("MATCHED PAN: ",matched_pan)
    print("\n")
    print("MATCHED Aadhar: ",matched_aadhar)
    print("\n")
    print("Matched Passport:",matched_passport)
    print("\n")
    print("Matched Driving:",matched_driving)
    print("\n")
    print("MATCHED VOTER ID:",matched_voterid)
    print("\n")
    print("MATCHED CVV:",matched_cvv)

    
