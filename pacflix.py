from datetime import datetime
from dateutil.relativedelta import relativedelta

class pacflix():
    list_of_referral_code = []

    def __init__(self, user_name):
        self.user_name = user_name
        self.start_date = None
        self.end_date = None
        self.current_plan = None
        self.duration = 0

        pacflix.list_of_referral_code.append(self.user_name)
        print(f"Your account successfully created, share this code '{self.user_name}' to your friend to get some benefits.")

    def list_plan(self):
        print('List of Pacflix plan:')
        print('1. Basic Plan.')
        print('SD, 1 device, Movie, Rp. 120.000,-.')
        print()
        print('2. Standard Plan.')
        print('HD, 2 devices, Movie + Sports, Rp. 160.000,-.')
        print()
        print('3. Premium Plan.')
        print('UHD, 4 devices, Movie + Sports + Original, Rp. 200.000,-.')

    def check_plan(self):
        if(self.current_plan == None):
            print('You do not have any subs yet')
        else:
            print(f'Your current plan is {self.current_plan}.')
            print(f'Start subs at {self.start_date}.')
            print(f'End subs at {self.end_date}.')

    def purchase(self, new_plan, ref_code, duration):
        total_price = 0

        if((ref_code != None) and (ref_code in pacflix.list_of_referral_code)):
            self.duration = duration
            self.start_date = datetime.now()
            self.end_date = self.start_date + relativedelta(months=duration)

            if (new_plan == 'Basic Plan'):
                self.current_plan = 'Basic Plan'
                total_price = (120000 - (0.04 * 120000))
                print(f"You're selected Basic Plan with referral code from {ref_code}, price {total_price}.")

            elif(new_plan == 'Standard Plan'):
                self.current_plan = 'Standard Plan'
                total_price = (160000 - (0.04 * 160000))
                print(f"You're selected Standard Plan with referral code from {ref_code}, price {total_price}.")

            elif(new_plan == 'Premium Plan'):
                self.current_plan = 'Premium Plan'
                total_price = (200000 - (0.04 * 200000))
                print(f"You're selected Premium Plan with referral code from {ref_code}, price {total_price}.")

            else:
                self.duration = 0
                self.start_date = None
                self.end_date = None
                print('Your selected plan in invalid!.')

        elif((ref_code != None) and (ref_code not in pacflix.list_of_referral_code)):
            print('Your referral code is invalid!.')

        elif(ref_code == None):
           self.duration = duration
           self.start_date = datetime.now()
           self.end_date = self.start_date + relativedelta(months=duration)

           if (new_plan == 'Basic Plan'):
                self.current_plan = 'Basic Plan'
                total_price = 120000
                print(f"You're selected Basic Plan, price {total_price}.")

           elif(new_plan == 'Standard Plan'):
                self.current_plan = 'Standard Plan'
                total_price = 160000
                print(f"You're selected Standard Plan, price {total_price}.")

           elif(new_plan == 'Premium Plan'):
                self.current_plan = 'Premium Plan'
                total_price = 200000
                print(f"You're selected Premium Plan, price {total_price}.")

           else:
                self.duration = 0
                self.start_date = datetime.now()
                self.end_date = self.start_date + relativedelta(months=duration)
                print('Your selected plan in invalid!.')

        else:
            print('Something back happen.')

    def upgrade_plan(self, new_plan):
        subs_time = self.end_date - datetime.now()
        total_price = 0

        if(subs_time.days > 360):
            if (self.current_plan == 'Basic Plan'):
                if(new_plan == 'Standard Plan'):
                    self.current_plan = 'Standard Plan'
                    total_price = (160000 - (0.05 * 160000))
                    print(f'Upgrade to {self.current_plan}, price + discount = {total_price}')

                elif(new_plan == 'Premium Plan'):
                    self.current_plan = 'Premium Plan'
                    total_price = (200000 - (0.05 * 200000))
                    print(f'Upgrade to {self.current_plan}, price + discount = {total_price}')

                else:
                    print('Your selected new plan is invalid')

            elif(self.current_plan == 'Standard Plan'):
                if(new_plan == 'Premium Plan'):
                    self.current_plan = 'Premium Plan'
                    total_price = (200000 - (0.05 * 200000))
                    print(f'Upgrade to {self.current_plan}, price + discount = {total_price}')
                
                else:
                    print('Your selected new plan is invalid!.')

            else:
                print("You're in highest tier, you can't downgrade!.")

        else:
            if (self.current_plan == 'Basic Plan'):
                if(new_plan == 'Standard Plan'):
                    self.current_plan = 'Standard Plan'
                    total_price = 160000
                    print(f'Upgrade to {self.current_plan}, price {total_price}')

                elif(new_plan == 'Premium Plan'):
                    self.current_plan = 'Premium Plan'
                    total_price = 200000
                    print(f'Upgrade to {self.current_plan}, price {total_price}')

                else:
                    print('Your selected new plan is invalid')

            elif(self.current_plan == 'Standard Plan'):
                if(new_plan == 'Premium Plan'):
                    self.current_plan = 'Premium Plan'
                    total_price = 200000
                    print(f'Upgrade to {self.current_plan}, price {total_price}')
                
                else:
                    print('Your selected new plan is invalid!.')

            else:
                print("You're in highest tier, you can't downgrade!.")