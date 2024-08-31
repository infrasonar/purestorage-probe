from libprobe.probe import Probe
from lib.check.certificates import check_certificates
from lib.check.connections import check_connections
from lib.check.drives import check_drives
from lib.check.hardware import check_hardware
from lib.check.hgroups import check_hgroups
from lib.check.hosts import check_hosts
from lib.check.interfaces import check_interfaces
from lib.check.pgroups import check_pgroups
from lib.check.pods import check_pods
from lib.check.ports import check_ports
from lib.check.volumes import check_volumes
from lib.version import __version__ as version


if __name__ == '__main__':
    checks = {
        'certificates': check_certificates,
        'connections': check_connections,
        'drives': check_drives,
        'hardware': check_hardware,
        'hgroups': check_hgroups,
        'hosts': check_hosts,
        'interfaces': check_interfaces,
        'pgroups': check_pgroups,
        'pods': check_pods,
        'ports': check_ports,
        'volumes': check_volumes,
    }

    probe = Probe("purestorage", version, checks)

    probe.start()
