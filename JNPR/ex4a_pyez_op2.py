from jnpr_devices import srx_device
from ex2b_pyez_func import gather_routes
from pprint import pprint
from jnpr.junos.utils.config import Config

def Config_from_file(path, a_device,merge= True):
    cfg = Config(a_device)
    cfg.lock()
    cfg.load(path="static_routes.conf", format="text", merge=True)
    if cfg.diff() is not None:
        cfg.commit()
    cfg.unlock()

def Del_routes(a_device):
    cfg= Config(a_device)
    cfg.lock()
    cfg.load("delete routing-options static route 203.0.113.5/32", format = "set", merge= True)
    cfg.load("delete routing-options static route 203.0.113.200/32", format = "set", merge=True)
    print("deleting the routes")
    if cfg.diff() is not None:
        cfg.commit()
    cfg.unlock()

def Compare_routes(routes, updated_routes):
    new_routes = []
    for route in updated_routes.keys():
        if route not in routes.keys():
            new_routes.append(route)
    return new_routes

if __name__ == "__main__":
    a_device = srx_device()
    a_device.timeout = 60
    cfg = Config(a_device)
    route = gather_routes(a_device)
    Config_from_file(path="static_routes.conf", a_device=a_device, merge=True)
    updated_routes = gather_routes(a_device)
    new_routes = Compare_routes(route, updated_routes)

    print("The new routes are", new_routes)
    Del_routes(a_device)
