import pywhatkit as kit # import pywhatkit module
import pyautogui as pg # Function to send WhatsApp message

phone_number = input("Enter phone number: ")
message = input("Enter your message: ")

# Function to send WhatsApp message
def send_whatsapp_message(phone_number, message):
    try:
        kit.sendwhatmsg_instantly(phone_number, message, 15, True,4) # send message to given number
        #Phone number, message, wait time, tab close, close time
        pg.press('enter') # press enter to send message
        print("Message sent successfully")
       
    except Exception as e:
        print("An error occurred", str(e))

if __name__ == "__main__":
    send_whatsapp_message(phone_number, message)




