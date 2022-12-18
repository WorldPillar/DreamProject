import random
from ..serializers.server_serializers import ServerDataSerializer
from .max_number_of_players import maxCount
from ..models import ServerData
from ..permissions.server_permission import GetBanServers


def generate_number_of_players(user):
    servers = ServerData.objects.all()
    ban_servers = GetBanServers.banservers(user)

    for ban in ban_servers:
        if ban.server in servers:
            servers = servers.exclude(id=ban.server.id)

    servers_with_count = []
    for server in servers:
        if server.name in maxCount:
            maximum = int(maxCount[server.name])
            current = random.randint(0, maximum)
        else:
            maximum = int(maxCount["Default"])
            current = random.randint(0, maximum)
        counter = {'maximum': maximum, 'current': current}
        server_data = ServerDataSerializer(server).data
        server_data.update(counter)
        servers_with_count.append(server_data)
    return servers_with_count
