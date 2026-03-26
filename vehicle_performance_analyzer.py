import matplotlib.pyplot as plt

print("Vehicle Performance Analyzer")

try:
    mass = float(input("Enter vehicle mass (kg): "))

    if mass <= 0:
        print("Mass must be greater than zero.")
    else:
        times = []
        forces = []
        accelerations = []

        print("\nEnter vehicle data over time.")
        print("Time: seconds (s)")
        print("Force: applied force in Newtons (N)")
        print("Example: 0,1000 means at time 0s, force = 1000N")
        print("Type 'stop' when finished.\n")

        while True:
            user_input = input("Enter (time, force): ")

            if user_input.lower() == "stop":
                break

            try:
                time_str, force_str = user_input.split(",")

                time_value = float(time_str.strip())
                force_value = float(force_str.strip())

                if force_value <= 0:
                    print("Force must be greater than zero.")
                    continue

                acceleration = force_value / mass

                times.append(time_value)
                forces.append(force_value)
                accelerations.append(acceleration)

            except:
                print("Invalid format. Use: time,force")

        print("\nTimes:", times)
        print("Forces:", forces)
        print("Accelerations:", accelerations)

        plt.figure(figsize=(8,5))
        plt.plot(times, accelerations, marker="o", linestyle="-", label="Acceleration")
        plt.xlabel("Time (s)")
        plt.ylabel("Acceleration (m/s^2)")
        plt.title("Vehicle Acceleration Analysis (F = ma Model)")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()

        plt.savefig("acceleration_vs_time.png", dpi =300)
        plt.show()

except ValueError:
    print("Invalid input. Please enter numeric values only.")
    
#2000
#0,500
#1,1200
#2,2000
#3,2800
#4,3200
#5,3500
#6,3600

