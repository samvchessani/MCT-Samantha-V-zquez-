#Characters
#nombremc: variable of the principal character, the player
#Mike, the guy of the pills
#Joseph, the man that gave you the card with the direction
#Teo, the bad one, that created the zombie world
#Max, your friend

#*cuando pongo muchos "#" es cuando acaba el if en especifico y quiero que los demás prints se incluyan en ambos ifs

#STORY:
#nombremc, is going to the school in bus, a weird man give him a card with a direction, the traffic was horrible, so he get down of the bus
#he decide to get down of the bus, went by the forest, found a cabain,
#meet Mike, a man that knows about the pills, nombremc ask about the pills, 
#Mike shh at nombremc, bc is the probability of someon hearing, Mike give nombremc a direction to go the next day
#DAY 2
#nombremc lied to his friend, after school he go to the direction, so both look for the pill plant
#Mike take it, ask to nombremc to watch him, nombremc take a pill,
#breaking mike ´s orders
#now, you both are in the zombie reality, but is like a videogame, you look for mike, but he found you first, you start to run, 
#mike tells you that you are not going to survive without him, you ask why, he say bc there are bad zombies
#is literally a real survival videogame
#mike tell you that this is not a game, it is real, so your levels are low, and you go to mike´s house, sleep
#DAY 3
#you ate a homemade fish, and explore the place
#and mike is not waking up, so they need to destroy the game
#they go to look for the main flower, that if you destroy it the game is over, but you need to get a liquid to take, to get back, to the normal reality


while True:
#first the introduction
 print("hello player")
 print("in this game. you are a boy.")
 nombremc=input("chose the name of the main character : ")
  #here the player choose the name
 print("okey then, welcome",nombremc)h
 print("you are already late for school,")
 input()
 print("so you decide to do something to get earlier, you could:")
#the variable for the name is called "nombremc"
  
#here I give the first decition to chose
 print(" a) you take the bus")
 print(" b) you go with your bike")
 getfast=input("what do you do? ")
  
#if one:getfast
 if(getfast=="a"):
  print(" you take the bus, there is just one seat to sit, and you have a freaky man by your side")
   #continue the story
 print(" he is eating his chips, and he offers you one, you say yes")
 input()
 print("but instead he gives you a card with a direction and a number ")
 print("you asked him what was that but he already is down of the bus")
  
 if(getfast=="b"):
  print("oh, come on! who in the world is taking the bike to go to school, wrong choice") 
  print("lets say that you choose the option to go by bus")
  input()
  print(" he is eating his chips, and he offers you one, you say yes")
  input()
  print("but instead he gives you a card with a direction and a number ")
  print("you asked him what was that but he already is down of the bus")
##############################
 print("the bus is being so slow because of the traffic, you could:")
 input()
 print("a) take the way that pass by the forest")
 print("b) dont care and go by the bus")
 print("ps: if you want to follow the story go by the forest")
 whatdo=input("what you are you going to do?")
  
#if two:whatdo
 if(whatdo=="a"):
  print("you take the forest, it was a rainy day so you are in the middle of a forest full of moho")
#############################
   
 if(whatdo=="b"):
  print("bad choice, ", nombremc, " you were supposed to go by the forest, because you were going to find something")
  input()
  print("but lets say that you choose to take the forest, ")

 print("you have been walking a lot and you already get lost,") 
 print("it was a rainy day so you are in the middle of a forest full of moho, ")
 input()
 print("you were walking and thinking what is the card that and you decided to follow the direction because it was in the forest")
 input()
 print("far away, you see an old building, you get closer and is an old cabain, ")
 input()
 print("you dont know what to do but you just have two options since it started to rain")
 input()

 print("you could:")
 print("a)Get inside the cabain.")      
 print("b)Still walking until you found another place to stay")
 c=input("What are you doing?                                PS: if you want to continue chose a")
#if three: c
 if(c=="a"):
  print("you choose to get inside the cabain,")
  input()
  print("you dont saw anyone in there") 
  print("so you just sit in the coach")
  print("you are so calm in there, but the rain have not stop")
  print("suddenly, you hear noises coming from the front door")
  input()
  print("like if someone is trying to open the door")

 if(c=="b"):
  print("You decided to keep walking until you find another place to stay")
  print("You walk a little more,")
  input()
  print("But started to rain again, but now was a storm")
  print("you choose to get inside the cabain again,")
  input()
  print("you dont saw anyone in there") 
  print("so you just sit in the coach")
  input()
  print("you are so calm in there, but the rain have not stop")
  print("suddenly, you hear noises coming from the front door")
  input()
  print("like if someone is trying to open the door")
 ################################
 print("you could: ")
 input()
 print("a) Hide in a room")
 print("b) Stay there and face the situation and whoever he/she is")
 h=("What are you going to do")
   
