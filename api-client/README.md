### Comments

Please see `../api/README.md` for how to start the `flask` API (note appeared to be a dependency conflict with the suggest flask version and Jinja2 dependency - this is resolved when moving flask to a later version in `requirements.txt`).

Ensure you have a `api-client/.env` with `api_key=<YOUR_API_KEY>` set.

Ensure you have created and activated the virtual environment when in the `api-client` directory by using `source client_venv/bin/activate`.

`CampaignsAPI` is a Python class that can be used to extract data from the Campaigns API (see `../api`). It includes pagination and data format options (currently just `json` or `DataFrame`).

Calling a specific page can be done in the initialisation of the class `CampaignsAPI` that takes an optional parameter `page`. Pagination is achieved through the methods `Next()` and `Prev()` in addition to an `AppendNext()` method that appends the data of the following page. Please see `client.py` for more details.

Examples using the client can be found in `foo.py`.

If I had more time I would add further functionality such as `Last()` that would retrive the final page and add functionality to download all data of a given route (e.g. `campaigns.`) in addition to adding a `withMetadata()` method joining data sources.