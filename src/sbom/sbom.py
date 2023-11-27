from pathlib import Path
import json
from collections import Counter


class Sbom:

    def __init__(self, sbom_path: str) -> None:
        self.sbom_path = Path(sbom_path)
        self.sbom = json.load(self.sbom_path.open())
        if list(self.sbom.keys())[0] != 'SPDXID':
            print('---\nIs this a valid SBOM?')

    def pp_sbom(self) -> None:
        print(json. dumps(self.sbom, indent=4))

    def print_count_licenses(self) -> None:
        licenses = []
        no_licensed_packages = []
        for package in self.sbom['packages']:
            if package['SPDXID'] not in self.sbom['documentDescribes']:
                if('licenseConcluded' in package):
                    licenses.append(package['licenseConcluded'])
                else:
                    no_licensed_packages.append(package['name'])

        licenses_counter = Counter(licenses)

        print('---\nSummarize\nSBOM-file: ', self.sbom_path.name,'\n')

        if len(licenses_counter) > 0: 
            print('License count:')
            for license_type in licenses_counter:
                print(license_type,':',licenses_counter[license_type])
        else:
            print('No packages with licenses found.')
        print('\n')

        if len(no_licensed_packages) > 0:
            print('Packages without licenses:')
            for no_lic_pack in no_licensed_packages:
                print(no_lic_pack)
        else:
            print('No packages without license found.')

        print('---')

