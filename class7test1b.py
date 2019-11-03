from __future__ import print_function, unicode_literals
import jinja2
crypto_vars = {
        "crypto_encr": "aes",
        "policy_group": "5",
        "isakmp_enable": False,
}
crypto_template = '''
crypto isakmp policy 10
    encr {{crypto_encr}}
    authentication pre-share
    group {{policy_group}}
{% if isakmp_enable -%}
crypto isakmp key my_key address 1.1.1.1 no-xauth
crypto isakmp keepalive 10 periodic
{% endif %}

'''

t= jinja2.Template(crypto_template)
print(t.render(crypto_vars))

