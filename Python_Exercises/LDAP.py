import ldap

#Open a connection
ldap_client = ldap.initialize("ldap://127.0.0.1:389/")

#Bind/Authenticate with a user with appropriate rights to add objects
ldap_client.simple_bind("dc=localdomain,dc=loc")

base_dn = "ou=users,dc=localdomain,dc=loc"
filter = '(objectclass=person)'
attrs = ['sn']

result = ldap_client.search_s(base_dn, ldap.SCOPE_SUBTREE, filter, attrs)
print(result)
