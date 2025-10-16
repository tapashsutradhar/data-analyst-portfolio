# Amazon_Sale_Report
End-to-end analysis of Amazon sales data to uncover business insights and drive growth.

# Amazon Sales Analysis – Summary Report
This repository contains a complete end-to-end data analysis project on Amazon sales data.
The goal is to uncover actionable business insights by exploring sales performance, product trends, fulfillment efficiency, customer behavior, and geographical distribution.

## Objectives

- Sales Overview – Understand overall sales performance, trends, and seasonality.
- Product Analysis – Identify top categories, sizes, and best-selling products.
- Fulfillment Analysis – Investigate delivery methods and their effectiveness.
- Customer Segmentation – Segment customers using RFM (Recency, Frequency, Monetary) and buying patterns.
- Geographical Analysis – Explore sales distribution across states and cities.
- Business Insights – Provide data-driven recommendations to optimize strategies, inventory, and customer experience.

## Contents
- Amazon_Sales_Analysis.ipynb → Jupyter notebook with step-by-step analysis & visualizations
-  Amazon_Sales_Analysis.xlsx → Processed results (KPIs, product sales, fulfillment, RFM, cohorts, geography)
- Amazon_Sales_Insights.md → Executive insights & recommendations
Supporting scripts and charts

## Tech Stack
- Python (pandas, numpy, matplotlib, seaborn, scikit-learn)
- Jupyter Notebook for analysis & storytelling
- Excel / CSV exports for business reporting
- Visualization: charts, graphs, cohorts, RFM segmentation

## Key Outcomes
- Clear understanding of sales trends and top-performing products
- Customer segmentation for targeted marketing strategies
- Fulfillment performance insights to reduce delays & returns
- Geo-based insights for marketing and logistics optimization
- Actionable recommendations to grow revenue and enhance customer satisfaction

# Insights & Recommendations

## Key Insights
- Sales trend available from 2022-03-01 to 2022-06-01.
- Top categories: T-shirt, Shirt, Blazzer
- Top sizes: M, L, XL
- Leading fulfillment channel by revenue: Amazon
- Top state by sales: MAHARASHTRA
- Top city by sales: BENGALURU
- RFM segment mix (%): {'Loyal': 33.2, 'Potential Loyalist': 28.3, 'Need Attention': 20.5, 'Champions': 9.2, 'At Risk': 8.8}

## Recommendations
- Increase investment in top categories/sizes; test bundles to lift AOV.
- Balance inventory toward fast-moving sizes; reduce slow movers.
- Prioritize the best-performing fulfillment channel; fix late/cancel issues in weaker channels.
- Cultivate Champions/Loyal with VIP offers; win-back 'At Risk' with time-bound coupons.
- Focus geo marketing in top states/cities; align last-mile capacity.

## Overview KPIs
- **Total Sales**: 78590170.24999999
- **Total Units**: 116479
- **Date Range**: 2022-03-31 to 2022-06-29
- **Unique Customers**: 112887

## Sales Overview
- Monthly sales trend plotted in `monthly_sales_trend.png`.
- Check seasonality and growth or decline over the analysis period.

Top records preview:
| order_month         |           amount |
|:--------------------|-----------------:|
| 2022-03-01 00:00:00 | 101684           |
| 2022-04-01 00:00:00 |      2.88362e+07 |
| 2022-05-01 00:00:00 |      2.62265e+07 |
| 2022-06-01 00:00:00 |      2.34258e+07 |

## Product Analysis
- Top contributing categories identified (see `top_categories_sales.png`).
- Top 20 products by sales listed in the 'Top Products' sheet.
- Size-level contributions shown in `top_sizes_sales.png` (if available).

Top records preview:
| category   |           amount |
|:-----------|-----------------:|
| T-shirt    |      3.92068e+07 |
| Shirt      |      2.12978e+07 |
| Blazzer    |      1.12151e+07 |
| Trousers   |      5.34629e+06 |
| Perfume    | 789420           |
| Wallet     | 458408           |
| Socks      | 150758           |
| Shoes      | 124753           |
| Watch      |    915           |

## Fulfillment Analysis
- Sales split by fulfillment method (see `sales_by_fulfillment.png`).
- Status mix by fulfillment available in 'Fulfillment Status' sheet.

Top records preview:
| fulfilment   |      amount |
|:-------------|------------:|
| Amazon       | 5.43275e+07 |
| Merchant     | 2.42626e+07 |

## Customer Segmentation
- RFM segmentation performed (Champions, Loyal, Potential Loyalist, Need Attention, At Risk).
- Segment distribution chart saved as `rfm_segment_distribution.png`.

Top records preview:
|   recency |   amount |   frequency |   r_score |   f_score |   m_score |   rfm_score | segment   |
|----------:|---------:|------------:|----------:|----------:|----------:|------------:|:----------|
|        18 |  1174    |           1 |         5 |         5 |         5 |          15 | Champions |
|        19 |  2067    |           2 |         5 |         5 |         5 |          15 | Champions |
|         2 |  1744    |           2 |         5 |         5 |         5 |          15 | Champions |
|        10 |  1163    |           1 |         5 |         5 |         5 |          15 | Champions |
|        14 |  1409    |           2 |         5 |         5 |         5 |          15 | Champions |
|         6 |  2380.95 |           3 |         5 |         5 |         5 |          15 | Champions |
|        14 |   974    |           2 |         5 |         5 |         5 |          15 | Champions |
|         7 |  3910    |           4 |         5 |         5 |         5 |          15 | Champions |
|        17 |  1226    |           2 |         5 |         5 |         5 |          15 | Champions |
|        18 |  1056    |           2 |         5 |         5 |         5 |          15 | Champions |

## Geographical Analysis
- Top states and cities by sales shown in `top_states_sales.png` and `top_cities_sales.png`.
- Use these to target regional promotions and inventory allocation.

Top records preview:
| ship_state     |      amount |
|:---------------|------------:|
| MAHARASHTRA    | 1.33403e+07 |
| KARNATAKA      | 1.04807e+07 |
| TELANGANA      | 6.91502e+06 |
| UTTAR PRADESH  | 6.82395e+06 |
| TAMIL NADU     | 6.51918e+06 |
| DELHI          | 4.23274e+06 |
| KERALA         | 3.82356e+06 |
| WEST BENGAL    | 3.50721e+06 |
| ANDHRA PRADESH | 3.21786e+06 |
| HARYANA        | 2.88036e+06 |

## Recommendations 
- Double down on top categories and products with targeted ads and bundling.
- Balance stock for best-selling sizes; reduce slow-moving size inventory.
- Prioritize the most profitable fulfillment method and address bottlenecks in low-performing channels.
- Cultivate 'Champions' and 'Loyal' customers with VIP offers; design win-back campaigns for 'At Risk' customers.
- Allocate marketing budgets to top-performing states/cities; test local promotions where share is growing.
