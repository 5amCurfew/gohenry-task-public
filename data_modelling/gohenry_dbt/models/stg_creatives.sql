{{ config(
    materialized = 'table',
    unlogged=True,
    indexes=[
        {'columns': ['id'], 'type': 'btree', 'unique': True},
    ]
)}}

SELECT
    creative_id::VARCHAR(100) as id,
    call_to_action_type,
    title,
    video_id,
    image_id,
    "text",
    redirect_url
FROM
    {{ ref('raw_creatives') }}
