# Register Dependencies
import time

# Program Start

def displayVehicles():
 print("The AutoCountry sales manager has authorized the purchase and selling of the following vehicles: ")
 file = open("availablevehicles.txt", "r")
 fileContents = file.read()
 print(fileContents)
 print("Returning to the menu in 5 seconds...")
 time.sleep(1)
 print("Returning to the menu in 4 seconds...")
 time.sleep(1)
 print("Returning to the menu in 3 seconds...")
 time.sleep(1)
 print("Returning to the menu in 2 seconds...")
 time.sleep(1)
 print("Returning to the menu in 1 seconds...")
 time.sleep(1)
 print("Returning to the menu now...")
 time.sleep(1)
 menu()

def menu():
 print("************************************")
 print("  AutoCountry Vehicle Finder v0.1")
 print("************************************")
 print("Please select one of the following numbers from the menu below:")

 print("1: PRINT all Authorized Vehicles")
 print("2: Exit")
 menuSelection = int(input("Your Selection: "))
 
 if menuSelection == int("1"):
  displayVehicles()

 if menuSelection == int("2"):
    print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
    exit()
menu()

# Program Complete. 
