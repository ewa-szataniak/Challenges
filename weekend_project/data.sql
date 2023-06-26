CREATE OR REPLACE FUNCTION insert_data() RETURNS VOID AS $MAIN$
BEGIN
  INSERT INTO "customer" ("customer_id", "first_name", "last_name", "email")
  VALUES 
      (1, 'John', 'Doe', 'johndoe@example.com'),
      (2, 'Jane', 'Smith', 'janesmith@example.com'),
      (3, 'Michael', 'Johnson', 'michaeljohnson@example.com');

  INSERT INTO "parts" (parts_id, part_name, price)
  VALUES 
      (1, 'Engine', 2500.00),
      (2, 'Brake Pads', 100.00),
      (3, 'Spark Plugs', 50.00);    

  INSERT INTO "sales_invoice" (s_invoice_id, customer_id, inventory_id, salesperson_id)
  VALUES 
      (13, 11, 125, 100),
      (24, 22, 236, 200),
      (36, 33, 357, 300);

  INSERT INTO "mechanic"(mechanic_id, first_name, last_name, price)
  VALUES 
      (1, 'Robert', 'Johnson', 25.00),
      (2, 'Sarah', 'Davis', 30.00),
      (3, 'Michael', 'Smith', 35.00);

  INSERT INTO "car" (car_id, color, year, make, model, service_history, customer_id)
  VALUES
      (1, 'Red', 2019, 'Toyota', 'Corolla', NULL, 1);

  INSERT INTO "salesperson" (salesperson_id, first_name, last_name, email, cars_sold)
  VALUES
      (1, 'Emily', 'Brown', 'emilybrown@example.com', 10),
      (2, 'David', 'Wilson', 'davidwilson@example.com', 8),
      (3, 'Jennifer', 'Taylor','jennifertaylor@example.com', 12);

  INSERT INTO "service_invoice" (mec_service_id, total_price, mechanic_id, parts_id, service_id, customer_id)
  VALUES
      (1, 150.00, 1, 1, 1, 1),
      (2, 80.00, 2, 2, 2, 2),
      (3, 120.00, 3, 3, 3, 3);
END;

$MAIN$
LANGUAGE plpgsql;

SELECT insert_data();