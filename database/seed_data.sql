USE WhatToEat;

-- Ingredients
INSERT INTO Ingredient (IngrdName) VALUES
  ('Tomato'),
  ('Lettuce'),
  ('Chicken'),
  ('Beef'),
  ('Rice'),
  ('Pasta'),
  ('Cheese'),
  ('Onion'),
  ('Pepper'),
  ('Cucumber'),
  ('Egg'),
  ('Flour'),
  ('Sugar'),
  ('Salt'),
  ('Olive Oil'),
  ('Mushroom'),
  ('Garlic'),
  ('Potato'),
  ('Carrot'),
  ('Milk');

-- Options (Meals)
INSERT INTO `Option` (MealName, EatOut, CuisineType, Mood) VALUES
  ('Caesar Salad', FALSE, 'Western', 'Light'),
  ('Beef Stir Fry', FALSE, 'Chinese', 'Savory'),
  ('Spaghetti Bolognese', FALSE, 'Italian', 'Comfort'),
  ('Chicken Tacos', TRUE, 'Mexican', 'Spicy'),
  ('Sushi Roll', TRUE, 'Japanese', 'Fresh'),
  ('Pancakes', FALSE, 'American', 'Sweet'),
  ('Curry Rice', FALSE, 'Indian', 'Spicy'),
  ('Burger', TRUE, 'American', 'Comfort'),
  ('Ramen', TRUE, 'Japanese', 'Warm'),
  ('Pho', TRUE, 'Vietnamese', 'Warm');

-- Restaurants
INSERT INTO Restaurant (RstrntName) VALUES
  ('Olive Garden'),
  ('Panda Express'),
  ('McDonald''s'),
  ('Taco Bell'),
  ('Sushi World'),
  ('Curry House'),
  ('Burger King'),
  ('Noodle Shop'),
  ('Pho 24'),
  ('Pancake House');

-- Menu (restaurant offerings)
INSERT INTO Menu (RstrntID, OptID, Price) VALUES
  (1, 3, 12.99),
  (1, 2, 10.50),
  (2, 2, 8.75),
  (2, 7, 9.25),
  (3, 8, 5.99),
  (3, 6, 4.50),
  (4, 4, 7.99),
  (4, 10, 8.50),
  (5, 5, 13.20),
  (5, 9, 11.00),
  (6, 7, 10.00),
  (7, 8, 6.49),
  (7, 6, 5.50),
  (8, 9, 9.99),
  (8, 1, 8.25),
  (9, 10, 10.75),
  (9, 5, 12.00),
  (10, 6, 6.00),
  (10, 1, 7.50);

-- Fridge (current stock)
INSERT INTO Fridge (IngredID, Qty) VALUES
  (1, 10),
  (2, 5),
  (3, 8),
  (4, 4),
  (5, 20),
  (6, 15),
  (7, 6),
  (8, 12),
  (9, 7),
  (10, 9),
  (11, 12),
  (12, 5),
  (13, 8),
  (14, 3),
  (15, 4),
  (16, 2),
  (17, 14),
  (18, 6),
  (19, 10),
  (20, 11);

-- Recipe (ingredients per meal)
INSERT INTO Recipe (OptID, IngrdID, Qty, Optional) VALUES
  (1, 1, 2, FALSE),
  (1, 2, 1, TRUE),
  (1, 7, 1, FALSE),
  (2, 4, 3, FALSE),
  (2, 8, 1, FALSE),
  (2, 9, 1, TRUE),
  (3, 6, 2, FALSE),
  (3, 4, 1, FALSE),
  (3, 13, 1, TRUE),
  (4, 3, 2, FALSE),
  (4, 8, 1, FALSE),
  (4, 10, 1, TRUE),
  (5, 11, 1, FALSE),
  (5, 17, 1, FALSE),
  (5, 18, 1, TRUE),
  (6, 12, 2, FALSE),
  (6, 11, 1, FALSE),
  (6, 13, 1, TRUE),
  (7, 5, 2, FALSE),
  (7, 16, 1, FALSE),
  (7, 14, 1, TRUE),
  (8, 7, 1, FALSE),
  (8, 6, 1, FALSE),
  (8, 1, 1, TRUE),
  (9, 18, 2, FALSE),
  (9, 20, 1, FALSE),
  (9, 17, 1, TRUE),
  (10, 5, 2, FALSE),
  (10, 17, 1, FALSE),
  (10, 2, 1, TRUE);
