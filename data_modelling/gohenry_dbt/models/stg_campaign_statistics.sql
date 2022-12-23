{{ config(
    materialized = 'table',
    unlogged=True,
    indexes=[
        {'columns': ['start'], 'type': 'btree'},
        {'columns': ['campaign_id', 'creative_id', 'start'], 'type': 'btree', 'unique': True},
    ]
)}}

SELECT
    campaign_id::VARCHAR(100),
    creative_id::VARCHAR(100),
    "start"::DATE,
    "end"::DATE,
    impressions::INTEGER,
    clicks::INTEGER,
    conversions::INTEGER,
    cost,
    currency,
    device
FROM
    {{ ref('raw_campaign_statistics') }}
