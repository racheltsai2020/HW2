# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

OUTPUT_SCHEMA = {
    "$schema": "http://json-schema.org/draft-07/schema",
    "$id": "http://example.com/example.json",
    "type": "object",
    "title": "Sample Output schema",
    "description": "The root schema comprises the entire JSON document of the Return Schema.",
    "examples": [{"statusCode": 200, "body": "bucket1|bucket2"}],
    "required": ["statusCode", "body"],
    "properties": {
        "statusCode": {
            "$id": "#/properties/statusCode",
            "type": "integer",
            "title": "HTTP Status Code",
            "examples": [200,401]
        },
        "body": {
            "$id": "#/properties/body",
            "type": "string",
            "title": "The return text",
            "examples": ["bucket1|bucket2","Error"],
            "maxLength": 20480,
        }
    },
}