def main():
    ids = ["P101","P102","P103","P104"]
    names = ["Laptop","Mouse","Keyboard","Monitor"]
    prices = {"P101":50000,"P102":500,"P103":1500,"P104":12000}

    while True:
        print("\n1.Search  2.Update  3.Above1000  4.Average  5.Exit")
        c = int(input("Choice: "))
        if c==1:
            pid = input("ID: ")
            if pid in ids: print(pid,names[ids.index(pid)],"₹",prices[pid])
            else: print("Not found")
        elif c==2:
            pid = input("ID: "); prices[pid]=float(input("New Price: "))
        elif c==3:
            for i in ids:
                if prices[i]>1000: print(i,names[ids.index(i)],"₹",prices[i])
        elif c==4:
            print("Average Price: ₹",sum(prices.values())/len(prices))
        elif c==5: break

if __name__=="__main__": main()
