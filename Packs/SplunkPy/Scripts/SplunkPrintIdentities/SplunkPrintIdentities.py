import json

import demistomock as demisto  # noqa: F401
import yaml
from CommonServerPython import *  # noqa: F401


def main():
    try:
        incident = demisto.incident()
        identities = incident.get('CustomFields', {}).get('identitytable', {})

        if not identities:
            return ''

        if not isinstance(identities, dict):
            identities = json.loads(identities)

        if not isinstance(identities, list):
            identities = [identities]

        markdown = tableToMarkdown("Identity Table", assets)
        return {'ContentsFormat': formats['markdown'], 'Type': entryTypes['note'], 'Contents': markdown}

    except Exception as exp:
        return_error('could not parse Splunk identities', error=exp)


if __name__ in ('__main__', '__builtin__', 'builtins'):
    return_results(main())
