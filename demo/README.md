# snowpy3 Demo Scripts

This directory contains demonstration scripts that show how to use snowpy3 with ServiceNow.

## Available Demos

### 1. Create Incident Demo (`create_incident_demo.py`)

Demonstrates how to create an incident in ServiceNow using snowpy3.

**Features:**
- Interactive credential input
- Environment variable support
- Comprehensive incident data creation
- Full incident details retrieval
- Error handling and troubleshooting tips

## Usage

### Prerequisites

1. **ServiceNow Instance**: You need access to a ServiceNow instance
2. **Credentials**: Valid username and password for ServiceNow
3. **Permissions**: User must have permission to create incidents
4. **snowpy3**: Library must be installed (`pip install snowpy3` or `uv add snowpy3`)

### Running the Demo

#### Option 1: Interactive Mode
```bash
cd demo
python create_incident_demo.py
```
The script will prompt you for:
- ServiceNow instance URL
- Username
- Password

#### Option 2: Environment Variables
```bash
export SNOW_URL="https://your-instance.service-now.com/"
export SNOW_USER="your_username"
export SNOW_PASS="your_password"

cd demo
python create_incident_demo.py
```

#### Option 3: PowerShell (Windows)
```powershell
$env:SNOW_URL="https://your-instance.service-now.com/"
$env:SNOW_USER="your_username"
$env:SNOW_PASS="your_password"

cd demo
python create_incident_demo.py
```

## What the Demo Does

1. **Connects** to your ServiceNow instance
2. **Creates** a new incident with sample data
3. **Retrieves** the created incident details
4. **Displays** comprehensive information about the incident

## Sample Output

```
🎯 snowpy3 Demo: Create Incident
==================================================

🔗 Connecting to ServiceNow instance...
   URL: https://your-instance.service-now.com/
   User: your_username
✅ Connected successfully!

📝 Creating a new incident...
   📋 Incident details:
      short_description: snowpy3 Demo Incident - 2025-09-13 13:30:00
      description: This incident was created by the snowpy3 demo script...
      category: Software
      subcategory: Application
      priority: 3
      urgency: 3
      impact: 3
      assignment_group: Software
      caller_id: your_username
      work_notes: Created via snowpy3 demo script - 2025-09-13 13:30:00

🚀 Creating incident...
✅ Incident created successfully!
   🆔 Sys ID: 27c8528483443210c0615e20ceaad334
   📝 Number: INC0010007
   📊 State: 1
   ⚡ Priority: 3

🔍 Fetching incident details...
✅ Incident details retrieved:
   📝 Short Description: snowpy3 Demo Incident - 2025-09-13 13:30:00
   📊 State: 1
   ⚡ Priority: 3
   📂 Category: Software
   👤 Assigned to: N/A
   📅 Created: 2025-09-13 13:30:00

🎉 Demo completed successfully!
   Your incident has been created and is ready for use.
```

## Troubleshooting

### Common Issues

1. **Connection Failed**
   - Verify your ServiceNow URL is correct
   - Check your username and password
   - Ensure your instance is accessible

2. **Permission Denied**
   - Verify you have permission to create incidents
   - Check if API access is enabled on your instance
   - Ensure your user role has incident creation rights

3. **Import Error**
   - Make sure snowpy3 is installed: `pip install snowpy3`
   - Check that you're running from the correct directory
   - Verify Python path includes the snowpy3 module

### Getting Help

- 📧 Email: snowpy3@tangonine.com
- 🌐 Website: https://www.tangonine.com
- 📚 Documentation: https://github.com/tango9/snowpy3/wiki
- 🐛 Issues: https://github.com/tango9/snowpy3/issues

## License

This demo is part of the snowpy3 project and is licensed under the GNU General Public License v3.0.
