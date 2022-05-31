from django.shortcuts import render

import json
from .models import Firewall

def firewall_list_view(request):
    """Parses the json file and feeds the objects through the class init. Compiles all objects within 'queryset'
    and renders it to entry_table.html"""
    queryset: dict = []
    with open('/Users/jamesfreeland/Firewall/dataentry/500_rules.json', 'r') as json_file:
        firewall_interm = json.loads(json_file.read())
        firewall_data = firewall_interm['results']
        for f in firewall_data:
            queryset.append(Firewall(**f))
    

    context = {
    "object_list":queryset,
    }

    return render(request, "/Users/jamesfreeland/NewFirewall/AuditTable/templates/FirewallAudit.html", context)
