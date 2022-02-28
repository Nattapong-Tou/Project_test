import orionsdk

swis = orionsdk.SwisClient("172.168.10.140", "sa", "P@ssw0rd")
aliases = swis.invoke('Metadata.Entity', 'GetAliases', 'SELECT B.Caption FROM Orion.Nodes B')
print(aliases)



