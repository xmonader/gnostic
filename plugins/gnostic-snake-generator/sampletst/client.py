// GENERATED FILE: DO NOT EDIT!

package sampletst
// Client represents an API client.
type Client struct {
  service string
  APIKey string
  client *http.Client
}
// NewClient creates an API client.
func NewClient(service string, c *http.Client) *Client {
	client := &Client{}
	client.service = service
  if c != nil {
    client.client = c
  } else {
    client.client = http.DefaultClient
  }
	return client
}
// 
func (client *Client) GetSample(
id str,
) (
response *GetSampleResponses,
err error,
 ) {
path := client.service + "/sample/{id}"
path = strings.Replace(path, "{id}", fmt.Sprintf("%v", id), 1)
req, err := http.NewRequest("GET", path, nil)
if err != nil {return}
resp, err := client.client.Do(req)
if err != nil {return}
defer resp.Body.Close()
if resp.StatusCode != 200 {
	return nil, errors.New(resp.Status)
}
response = &GetSampleResponses{}
switch {
case resp.StatusCode == 200:
  body, err := ioutil.ReadAll(resp.Body)
  if err != nil {return nil, err}
  result := &Sample{}
  err = json.Unmarshal(body, result)
  if err != nil {return nil, err}
  response.OK = result
case resp.StatusCode == 401:
  body, err := ioutil.ReadAll(resp.Body)
  if err != nil {return nil, err}
  result := &APIError{}
  err = json.Unmarshal(body, result)
  if err != nil {return nil, err}
  response.Code401 = result
case resp.StatusCode == 404:
  body, err := ioutil.ReadAll(resp.Body)
  if err != nil {return nil, err}
  result := &APIError{}
  err = json.Unmarshal(body, result)
  if err != nil {return nil, err}
  response.Code404 = result
default:
  break
}
return
}
