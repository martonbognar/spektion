import api.parsers.fls980
import api.analysis

file_name = input("Enter csv file name: ")
data = api.parsers.fls980.read_csv(file_name)
result = api.analysis.stern_volmer(1.0, 0.5, data)

print(result)
