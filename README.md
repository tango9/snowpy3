```
███████╗███╗   ██╗ ██████╗ ██╗    ██╗██████╗ ██╗   ██╗██████╗ 
██╔════╝████╗  ██║██╔═══██╗██║    ██║██╔══██╗╚██╗ ██╔╝╚════██╗
███████╗██╔██╗ ██║██║   ██║██║ █╗ ██║██████╔╝ ╚████╔╝  █████╔╝
╚════██║██║╚██╗██║██║   ██║██║███╗██║██╔═══╝   ╚██╔╝   ╚═══██╗
███████║██║ ╚████║╚██████╔╝╚███╔███╔╝██║        ██║   ██████╔╝
╚══════╝╚═╝  ╚═══╝ ╚═════╝  ╚══╝╚══╝ ╚═╝        ╚═╝   ╚═════╝

      Python 3 Library for ServiceNow JSONv2 Rest API


*---------------------------------------------------------[ NOTE ]-*
* Based on servicenow 2.1.0 <https://pypi.org/project/servicenow/> *
* Wrttien by Francisco Freire <francisco.freire@locaweb.com.br>    *
*------------------------------------------------------------------*
```

## Installing

```
pip install snowpy3
```
Current version of SNOWPY3 works with NOW (Yokohama version)

## Dependencies

- python-requests
- python-redis



## NOTES
   Works with the latest version of SNOW (Sep 13, 2025 checks)

---

# SNOWPY3 Documentation

## Overview

SNOWPY3 is a Python 3 library designed to interact with ServiceNow instances via the JSONv2 REST API. It provides an ORM-like interface for common ServiceNow operations with built-in caching capabilities.

## Features

- 🔐 **Authentication**: Secure credential-based authentication
- 🚀 **CRUD Operations**: Complete Create, Read, Update, Delete functionality
- 📊 **Caching**: Redis-based caching with TTL support
- 🏗️ **ORM Pattern**: Object-oriented approach to ServiceNow tables
- 🔧 **Flexible Queries**: Support for both meta-based and query string operations
- 📋 **Pre-built Tables**: Ready-to-use classes for common ServiceNow tables

## Quick Start

### Basic Authentication

```python
from snowpy3 import Auth

# Initialize connection
auth = Auth(
    username='your_username',
    password='your_password',
    instance='your_instance',  # or full URL like 'https://yourinstance.service-now.com'
    timeout=120,
    debug=False,
    api='JSONv2'
)
```

### Working with Incidents

```python
from snowpy3 import SNOWPY3
from snowpy3 import Auth

# Create connection
auth = Auth('username', 'password', 'instance')

# Initialize Incident table handler
incident = SNOWPY3.Incident(auth)

# Create a new incident
new_incident = incident.create({
    'short_description': 'Server Down',
    'description': 'Production server is not responding',
    'priority': '1',
    'category': 'Hardware'
})

# List incidents
incidents = incident.list({'state': '1'})  # Active incidents

# Fetch specific incident
incident_data = incident.fetch_one({'number': 'INC0010001'})

# Update incident
incident.update(
    where={'number': 'INC0010001'},
    data={'state': '2', 'close_notes': 'Issue resolved'}
)
```

## Available Table Classes

SNOWPY3 provides pre-built classes for common ServiceNow tables:

| Class | Table | Description |
|-------|-------|-------------|
| `Incident` | `incident.do` | IT Service Management incidents |
| `Change` | `change_request.do` | Change management requests |
| `Problem` | `problem.do` | Problem management records |
| `User` | `sys_user.do` | System users |
| `Group` | `sys_user_group.do` | User groups |
| `ConfigurationItem` | `cmdb_ci.do` | Configuration items |
| `Server` | `cmdb_ci_server.do` | Server configuration items |
| `Router` | `cmdb_ci_ip_router.do` | Router configuration items |
| `Switch` | `cmdb_ci_ip_switch.do` | Switch configuration items |
| `Customer` | `core_company.do` | Company records |
| `Journal` | `sys_journal_field.do` | Journal entries |
| `Task` | `task_ci_list.do` | Task lists |
| `Cluster` | `cmdb_ci_cluster.do` | Cluster configuration items |
| `VPN` | `cmdb_ci_vpn.do` | VPN configuration items |
| `Racks` | `cmdb_ci_rack.do` | Rack configuration items |

