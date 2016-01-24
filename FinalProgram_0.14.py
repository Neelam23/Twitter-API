import urllib2
import json
import oauth2
from Tkinter import *
import tkMessageBox
import tkFont
import pyglet

#Keys for authorizing user account and accessing it
CONSUMER_KEY = "5apF4IMmoot5NXjqFZtXcdYV2"
CONSUMER_SECRET = "UqoWBwxk8BH3SO3fsmw5ypktCQJ2FajJOY464KfFDWwPCYpTWY"
ACCESS_KEY = "3646310174-RVvCYmcd9cLOGBWRZFMz2VXjPjoESoG7e8hd5VS"
ACCESS_SECRET = "3MpXFkGsZDSky16MgriC5SoJ5OvydgbGEnjR2CxTuysmV"

    
consumer = oauth2.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
access_token = oauth2.Token(key=ACCESS_KEY, secret=ACCESS_SECRET)
client = oauth2.Client(consumer, access_token)

#Method to create GET call
def get_req(url, key, secret, http_method="GET", post_body="", http_headers=None):
    consumer = oauth2.Consumer(key='5apF4IMmoot5NXjqFZtXcdYV2', secret='UqoWBwxk8BH3SO3fsmw5ypktCQJ2FajJOY464KfFDWwPCYpTWY')
    token = oauth2.Token(key=key, secret=secret)
    client = oauth2.Client(consumer, token)
    resp, content = client.request( url, method=http_method, body=post_body, headers=http_headers )
    return resp,content

#Method to create PUT call
def put_req(url, key, secret, http_method="POST", post_body="", http_headers=None):
    consumer = oauth2.Consumer(key='5apF4IMmoot5NXjqFZtXcdYV2', secret='UqoWBwxk8BH3SO3fsmw5ypktCQJ2FajJOY464KfFDWwPCYpTWY')
    token = oauth2.Token(key=key, secret=secret)
    client = oauth2.Client(consumer, token)
    resp, contents = client.request( url, method=http_method, body=post_body, headers=http_headers )
    return resp,contents
###################################################################################################################################
#Dvora changes starts
def twitSearch():
	if not var1.get():
		tkMessageBox.showinfo("HotTwitt", "You can not perform this function with empty text box.")
	else:
		count1 = 10
		var1text=var1.get()
		var2text=var1text.replace(' ','%20')
		url2 = 'https://api.twitter.com/1.1/search/tweets.json?q='+var2text+'&result_type=mixed&lang=en&count=count1'
		response, data = client.request(url2,"GET")
		decoded = json.loads(data)
	 	string = ""
	 	for i in range(0,count1+1):
	  		# print decoded['statuses'][i]['text'].encode('utf8')
	  		string = string + "->" + decoded['statuses'][i]['text'].encode('utf8') + '\n\n'
	  	tkMessageBox.showinfo("HotTwitt", string)

###################################################################################################################################
def twitTrend():
	count1 = 10
	url2 = 'https://api.twitter.com/1.1/trends/place.json?id=2450022'
	response, data = client.request(url2,"GET")
	decoded = json.loads(data)
	string = ""
	for i in decoded:
		for trend in i["trends"]:
			string = string + " - %s" % trend["name"].encode('utf8') + '\n\n'
 			
        tkMessageBox.showinfo("HotTwitt", string)

##Dvora changes Ends
###################################################################################################################################
##Neelam Changes starts
def updateName():    
	if not var1.get():
		tkMessageBox.showinfo("HotTwitt", "You can not perform this function with empty text box. Please enter the valid name.")
	else:
		var1text=var1.get()
		# print var1text
		var2text=var1text.replace(' ','%20')
		# print var2text
		timeline_endpoint = 'https://api.twitter.com/1.1/account/update_profile.json?name='+var2text
		resp1, data = client.request(timeline_endpoint,"POST")

		if resp1['status'] == '200':
			decoded = json.loads(data)
			updated_name = decoded['name'].encode('utf8')
			tkMessageBox.showinfo("HotTwitt", "The name has been successfully updated to "+updated_name)
		else:
			tkMessageBox.showinfo("HotTwitt", "Please enter the valid name.")	

