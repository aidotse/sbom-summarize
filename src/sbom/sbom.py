from pathlib import Path
import json
from collections import Counter


class Sbom:

    def __init__(self, sbom_path: str) -> None:
        self.sbom_path = Path(sbom_path)
        self.sbom = json.load(self.sbom_path.open())

    def pp_sbom(self) -> None:
        print(json. dumps(self.sbom, indent=4))

    def print_count_licenses(self) -> None:
        licenses = []
        no_licensed_packages = []
        for package in self.sbom['packages']:
            if('licenseConcluded' in package):
                licenses.append(package['licenseConcluded'])
            else:
                no_licensed_packages.append(package['name'])

        licenses_counter = Counter(licenses)

        for license_type in licenses_counter:
            print(license_type,':',licenses_counter[license_type])

        print('Packages without licenses:\n',no_licensed_packages)

