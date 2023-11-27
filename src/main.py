""" Main module to start the application """
import sys

from sbom.sbom import Sbom

def main() -> None:
    sbom_obj = Sbom('sbom/Balsam_statisticssweden_0e8ec48af3aa96dd9e6c3c517a28b6d3b7ec03e5.json')
    sbom_obj.print_count_licenses()
    return 0

if __name__ == '__main__':
    sys.exit(main())