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
	"strings"
)

func (renderer *Renderer) RenderProvider() ([]byte, error) {
	f := NewLineWriter()
	modelName := renderer.Model.GetName()
	f.WriteLine(`
from flask import Flask, send_from_directory, send_file

import os
dir_path = os.path.dirname(os.path.realpath(__file__))

app = Flask(__name__)

# we will add all of the resources here for now.
		
		`)
	f.WriteLine(fmt.Sprintf(`%s_api = Blueprint('%s_api', __name__)`, modelName, modelName))
	f.WriteLine(``)

	for _, method := range renderer.Model.Methods {

		parametersType := renderer.Model.TypeWithTypeName(method.ParametersTypeName)
		// responsesType := renderer.Model.TypeWithTypeName(method.ResponsesTypeName)
		f.WriteLine(commentForText(method.Description))
		f.WriteLine(fmt.Sprintf(`@%s_api.route('%s', methods=['%s']`, modelName, method.GetPath(), method.GetMethod()))

		if parametersType != nil {
			f.WriteLine(`def ` + method.GetOperation() +
				`(*fields(parameters) :` + `): pass`)
		} else {
			f.WriteLine(`def ` + method.GetOperation() + `(): pass`)
		}

	}
	f.WriteLine(``)
	return f.Bytes(), nil
}

func commentForText(text string) string {
	result := ""
	lines := strings.Split(text, "\n")
	for _, line := range lines {
		result += "# " + line
	}
	result += "\n\n"
	return result
}