## Advanced Usage

### Custom Queries

```python
# Using query strings
incidents = incident.fetch_all_by_query("state=1^priority=1")

# Using meta parameters
incidents = incident.fetch_all({'state': '1', 'priority': '1'})
```

### Time-based Queries

```python
# Get incidents updated in the last 30 minutes
recent_incidents = incident.last_updated(30)
```

### Batch Operations

```python
# Create multiple incidents
incident_data = [
    {'short_description': 'Issue 1', 'priority': '1'},
    {'short_description': 'Issue 2', 'priority': '2'}
]
result = incident.create_multiple(incident_data)

# Delete multiple records
incident.delete_multiple("state=6")  # Delete all closed incidents
```

### Caching Configuration

```python
from snowpy3 import Utils

# Enable caching (default is disabled)
Utils.ttl_cache = 300  # 5 minutes

# The caching is automatically applied to:
# - list()
# - list_by_query()
# - fetch_all()
# - fetch_all_by_query()
```

## Configuration Options

### Auth Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `username` | str | Required | ServiceNow username |
| `password` | str | Required | ServiceNow password |
| `instance` | str | Required | Instance name or full URL |
| `timeout` | int | 120 | Request timeout in seconds |
| `debug` | bool | False | Enable debug mode |
| `api` | str | 'JSONv2' | API version to use |
| `proxies` | dict | {} | HTTP proxies configuration |
| `verify` | bool | True | SSL certificate verification |

### Redis Configuration

SNOWPY3 uses Redis for caching. Make sure Redis is running and accessible:

```bash
# Install and start Redis
sudo apt-get install redis-server
sudo systemctl start redis
```

## Error Handling

```python
try:
    incidents = incident.fetch_all({'invalid_field': 'value'})
except Exception as e:
    print(f"Error occurred: {e}")
```

## Best Practices

1. **Security**: Store credentials securely using environment variables or configuration files
2. **Caching**: Enable caching for frequently accessed data
3. **Error Handling**: Always implement proper error handling
4. **Rate Limiting**: Be mindful of ServiceNow API rate limits
5. **Connection Pooling**: Reuse Auth instances when possible

## Troubleshooting

### Common Issues

1. **Authentication Failed**: Verify username/password and instance URL
2. **Timeout Errors**: Increase timeout value for large queries
3. **Redis Connection**: Ensure Redis server is running
4. **SSL Errors**: Set `verify=False` for self-signed certificates (not recommended for production)

### Debug Mode

Enable debug mode for detailed logging:

```python
auth = Auth('username', 'password', 'instance', debug=True)
```

## Contributing

Contributions are welcome! Please ensure:

1. Code follows PEP 8 standards
2. Add appropriate error handling
3. Include docstrings for new methods
4. Update tests for new functionality

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.

## Changelog

### Version 2025.09.12.002
- Comprehensive testing framework with real ServiceNow instance validation
- Production readiness verification completed
- Enhanced error handling and type hints
- Complete test suite with 100% functionality coverage

### Version 2025.09.12.001
- Initial release with Python 3.12 support
- Redis-based caching implementation
- Comprehensive ServiceNow table support
- JSONv2 API integration

## Support

For support and questions:
- 📧 Email: snowpy3@tangonine.com
- 🌐 Website: https://www.tangonine.com
- 📚 Documentation: https://github.com/tango9/snowpy3/wiki
- 🐛 Issues: https://github.com/tango9/snowpy3/issues
