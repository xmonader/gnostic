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
	"os"

	surface "github.com/googleapis/gnostic/surface"
)

func (renderer *Renderer) RenderTypes() ([]byte, error) {
	f := NewLineWriter()
	f.WriteLine(`# GENERATED FILE: DO NOT EDIT!`)
	f.WriteLine(`# Types used by the API.`)

	f.WriteLine(``)
	f.WriteLine(`from dataclasses import dataclass, fields`)
	f.WriteLine(``)

	for _, modelType := range renderer.Model.Types {
		f.WriteLine(`# ` + modelType.Description)
		if modelType.Kind == surface.TypeKind_STRUCT {
			f.WriteLine("@dataclass")
			f.WriteLine(`class ` + modelType.TypeName + `:`)
			fmt.Fprintln(os.Stderr, modelType.TypeName)
			if len(modelType.Fields) > 0 {
				for _, field := range modelType.Fields {
					prefix := ""
					suffix := ""
					if field.Kind == surface.FieldKind_REFERENCE {
						prefix = ""
					} else if field.Kind == surface.FieldKind_ARRAY {
						prefix = "List["
						suffix = "]"
					} else if field.Kind == surface.FieldKind_MAP {
						prefix = "Dict[str,"
						suffix = "]"
					}
					f.WriteLine(`    ` + field.FieldName + `: ` + prefix + field.NativeType + suffix)
				}
			} else {
				f.WriteLine(`    pass`)
			}

			f.WriteLine(``)
		}
		// } else if modelType.Kind == surface.TypeKind_OBJECT {
		// 	f.WriteLine(`type ` + modelType.TypeName + ` map[string]` + modelType.ContentType)
		// } else {
		// 	f.WriteLine(`type ` + modelType.TypeName + ` interface {}`)
		// }
	}
	return f.Bytes(), nil
}
