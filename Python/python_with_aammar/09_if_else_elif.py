required_age_at_school = 4
hammad_age = 1

# question: can hammad go to school ?

if hammad_age==required_age_at_school:
    print("Congratulations! hammad can join the school.")
elif hammad_age > required_age_at_school:
    print("Hammad should join college or higher secondary school")
elif hammad_age <= 2:
    print("You should take care of Hammad, he is still a baby")

else:
    print("hammad can not go to school")