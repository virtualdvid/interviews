 /*
 BACKGROUND:

 The following schema is a subset of a relational database of a grocery store
 chain. This chain sells many products of different product classes to its
 customers across its different stores. It also conducts many different
 promotion campaigns.

 The relationship between the four tables we want to analyze is depicted below:

        # sales                                # products
        +------------------+---------+         +---------------------+---------+
        | product_id       | INTEGER |>--------| product_id          | INTEGER |
        | store_id         | INTEGER |    +---<| product_class_id    | INTEGER |
        | customer_id      | INTEGER |    |    | brand_name          | VARCHAR |
   +---<| promotion_id     | INTEGER |    |    | product_name        | VARCHAR |
   |    | store_sales      | DECIMAL |    |    | is_low_fat_flg      | TINYINT |
   |    | store_cost       | DECIMAL |    |    | is_recyclable_flg   | TINYINT |
   |    | units_sold       | DECIMAL |    |    | gross_weight        | DECIMAL |
   |    | transaction_date | DATE    |    |    | net_weight          | DECIMAL |
   |    +------------------+---------+    |    +---------------------+---------+
   |                                      |
   |    # promotions                      |    # product_classes
   |    +------------------+---------+    |    +---------------------+---------+
   +----| promotion_id     | INTEGER |    +----| product_class_id    | INTEGER |
        | promotion_name   | VARCHAR |         | product_subcategory | VARCHAR |
        | media_type       | VARCHAR |         | product_category    | VARCHAR |
        | cost             | DECIMAL |         | product_department  | VARCHAR |
        | start_date       | DATE    |         | product_family      | VARCHAR |
        | end_date         | DATE    |         +---------------------+---------+
        +------------------+---------+
 */
 /*
 PROMPT:
 -- The VP of Sales feels that some product categories don't sell
 -- and can be completely removed from the inventory.
 -- As a first pass analysis, they want you to find what percentage
 -- of product categories have never been sold.

 EXPECTED OUTPUT:
 Note: Please use the column name(s) specified in the expected output in your solution.
 +-----------------------------------+
 | pct_product_categories_never_sold |
 +-----------------------------------+
 |               13.8888888888888889 |
 +-----------------------------------+

 -------------- PLEASE WRITE YOUR SQL SOLUTION BELOW THIS LINE ----------------
 */

select (sum(case when total_units_sold is null then 1.0 else 0.0 end) / count(*)) * 100.0 as pct_product_categories_never_sold
from (select pc.product_category, sum(s.units_sold) total_units_sold
from product_classes pc left join products p on pc.product_class_id = p.product_class_id
                        left join sales s on p.product_id = s.product_id
group by pc.product_category
order by total_units_sold desc) a
