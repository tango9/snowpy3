import requests
import json
from typing import Dict, Any, Optional, Union

from . import Utils


class Auth(object):

    def __init__(self, username: str, password: str, instance: str, timeout: int = 120,
                 debug: bool = False, api: str = 'JSONv2', proxies: Dict[str, str] = None, verify: bool = True) -> None:
        self.username = username
        self.password = password
        if 'https://' in instance:
            self.instance = instance
        else:
            self.instance = 'https://{0}.service-now.com/'.format(instance)
        self.timeout = timeout
        self.session = requests.Session()
        self.session.auth = (self.username, self.password)
        self.api = api
        self.proxies = proxies or {}
        self.verify = verify
        if api.startswith('JSONv2'):
            self.session.headers.update({'Accept': 'application/json'})

    def _list(self, table: str, meta: Dict[str, Any] = None, **kwargs) -> requests.Response:
        query = Utils.format_query(meta or {}, kwargs.get('metaon', {}))
        params = kwargs.get('params', {})
        params.update({
            self.api:             '',
            'sysparm_action':   'getKeys',
            'sysparm_query': query,
            'displayvalue': 'true'
        })
        return self.session.get('{0}/{1}'.format(self.instance, table),
                                params=params, timeout=self.timeout,
                                proxies=self.proxies, verify=self.verify)

    def _list_by_query(self, table: str, query: str, **kwargs) -> requests.Response:
        params = kwargs.get('params', {})
        params.update({
            self.api:             '',
            'sysparm_action':   'getKeys',
            'sysparm_query':    query,
            'displayvalue': 'true'
        })
        return self.session.get('{0}/{1}'.format(self.instance, table),
                                params=params, timeout=self.timeout,
                                proxies=self.proxies, verify=self.verify)

    def _get(self, table: str, meta: Dict[str, Any] = None, **kwargs) -> requests.Response:
        query = Utils.format_query(meta or {}, kwargs.get('metaon', {}))
        params = kwargs.get('params', {})
        params.update({
            self.api:             '',
            'sysparm_action':   'getRecords',
            'sysparm_query': query,
            'displayvalue': 'true'
        })
        return self.session.get('{0}/{1}'.format(self.instance, table),
                                params=params, timeout=self.timeout,
                                proxies=self.proxies, verify=self.verify)

    def _get_by_query(self, table: str, query: str, **kwargs) -> requests.Response:
        params = kwargs.get('params', {})
        params.update({
            self.api:             '',
            'sysparm_action':   'getRecords',
            'sysparm_query': query,
            'displayvalue': 'true'
        })
        return self.session.get('{0}/{1}'.format(self.instance, table),
                                params=params, timeout=self.timeout,
                                proxies=self.proxies, verify=self.verify)

    def _post(self, table: str, data: Dict[str, Any], **kwargs) -> requests.Response:
        params = kwargs.get('params', {})
        params.update({
            self.api:             '',
            'sysparm_action':   'insert'
        })
        return self.session.post('{0}/{1}'.format(self.instance, table),
                                 params=params, data=json.dumps(data),
                                 timeout=self.timeout, proxies=self.proxies,
                                 verify=self.verify)

    def _post_multiple(self, table: str, data: list, **kwargs) -> requests.Response:
        params = kwargs.get('params', {})
        params.update({
            self.api:             '',
            'sysparm_action':   'insertMultiple'
        })
        return self.session.post('{0}/{1}'.format(self.instance, table),
                                 params=params, data=json.dumps(data),
                                 timeout=self.timeout, proxies=self.proxies,
                                 verify=self.verify)

    def _update(self, table: str, where: Dict[str, Any], data: Dict[str, Any], **kwargs) -> requests.Response:
        query = Utils.format_query(where, {})
        params = kwargs.get('params', {})
        params.update({
            self.api:             '',
            'sysparm_action':   'update',
            'sysparm_query':    query
        })
        return self.session.post('{0}/{1}'.format(self.instance, table),
                                 params=params, data=json.dumps(data),
                                 timeout=self.timeout, proxies=self.proxies,
                                 verify=self.verify)

    def _update_by_query(self, table: str, query: str, data: Dict[str, Any], **kwargs) -> requests.Response:
        params = kwargs.get('params', {})
        params.update({
            self.api:             '',
            'sysparm_action':   'update',
            'sysparm_query':    query
        })
        return self.session.post('{0}/{1}'.format(self.instance, table),
                                 params=params, data=json.dumps(data),
                                 timeout=self.timeout, proxies=self.proxies,
                                 verify=self.verify)

    def _delete(self, table: str, id: str, **kwargs) -> requests.Response:
        params = kwargs.get('params', {})
        params.update({
            self.api:             '',
            'sysparm_action':   'deleteRecord',
            'sysparm_sys_id':    id
        })
        return self.session.post('{0}/{1}'.format(self.instance, table),
                                 params=params, timeout=self.timeout,
                                 proxies=self.proxies, verify=self.verify)

    def _delete_multiple(self, table: str, query: str, **kwargs) -> requests.Response:
        params = kwargs.get('params', {})
        params.update({
            self.api:             '',
            'sysparm_action':   'deleteMultiple',
            'sysparm_query':    query
        })
        return self.session.post('{0}/{1}'.format(self.instance, table),
                                 params=params, timeout=self.timeout,
                                 proxies=self.proxies, verify=self.verify)

    def _format(self, response: requests.Response) -> Dict[str, Any]:
        return json.loads(response.text)
