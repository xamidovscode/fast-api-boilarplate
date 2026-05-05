from enum import Enum

class UserRoles(str, Enum):
    admin = 'admin'
    seller = 'seller'
    super_admin = 'super_admin'

