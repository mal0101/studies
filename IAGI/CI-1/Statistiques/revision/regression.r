

# Define the path to the data file
file_path <- paste0("/Users/malakmekyassi/Documents/GitHub/studies/",
					"IAGI/CI-1/Statistiques/revision/ozone.txt")

# Import the data
ozone_data <- read.table(file_path, header = TRUE, sep = "\t")

# Display the first few rows of the data
head(ozone_data)

# Check the column names of the data
print(colnames(ozone_data))
# plot(maxO3 ~ T12, data = ozone_data)
reg_simple <- lm(maxO3 ~ T12, data = ozone_data)