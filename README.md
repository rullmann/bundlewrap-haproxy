# haproxy

haproxy, the well-known tcp/http load balancer, combined with bundlewrap.
This bundle is pretty simple and won't cover compley use cases.

Assigning this bundle to a node will also trigger an integration from the [telegraf](https://github.com/rullmann/bundlewrap-telegraf) bundle.

## Requirements

* Existing `haproxy.cfg`

## Setup notes

As this bundle is currently very simple it won't manage your `haproxy.cfg`.
Instead you already should have one.

Put the config inside `data/haproxy/files/`. Naming scheme for the file: `<node.name>.haproxy.cfg`

## Integrations

* Bundles:
  * [telegraf](https://github.com/rullmann/bundlewrap-telegraf)

### notes on the telegraf

The telegraf integration requires an url to access the haproxy statistics.
Something like this in your `haproxy.cfg` will do the trick:

    # haproxy statistics
    listen stats
      bind 127.0.0.1:11111
      mode http
      stats enable
      stats uri /stats