#if four: a
 if(h=="a"):
  print("You decide to hide in a room")
  print("There are two doors")
  input()
  print("It seems that the big one is of the room")
  print("And the little one of the bathroom")
  input()
  print("You enter to the big one")
  print("You stop hearing noises, and you go out ")
  print("You see someone in the kitchen and he sees you")
  input()
  print("Man 1: Ah! Who are you, and what are you doing in my house?!??")
  print("You, hi, my name is ", nombremc)

 if(h=="b"):
  print("You see someone in the kitchen and he sees you") 
  input()
  print("Man 1: Ah! Who are you, and what are you doing in my house?!??")
  print("You, hi, my name is ", nombremc)
###################################
 input()
 print("Man 1: And you are here because...?")
 input()
 print("a) Tell him more about you")
 print("b) Start to ask about him")
  
 #if five: s
 s=("Action?: ")

 if(s=="a"):
  print("Tell him more about you:")
  print("You: As I was saying, I'm here because today I was on the school bus,")
  input()
  print("and someone gave me a card with a name and this direction, ")
  print("And I wanted to know more about it")
############################### 
 print("Man 1: Sorry I can't talk about it now, I need you to leave")
 print("The man sayed that, but he was writing something in a little paper")
 input()
 print("He made that sign of shh by putting his finger over his mouth,")
 print("He whisper to you;")
 print("Man 1: I'm Mike, do what this card say")
 input()
 print("You went out of the cabain")
 print("To go to your house, because it was already late")
 input()
 print("In your thoughts you were thinking:")
 print("Should I go?")
 print("What if it is dangerous?")
 print("Tired of thinking you just fell asleep")
 input()
#####################
  #### DAY 2 #####
 print("*NEXT DAY*")
 print("You: I think I'm going")
 print("Of course first you need to go to the school")
 print("Because yesterday you didnt went")
 print("Your friend, Max: Why didnt you came yesterday?")
 input()
 print("You dont know if ")
 print("a)Lie to him")
 print("b)Tell him the truth")
            
#if six: l
 l=input("So, what are you going to do?")

 if(l=="a"):
  print("You choose to lie to him;")
   
 if(l=="b"):
  print("You are telling him the truth;")
  print("You: See, I was in the bus yesterday,")
  print("but someone gave me a card with a direction")
  input()
  print("I stuck in the forest and I found a cabain")
  print("*You finish to told him the story*")
  input()
  print("Now, you have a friend that thinks that you are crazy")
  print("He tell everything to the teachers,")
  input()
  print("and they tell that to your parents")
  print("They send you to a phsycology")
  print("and you never know about what was going on with Mike")
  input()
  print("As you can see, that option didnt work, but lets give it a try with choosing to lie to him,") 
  print("because your intention of telling the truth was nice, and loyal")
  input()
  print("Now, lets say you choose to lie to him,")
   
 print("You: I was feeling kinda sick, so I decided to lay in bed, but now Im better")
 print("Max: Oh, ok")
 input()
 print("He actually believed that, great")
 input()
 print("School is over, you are in your way to the direction that Mike´s card say")
 input()
 print("You arrived and Mike was already there")
 print("Mike: Finally, you are here, I thought you were not coming")
 input()
 print("You: Sorry, school")
 print("Mike: Ok,")
 print("Mike: today, we are going to the plant for get pills")
 input()
 print("You: Are we going to try them?")
 print("Mike: We are not, you don't ")
 input()
 print("You: But why not?")
 print("Mike: You still a kid")
 input()
 print("You both started a conversation of you being or not a kid")
 input()
 print("Mike: Ok, this are the pills,")
 print(" I will take one but, I need you to see how I react,")
 print("also, you are going to count the time")
 input()
 print("If i spend more than 2 hrs I will need you to give me this")
 print("*Mike extend you a syringe with a green liquid*")
 print("Mike took the pill and he was like if he was sleeping")
 input()
 print("You were there like 30 minutes")
 print("But in your head was that idea of taking a pill")
 input()
 print("So, you could")
 print("a) Take the pill")
 print("b) Stay until Mike wakes up")
 print("Extra help: This is the part where the action begins,")
 input()
 print("so, if you want to continue, choose option a...")
#if seven: t
 t=input("???:")

 if(t=="a"):
  print("Great, you are taking a pill")
  print("Without Mike's supervision ")
  print("Risky, but you want to know what is this new world thing about")
  input()

 if(t=="b"):
  print("This choose talks good about you", nombremc)
  print("You are a loyal person")
  print("because you decibe to stay until Mike wakes up")
  input()
  print("But...")
  print("in this game we kinda need you to take more risky decisions ")
  input()
  print("So let's say that you choose to take the pill")
  print("Because you have the curiosity to look further this world")
  input()
  
 print("There's the pill in the table")
 print("You see it to easy to do it")
 input()
 print("Your last thought before entering to that world was: ")
 print("*Am I doing the right thing?*")
 print("*What if Mike doesn't wake up*")
 input()
 print("Suddenly, you start to see black")

