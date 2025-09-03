# Amazon Sales Analysis – Summary Report

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
