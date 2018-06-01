
basictypes = {'string': 'str', 'integer': 'int', 'array':'List'}

def render_prop(propertytuple):

    name, type, default = propertytuple
    type = basictypes.get(type, type)
    if default != "XX":
        return f"    {name}: {type} = {default}"
    else:
        return f"    {name}: {type}"


def render_definition(definition):
    classname, val = definition.name, definition.value

    props = []
    for propinfo in val.properties.additional_properties:
        propname, propval = propinfo.name, propinfo.value
        proptype = propval.type.value[0]
        propdefault = 'XX'
        props.append( (propname, proptype, propdefault) )
    
    if not props: # LIST any other type Like `Pets`
        return "\n"
    
    propsstr="\n".join([render_prop(p) for p in props])

    template = """
@dataclass
class {classname}:

{propsstr}

""".format(classname=classname, propsstr=propsstr)

    return template

def render_defintions(defintions):
    res = "from dataclasses import dataclass\n"
    for definition in defintions.additional_properties:
        res += render_definition(definition) 

    return res

# definitions:
#   Pet:
#     required:
#       - id
#       - name
#     properties:
#       id:
#         type: integer
#         format: int64
#       name:
#         type: string
#       tag:
#         type: string
#   Pets:
#     type: array
#     items:
#       $ref: '#/definitions/Pet'
#   Error:
#     required:
#       - code
#       - message
#     properties:
#       code:
#         type: integer
#         format: int32
#       message:
#         type: string