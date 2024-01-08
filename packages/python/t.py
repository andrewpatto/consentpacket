from jsonschema import validate
import yaml
from referencing import Registry, Resource
from referencing.jsonschema import UnknownDialect

with open('../../schema/consentpackets-source.yaml', 'r') as schema_file:
    schema_content = yaml.safe_load(schema_file)

    schema = Resource.from_contents(schema_content)

    registry = Registry().with_resource(uri="http://example.com/my/schema", resource=schema)

    print(registry)

    # a sample consent packet we are going to check
    cp = {
        "schemaMajorVersion": 1,
        "consents": [
            {
                "target": {
                    "individualId": "UR12345",
                },
                "statements": [
                    {
                        "code": "DUO:0000007",
                        "shorthand": "DS",
                        "disease": "MONDO:diabetes",
                        "modifiers": [
                            {
                                "code": "DUO:0000024",
                                "after": "2023-10-03"
                            }
                        ]

                    }
                ]
            }
        ]}

    validate(instance=cp, schema=registry.contents("http://example.com/my/schema"))
