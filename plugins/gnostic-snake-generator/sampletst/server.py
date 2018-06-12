// GENERATED FILE: DO NOT EDIT!

package sampletst


import (
"github.com/gorilla/mux"
"net/http"
)
func intValue(s string) (v int64) {
	v, _ = strconv.ParseInt(s, 10, 64)
	return v
}

// This package-global variable holds the user-written Provider for API services.
// See the Provider interface for details.
var provider Provider

// These handlers serve API methods.

// Handler
// 
func HandleGetSample(w http.ResponseWriter, r *http.Request) {
  var err error
// instantiate the parameters structure
parameters := &GetSampleParameters{}
// get request fields in path and query parameters
vars := mux.Vars(r)
// name:"id" type:"string" position:PATH nativeType:"str" fieldName:"Id" parameterName:"id" serialize:true 
if value, ok := vars["id"]; ok {
	parameters.Id = value
}
// instantiate the responses structure
responses := &GetSampleResponses{}
// call the service provider
err = provider.GetSample(parameters, responses)
if err == nil {
if responses.OK != nil {
  // write the normal response
  encoder := json.NewEncoder(w)
  encoder.Encode(responses.OK)
  return
}
} else {
  w.WriteHeader(http.StatusInternalServerError)
  w.Write([]byte(err.Error() + "\n"))
  return
}
}

// Initialize the API service.
func Initialize(p Provider) {
  provider = p
  var router = mux.NewRouter()
router.HandleFunc("/sample/{id}", HandleGetSample).Methods("GET")
  http.Handle("/", router)
}

// Provide the API service over HTTP.
func ServeHTTP(address string) error {
  if provider == nil {
    return errors.New("Use sampletst.Initialize() to set a service provider.")
  }
  return http.ListenAndServe(address, nil)
}
