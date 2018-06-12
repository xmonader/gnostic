// GENERATED FILE: DO NOT EDIT!

package pettst
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
# 


func (client *Client) ListPets(
limit int,
) (
response *ListPetsResponses,
err error,
 ) {
path := client.service + "/pets"
v := url.Values{}
if client.APIKey != "" {
  v.Set("key", client.APIKey)
}
if len(v) > 0 {
  path = path + "?" + v.Encode()
}
req, err := http.NewRequest("GET", path, nil)
if err != nil {return}
resp, err := client.client.Do(req)
if err != nil {return}
defer resp.Body.Close()
if resp.StatusCode != 200 {
	return nil, errors.New(resp.Status)
}
response = &ListPetsResponses{}
switch {
case resp.StatusCode == 200:
  body, err := ioutil.ReadAll(resp.Body)
  if err != nil {return nil, err}
  result := &Pets{}
  err = json.Unmarshal(body, result)
  if err != nil {return nil, err}
  response.OK = result
default:
  defer resp.Body.Close()
  body, err := ioutil.ReadAll(resp.Body)
  if err != nil {return nil, err}
  result := &Error{}
  err = json.Unmarshal(body, result)
  if err != nil {return nil, err}
  response.default = result
}
return
}
# 


func (client *Client) CreatePets(
) (
response *CreatePetsResponses,
err error,
 ) {
path := client.service + "/pets"
body := new(bytes.Buffer)
req, err := http.NewRequest("POST", path, body)
reqHeaders := make(http.Header)
reqHeaders.Set("Content-Type", "application/json")
req.Header = reqHeaders
if err != nil {return}
resp, err := client.client.Do(req)
if err != nil {return}
defer resp.Body.Close()
if resp.StatusCode != 200 {
	return nil, errors.New(resp.Status)
}
response = &CreatePetsResponses{}
switch {
default:
  defer resp.Body.Close()
  body, err := ioutil.ReadAll(resp.Body)
  if err != nil {return nil, err}
  result := &Error{}
  err = json.Unmarshal(body, result)
  if err != nil {return nil, err}
  response.default = result
}
return
}
# 


func (client *Client) ShowPetById(
petId str,
) (
response *ShowPetByIdResponses,
err error,
 ) {
path := client.service + "/pets/{petId}"
path = strings.Replace(path, "{petId}", fmt.Sprintf("%v", petId), 1)
req, err := http.NewRequest("GET", path, nil)
if err != nil {return}
resp, err := client.client.Do(req)
if err != nil {return}
defer resp.Body.Close()
if resp.StatusCode != 200 {
	return nil, errors.New(resp.Status)
}
response = &ShowPetByIdResponses{}
switch {
case resp.StatusCode == 200:
  body, err := ioutil.ReadAll(resp.Body)
  if err != nil {return nil, err}
  result := &Pets{}
  err = json.Unmarshal(body, result)
  if err != nil {return nil, err}
  response.OK = result
default:
  defer resp.Body.Close()
  body, err := ioutil.ReadAll(resp.Body)
  if err != nil {return nil, err}
  result := &Error{}
  err = json.Unmarshal(body, result)
  if err != nil {return nil, err}
  response.default = result
}
return
}
