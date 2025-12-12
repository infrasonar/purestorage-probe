from libprobe.probe import Probe
from lib.check.alerts import CheckAlerts
from lib.check.certificates import CheckCertificates
from lib.check.connections import CheckConnections
from lib.check.drives import CheckDrives
from lib.check.hardware import CheckHardware
from lib.check.hgroups import CheckHgroups
from lib.check.hosts import CheckHosts
from lib.check.interfaces import CheckInterfaces
from lib.check.pgroups import CheckPgroups
from lib.check.pods import CheckPods
from lib.check.ports import CheckPorts
from lib.check.volumes import CheckVolumes
from lib.version import __version__ as version


if __name__ == '__main__':
    checks = (
        CheckAlerts,
        CheckCertificates,
        CheckConnections,
        CheckDrives,
        CheckHardware,
        CheckHgroups,
        CheckHosts,
        CheckInterfaces,
        CheckPgroups,
        CheckPods,
        CheckPorts,
        CheckVolumes,
    )

    probe = Probe("purestorage", version, checks)
    probe.start()
