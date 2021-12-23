import urllib.request as req
import bs4


# # regular season
# url = "https://pleagueofficial.com/schedule-regular-season"
# request = req.Request(url, headers = {
#     "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36"
# })
# with req.urlopen(request) as response:
#     data = response.read().decode("utf-8")
    

# root = bs4.BeautifulSoup(data, "html.parser")
# # print(root)

# # stadium / game number / date / day_of_weak / time 
# stadiums = root.find_all("h5", class_= "fs12 mb-0")
# game_num = root.find_all("h5", class_= "fs14 mb-2")
# date = root.find_all("h5", class_= "fs16 mt-2 mb-1")
# day_of_weak = root.find_all("h5", class_= "fs12 mb-2")
# time = root.find_all("h6", class_= "fs12")
# teams = root.find_all("h6", class_= "fs12 mb-2 PC_only") 
# scores = root.find_all("h6", class_ = "PC_only fs22")

# stadiums_arr = []
# game_num_arr = []
# date_arr = []
# day_of_weak_arr = []
# time_arr = []
# team_arr = []
# score_arr = []

# for stadium in stadiums:
#     stadiums_arr.append(stadium.string)
    
# for num in game_num:
#     game_num_arr.append(num.string)
    
# for d in date:
#     date_arr.append(d.string)
    
# for day in day_of_weak:
#     day_of_weak_arr.append(day.string)
    
# for t in time:
#     if t.string:
#         time_arr.append(t.string)
    
# for team in teams:
#     text = str(team.text)
#     n = 0
#     for i, char in enumerate(text):
#         if char == '\n':
#             n += 1
#             if n == 1:
#                 front = i + 1
#             elif n == 2:
#                 end = i - 1
#     mid = (front + end) // 2
#     text = text[:mid + 1] + text[end + 1:]
#     team_arr.append(text)

# for score in scores:
#     score_arr.append(score.string)
        
    
# j = 0
# for i in range(len(stadiums_arr)):
#     print(stadiums_arr[i], game_num_arr[i], date_arr[i], day_of_weak_arr[i], time_arr[i])
#     print(team_arr[j], score_arr[j])
#     print(team_arr[j + 1], score_arr[j + 1])
#     j += 2
#     print("\n")
    
    
    
# # preseason
url = "https://pleagueofficial.com/schedule-pre-season"
request = req.Request(url, headers = {
    "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36"
})
with req.urlopen(request) as response:
    data = response.read().decode("utf-8")
    

root = bs4.BeautifulSoup(data, "html.parser")
# print(root)

# stadium / game number / date / day_of_weak / time 
stadiums = root.find_all("h5", class_= "fs12 mb-0")
game_num = root.find_all("h5", class_= "fs14 mb-2")
date = root.find_all("h5", class_= "fs16 mt-2 mb-1")
day_of_weak = root.find_all("h5", class_= "fs12 mb-2")
time = root.find_all("h6", class_= "fs12")
teams = root.find_all("h6", class_= "fs12 mb-2 PC_only") 
scores = root.find_all("h6", class_ = "PC_only fs22")

stadiums_arr = []
game_num_arr = []
date_arr = []
day_of_weak_arr = []
time_arr = []
team_arr = []
score_arr = []

for stadium in stadiums:
    stadiums_arr.append(stadium.string)
    
for num in game_num:
    game_num_arr.append(num.string)
    
for d in date:
    date_arr.append(d.string)
    
for day in day_of_weak:
    day_of_weak_arr.append(day.string)
    
for t in time:
    if t.string:
        time_arr.append(t.string)
    
for team in teams:
    text = str(team.text)
    n = 0
    for i, char in enumerate(text):
        if char == '\n':
            n += 1
            if n == 1:
                front = i + 1
            elif n == 2:
                end = i - 1
    mid = (front + end) // 2
    text = text[:mid + 1] + text[end + 1:]
    team_arr.append(text)

for score in scores:
    score_arr.append(score.string)
        
    
j = 0
for i in range(len(stadiums_arr)):
    print(stadiums_arr[i], game_num_arr[i], date_arr[i], day_of_weak_arr[i], time_arr[i])
    print(team_arr[j], score_arr[j])
    print(team_arr[j + 1], score_arr[j + 1])
    j += 2
    print("\n")


    

        