#Now you are in the zombie world 
 print("And then, you see that you are in a hospital, laying down ")
 input()
 print("You: Where am I?")
 print("Computer voice: Hi player, welcome to zombie reality")
 input()
 print("Computer voice: Your first mission is to look for a partner that will go with you on your next missions")
 input()
 print("Computer voice: Before that, here is your status-")
 print("Health: 100%")
 print("Food: 70%")
 print("Energy: 95%")
 input()
 print("You see more players,") 
 print("so you decide to ask for Mike")
 print("but you remember he mentioned something about a building where the leader is")
 input()
 print("so, you look in the map that was there")
 print("and you find a big name")
 print("PRINCIPAL BUILDING")
 input()
 print("You were in the way to get in there")
 print("But suddenly you start to hear that someone is yelling at you")
 input()
 print("Unknown voice: ", nombremc, "why on Earth are you here?!!")
 print("You start to recognize that voice, it's Mike!")
 print("But bad news")
 input()
 print("He sounds a little bit angry")
 print("Your instinct is to start running")
 print("Mike: Stop! You are not going to survive by your own")
 input()
 print("So?")
 print("a) Stop running")
 print("b) Still running")
 print("Consider that you don't know anything about this reality")
 print("And the man that is telling you that you are going to die if you don't go with him, have been there a few times")
 print("Literally, go with him or die")

 #if eight: r
 r=input("???:")

 if(r=="a"):
  print("Great decision, you stop running")
  print("But now, you will take Mike´s TED talk")

 if(r=="b"):
  print("I literally just told you to choose the option a")
  print("So this was a bad decision")
  print("Please, every time I give you a tip follow it")
  input()
  print("Now, let´s say you decide to stop running")
  print("But now, you will take Mike´s TED talk")
   #########################

 print("Mike: What were you thinking?")
 print("Mike: First of all, you took a drug, you are too young for that")
 print("Mike: Second, you risk yourself")
 print("Mike: Also me, what if I can't wake up")
 input()
 print("You: There is nothing to be worry about")
 print("Mike: You can not be here, and not alone")
 print("Mike: What if someone hurts you")
 print("You: How can it be?")
 print("You: Everything here, seems calm")
 print("Mike: It is not, there are zombies")
 print("Mike: Real zombies")
 input()
 print("You: But this is like a dream, if they hurt me, I just wake up")
 print("Mike: Come here, I need to tell you something")
 print("*You both sit in a big rock that was there*")
 input()
 print("Mike: Look, ", nombremc, "this is not a game")
 print("Mike: You are in a kind of other reality")
 print("Mike: If something happens here, when you wake up, it is going to be in our normal reality")
 input()
 print("After that talk")
 print("You both go in direction to the castle ")
 print("In order to see who is in charge of this pill stuff")
 input()
 print("Suddenly, a computer man appears")
 print("Computer voice: This is your actual status, ", nombremc)
 print("Health: 95%")
 print("Food: 40%")
 print("Energy: 55%")
 input()
 print("You: Ok, thanks")
 print("You: Mike, why did the computer didn't told you your status?")
 print("Mike: I don't know")
 print("Mike: Maybe a machine error")
 print("*He said that nervously and you noticed it*")
 input()
 print("Mike: So, food up to 40%, you need to eat")
 print("You: But I'm not hungry")
 print("Mike: Because is a videogame, you don't feel it")
 print("You found a bush with cranberries")
 input()
 print("Mike: Eat this")
 print("Mike: Also, your energy is low")
 print("Mike: And is night, so you need to sleep")
 input()
 print("You: Yeah, but where, anywhere?")
 print("Mike: No, follow me...")
 print("You arrive to a cave that look like a little house ")
 print("And you stayed there, until the next day")
 ###########DAY 03##############
 input()
 print("###DAY 3###")
 print("Mike waked you up,")
 print("Mike: Morning sleep beauty")
 print("You saw a recently extinguished campfire and a plate with a fish already cooked")
 input()
 print("Mike: Eat that, I need to see something, stay here")
 print("You started eating and it was actually sorprising the good flavor that it had")
 print("You finish the food, and you want to go out, but Mike told you not to so,")
 input()
 print("a) Go out to explore")
 print("b) Explore inside the cave")

 #if nine: e
 e=input("???: ")
 

#STORY IDEA: Mike can not get out of the game so nombremc needs to end the game, at the end, you never knew what was the zombie world really about