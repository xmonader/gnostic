from gnostic.OpenAPIv2_pb2 import Document


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
    from sys import argv
    srcfile = argv[1]
    source = open(srcfile, "rb").read()
    dumpinfo(source)