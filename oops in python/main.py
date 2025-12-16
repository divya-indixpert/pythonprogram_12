import json
import os

class UserApp:
    FILE_NAME="oops in python\\users.json"

    def __init__(self):
        if not os.path.exists(self.FILE_NAME):
            with open(self.FILE_NAME,"w") as f:
                json.dump([],f)

    def read_file(self):
        with open(self.FILE_NAME,"r") as f:
            return json.load(f)

    def write_file(self,data):
        with open(self.FILE_NAME,"w") as f:
            json.dump(data,f,indent=4)

    
    def create_user(self):
        data=self.read_file()
        user_id=int(input("Enter ID: "))
        name=input("Enter Name: ")
        email=input("Enter Email: ")

        data.append({
            "user_id": user_id,
            "name": name,
            "email": email
        })
        self.write_file(data)
        print("User added successfully")

    
    def view_users(self):
        data=self.read_file()
        if not data:
            print("No users found")
        else:
            for user in data:
                print(user)

    
    def update_user(self):
        data=self.read_file()
        user_id=int(input("Enter ID to update: "))

        for user in data:
            if user["user_id"]==user_id:
                user["name"]=input("Enter new Name: ")
                user["email"]=input("Enter new Email: ")
                self.write_file(data)
                print("User updated successfully")
                return

        print("User not found")

    
    def delete_user(self):
        data=self.read_file()
        user_id=int(input("Enter ID to delete: "))

        new_data=[u for u in data if u["user_id"] !=user_id]
        self.write_file(new_data)
        print("User deleted successfully")

    
    def menu(self):
        while True:
            print("\n=====USER MENU=====")
            print("1. Create User")
            print("2. View Users")
            print("3. Update User")
            print("4. Delete User")
            print("5. Exit")

            choice=input("Enter choice: ")

            if choice=="1":
                self.create_user()
            elif choice=="2":
                self.view_users()
            elif choice=="3":
                self.update_user()
            elif choice=="4":
                self.delete_user()
            elif choice=="5":
                print("Exiting program...")
                break
            else:
                print("Invalid choice")

if __name__=="__main__":
    app=UserApp()
    app.menu()
