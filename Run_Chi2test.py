import ROOT
import yaml
import csv

def read_config(config_file):
    """
    read YAML configuration
    """
    with open(config_file, 'r') as file:
        config = yaml.safe_load(file)
    return config

# Load configuration from YAML file                                                                                                                                                           
config = read_config('configStat.yaml')

# Extract configuration values                                                                                                                                                                
root_file_name = config['root_file']
nominal_hist_name = config['nominal_histogram']
distribution_for_test = config['distribution']
histograms_to_compare = config.get('histograms_to_compare', [])
output_csv =  f"outputChi2_{distribution_for_test}.csv"

# Open the ROOT file                                                                                                                                                                          
file = ROOT.TFile.Open(root_file_name)

# Retrieve the nominal histogram
print(f"Nominal is hist_{distribution_for_test}_{nominal_hist_name}")
nominal_hist = file.Get(f"hist_{distribution_for_test}_{nominal_hist_name}")

# Check if the nominal histogram exists
if not nominal_hist:
    print(f"Nominal histogram '{nominal_hist_name}' not found in file")
    exit(1)

# Generate pseudodata using the expected values
pseudodata_hist = nominal_hist.Clone()
pseudodata_hist.Reset()
pseudodata_hist.FillRandom(nominal_hist, int(nominal_hist.Integral()*10_000_000)) # Fixed cross-section of 10 ab-1

# Open CSV file for writing
with open(output_csv, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    # Write CSV header
    csvwriter.writerow(['Wmass', 'Chi2',' Pvalue'])
    
    # Loop over all histograms you want to compare nominal to
    for hist_name in histograms_to_compare:
        hist = file.Get(f"hist_{distribution_for_test}_{hist_name}")
        
        if not hist:
            print(f" Histogram 'hist_{distribution_for_test}_{hist_name}' not found in file")
            continue
         
        chi2 = pseudodata_hist.Chi2Test(hist, "UW CHI2")
        p_value = pseudodata_hist.Chi2Test(hist, "UW P")
        
        csvwriter.writerow([hist_name, chi2, p_value])
        # Print results                                                                                                                                                                       
        print(f"Comparing pseudodata histogram (hist_{distribution_for_test}_{nominal_hist_name}) with 'hist_{distribution_for_test}_{hist_name}':")
        print(f"Chi2: {chi2}")
        print(f"p-value: {p_value}")
        
# Close the file                                                                                                                                                                              
file.Close()
