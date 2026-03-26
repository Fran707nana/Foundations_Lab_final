attack_count = 0
with open("auth_audit.log", "r") as log_file:
    with open("brute_report.txt", "w") as report_file:
	# The Conveyor Belt:
        for line in log_file:
            # The X-Ray (Looking for the fingerprint):
            if "Failed password" in line:
                # The Action:
                report_file.write(line)
                attack_count = attack_count + 1


# The Final Briefing (Flush against the left wall):
print("Analysis Complete.")
print("Total Brute Force Attempts Found:", attack_count)
