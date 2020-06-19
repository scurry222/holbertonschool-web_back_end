-- Create a trigger for the items table in the holberton database
-- Decrease the quantity of an item when a new order is inserted
CREATE TRIGGER trigger_name BEFORE INSERT
ON orders FOR EACH ROW
UPDATE items
SET quantity = quantity - number
WHERE name = item_name
