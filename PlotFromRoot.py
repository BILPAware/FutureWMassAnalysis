import ROOT
import argparse

from analysis import config
from analysis import Sample
from analysis import ExampleAnalysis

from kkconfig import runconfig

from kkroot import style
from kkroot import canvas

def plot_and_save(*args, ratio=None):
    """
    Creates a THStack to overlay the histograms inside `*args, draws the
    stack on a canvas, and saves the plot as a PNG file.
    """

    #
    # Get a list of histograms

    hnames=filter(lambda key: key.startswith('hist'), dir(args[0]))
    
    for hname in hnames:
        print(f'Plotting {hname}')
        # Create a canvas
        c = ROOT.TCanvas()
        if ratio is None:
            pad,pad_ratio = c,None
        else:
            pad,pad_ratio = canvas.apply_ratio_canvas_style(c)

        # Create THStack
        hs = ROOT.THStack(f"hs_{hname}", '')
        hs_ratio = ROOT.THStack(f"hs_ratio_{hname}", '')

        exhist=getattr(args[0],hname)

        # Get reference histogram for ratios
        h_ref = getattr(args[ratio.get('reference',0)], hname) if ratio is not None else None

        # Create and style the histogram
        for histobj in args:
            # Add and style histogram
            hist=getattr(histobj, hname)
            style.style(hist,**histobj.style)
            hs.Add(hist, 'HIST')

            # Add the ratio plot
            if h_ref is not None:
                hrat=hist.Clone()
                hrat.Divide(h_ref)
                hs_ratio.Add(hrat, 'HIST')

        # Draw stack
        pad.cd()
        hs.Draw("nostack")
        hs.GetXaxis().SetTitle(exhist.GetXaxis().GetTitle())
        hs.GetYaxis().SetTitle(exhist.GetYaxis().GetTitle())
        pad.BuildLegend()
        pad.Update()

        # Draw ratio (if requested)
        if pad_ratio is not None:
            pad_ratio.cd()
            hs_ratio.Draw("nostack")
            hs_ratio.GetXaxis().SetTitle(exhist.GetXaxis().GetTitle())
            canvas.apply_ratio_axis_style(hs_ratio)

            style.style(hs_ratio, **ratio)

            pad_ratio.Update()

        # Save the canvas as a PNG file
        c.SaveAs(f'{hname}.png')

def main(runconfig_path):
    """
    Main function to read tree contents, create distributions, and plot/save 
    the histograms.
    """

    runcfg=runconfig.load([runconfig_path])

    samples=[]
    for input in runcfg.get('inputs',[]):

        sample=Sample.Sample(input.get('title',''))

        path=input.get('path',[])
        if type(path) is not list:
            path=[path]

        for p in path:
            sample.add_file(p)
        sample.style=input.get('style', {})
        sample.open()

        samples.append(sample)

    analysis=ExampleAnalysis.ExampleAnalysis()

    hists=map(analysis.run, samples)

    plot_and_save(*list(hists), ratio=runcfg.get('ratio', None))

if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(description="script that reads root files to create and plot distributions.")
    parser.add_argument("runconfig", type=str, help="Path to the run configuration YAML file.")

    ROOT.gInterpreter.AddIncludePath(f"{config.mg5amcnlo}/Delphes");
    ROOT.gInterpreter.AddIncludePath(f"{config.mg5amcnlo}/Delphes/external");

    ROOT.gSystem.Load(f'{config.mg5amcnlo}/Delphes/libDelphes.so')
    
    # Parse the arguments
    args = parser.parse_args()

    # Execute the main function with the provided arguments
    main(args.runconfig)
