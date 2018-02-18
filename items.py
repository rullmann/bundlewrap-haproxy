pkg_dnf = {
    'haproxy': {},
}

svc_systemd = {
    'haproxy': {
        'needs': ['pkg_dnf:haproxy']
    },
}

files = {
    '/etc/haproxy/haproxy.cfg': {
        'mode': '0664',
        'source': '{}.haproxy.cfg'.format(node.name),
        'triggers': ['svc_systemd:haproxy:restart'],
    },
}
