# HostVDS Availability Checker 🖥️

A Python script that continuously monitors HostVDS server availability and alerts you when VPS servers in Paris become available.

## 🎯 Overview

This tool automatically checks the availability of HostVDS virtual private servers (VPS) in specific regions and plays an audible alert when servers matching your criteria become available. Perfect for getting servers during high-demand periods when they're frequently out of stock.

## ✨ Features

- **🔔 Real-time Alerts**: Plays sound notification when Paris servers are available
- **⚡ High-Frequency Checks**: Monitors every 0.5 seconds for instant detection
- **🎯 Smart Filtering**: Checks multiple availability conditions
- **�️ Paris-Focused**: Specifically monitors Paris datacenter
- **🛡️ Error Resilient**: Silent error handling for network issues
- **🔄 Continuous Monitoring**: Runs indefinitely until manually stopped
- **🌐 API Integration**: Uses official HostVDS regions API

## 🛠️ Requirements

- Python 3.6+
- `requests` library
- `playsound` library
- Internet connection

## 📦 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/hostvds-checker.git
cd hostvds-checker
```

### 2. Install Dependencies
```bash
pip install requests playsound
```

### 3. Add Alert Sound
Place an MP3 file named `beep.mp3` in the project directory for the alert sound.

## 🚀 Usage

### Basic Usage
```bash
python checker.py
```

### What the Script Does:
1. **Starts continuous monitoring** of HostVDS API
2. **Checks every 0.5 seconds** for server availability
3. **Filters for Paris servers** that meet all conditions:
   - Server is available (`is_available`)
   - Not out of stock (`is_out_of_stock`)
   - Not in maintenance (`is_maintenance`)
   - Not read-only (`is_read_only`)
   - Has available IPv4 addresses (`available_ips_v4`)
   - Located in Paris (`city_code` = "paris")
4. **Plays beep sound** when matching servers are found
5. **Prints notification** to console

### Example Output
```
Region paris meets the conditions.
🔊 *beep sound plays*
```

## 📁 Project Structure

```
hostvds-checker/
├── checker.py          # Main monitoring script
├── beep.mp3           # Alert sound file
├── requirements.txt   # Python dependencies
└── README.md         # Documentation
```

## ⚙️ Configuration

### API Endpoint
Uses HostVDS official API:
```
GET https://hostvds.com/api/regions/
```

### Current Filter Criteria
The script looks for servers that meet ALL conditions:
- ✅ `is_available`: True
- ❌ `is_out_of_stock`: False
- ❌ `is_maintenance`: False
- ❌ `is_read_only`: False
- ✅ `available_ips_v4`: > 0
- ✅ `city_code`: "paris"

## 🔧 Customization

### Modify Check Interval
Change the sleep time in the main loop:
```python
time.sleep(1)  # Check every 1 second instead of 0.5
```

### Monitor Different Regions
Change the region filter in the condition:
```python
region.get("city_code") in {"paris", "london", "frankfurt"}
```

### Add Additional Filters
Extend the filtering conditions:
```python
if (
    region.get("is_available") and
    not region.get("is_out_of_stock") and
    # Add more conditions here
    region.get("available_ips_v4", 0) > 5  # Minimum 5 IPs available
):
```

### Custom Alert Sound
Replace `beep.mp3` with any MP3 file of your choice.

## 🏗️ How It Works

### 1. API Request
- Sends GET request to HostVDS regions API
- 1-second timeout to prevent hanging

### 2. Response Processing
- Parses JSON response containing all regions
- Applies filter conditions to each region

### 3. Alert System
- Plays sound when conditions are met
- Prints console notification
- Continues monitoring

### 4. Error Handling
- Silently handles connection errors
- Continues monitoring after failures
- No console spam from expected errors

## ⚠️ Important Notes

### Rate Limiting
- **Current interval**: 0.5 seconds between checks
- **Consider increasing** to 1-2 seconds for extended use
- **Respect the API** - avoid excessive requests

### Server Availability
- HostVDS servers, especially in Paris, are often out of stock
- This tool helps catch brief availability windows
- Be ready to purchase quickly when alerted

### Network Requirements
- Stable internet connection required
- Script handles temporary network issues gracefully
- May need to run for extended periods to catch availability

## 🐛 Troubleshooting

### Common Issues

1. **No Sound Alert**
   ```
   Error: beep.mp3 not found
   ```
   **Solution**: Ensure `beep.mp3` exists in the same directory

2. **No Servers Found**
   - Paris servers are frequently out of stock
   - Run the script during business hours or server maintenance periods
   - Consider monitoring multiple regions

3. **Connection Errors**
   - Script silently handles connection issues
   - Will automatically retry on next iteration
   - Check your internet connection if persistent

4. **Module Not Found**
   ```
   ModuleNotFoundError: No module named 'playsound'
   ```
   **Solution**: Install missing dependencies: `pip install playsound`

### Debug Mode
Add verbose output to see all regions and their status:
```python
print(f"Checking {region.get('city_code')} - Available: {region.get('is_available')} - Stock: {region.get('is_out_of_stock')}")
```

## 🔒 Privacy & Security

- **No Authentication**: Uses public API endpoint
- **No Personal Data**: Doesn't store or transmit personal information
- **Local Execution**: All processing happens on your machine

## 🤝 Contributing

Contributions welcome! Here's how:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/improvement`)
3. **Commit** changes (`git commit -m 'Add new feature'`)
4. **Push** to branch (`git push origin feature/improvement`)
5. **Open** a Pull Request

### Potential Enhancements
- Multiple region monitoring
- Email/SMS notifications
- Web interface
- Historical availability tracking
- Auto-purchase integration
- Multiple sound alerts for different regions

## 👥 Author

- **Mohammad Fazel Samavati** - [m-fazel](https://github.com/m-fazel)

## 🙏 Acknowledgments

- **HostVDS** for the VPS hosting service and API
- **Python requests** library for API calls

## 🆘 Support

If you encounter issues:

1. Check the troubleshooting section above
2. Ensure all dependencies are installed
3. Verify your internet connection
4. Check that the `beep.mp3` file exists

---

**Happy server hunting!** 🖥️🎯

*Note: This tool is for availability monitoring only. Actual purchase must be done through the HostVDS website.*