###################################################################################################################################
def getFollow():
	if not var1.get():
		tkMessageBox.showinfo("HotTwitt", "You can not perform this function with empty text box.")
	else:
		var1text=var1.get()
		resp1,followers = get_req( 'https://api.twitter.com/1.1/users/lookup.json?screen_name='+var1text, '3646310174-RVvCYmcd9cLOGBWRZFMz2VXjPjoESoG7e8hd5VS', '3MpXFkGsZDSky16MgriC5SoJ5OvydgbGEnjR2CxTuysmV' )
		if resp1['status'] == '200':
			decoded = json.loads(followers)
			follow_count = decoded[0]['followers_count']
			# print 'Total number of followers are '+str(follow_count)+'.'
			tkMessageBox.showinfo("HottTwitt", "Total number of followers for "+var1text+" are "+str(follow_count)+".")	
		else:
			tkMessageBox.showinfo("HotTwitt", "Please enter the valid user name.")					
##Neelam changes ends
###################################################################################################################################
##Manjeet changes start
def twitPost():
	if not var1.get():
		tkMessageBox.showinfo("HotTwitt", "You can not perform this function with empty text box.")
	else:
		var1text=var1.get()
		# print var1text
		# print len(var1text)
		if len(var1text) < 140:
			var2text=var1text.replace(' ','%20')
			# print var2text
			resp1,tweet_result = put_req( 'https://api.twitter.com/1.1/statuses/update.json?status='+var2text+'&display_coordinates=false', '3646310174-RVvCYmcd9cLOGBWRZFMz2VXjPjoESoG7e8hd5VS', '3MpXFkGsZDSky16MgriC5SoJ5OvydgbGEnjR2CxTuysmV' )
			# print resp1
			# print resp1['status']
			if resp1['status'] == '403':
				tkMessageBox.showinfo("HotTwitt", "Duplicate Status.")
			else:
				if resp1['status'] == '200':
					tkMessageBox.showinfo("HotTwitt", "Your status has been successfully updated.")
				else:
					tkMessageBox.showinfo("HotTwitt", "Something went wrong. Please try after some time.")
		else:
			tkMessageBox.showinfo("HotTwitt", "The text you have entered is more than 140 characters.")		

###################################################################################################################################
def followUser():
	if not var1.get():
		tkMessageBox.showinfo("HotTwitt", "You can not perform this function with empty text box.")
	else:
		var1text=var1.get()
		# print var1text
		resp1,result=put_req( 'https://api.twitter.com/1.1/friendships/create.json?screen_name='+var1text, '3646310174-RVvCYmcd9cLOGBWRZFMz2VXjPjoESoG7e8hd5VS', '3MpXFkGsZDSky16MgriC5SoJ5OvydgbGEnjR2CxTuysmV' )
		# print resp1
		# print result
		if resp1['status'] == '200':
			# print resp1['status']
			tkMessageBox.showinfo("HotTwitt", "You have successfully followed the user "+var1text+".")
		else:
			# print resp1['status']
			tkMessageBox.showinfo("HotTwitt", "Something went wrong. Please try again with correct user id.")
##Manjeet changes ends
###################################################################################################################################
##Ankit changes starts
def userTimeline():
	if not var1.get():
		tkMessageBox.showinfo("HotTwitt", "You can not perform this function with empty text box.")
	else:
		var1text=var1.get()
		count1 = 10
		string = ""
		resp1,user_timeline = get_req( 'https://api.twitter.com/1.1/statuses/user_timeline.json?count='+str(count1)+'&screen_name='+var1text, '3646310174-RVvCYmcd9cLOGBWRZFMz2VXjPjoESoG7e8hd5VS', '3MpXFkGsZDSky16MgriC5SoJ5OvydgbGEnjR2CxTuysmV' )
		# print user_timeline
		# print resp1
		if resp1['status'] == '200':
			# print resp1['status']
			decoded = json.loads(user_timeline)
			for i in range(0,count1):
				# print decoded[i]['text'].encode('utf8')
				# string = string + str(i+1) + '. ' +decoded['statuses'][i]['text'].encode('utf8') + '\n'
				string = string + str(i+1) + '. ' + decoded[i]['text'].encode('utf8') + '\n\n'	
		  	tkMessageBox.showinfo("HotTwitt", string)
		else:
			# print resp1['status']
			tkMessageBox.showinfo("HotTwitt", "Something went wrong. Please try again with correct user id.")


###################################################################################################################################
def unfollowUser():
	if not var1.get():
		tkMessageBox.showinfo("HotTwitt", "You can not perform this function with empty text box.")
	else:
		var1text=var1.get()
		# print var1text
		resp1,result=put_req( 'https://api.twitter.com/1.1/friendships/destroy.json?screen_name='+var1text, '3646310174-RVvCYmcd9cLOGBWRZFMz2VXjPjoESoG7e8hd5VS', '3MpXFkGsZDSky16MgriC5SoJ5OvydgbGEnjR2CxTuysmV' )
		# print resp1
		# tkMessageBox.showinfo("hotTwitt", "Total number of followers for "+var1text+"are "+follow_count+".")
		if resp1['status'] == '200':
			tkMessageBox.showinfo("HotTwitt", "You have successfully unfollowed the user "+var1text+".")
		else:
			tkMessageBox.showinfo("HotTwitt", "Something went wrong. Please try again with correct user id.")
##Ankit changes ends
###################################################################################################################################
def reveal():
	print "****Get text: ***"
	print twittext.get

def on_click(event):
	sound = pyglet.media.load('birds007.wav')
	sound.play()

###################################################################################################################################
## GUI interface Code: by Neelam,Ankit,Dvora,Manjeet
app = Tk()
app.title("HotTwitt Application") 
app.geometry("600x390")
var1=StringVar()


f=Frame(app,width="600",height="25",bg="#0087BD",highlightbackground="lightblue")
f.pack(fill='x',side="top")

f1=Frame(app,width="200",height="400",bg="#0087BD")
f1.pack(side="left",expand=YES)

f2=Frame(app,width="20",height="400",bg="#ccd6dd")
f2.pack(side ="left",fill='both', expand=YES)

f3=Frame(app,width="430",height="400",bg="#ccd6dd")
f3.pack(side ="left",fill='both', expand=YES)

customFont = tkFont.Font(family="Monotype Corsiva", slant='italic', size=22, weight='bold')
header = Label(f,text = "***HotTwitt***", font=customFont, fg='#FEFEFA',bg="#0087BD",justify="right")
header.pack(pady = 5, padx = 5)

sound = pyglet.media.load('birds007.wav')
sound.play()

instruction = Label(f3, bg="#ccd6dd",text = "Enter text: ",font=30)
instruction.grid(row = 200, column = 10)

textBox1 = Entry(f3,textvariable=var1,bg="grey",width=50)
textBox1.grid(row = 200, column = 20,pady=10)

b1 = Button(f1, text='    Trending    ', command = twitTrend,padx = 20)
b1.pack(pady = 8, padx = 8)

b2 = Button(f1, text='Search Tweets',command = twitSearch, activebackground="#55acee",padx = 20)
b2.pack(pady = 8, padx = 8)

b3 = Button(f1, text='   Post Tweet    ', command = twitPost,padx = 20)
b3.pack(pady = 8, padx = 8)

b4 = Button(f1, text='Update Name', command = updateName,padx = 20)
b4.pack(pady = 8, padx = 8)

b5 = Button(f1, text='Get Followers', command = getFollow,padx = 20)
b5.pack(pady = 8, padx = 8)

b6 = Button(f1, text=' Follow User  ', command = followUser,padx = 20)
b6.pack(pady = 8, padx = 8)

b7 = Button(f1, text='Unfollow User', command = unfollowUser,padx = 20)
b7.pack(pady = 8, padx = 8)

b8 = Button(f1, text='User Timeline', command = userTimeline,padx = 20)
b8.pack(pady = 8, padx = 8)

##Adding Images
image1=PhotoImage(file = 'bird3.gif')
image2=PhotoImage(file = 'bird2.gif')
img1 = Label(f2,image = image1,)
img1.grid(rowspan=1,row = 5, columnspan=50,column = 10)
img2 = Button(f3,image = image2)
img2.grid(rowspan=50,row = 50, columnspan=15,column = 15)
img2.bind('<Button-1>', on_click)

def reveal():
	print twittext.get



app.mainloop()
