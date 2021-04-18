import json

import demistomock as demisto  # noqa: F401
import yaml
from CommonServerPython import *  # noqa: F401


def main():
    try:
        incident = demisto.incident()
        assets = incident.get('CustomFields', {}).get('assettable', {})

        if not assets:
            return ''

        if not isinstance(assets, dict):
            assets = json.loads(assets)

        if not isinstance(assets, list):
            assets = [assets]

        markdown = tableToMarkdown("Asset Table", assets)
        return {'ContentsFormat': formats['markdown'], 'Type': entryTypes['note'], 'Contents': markdown}

    except Exception as exp:
        return_error('could not parse Splunk assets', error=exp)


if __name__ in ('__main__', '__builtin__', 'builtins'):
    return_results(main())
