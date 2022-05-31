from django.db import models
from django.conf import settings

class Firewall(models.Model):
    """Initializes objects fed through by firewall_list_view. """
    def __init__(self, id, firewall, seq, name, permit, src_ip, src_ad, src_port, src_policy, dst_ip, dst_port, dst_policy, proto, hits, last_hit_at, created_at, updated_at, deleted_at):
        self.index = id
        self.id = firewall['id']
        self.firewall_name = firewall['name']
        self.ip = firewall['ip']
        self.type = firewall['type']
        self.env = firewall['env']
        self.seq = seq
        self.name = name
        self.permit = permit
        self.src_ip = src_ip
        self.src_ad = src_ad
        self.src_port = src_port
        self.src_policy = src_policy
        self.dst_ip = dst_ip
        self.dst_port = dst_port
        self.proto = proto
        self.hits = hits
        self.last_hit_at = last_hit_at
        self.created_at = created_at
        self.updated_at = updated_at
        self.deleted_at = deleted_at

    @classmethod
    def from_json(cls, json_string):
        json_dict = json.loads(json_string)
        return cls(**json_dict)

    def __repr__(self):
        return f'<{ self.firewall_name }>'