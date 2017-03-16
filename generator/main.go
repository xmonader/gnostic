// Copyright 2017 Google Inc. All Rights Reserved.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//    http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"os"
	"os/exec"
	"runtime"
	"strings"

	"github.com/googleapis/gnostic/jsonschema"
)

const LICENSE = "" +
	"// Copyright 2017 Google Inc. All Rights Reserved.\n" +
	"//\n" +
	"// Licensed under the Apache License, Version 2.0 (the \"License\");\n" +
	"// you may not use this file except in compliance with the License.\n" +
	"// You may obtain a copy of the License at\n" +
	"//\n" +
	"//    http://www.apache.org/licenses/LICENSE-2.0\n" +
	"//\n" +
	"// Unless required by applicable law or agreed to in writing, software\n" +
	"// distributed under the License is distributed on an \"AS IS\" BASIS,\n" +
	"// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n" +
	"// See the License for the specific language governing permissions and\n" +
	"// limitations under the License.\n"

var PROTO_OPTIONS = []ProtoOption{
	ProtoOption{
		Name:  "java_multiple_files",
		Value: "true",
		Comment: "// This option lets the proto compiler generate Java code inside the package\n" +
			"// name (see below) instead of inside an outer class. It creates a simpler\n" +
			"// developer experience by reducing one-level of name nesting and be\n" +
			"// consistent with most programming languages that don't support outer classes.",
	},

	ProtoOption{
		Name:  "java_outer_classname",
		Value: "OpenAPIProto",
		Comment: "// The Java outer classname should be the filename in UpperCamelCase. This\n" +
			"// class is only used to hold proto descriptor, so developers don't need to\n" +
			"// work with it directly.",
	},

	ProtoOption{
		Name:    "java_package",
		Value:   "org.openapi.v2",
		Comment: "// The Java package name must be proto package name with proper prefix.",
	},

	ProtoOption{
		Name:  "objc_class_prefix",
		Value: "OAS",
		Comment: "// A reasonable prefix for the Objective-C symbols generated from the package.\n" +
			"// It should at a minimum be 3 characters long, all uppercase, and convention\n" +
			"// is to use an abbreviation of the package name. Something short, but\n" +
			"// hopefully unique enough to not conflict with things that may come along in\n" +
			"// the future. 'GPB' is reserved for the protocol buffer implementation itself.",
	},
}

func GenerateOpenAPIV2() {
	// the OpenAPI schema file and API version are hard-coded for now
	input := "openapi-2.0.json"
	filename := "OpenAPIv2"
	proto_packagename := "openapi.v2"
	go_packagename := strings.Replace(proto_packagename, ".", "_", -1)

	base_schema := jsonschema.NewSchemaFromFile("schema.json")
	base_schema.ResolveRefs()
	base_schema.ResolveAllOfs()

	openapi_schema := jsonschema.NewSchemaFromFile(input)
	openapi_schema.ResolveRefs()
	openapi_schema.ResolveAllOfs()

	// build a simplified model of the types described by the schema
	cc := NewDomain(openapi_schema)
	// generators will map these patterns to the associated property names
	// these pattern names are a bit of a hack until we find a more automated way to obtain them
	cc.PatternNames = map[string]string{
		"^x-": "vendorExtension",
		"^/":  "path",
		"^([0-9]{3})$|^(default)$": "responseCode",
	}
	cc.Build()
	log.Printf("Type Model:\n%s", cc.Description())

	var err error

	// generate the protocol buffer description
	proto := cc.GenerateProto(proto_packagename, LICENSE, PROTO_OPTIONS, []string{"google/protobuf/any.proto"})
	proto_filename := filename + "/" + filename + ".proto"
	err = ioutil.WriteFile(proto_filename, []byte(proto), 0644)
	if err != nil {
		panic(err)
	}

	// generate the compiler
	compiler := cc.GenerateCompiler(go_packagename, LICENSE, []string{
		"fmt",
		"gopkg.in/yaml.v2",
		"strings",
		"github.com/googleapis/gnostic/compiler",
	})
	go_filename := filename + "/" + filename + ".go"
	err = ioutil.WriteFile(go_filename, []byte(compiler), 0644)
	if err != nil {
		panic(err)
	}
	// format the compiler
	err = exec.Command(runtime.GOROOT()+"/bin/gofmt", "-w", go_filename).Run()
}

func main() {
	var ext_gen = false
	var v2_gen = true

	usage := `
Usage: generator [OPTIONS]
Options:
  --v1       Generates the  Protocol Buffer representation and Go-language support code for OpenAPI v1
  --extension EXTENSION_SCHEMA_SOURCE [OPTIONS_FOR_EXTENSION_GENERATOR] Generates the compiler extensions that convert extensions found by gnostic into compiled protocol buffers. 
    EXTENSION_SCHEMA_SOURCE is the json schema for the supported vendor extension names.
    OPTIONS_FOR_EXTENSION_GENERATOR:
	  --out_dir=PATH: For the given EXTENSION_SCHEMA_SOURCE, write the Protocol Buffer representation and the Go-language support code to the specified location.
`
	if len(os.Args) > 1 {
		if os.Args[1] == "--v1" {
			v2_gen = true
		} else if os.Args[1] == "--extension" {
			ext_gen = true
		} else {
			fmt.Printf("Unknown option: %s.\n%s\n", os.Args[1], usage)
			os.Exit(-1)
		}
	}

	if ext_gen {
		ProcessExtensionGenCommandline(usage)
	} else if v2_gen {
		GenerateOpenAPIV2()
	}
}
