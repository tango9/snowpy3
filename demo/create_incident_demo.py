#!/usr/bin/env python3
"""
snowpy3 Demo: Create Incident
============================

This demo script shows how to create an incident in ServiceNow using snowpy3.

Requirements:
- ServiceNow instance URL
- Valid username and password
- snowpy3 library installed

Usage:
    python create_incident_demo.py

Or with environment variables:
    SNOW_URL=https://your-instance.service-now.com/
    SNOW_USER=your_username
    SNOW_PASS=your_password
    python create_incident_demo.py
"""

import os
import sys
from datetime import datetime

# Add the parent directory to the path so we can import snowpy3
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from snowpy3.Connection import Auth
from snowpy3 import SNOWPY3


def main():
    """Main demo  function to create an incident."""
    
    print("🎯 snowpy3 Demo: Create Incident")
    print("=" * 50)
    
    # Get ServiceNow credentials from environment variables or prompt user
    snow_url = os.getenv('SNOW_URL')
    snow_user = os.getenv('SNOW_USER')
    snow_pass = os.getenv('SNOW_PASS')
    
    if not snow_url:
        snow_url = input("Enter your ServiceNow instance URL (e.g., https://your-instance.service-now.com/): ")
    
    if not snow_user:
        snow_user = input("Enter your ServiceNow username: ")
    
    if not snow_pass:
        snow_pass = input("Enter your ServiceNow password: ")
    
    try:
        print(f"\n🔗 Connecting to ServiceNow instance...")
        print(f"   URL: {snow_url}")
        print(f"   User: {snow_user}")
        
        # Initialize the connection
        auth = Auth(username=snow_user, password=snow_pass, instance=snow_url)
        
        print("✅ Connected successfully!")
        
        # Initialize the Incident class
        incident = SNOWPY3.Incident(auth)
        
        print("\n📝 Creating a new incident...")
        
        # Prepare incident data
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        incident_data = {
            'short_description': f'snowpy3 Demo Incident - {current_time}',
            'description': f'This incident was created by the snowpy3 demo script at {current_time}.\n\n'
                          f'This demonstrates how to create incidents programmatically using snowpy3.',
            'category': 'Software',
            'subcategory': 'Application',
            'priority': 3,  # 3 = Moderate
            'urgency': 3,   # 3 = Moderate
            'impact': 3,    # 3 = Moderate
            'assignment_group': 'Software',  # Adjust based on your instance
            'caller_id': snow_user,  # Set caller to current user
            'work_notes': f'Created via snowpy3 demo script - {current_time}'
        }
        
        print("   📋 Incident details:")
        for key, value in incident_data.items():
            print(f"      {key}: {value}")
        
        # Create the incident
        print("\n🚀 Creating incident...")
        response = incident.create(incident_data)
        
        # Handle the response format (ServiceNow returns records array)
        if response and 'records' in response and len(response['records']) > 0:
            incident_record = response['records'][0]
            print("✅ Incident created successfully!")
            print(f"   🆔 Sys ID: {incident_record['sys_id']}")
            print(f"   📝 Number: {incident_record.get('number', 'N/A')}")
            print(f"   📊 State: {incident_record.get('state', 'N/A')}")
            print(f"   ⚡ Priority: {incident_record.get('priority', 'N/A')}")
            
            # Fetch the created incident to show full details
            print("\n🔍 Fetching incident details...")
            try:
                created_incident = incident.fetch_one({'sys_id': incident_record['sys_id']})
                
                if created_incident and isinstance(created_incident, dict):
                    print("✅ Incident details retrieved:")
                    print(f"   📝 Short Description: {created_incident.get('short_description', 'N/A')}")
                    print(f"   📊 State: {created_incident.get('state', 'N/A')}")
                    print(f"   ⚡ Priority: {created_incident.get('priority', 'N/A')}")
                    print(f"   📂 Category: {created_incident.get('category', 'N/A')}")
                    print(f"   👤 Assigned to: {created_incident.get('assigned_to', 'N/A')}")
                    print(f"   📅 Created: {created_incident.get('sys_created_on', 'N/A')}")
                else:
                    print("⚠️  Incident details could not be retrieved (empty response)")
            except Exception as fetch_error:
                print(f"⚠️  Could not fetch incident details: {str(fetch_error)}")
                print("   (Incident was created successfully, but details retrieval failed)")
        elif response and 'sys_id' in response:
            # Fallback for direct sys_id response format
            print("✅ Incident created successfully!")
            print(f"   🆔 Sys ID: {response['sys_id']}")
            print(f"   📝 Number: {response.get('number', 'N/A')}")
            print(f"   📊 State: {response.get('state', 'N/A')}")
            print(f"   ⚡ Priority: {response.get('priority', 'N/A')}")
            
            # Fetch the created incident to show full details
            print("\n🔍 Fetching incident details...")
            try:
                created_incident = incident.fetch_one({'sys_id': response['sys_id']})
                
                if created_incident and isinstance(created_incident, dict):
                    print("✅ Incident details retrieved:")
                    print(f"   📝 Short Description: {created_incident.get('short_description', 'N/A')}")
                    print(f"   📊 State: {created_incident.get('state', 'N/A')}")
                    print(f"   ⚡ Priority: {created_incident.get('priority', 'N/A')}")
                    print(f"   📂 Category: {created_incident.get('category', 'N/A')}")
                    print(f"   👤 Assigned to: {created_incident.get('assigned_to', 'N/A')}")
                    print(f"   📅 Created: {created_incident.get('sys_created_on', 'N/A')}")
                else:
                    print("⚠️  Incident details could not be retrieved (empty response)")
            except Exception as fetch_error:
                print(f"⚠️  Could not fetch incident details: {str(fetch_error)}")
                print("   (Incident was created successfully, but details retrieval failed)")
            
            print(f"\n🎉 Demo completed successfully!")
            print(f"   Your incident has been created and is ready for use.")
            
        else:
            print("❌ Failed to create incident")
            print(f"   Response: {response}")
            
    except Exception as e:
        print(f"❌ Error occurred: {str(e)}")
        print("\n💡 Troubleshooting tips:")
        print("   - Verify your ServiceNow URL is correct")
        print("   - Check your username and password")
        print("   - Ensure you have permission to create incidents")
        print("   - Check if your instance allows API access")
        return 1
    
    return 0


if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)
