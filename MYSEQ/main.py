from seqbio.calculation.SeqCal import gcContent, countBasesDict
from seqbio.pattern.SeqPattern import enzTargetsScan
from seqbio.seqMan.dnaconvert import *
def argparserLocal():
    from argparse import ArgumentParser

    parser = ArgumentParser(prog='myseq', description='Work with sequence' )
    subparsers = parser.add_subparsers(title='commands',description= 'Please choose command below:', dest='command')
    subparsers.required = True
    #-------------- GC Content ------------------
    cgc_command = subparsers.add_parser('gcContent',help= 'Calculate  GC content')
    cgc_command.add_argument('-s','--seq',type=str,default=None, help= "Provide Sequence")
    #-------------- countBases ------------------
    cbase_command = subparsers.add_parser('countBases', help= 'Count number of each base')
    cbase_command.add_argument('-s','--seq',type=str,default=None, help= "Provide Sequence")
    cbase_command.add_argument('-r','--revcomp',action='store_true', help= "Convert DNA to reverse-complementary")
    #-------------- transcription ------------------
    transci_command = subparsers.add_parser('transcription', help= 'Convert DNA->RNA')
    transci_command.add_argument('-s','--seq',type=str,default=None, help= "Provide Sequence")
    transci_command.add_argument('-r','--revcomp',action='store_true', help= "Convert DNA to reverse-complementary")
    #-------------- translation ------------------
    transla_command = subparsers.add_parser('translation', help= 'Convert DNA->Protein')
    transla_command.add_argument('-s','--seq',type=str,default=None, help= "Provide Sequence")
    transla_command.add_argument('-r','--revcomp',action='store_true', help= "Convert DNA to reverse-complementary")
    #-------------- enzTargetScan ------------------
    renz_command = subparsers.add_parser('enzTargetsScan', help= 'Find restriction enzyme')
    renz_command.add_argument('-s','--seq',type=str,default=None, help= "Provide Sequence")
    renz_command.add_argument('-e','--enz',type=str,default=None, help= "Enzyme name")
    renz_command.add_argument('-r','--revcomp',action='store_true', help= "Convert DNA to reverse-complementary")
    return parser
def main():
    parser = argparserLocal()
    args = parser.parse_args()
    if(args.command == "gcContent"):
        if args.seq == None:
            print("---------------\nError: You did not provide sequence input\n------------\n")
            exit(parser.parse_args(['gcContent','-h']))
        print("Input " + args.seq +'\n'+"GC content = "+str(gcContent(args.seq.upper())))
    elif(args.command == "countBases"):
        if args.seq == None:
            print("---------------\nError: You did not provide sequence input\n------------\n")
            exit(parser.parse_args(['countBases','-h']))
        if args.revcomp:
            print("Input " + args.seq +'\n'+"Count Bases = "+ str(countBasesDict(reverseComplementSeq(args.seq.upper()))))
        else:
            print("Input " + args.seq +'\n'+"Count Bases = "+ str(countBasesDict(args.seq.upper())))
    elif(args.command == "transcription"):
        if args.seq == None:
            print("---------------\nError: You did not provide sequence input\n------------\n")
            exit(parser.parse_args(['countBases','-h']))
        if args.revcomp:
            print("Input " + args.seq +'\n'+"Transcription = "+ dna2rna(reverseComplementSeq(args.seq.upper())))
        else:
            print("Input " + args.seq +'\n'+"Transcription = "+ dna2rna(args.seq.upper()))
    elif(args.command == "translation"):
        if args.seq == None:
            print("---------------\nError: You did not provide sequence input\n------------\n")
            exit(parser.parse_args(['countBases','-h']))
        if args.revcomp:
            print("Input " + args.seq +'\n'+"Translation = "+ dna2protein(reverseComplementSeq(args.seq.upper())))
        else:
            print("Input " + args.seq +'\n'+"Translation = "+ dna2protein(args.seq.upper()))

        
    elif(args.command == "enzTargetsScan"):
        if args.seq == None:
            print("---------------\nError: You did not provide sequence input\n------------\n")
            exit(parser.parse_args(['enzTargetsScan','-h']))
        if args.enz == None:
            print("---------------\nError: You did not provide Target Enzyme \n------------\n")
            exit(parser.parse_args(['enzTargetsScan','-h']))
        if args.revcomp:
            print("Input " + args.seq +'\n' + args.enz +' sites = '+str(enzTargetsScan(reverseComplementSeq(args.seq.upper()),args.enz)))
        else:
            print("Input "+ args.seq + '\n' + args.enz +' sites = '+str(enzTargetsScan(args.seq.upper(),args.enz)))
if __name__ == "__main__":
    main()