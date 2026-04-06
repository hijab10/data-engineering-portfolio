with source as (

    select *
    from  {{ ref('l1_orders') }}

),

filtered as (

    select
        invoice_date::date as order_date,
        invoice_no,
        quantity,
        unit_price,
        is_cancellation,
        is_return
    from source
    where invoice_no is not null
      and unit_price is not null
      and not is_cancellation
      and not is_return

),

aggregated as (

    select
        order_date,
        count(distinct invoice_no) as total_orders,
        sum(quantity) as total_items_sold,
        sum(quantity * unit_price) as gross_revenue
    from filtered
    group by order_date

)

select *
from aggregated
order by order_date