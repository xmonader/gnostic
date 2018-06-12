// GENERATED FILE: DO NOT EDIT!

// Types used by the API.
// implements the service definition of APIError
@dataclass
class APIError:
Code int `json:"code,omitempty"`
Message str `json:"message,omitempty"`

// implements the service definition of Sample
@dataclass
class Sample:
Id str `json:"id,omitempty"`
Thing Dict[str,object] `json:"thing,omitempty"`
Count int `json:"count,omitempty"`

// GetSampleParameters holds parameters to GetSample
@dataclass
class GetSampleParameters:
Id str `json:"id,omitempty"`

// GetSampleResponses holds responses of GetSample
@dataclass
class GetSampleResponses:
OK Sample
Code401 APIError
Code404 APIError

