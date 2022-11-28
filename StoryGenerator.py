import random

when = ['A few years ago', 'Yesterday', 'Last night', 'A long time ago', 'On 20th Jan', 'Last week']
who = ['a rabbit', 'an elephant', 'a mouse', 'a turtle', 'a cat', 'a dog', 'a lion', 'a monkey', 'a giraffe']
name = ['Ali', 'Miriam', 'daniel', 'Hoouk', 'Starwalker', 'Mohammad', 'Sara', 'Fatima', 'Zainab', 'Kareem', 'Jack', 'Jill']
residence = ['Barcelona', 'India', 'Germany', 'Venice', 'England', 'Scotland', 'Brazil', 'Pakistan', 'Italy', 'France', 'Sweden', 'Norway', 'Iceland', 'South Africa', 'China', 'Japan', 'Australia']
went = ['cinema', 'university', 'seminar', 'school', 'concert', 'party', 'club', 'restaurant', 'pub', 'disco', 'zoo']
happened = ['made a lot of friends', 'Eats a burger', 'found a secret key', "didn't find his friend", 'solved a mistery', 'wrote a book', 'made a lot of money', 'found a secret door']
print(random.choice(when) + ', ' + random.choice(who) + ' that lived in ' + random.choice(residence) + ', went to the ' + random.choice(went) + ' and ' + random.choice(happened))
