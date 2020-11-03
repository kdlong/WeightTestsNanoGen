import DataFormats.FWLite as fwlite
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("rtfile", type=str, help="EDM file")
args = parser.parse_args()

if "/store" in args.rtfile[:6]:
    args.rtfile = "root://cms-xrd-global.cern.ch/"+args.rtfile

lumis = fwlite.Lumis(args.rtfile)
handle = fwlite.Handle("GenLumiInfoHeader")
lumis.getByLabel("generator", handle)
genlumi = handle.product()
print "Length of weight names is", len(genlumi.weightNames())