BEGIN;
--
-- Create model Product
--
CREATE TABLE "app_product" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(100) NOT NULL, "selling_price" real NOT NULL, "discounted_price" real NOT NULL, "description" text NOT NULL, "composition" text NOT NULL, "prodapp" text NOT NULL, "category" varchar(2) NOT NULL, "product_image" varchar(100) NOT NULL);
COMMIT;
