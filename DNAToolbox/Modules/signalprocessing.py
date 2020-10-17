import Bio
from Bio.Seq import Seq
import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plot

s= 'ACGTATGCACTAAGTCATGCTAATGCTCTATATACATTCTATGTATAATGAGCATAAATTTAATTTCCCCACGTAACATATTTTATGGTTATATACATTCTATGTATAATGAGCATAAATTTAATTTCCCCACGAATAATATTTACAATTAAACATCAAGAATTCAACAATTTATAAAATTTATTACAAACATTAAATAACTAAAACTGAGCAAATCAATCTTTATAACATGTATAATAAACTAAATATATAATTATTTATAACCATATTATTATGAAAACATACAAGAAAATATAATTTTACATTAATCTATTTCAAACATTAATATCATAACACATATATATGAAGACTTAACATTTAACATATAAATCTCACACCAATAATTTCTCAATAAACATAATATTTTTACAAACAATTTCTATGTAACTTTAATTCTCTATATAAAGTATATGTTAACCATAACGGTAAAAAAATAATATATCAAGCATACATCCCCAACACTACAACAATAAAATCAACCAAAATATAATTAACCTCATTTCTCTCGCATATCTGTATAATAACCATTATAACACATCAGTTACATAATAACTTATTTCTTCAAAGAAAATGAATGCATGAACACATACTTTAATA'


