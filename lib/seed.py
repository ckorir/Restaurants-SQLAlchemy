from faker import Faker
from sqlalchemy.orm import Session, sessionmaker
from models import Customer, Restaurant, Review, Base, engine

fake = Faker()

Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

restaurant1 = Restaurant(name="Kilimanjaro", price=33)
restaurant2 = Restaurant(name="Pizza Inn", price=27)
restaurant3 = Restaurant(name="Mayuras", price=41)
restaurant4 = Restaurant(name="Kukito", price=35)
restaurant5 = Restaurant(name="Debonairs", price=25)

# Generate fake customer names
customer_names = [fake.first_name() for _ in range(8)]

# Create customer instances with fake names
customers = [Customer(first_name=first_name, last_name=fake.last_name()) for first_name in customer_names]

review1 = Review(star_rating=5, customer=customers[0], restaurant=restaurant3)
review2 = Review(star_rating=5, customer=customers[1], restaurant=restaurant2)
review3 = Review(star_rating=4, customer=customers[2], restaurant=restaurant5)
review4 = Review(star_rating=3, customer=customers[1], restaurant=restaurant4)
review5 = Review(star_rating=5, customer=customers[4], restaurant=restaurant1)

# Add instances to the session
session.add_all([restaurant1, restaurant2, restaurant3, restaurant4, restaurant5] + customers + [review1, review2, review3, review4, review5])

# Commit the changes
session.commit()

print("\nFanciest Restaurant:", Restaurant.restaurant_fanciest().name)
print("\nAll Reviews for Restaurant One:")
for review in restaurant1.restaurant_all_reviews():
    print(review)

print("\nAll Reviews for Restaurant Two:")
for review in restaurant2.restaurant_all_reviews():
    print(review)

print("\nAll Reviews for Restaurant Three:")
for review in restaurant3.restaurant_all_reviews():
    print(review)

print("\nAll Reviews for Restaurant Four:")
for review in restaurant4.restaurant_all_reviews():
    print(review)

print("\nAll Reviews for Restaurant Five:")
for review in restaurant5.restaurant_all_reviews():
    print(review)

print(f"\nCustomer {customers[1].full_name()}'s Reviews:")
for review in customers[1].customer_reviews():
    print(review.review_full_review())

print(f"\nCustomer {customers[0].full_name()}'s Reviews:")
for review in customers[0].customer_reviews():
    print(review.review_full_review())

# Display all reviews before delete
print("\nAll Reviews before Delete:")
for review in restaurant1.restaurant_all_reviews():
    print(review)

# Delete the reviews
customers[0].customer_delete_reviews(restaurant1)

# Display all reviews after delete
print("\nAll Reviews after Delete:")
for review in restaurant1.restaurant_all_reviews():
    print(f"{review}\n")

# Close the session
session.close()
