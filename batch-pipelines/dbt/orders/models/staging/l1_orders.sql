with source as (

    select * from {{ source('raw', 'l0_orders') }}

),

typed as (

    select
        trim(invoice_no::text) as invoice_no,
        trim(stock_code::text) as stock_code,
        description,
        quantity,
        invoice_date,
        unit_price,
        customer_id,
        country
    from source

)

select
    invoice_no,
    stock_code,
    description,
    quantity,
    invoice_date,
    unit_price,
    customer_id,
    country,
    case
        when invoice_no like 'C%' then true
        else false
    end as is_cancelled,
    case
        when quantity < 0 then true 
        else false 
    end as is_return
from typed