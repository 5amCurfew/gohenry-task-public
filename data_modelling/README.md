Like other directories in this project, ensure to activate the virtual environment by using `source venv/bin/activate` (this contains `dbt`).

### Run a Postgres db in Docker:

Build and run a postgres db in a Docker container by

`cd data_modelling`

`docker build -t gohenry-task .`

`docker run -d --name postgresdb -p 5432:5432 gohenry-task`

### Run dbt on this database:

```bash
cd gohenry_dbt
dbt deps --profiles-dir ./.dbt
dbt seed --profiles-dir ./.dbt
dbt run --profiles-dir ./.dbt
```

Generate documentation and schema using

`dbt docs generate --profiles-dir ./.dbt`

Full catalog can be found at `data_modelling/gohenry_dbt/target/catalog.json` in addition to in the `models/models.yml`.

Optimising for aggregation has been achieved with the selection of indexing what I would expect to be the most common aggregations per data source. This is achieved using dbt config blocks.

With further time I would have generated some example reporting models from these staging tables.