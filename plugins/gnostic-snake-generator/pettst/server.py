// GENERATED FILE: DO NOT EDIT!

package pettst


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
# 


func HandleListPets(w http.ResponseWriter, r *http.Request) {
  var err error
// instantiate the parameters structure
parameters := &ListPetsParameters{}
// get request fields in path and query parameters
// instantiate the responses structure
responses := &ListPetsResponses{}
// call the service provider
err = provider.ListPets(parameters, responses)
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

// Handler
# 


func HandleCreatePets(w http.ResponseWriter, r *http.Request) {
  var err error
// instantiate the responses structure
responses := &CreatePetsResponses{}
// call the service provider
err = provider.CreatePets(responses)
if err == nil {
} else {
  w.WriteHeader(http.StatusInternalServerError)
  w.Write([]byte(err.Error() + "\n"))
  return
}
}

// Handler
# 


func HandleShowPetById(w http.ResponseWriter, r *http.Request) {
  var err error
// instantiate the parameters structure
parameters := &ShowPetByIdParameters{}
// get request fields in path and query parameters
vars := mux.Vars(r)
// name:"petId" type:"string" position:PATH nativeType:"str" fieldName:"petId" parameterName:"petId" serialize:true 
if value, ok := vars["petId"]; ok {
	parameters.petId = value
}
// instantiate the responses structure
responses := &ShowPetByIdResponses{}
// call the service provider
err = provider.ShowPetById(parameters, responses)
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
router.HandleFunc("/pets", HandleListPets).Methods("GET")
router.HandleFunc("/pets", HandleCreatePets).Methods("POST")
router.HandleFunc("/pets/{petId}", HandleShowPetById).Methods("GET")
  http.Handle("/", router)
}

// Provide the API service over HTTP.
func ServeHTTP(address string) error {
  if provider == nil {
    return errors.New("Use pettst.Initialize() to set a service provider.")
  }
  return http.ListenAndServe(address, nil)
}
