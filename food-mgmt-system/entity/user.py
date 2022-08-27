class user:
    def __init__(self,user_id,user_name,user_mobile,user_email,user_address,user_password,user_profile):
        self.user_id =user_id
        self.user_name = user_name
        self.user_mobile = user_mobile
        self.user_email = user_email
        self.user_address =user_address
        self.user_password = user_password
        self.user_profile = user_profile

    def __str__(self):
        return f"USER ID : {self.user_id} \nUSER NAME : {self.user_name} \nUSER MOBILE : {self.user_mobile} \nUSER EMAIL : {self.user_email} \nUSER ADDRESS : {self.user_address} \nUSER PASSWORD : {self.user_password} \nUSER PROFILE : {self.user_profile}"

    def set_user_id(self,user_id):
        self.user_id = user_id
    
    def get_user_id(self,user_id):
        self.user_id = user_id

    def set_user_name (self,user_name):
        self.user_name = user_name
    
    def get_user_name(self,user_name):
        self.user_name = user_name

    def set_user_mobile (self,user_mobile):
        self.user_mobile = user_mobile
    
    def get_user_mobile(self,user_mobile):
        self.user_mobile = user_mobile
 
    def set_user_email (self,user_email):
        self.user_email = user_email
    
    def get_user_email(self,user_email):
        self.user_email = user_email
   
    def set_user_address (self,user_address):
        self.user_address = user_address
    
    def get_user_address(self,user_address):
        self.user_address = user_address
   
    def set_user_password (self,user_password):
        self.user_password = user_password
    
    def get_user_password(self,user_password):
        self.user_password = user_password

    def set_user_profile (self,user_profile):
        self.user_profile = user_profile
    
    def get_user_profile(self,user_profile):
        self.user_profile = user_profile

    
