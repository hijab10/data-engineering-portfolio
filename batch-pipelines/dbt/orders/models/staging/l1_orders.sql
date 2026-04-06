with source as (

    select *
    from {{ source('raw', 'l0_orders') }}

),

cleaned as (

    select
        trim(invoice_no) as invoice_no,
        trim(stock_code) as stock_code,
        trim(description) as description,
        quantity,
        invoice_date,
        unit_price,
        customer_id,
        trim(country) as country,
        case when invoice_no like 'C%' then true else false end as is_cancellation,
        case when quantity < 0 then true else false end as is_return
    from source

)

select *
from cleaned