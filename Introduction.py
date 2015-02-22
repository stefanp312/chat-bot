def helloWorld(input):
	input=input.lower()
	arr=input.split()
	key_counter=0

	for i in range (0,len(arr)):
		if arr[i]=="wat"or arr[i]=="what"or arr[i]=="name"or arr[i]=="name?" or arr[i]=="what's" or arr[i]=="wats"or arr[i]=="?"or arr[i]=="your"or arr[i]=="ur"or arr[i]=="whats":
			key_counter=key_counter+1
	if key_counter>2:
		#print "My name is Jonas!\nhttp://youtu.be/yk0_i8u_bgs"
		return "My name is Jonas!\nhttp://youtu.be/yk0_i8u_bgs"
	else:
		#print "Hello world"
		return "Hello world"


