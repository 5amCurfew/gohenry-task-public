{{ config(
    materialized = 'table',
    unlogged=True,
    indexes=[
        {'columns': ['created_at_date'], 'type': 'btree'},
        {'columns': ['country'], 'type': 'btree'},
        {'columns': ['id'], 'type': 'btree', 'unique': True},
    ]
)}}

SELECT
    campaign_id::VARCHAR(100) as id,
    country,
    created::TIMESTAMP as created_at,
    date_trunc('day', created)::DATE as created_at_date,
    modified::TIMESTAMP as updated_at,
    status
FROM
    {{ ref('raw_campaigns') }}
