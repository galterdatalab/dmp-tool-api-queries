## DMP Tool Documentation
See the DMP Tool API documentation on this [California Digital Libraries / UC3 GitHub repo](https://github.com/CDLUC3/dmptool/wiki/API-Overview) for how to obtain the `client_id` and `client_secret`.

## Authorize yourself and get an access token¶
`curl -v https://dmptool.orgoauth/token -X POST -H "Accept: application/json" -d "grant_type=client_credentials&client_id=[CLIENT ID]&client_secret=[CLIENT SECRET]"`

### Example Output
`...{"access_token":"_abcdefg-1234567_","token_type":"Bearer","expires_in":7200,"scope":"public read_dmps","created_at":1714684830}`

## Examples

### Retrieve All Plans
`curl -v https://dmptool.org/api/v2/plans -H "Accept: application/json" -H "Authorization: Bearer _abcdefg-1234567_"`

### Retrieve One Plan
`curl -v https://dmptool.org/api/v2/plans/89799 -H "Accept: application/json" -H "Authorization: Bearer _abcdefg-1234567_"`

`curl -v https://dmptool.org/api/v2/plans/126595 -H "Accept: application/json" -H "Authorization: Bearer _abcdefg-1234567_"`

### Retrieve a List of Templates

`curl -v https://dmptool.org/api/v2/templates -H "Accept: application/json" -H "Authorization: Bearer _abcdefg-1234567_"`
