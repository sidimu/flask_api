

class Scope:
    allow_api = []
    allow_module = []
    forbidden = []
    #重载运算符
    def __add__(self, other):
        self.allow_api = self.allow_api + other.allow_api
        self.allow_api = list(set(self.allow_api))#去重

        self.allow_module = self.allow_module + other.allow_module
        self.allow_module = list(set(self.allow_module))  # 去重

        self.forbidden = self.forbidden + other.forbidden
        self.forbidden = list(set(self.forbidden))  # 去重
        return self



#普通用户
class UserScope(Scope):
    forbidden = ['v1.user+super_get_user', 'v1.user+super_delete_user']
    # allow_api = ['v1.user+get_user', 'v1.user+delete_user']

    def __init__(self):
        self + AdminScope()





#管理员
class AdminScope(Scope):
    # allow_api = ['v1.user+super_get_user', 'v1.user+super_delete_user']
    allow_module = ['v1.user']

    def __init__(self):
        self + UserScope()



def is_in_scope(scope, endpoint):
    scope = globals()[scope]()
    splits = endpoint.split('+')
    module_name = splits[0]
    if endpoint in scope.forbidden:
        return False
    if endpoint in scope.allow_api:
        return True
    if module_name in scope.allow_module:
        return True
    else:
        return False
