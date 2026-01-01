num=[1,2,3,4,5,6,7,8,9]

odd=[count for count in num if count%2!=0]
print(odd)

# i wanted to do something using list comprehension

less=[count**2 for count in num if count<=5]
print(less)

print([x ** 2 if x % 2 == 0 else x for x in num])
results = [{
    "name": "sarvin",
    "score": 10
}, {
    "name": "ali",
    "score": 20
}, {
    "name": "reza",
    "score": 5
}, {
    "name": "sina",
    "score": 15
}
]
print([x for x in results if x["score"]>10])
# in this section we are writing a list comprehension that works like filter
# we first get the x to loop over each item in results and then checking if the score is over 10

print([{"name" : x["name"], "passed" : x["score"] >= 10} for x in results])
# here we wrote a list comprehension like map 
#we said the key is "name" and then assign the x["name"] to it 
# then we created another dict and the def the key="passed" and the value x["score"] and then checking that is it over or eq to 10 or no 
# then loop x through resulst

