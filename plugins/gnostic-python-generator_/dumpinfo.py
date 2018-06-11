from sys import argv
import os
# from gnostic.discovery_pb2 import Request, Response
from gnostic.OpenAPIv2_pb2 import Document
from gnostic.plugin_pb2 import *
from gnostic.surface_pb2 import Model



def printprotomsg(node, indent=0):
    # print("NODE: ", node)
    if hasattr(node, "DESCRIPTOR"):
        for f in node.DESCRIPTOR.fields_by_name.keys():
            print("FIELD: ", f)
            # printprotomsg("\n\n====\n\n" + f + " => " + str(getattr(node, f)) + "\n\n=======\n\n", indent+1)
            printprotomsg(getattr(node, f), indent+1)
    else:
        print(indent* " ", node)

def dumpinfo(source):
    doc = Document().FromString(source)
    printprotomsg(doc, 0)
    # print(doc.swagger)
    # print(doc.host)
    # # print(doc.basePath)
    # print(doc.info)
    # print(doc.info.title)
    # print(doc.info.description)
    # print(doc.info.version)
    # print("Paths: ")
    # for pair in doc.paths.path: 
    #     val = pair.value
    #     name = pair.name
    #     # print(val.summary)
    #     print(val.operation)
    #     for p in val.parameters:
    #         print("PARAM: ", p)
    #     print(f"NAME: {name}")
    #     print(f"VAL: {val}")

if __name__ == "__main__":
    srcfile = ""
    if len(argv) > 2:
        srcfile = argv[2]
    else:
        srcfile = os.path.join(os.path.dirname(__file__), "petstore.pb")
    print("SRCFILE: ", srcfile)
    sourceb = open(srcfile, "rb").read()
    print("SOURCE: ", sourceb)
    # dumpinfo(sourceb)

    req = Request()
    req.FromString(sourceb)
    res = Response()


#   // read the code generation request
#   let rawRequest = try Stdin.readall()
#   let request = try Gnostic_Plugin_V1_Request(serializedData:rawRequest)

#   var response = Gnostic_Plugin_V1_Response()
  
#   var openapiv2 : Openapi_V2_Document?
#   var surface : Surface_V1_Model?
  
#   for model in request.models {
#     if model.typeURL == "openapi.v2.Document" {
#       openapiv2 = try Openapi_V2_Document(serializedData: model.value)      
#     } else if model.typeURL == "surface.v1.Model" {
#       surface = try Surface_V1_Model(serializedData: model.value)      
#     }
#   }  