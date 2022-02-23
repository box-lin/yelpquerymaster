import json

def cleanStr4SQL(s):
    return s.replace("'","`").replace("\n"," ")

def parseBusinessData():
    #read the JSON file
    # We assume that the Yelp data files are available in the current directory. If not, you should specify the path when you "open" the function. 
    with open('./data/yelp_business.JSON','r') as f:  
        outfile =  open('./output/business.txt', 'w')
        line = f.readline()
        count_line = 0
        #read each JSON abject and extract data
        while line:
            data = json.loads(line)
            outfile.write("{} - business info : '{}' ; '{}' ; '{}' ; '{}' ; '{}' ; '{}' ; {} ; {} ; {} ; {}\n".format(
                              str(count_line), # the line count
                              cleanStr4SQL(data['business_id']),
                              cleanStr4SQL(data["name"]),
                              cleanStr4SQL(data["address"]),
                              cleanStr4SQL(data["state"]),
                              cleanStr4SQL(data["city"]),
                              cleanStr4SQL(data["postal_code"]),
                              str(data["latitude"]),
                              str(data["longitude"]),
                              str(data["stars"]),
                              str(data["is_open"])) )

            #process business categories
            categories = data["categories"].split(', ')
            outfile.write("      categories: {}\n".format(str(categories)))

            
            # TO-DO : write your own code to process attributes
            # make sure to **recursively** parse all attributes at all nesting levels. You should not assume a particular nesting level. 
            # attributes: [('GoodForKids', 'True'), ('NoiseLevel', 'average'), ('RestaurantsDelivery', 'False'),....
            flatAttributes = parseAttributes(data["attributes"], [])
            outfile.write("      attributes: {}\n".format(str(flatAttributes))) 

            # TO-DO : write your own code to process hours data
            # hours: [('Monday', ['17:30', '21:30']), ('Wednesday', ['17:30', '21:30']), ('Thursday', ['17:30', '21:30']),....
            formatedHours = parseHours(data["hours"])
            outfile.write("      hours: {}\n".format(str(formatedHours))) 

            outfile.write('\n')

            line = f.readline()
            count_line +=1
    print("business", count_line)
    outfile.close()
    f.close()

"""[summary: recursively flatten the nested dictionary using tail recursion]
   [Return: list]
"""
def parseAttributes(dic, acc):
    for k,v in dic.items():
        if isinstance(v, dict):
            parseAttributes(v, acc)
        else:
            tup = (k, v)
            acc.append(tup)
    return acc

"""[summary: Reformat the hour dict to list in format: [('Monday', ['17:30', '21:30']), ('Wednesday', ['17:30', '21:30']),...]
   [Return: list]
"""
def parseHours(dic):
    res = []
    for k, v in dic.items():
        timelst = v.split('-')
        tup = (k, timelst)
        res.append(tup)
    return res

def parseUserData():
    with open('./data/yelp_user.JSON','r') as f:  
        outfile =  open('./output/user.txt', 'w')
        line = f.readline()
        count_line = 0
        while line:
            data = json.loads(line)
            outfile.write("{} - user info: '{}' ; '{}' ; '{}' ; '{}' ; '{}' ; '{}' ; {}\n".format(
                              str(count_line), # the line count
                              data['user_id'],
                              data["name"],
                              data["yelping_since"],
                              data['tipcount'],
                              data['fans'],
                              data['average_stars'],
                              (data['funny'], data['useful'], data['cool'])
            ))
            
            friendLst = [friend for friend in data["friends"]]
            outfile.write("      friends: {}\n".format(str(friendLst))) 
            outfile.write('\n')
            line = f.readline()
            count_line +=1
    print("user", count_line)
    outfile.close()
    f.close()

def parseCheckinData():
    with open('./data/yelp_checkin.JSON','r') as f:  
        outfile =  open('./output/checkin.txt', 'w')
        line = f.readline()
        count_line = 0
        while line:
            data = json.loads(line)
            outfile.write("{} - checkin info: '{}'; \n".format(
                              str(count_line), # the line count
                              data['business_id']
            ))
            
            outfile.write("    {}\n".format(parseDates(data["date"])))

            line = f.readline()
            count_line +=1
    print("checkin", count_line)
    outfile.close()
    f.close()

def parseDates(dateStr):
    dates = dateStr.split(",")
    res = []
    for date in dates:
        dayTime = date.split(" ")
        day = dayTime[0].split("-")
        day.append(dayTime[1])
        res.append(day)
    return str(res)

def parseTipData():
    with open('./data/yelp_tip.JSON','r') as f:  
        outfile =  open('./output/tip.txt', 'w')
        line = f.readline()
        count_line = 0
        while line:
            data = json.loads(line)
            outfile.write("{} - user info: '{}' ; '{}' ; '{}' ; '{}' ; '{}' \n".format(
                              str(count_line), # the line count
                              data['business_id'],
                              data["date"],
                              str(data["likes"]),
                              data['text'],
                              data['user_id']
            ))
            
            line = f.readline()
            count_line +=1
    print("tip", count_line)
    outfile.close()
    f.close()

if __name__ == "__main__":
    parseBusinessData()
    parseUserData()
    parseCheckinData()
    parseTipData()