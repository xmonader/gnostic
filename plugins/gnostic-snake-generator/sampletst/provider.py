// GENERATED FILE: DO NOT EDIT!

package sampletst

// To create a server, first write a class that implements this interface.
// Then pass an instance of it to Initialize().
type Provider interface {

// 
GetSample(parameters *GetSampleParameters, responses *GetSampleResponses) (err error)
}
