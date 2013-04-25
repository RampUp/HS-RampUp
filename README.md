High School RampUp: The Docs
=========

Variables
---

```
x = "hi"
print x
```
Returns:
```
hi
```

Functions
---

```
def print_arg(a):
	print a
	return a

print_arg(x)
```
Returns:
```
hi
```

The input of the function is the arguement "a".
The "return" command returns the result of the function. (You want these.)

Lists
---

```
x = ["hi", "whatup", "bye"]
print x[0]
```
Returns:
```
hi
```

Lists (as with everything in code) started counting at 0. So you have words 0, 1, 2, and 3 if there are 4 words.

Conditionals
---

```
def findGoodTeams(s):
	if s == "Yankees":
		print "keep looking"
	if s == "Red Sox":
		print "found it"
findGoodTeams("Red Sox")
```
Returns:
```
found it
```

if s == "Yankees" and if s == "RedSox" are both if statements. If they are true, the computer looks inside the if statement for an action. If they are false, the computer moves on.


For loops
---
```
def findGoodTeams(teams):
	for team in teams:
		if team == "Yankees":
			print "keep looking"
		if team == "Red Sox":
			print "found it"

baseball_teams = ["Yankees", "Red Sox"]
findGoodTeams(baseball_teams)
```
Returns:
```
keep looking
found it
```

Adding to a list
---
```
baseball_teams = ["Yankees", "Red Sox"]
baseball_teams.append("Nats")
print baseball_teams
```
Returns:
```
("Yankees", "Red Sox", "Nats")
```

Popping an element out of a list
---
```
def findGoodTeams(teams):
	ct = 0
	for team in teams:
		if team == "Yankees":
			teams.pop(ct)
		ct = ct + 1
	return teams

baseball_teams = ["Yankees", "Red Sox"]
findGoodTeams(baseball_teams)
```
Returns:
```
("Red Sox", "Nats")
```