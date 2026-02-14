# UPS Load Optimization

ups_capacity = 100  # kVA

loads = {
    "Server": 30,
    "Lighting": 15,
    "HVAC": 40,
    "CCTV": 10,
    "NonCritical": 20
}

total_load = sum(loads.values())
print("Total Load:", total_load)

if total_load > ups_capacity:
    print("Overload! Removing non-critical load")
    loads.pop("NonCritical")

print("Optimized Load:", sum(loads.values()))
