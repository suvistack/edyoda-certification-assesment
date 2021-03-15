#!/usr/bin/env python
# coding: utf-8

# In[8]:


from tkinter import * 
class gym():
    global users
    users=[]
    global data
    data=dict()
    global data2
    data2=dict()
    global BMI_dict 
    BMI_dict=dict()
    BMI_dict['0-18.5']={'Mon': 'Chest' , 'Tue': 'Biceps' , 'Wed': 'Rest' , 'Thu': 'Back' , 'Fri': 'Triceps' , 'Sat': 'Rest' , 'Sun': 'Rest'}
    BMI_dict['18.5-25']={'Mon': 'Chest' , 'Tue': 'Biceps' , 'Wed': 'Cardio/Abs' , 'Thu': 'Back' , 'Fri': 'Triceps' , 'Sat': 'Legs' , 'Sun': 'Rest'}
    BMI_dict['25-30']={'Mon': 'Chest' , 'Tue': 'Biceps' , 'Wed': 'Cardio/Abs' , 'Thu': 'Back' , 'Fri': 'Triceps' , 'Sat': 'Legs' , 'Sun': 'Cardio'}
    BMI_dict['>30']={'Mon': 'Chest' , 'Tue': 'Biceps' , 'Wed': 'Cardio/Abs' , 'Thu': 'Back' , 'Fri': 'Triceps' , 'Sat': 'Cardio' , 'Sun': 'Cardio'}
    def welcome(self):
        print('====================================')
        print('            FITNESS FREAK             ')
        print('====================================')
        print('              ^ ^                   ')
        print("            '(o o)'                 ")
        print('               Y                    ')
        print("             _/|\_                  ")
        print("               |                    ")
        print("             _/ \_                  ")
        print("HELLO!!!  Welcome to Fitness Freak Member management ")
        print('Are you a SuperUSER or a Member')
        print('For SuperUSER press:1')
        print('For Member press:2')
        key=(input('Enter the no.:'))
        if key=="1":
            self.SuperUser_login()
        elif key=="2":
            self.Member_login()
        else:
            print('Choose only 1 or 2')
            self.welcome()
            
    def SuperUser_login(self):
        print('Superuser only!! Please login to continue')
        Username=input('Enter Your Username:' )
        Password=input('Enter Your Password: ')
        if Password=='admin001':
            print('Welcome', Username)
            self.Main_menu_super()
        else:
            print('Sorry access denied')
            self.SuperUser_login()
        
    def Member_login(self):
        print('Hello Member!! Please login to continue')
        Username=input('Enter Your Username:' )
        self.Username=Username
        Password=input('Enter Your Password: ')
        if Username in users:
            print('Welcome', Username)
            self.Main_menu_member()
        else:
            print('You are not a registered member. Please contact the superuser.')
        
    def Main_menu_super(self):
        print('The following are the options')
        print('1:Create Member') 
        print('2:View Member')
        print('3:Delete Member')
        print('4:Update Member') 
        print('5:Create Regimen')
        print('6:View Regimen')
        print('7:Delete Regimen')
        print('8:Update Regimen')
        print('9:Exit')
        key=input('Enter the no.: ')
        if key=='1':
            self.create_member()
        elif key=='2':
            self.view_member()
        elif key=='3':
            self.delete_member()
        elif key=='4':
            self.update_member()
        elif key=='5':
            self.create_regimen()
        elif key=='6':
            self.view_regimen()
        elif key=='7':
            self.delete_regimen()
        elif key=='8':
            self.update_regimen()
        elif key=='9':
            self.exit()
        else:
            print('Please select only from above options')
            self.Main_menu_super()
            
    def Main_menu_member(self):
        print('The following are the options')
        print('1:My regimen') 
        print('2:My profile')
        print('3: Exit')
        key=input('Enter the no.: ')
        if key=='1':
            self.My_regimen()
        elif key=='2':
            self.My_profile()
        elif key=='3':
            self.exit()
        else:
            print('Please select only from above options')
            self.Main_menu_member()
    def My_regimen(self):
        try:
            print(data2[self.Username]['Regimen'])
            self.Main_menu_member()
        except:
            print('Regimen is not valid for thie membership')
            self.Main_menu_member()
    def My_profile(self):
        print(data2[self.Username])
        self.Main_menu_member()
        
            
            
        
    def create_member(self):
        info=dict()
        print("Fill the following details of a memeber to register")
        info['Name']=input('Enter the name: ')
        info['Age']=input('Enter the Age: ')
        info['Gender']=input('Enter the Gender: ')
        info['Mobile_no']=input('Enter the mobile no.: ')
        info['Email']=input('Enter the Email id: ')
        try:
            info['BMI']=int(input('Enter the BMI: '))
        except:
            print('Please enter a valid value.')
            info['BMI']=int(input('Enter the BMI: '))
        print('The allowed values for membership are 1, 3, 6 and 12.') 
        print('If the entered are values are not found such, the default value becomes 1 month')
        info['Membership']=input('Enter the duration or no. of months:')
        if info['Membership']=='1' or info['Membership']=='3' or info['Membership']=='6' or info['Membership']=='12':
            pass
        else:
            
            info['Membership']='1'
        data[info['Mobile_no']]=info
        data2[info['Name']]=info
        
        users.append(info["Name"])
        
        print('The member is now registered!!')
        root=Tk()
        root.title('Fitness freak')
        root.geometry('350x200')
        label = Label(root , text ="The member is registered") 
        label.pack()

        root.mainloop()
        print('To go back to main menu , press any key')
        key=input()
        self.Main_menu_super()
        
    def view_member(self):
        try:
            Mobileno=input('Enter the mobile no.')
            print(data[Mobileno])
            self.Main_menu_super()
        except:
            print('The given contact no. is not registered')
            print('Press 1 to re-enter the contact no.')
            print('Press 2 to go to main menu')
            key=input('Enter the no.: ')
            if key=='1':
                self.view_member()
            elif key=='2':
                self.Main_menu_super ()
            else:
                print('The no. is out of range')
    def delete_member(self):
        try:
            Mobileno=input('Enter the mobile no.')
            del data[Mobileno]
            print('The member registered with contact no.', Mobileno, 'is deleted')
            self.Main_menu_super ()
        except:
            print('The given contact no. is not registered')
            print('Press 1 to re-enter the contact no.')
            print('Press 2 to go to main menu')
            key=input('Enter the no.: ')
            if key=='1':
                self.delete_member()
            elif key=='2':
                self.Main_menu_super ()
            else:
                print('The no. is out of range')
        
    def update_member(self):
        try:
            Mobileno=input('Enter mobile no.')
            print(data[Mobileno])
            change_to=input('Change the membership to:')
            data[Mobileno]['Membership']=change_to
            print('The new membership details are')
            print(data[Mobileno])
            self.Main_menu_super ()
        except:
            print('The entered mobile no. is not registered')
            print('Press 1 to re-enter the contact no.')
            print('Press 2 to go to main menu')
            key=input('Enter the no.: ')
            if key=='1':
                self.update_member()
            elif key=='2':
                self.Main_menu_super ()
            else:
                print('The no. is out of range')
    def create_regimen(self):
        try:
            mobileno=input('Enter the contact no:')
            BMI=data[mobileno]['BMI']
            name=data[mobileno]['Name']
            if 0<int(BMI)<18.5:
                data[mobileno]['Regimen']=BMI_dict['0-18.5']
                data2[name]['Regimen']=BMI_dict['0-18.5']
            elif 18.5<=int(BMI)<25:
                data[mobileno]['Regimen']=BMI_dict['18.5-25']
                data2[name]['Regimen']=BMI_dict['18.5-25']
            elif 25<=int(BMI)<30:
                data[mobileno]['Regimen']=BMI_dict['25-30']
                data2[name]['Regimen']=BMI_dict['25-30']
            elif int(BMI)>30:
                data[mobileno]['Regimen']=BMI_dict['>30']
                data2[name]['Regimen']=BMI_dict['>30']
            print('The regimen is created ')
            self.Main_menu_super ()
        except:
            print('The entered mobile no. is not registered')
            print('Press 1 to re-enter the contact no.')
            print('Press 2 to go to main menu')
            key=input('Enter the no.: ')
            if key=='1':
                self.create_regimen()
            elif key=='2':
                self.Main_menu_super ()
            else:
                print('The no. is out of range')
    def view_regimen(self):
        try:
            mobileno=input('Enter the contact no:')
            print('The regimen is:')
            print(data[mobileno]['Regimen'])
            self.Main_menu_super ()
        except:
            print('The entered mobile no. has no regimen created')
            print('Press 1 to re-enter the contact no.')
            print('Press 2 to go to main menu')
            key=input('Enter the no.: ')
            if key=='1':
                self.view_regimen()
            elif key=='2':
                self.Main_menu_super ()
            else:
                print('The no. is out of range')
        
    def delete_regimen(self):
        try:
            mobileno=input('Enter the contact no:')
            del data[mobileno]['Regimen']
        
            print('The regimen has been deleted')
            
            self.Main_menu_super ()
        except:
            print('The entered mobile no. has no regimen created')
            print('Press 1 to re-enter the contact no.')
            print('Press 2 to go to main menu')
            key=input('Enter the no.: ')
            if key=='1':
                self.view_regimen()
            elif key=='2':
                self.Main_menu_super ()
            else:
                print('The no. is out of range')
    def update_regimen(self):
        mobileno=input('Enter mobile no. :')
        print('The following are the details:')
        print(data[mobileno])
        name=data[mobileno]['Name']
        BMI=input("Change the BMI to:")
        data[mobileno]['BMI']=BMI
        if 0<int(BMI)<18.5:
            data[mobileno]['Regimen']=BMI_dict['0-18.5']
            data2[name]['Regimen']=BMI_dict['0-18.5']
        elif 18.5<=int(BMI)<25:
            data[mobileno]['Regimen']=BMI_dict['18.5-25']
            data2[name]['Regimen']=BMI_dict['18.5-25']
        elif 25<=int(BMI)<30:
            data[mobileno]['Regimen']=BMI_dict['25-30']
            data2[name]['Regimen']=BMI_dict['25-30']
        elif int(BMI)>30:
            data[mobileno]['Regimen']=BMI_dict['>30']
            data2[name]['Regimen']=BMI_dict['>30']
        print('The regimen is updated ')
        print(data[mobileno]['Regimen'])
        self.Main_menu_super ()
        
        
    def exit(self):
        pass


# In[9]:


obj=gym() 
obj.welcome()


# 

# In[ ]:




