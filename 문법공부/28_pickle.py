# pickle
import pickle

profile_file = open("profile.pickle","wb")
profile = {"이름" : "박명수","나이" : 30,"취미" : ["골프","축구","코딩"]}
pickle.dump(profile,profile_file)
profile_file = open("profile.pickle","rb")
profile = pickle.load(profile_file)
print(profile)
