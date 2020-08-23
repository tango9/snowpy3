from snowpy3 import Utils

ttl_cache=0


class Base(object):
    __table__ = None

    def __init__(self, Connection):
        self.Connection = Connection

    @Utils.cached(ttl=ttl_cache)
    def list_by_query(self, query, **kwargs):
        return self.format(self.Connection._list_by_query(self.__table__, query, **kwargs))

    @Utils.cached(ttl=ttl_cache)
    def list(self, meta, **kwargs):
        return self.format(self.Connection._list(self.__table__, meta, **kwargs))

    @Utils.cached(ttl=ttl_cache)
    def fetch_all(self, meta, **kwargs):
        return self.format(self.Connection._get(self.__table__, meta, **kwargs))

    @Utils.cached(ttl=ttl_cache)
    def fetch_all_by_query(self, query, **kwargs):
        return self.format(self.Connection._get_by_query(self.__table__, query, **kwargs))

    @Utils.cached(ttl=ttl_cache)
    def fetch_one(self, meta, **kwargs):
        response = self.fetch_all(meta, **kwargs)
        if 'records' in response:
            if len(response['records']) > 0:
                return response['records'][0]
        else:
            if len(response) > 0:
                return response[0]
        return {}

    def create(self, data, **kwargs):
        return self.format(self.Connection._post(
            self.__table__, data, **kwargs))
        """ Test one create"""

    def create_multiple(self, data, **kwargs):
        return self.format(self.Connection._post_multiple(
            self.__table__, data, **kwargs))

    def update(self, where, data, **kwargs):
        return self.format(self.Connection._update(
            self.__table__, where, data, **kwargs))

    def delete(self, id, **kwargs):
        return self.format(self.Connection._delete(
            self.__table__, id, **kwargs))

    def delete_multiple(self, query, **kwargs):
        return self.format(self.Connection._delete_multiple(
            self.__table__, query, **kwargs))

    def format(self, response):
        return self.Connection._format(response)

    def last_updated(self, minutes, meta={}, **kwargs):
        metaon = {'sys_updated_on':
                      'Last {0} minutes@javascript:gs.minutesAgoStart({1})@'
                      'javascript:gs.minutesAgoEnd(0)'.format(minutes, minutes)}
        return self.format(self.Connection._get(
            self.__table__, meta, metaon=metaon, **kwargs))


#
# ServiceNow OOB Tables
#

class Change(Base):
    __table__ = 'change_request.do'


class Incident(Base):
    __table__ = 'incident.do'


class Problem(Base):
    __table__ = 'problem.do'


class Group(Base):
    __table__ = 'sys_user_group.do'


class ConfigurationItem(Base):
    __table__ = 'cmdb_ci.do'


class Journal(Base):
    __table__ = 'sys_journal_field.do'


class Server(Base):
    __table__ = 'cmdb_ci_server.do'


class Task(Base):
    __table__ = 'task_ci_list.do'


class User(Base):
    __table__ = 'sys_user.do'


class Customer(Base):
    __table__ = 'core_company.do'


class Router(Base):
    __table__ = 'cmdb_ci_ip_router.do'


class Switch(Base):
    __table__ = 'cmdb_ci_ip_switch.do'


class Cluster(Base):
    __table__ = 'cmdb_ci_cluster.do'


class VPN(Base):
    __table__ = 'cmdb_ci_vpn.do'


class Racks(Base):
    __table__ = 'cmdb_ci_rack.do'