class SignalProcessorScreen(tk.Frame):
    def __init__(self, parent, controller):

        ### INTERFAZ
    
        tk.Frame.__init__(self, parent)
        self.controller = controller
        title_label = tk.Label(self, text="Signal processing kit")
        title_label.grid(column = 0, row = 0)
        return_button = tk.Button(self, text="Back to main menu",
                           command=lambda: controller.show_frame("StartPage"))
        return_button.grid(column = 1, row = 0)

        self.columnconfigure(0, weight = 0)
        self.columnconfigure(1, weight = 1)
        self.rowconfigure(0, weight = 0)
        self.rowconfigure(1, weight = 1)

        self.leftpanel = tk.Frame(self, borderwidth = 5, relief = tk.RIDGE)
        #self.rightpanel = tk.Frame(self)

        self.leftpanel.grid(column = 0, row =1, sticky=(tk.N, tk.W, tk.S))
        #self.rightpanel.grid(column = 1, row =1, sticky=(tk.N, tk.S, tk.E, tk.W))

        ######### DATA FOR SIGNAL PROCESSING
        self.testseq = Seq(s)
        self.numSeq = np.array
        #  Array containing the numerical representation
        self.codingScheme = 'justa'

        self.samplingFrequency = 1
        #  The sampling frequency (samples per time unit).
        #  It is used to calculate the Fourier frequencies, freqs,
        #  in cycles per time unit. The default value is 1

        self.NFFT = 256 
        #  The length of the windowing segments
        #  The number of data points used in each block for the FFT. 
        #  A power 2 is most efficient. The default value is 256. 
        #  This should NOT be used to get zero padding,

        self.scale_by_freq = True
        #  Specifies whether the resulting density values should be scaled
        #  by the scaling frequency, which gives density in units of Hz^-1.
        #  This allows for integration over the returned frequency values.
        #  The default is True for MATLAB compatibility.

        self.mode = tk.StringVar()
        #   {'default', 'psd', 'magnitude', 'angle', 'phase'}
        #   What sort of spectrum to use. Default is 'psd', which takes the power spectral density.
        #  'magnitude' returns the magnitude spectrum.
        #  'angle' returns the phase spectrum without unwrapping.
        #  'phase' returns the phase spectrum with unwrapping.

        self.sides = tk.StringVar()
        #  {'default', 'onesided', 'twosided'}
        #  Specifies which sides of the spectrum to return.
        #  Default gives the default behavior, which returns one-sided
        #  for real data and both for complex data.

    
        self.codingSchemes = ('EEIP', 'Integrer', 'PP','Real',
                                'Atomic', 'AC_TG', 'codons', 'doublet',
                                'Just A', 'Just T', 'Just G', 'Just C')
        self.drawLeftPanel()


    ################ INTERFAZ

    def drawLeftPanel(self):
        
        for widget in self.leftpanel.winfo_children():
            widget.destroy()
        
        #NFFT
        NFFT_label = tk.Label(self.leftpanel, text = "NFFT:", pady = 5)
        NFFT_label.grid(row=0, column = 0)

        NFFT_entry = tk.Entry(self.leftpanel, width = 10)
        NFFT_entry.grid(row = 0, column = 1)

        #Sampling Frequency
        SF_label = tk.Label(self.leftpanel, text = "Sampling Frequency", pady = 5)
        SF_label.grid(row=1, column = 0)

        NFFT_entry = tk.Entry(self.leftpanel, width = 10)
        NFFT_entry.grid(row = 1, column = 1)

        #sides
        sides_label = tk.Label(self.leftpanel, text = "Sides:", pady = 5)
        sides_label.grid(row=5, column = 0)

        self.sides.set("default")
        sides_default = ttk.Radiobutton(self.leftpanel, text='Default', variable=self.sides, value='default')
        sides_onesided = ttk.Radiobutton(self.leftpanel, text='One side', variable=self.sides, value='onesided')
        sides_twosided = ttk.Radiobutton(self.leftpanel, text='Two sides', variable=self.sides, value='twosided')

        sides_default.grid(row = 5, column =1)
        sides_onesided.grid(row = 6, column =1)
        sides_twosided.grid(row = 7, column =1)

        #mode
        mode_label = tk.Label(self.leftpanel, text = "Mode:", pady = 5)
        mode_label.grid(row=5, column = 3)

        self.mode.set("psd")
        mode_default = ttk.Radiobutton(self.leftpanel, text='default (psd)', variable=self.mode, value='psd')
        mode_magnitude = ttk.Radiobutton(self.leftpanel, text='magnitude', variable=self.mode, value='magnitude')
        mode_angle = ttk.Radiobutton(self.leftpanel, text='angle', variable=self.mode, value='angle')
        mode_phase = ttk.Radiobutton(self.leftpanel, text='phase', variable=self.mode, value='phase')

        mode_default.grid(row = 5, column =4)
        mode_magnitude.grid(row = 6, column =4)
        mode_angle.grid(row = 7, column =4)
        mode_phase.grid(row = 8, column =4)

        #scalebyfreq
        scale_by_freq_check = tk.Checkbutton(self.leftpanel, text='Use Metric',
                    variable=self.scale_by_freq,
	                onvalue=True, offvalue=False)
        scale_by_freq_check.grid(row = 0, column = 3)

        #coding scheme
        
        scheme_label = tk.Label(self.leftpanel, text = "Coding Scheme:", pady = 5)
        scheme_label.grid(row=50, column = 3)

        scheme_combo = ttk.Combobox(self.leftpanel, textvariable=self.codingScheme)
        scheme_combo['values'] = self.codingSchemes
        scheme_combo.state(["readonly"])
        scheme_combo.set("EEIP")
        scheme_combo.grid(row = 50 , column=4)
        
        # --- RUN BUTTON
        run_process_button = tk.Button(self.leftpanel, text = "Run signal analysis",
                            pady = 5, command = lambda: self.run())
        run_process_button.grid(row=50, column = 0, sticky = (tk.S))

    ######### FUNCTIONS FOR SIGNAL PROCESSING
    def run(self):
        self.code(self.codingScheme)
        self.spectrogram()

    def spectrogram(self):
        plot.subplot()
        powerSpectrum, freqenciesFound, time, imageAxis = plot.specgram(
        x = self.numSeq,
        NFFT=self.NFFT,
        Fs=self.samplingFrequency,
        mode = self.mode.get(),
        sides= self.sides.get(),
        scale_by_freq=self.scale_by_freq,)
        plot.xlabel('Sampleset')
        plot.ylabel('Frequency')
        plot.show()

    def code(self, mode):
        self.code_EIIP()


    ########## CODING SCHEMES

    # electron ion interaction potential 
    def code_EIIP(self):
        self.numSeq = np.zeros(len(self.testseq),'double')
        for k in range(len(self.testseq)):
            t = self.testseq[k]
            if t == 'A':
                self.numSeq[k] = 0.1260
            if t == 'C':
                self.numSeq[k] = 0.1340
            if t == 'G':
                self.numSeq[k] = 0.0806
            if t == 'T':
                self.numSeq[k] = 0.1335
    
    # int for different values
    def code_integrer(self):
        self.numSeq = np
        self.numSeq = np.zeros(len(self.testseq),'double')
        bases = ('T','C','A','G')

        for k in range(len(self.testseq)):
            t = self.testseq[k]
            for i,b in enumerate(bases):
                if b == t: self.numSeq[k] = i
        #esto es asqueroso, seguro se puede hacer mejor en python

    # 1 for base, 0 for others
    def code_just_letter(self, base):
        self.numSeq = np
        self.numSeq = np.zeros(len(self.testseq),'double')
        for k in range(len(self.testseq)):
            t = self.testseq[k]
            if t == base: self.numSeq[k] = 1 
            else: self.numSeq[k] = 0

    # purine/pirimidine
    def code_PP(self):
        self.numSeq = np.zeros(len(self.testseq),'double')
        for k in range(len(self.testseq)):
            t = self.testseq[k]
            if t == 'A':
                self.numSeq[k] = -1
            if t == 'C':
                self.numSeq[k] = 1
            if t == 'G':
                self.numSeq[k] = -1
            if t == 'T':
                self.numSeq[k] = 1

    # purine/pirimidine
    def code_Real(self):
        self.numSeq = np.zeros(len(self.testseq),'double')
        for k in range(len(self.testseq)):
            t = self.testseq[k]
            if t == 'A':
                self.numSeq[k] = -1.5
            if t == 'C':
                self.numSeq[k] = 0.5
            if t == 'G':
                self.numSeq[k] = -0.5
            if t == 'T':
                self.numSeq[k] = 1.5
    
    # atomic number
    def code_Atomic(self):
        self.numSeq = np.zeros(len(self.testseq),'double')
        for k in range(len(self.testseq)):
            t = self.testseq[k]
            if t == 'A':
                self.numSeq[k] = 70
            if t == 'C':
                self.numSeq[k] = 58
            if t == 'G':
                self.numSeq[k] = 78
            if t == 'T':
                self.numSeq[k] = 66


    # AT-CG
    def code_AC_TG(self):
        self.numSeq = np.zeros(len(self.testseq),'double')
        for k in range(len(self.testseq)):
            t = self.testseq[k]
            if t == 'A':
                self.numSeq[k] = 1
            if t == 'C':
                self.numSeq[k] = -1
            if t == 'G':
                self.numSeq[k] = -1
            if t == 'T':
                self.numSeq[k] = 1

    def code_codons(self):
        self.numSeq = np.zeros(len(self.testseq),'double')        
        codons = ('TTT','TTC','TTA','TTG','CTT','CTC','CTA','CTG','TCT','TCC','TCA','TCG','AGT','AGC','TAT','TAC',
                'TAA','TAG','TGA','TGT','TGC','TGG','CCT','CCC','CCA','CCG','CAT','CAC','CAA','CAG','CGT','CGC',
                'CGA','CGG','AGA','AGG','ATT','ATC','ATA','ATG','ACT','ACC','ACA','ACG','AAT','AAC','AAA','AAG',
                'GTT','GTC','GTA','GTG','GCT','GCC','GCA','GCG','GAT','GAC','GAA','GAG','GGT','GGC','GGA','GGG')
        for k in range(len(self.testseq)-2):
            t = self.testseq[k:k+2]
            self.numSeq[k] = codons.index(t)


    def code_doublet(self):
        self.numSeq = np.zeros(len(self.testseq),'double')        
        doublet = ('AA','AT','TA','AG','TT','TG','AC','TC','GA','CA','GT','GG','CT','GC','CG','CC')
        for k in range(len(self.testseq)-1):
            t = self.testseq[k:k-1]
            self.numSeq[k] = doublet.index(t)


if __name__ == "__main__":
    pass

