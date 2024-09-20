# დაწერეთ პროგრამა ონლაინ ბილეთების გაყიდვის ვებ 
# გვერდისთვის. შექმენით მომხმარებლების სია (10-15 პერსონა) 
# უნდა მოახდინოთ რიგის მენეჯმენტი ვებსაიტზე, ერთდროულად 
# 5 ადამიანს უნდა შეეძლოს ყიდვის სესიაში შესვლა(Semaphore)
# დაბეჭდეთ რომ მომხმარებელი ცდილობს სესიაში შესვლას და თუ
# შევიდა სესიაში დაბეჭდეთ რომ დაიკავა ადგილი კონკრეტულმა
# მომხმარებელმა. მომხმარებელი რომელიც შესულია სესიაში 
# ბილეთს იყიდის 5 წამში (sleep) და გაათავისუფლებს ადგილს 
# შემდეგი მომხმარებლისთვის. პროგრამა დაასრულებს მუშაობას 
# როდესაც ყველა მომხმარებელი იყიდის ბილეთს. 
import time
import threading

semphore = threading.Semaphore(5)

customers = ["customer1", "Customer 2", "Customer 3", "Customer 4", "Customer 5",
             "Customer 6", "Customer 7", "Customer 8", "Customer 9", "Customer 10",
             "Customer 11", "Customer 12", "Customer 13", "Customer 14", "Customer 15"]

def buy_tickets(customer):
    print(f"{customer} is trying to buy tickets")

    with semphore:
        print(f"{customer} is waiting for the tickets")
        time.sleep(5)
        print(f"{customer} has bought tickets")

def ticket_sales():
    threads = []

    for customer in customers:
        thread = threading.Thread(target=buy_tickets, args=(customer,))
        threads.append(thread)
        thread.start()

    for thread  in threads:
        thread.join()
        print("all customers have bought tickets")

if __name__ == "__main__":
    ticket_sales()
    
        



    