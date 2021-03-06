import FWCore.ParameterSet.Config as cms
import os
def customise(process):

  slhacontent = """# NMSSMTools OUTPUT IN SLHA FORMAT
# Info about spectrum calculator
BLOCK SPINFO   # Program information
     1   NMSSMTools # Spectrum calculator
     2   3.2.0      # Version number
     8   1          # Higgs mass precision
     3   # Muon magn. mom. more than 2 sigma away
# Input parameters
BLOCK MODSEL
    3     1         # NMSSM PARTICLE CONTENT
BLOCK SMINPUTS
     1     1.27920000E+02   # ALPHA_EM^-1(MZ)
     2     1.16639000E-05   # GF
     3     1.17200000E-01   # ALPHA_S(MZ)
     4     9.11870000E+01   # MZ
     5     4.20000000E+00   # MB(MB)
     6     1.73300000E+02   # MTOP (POLE MASS)
     7     1.77700000E+00   # MTAU
# SMINPUTS Beyond SLHA:
# MW:     0.80420000E+02
# MS:     0.19000000E+00
# MC:     0.14000000E+01
# VUS:     0.22000000E+00
# VCB:     0.40000000E-01
# VUB:     0.40000000E-02
BLOCK MINPAR
     3     2.60000000E+00   # TANBETA(MZ)
BLOCK EXTPAR
     1     3.00000000E+02   # M1
     2     6.00000000E+02   # M2
     3     1.00000000E+03   # M3
    11     1.15244910E+03   # ATOP
    12     1.15244910E+03   # ABOTTOM
    13     1.15244910E+03   # ATAU
    16     1.15244910E+03   # AMUON
    31     1.00000000E+03   # LEFT SELECTRON
    32     1.00000000E+03   # LEFT SMUON
    33     1.00000000E+03   # LEFT STAU
    34     1.00000000E+03   # RIGHT SELECTRON
    35     1.00000000E+03   # RIGHT SMUON
    36     1.00000000E+03   # RIGHT STAU
    41     1.00000000E+03   # LEFT 1ST GEN. SQUARKS
    42     1.00000000E+03   # LEFT 2ND GEN. SQUARKS
    43     1.00000000E+03   # LEFT 3RD GEN. SQUARKS
    44     1.00000000E+03   # RIGHT U-SQUARKS
    45     1.00000000E+03   # RIGHT C-SQUARKS
    46     1.00000000E+03   # RIGHT T-SQUARKS
    47     1.00000000E+03   # RIGHT D-SQUARKS
    48     1.00000000E+03   # RIGHT S-SQUARKS
    49     1.00000000E+03   # RIGHT B-SQUARKS
    61     6.00000000E-01   # LAMBDA
    62     1.20000000E-01   # KAPPA
    63    -5.10000000E+02   # ALAMBDA
    64     2.53576314E+02   # AKAPPA
    65    -2.00000000E+02   # MUEFF
# 
BLOCK MASS   # Mass spectrum 
#  PDG Code     mass             particle 
        25     2.50000000E+01   # lightest neutral scalar
        35     1.25300000E+02   # second neutral scalar
        45     5.76499745E+02   # third neutral scalar
        36     1.92965093E+02   # lightest pseudoscalar
        46     5.77284011E+02   # second pseudoscalar
        37     5.65383345E+02   # charged Higgs
   1000001     1.03816356E+03   #  ~d_L
   2000001     1.03719659E+03   #  ~d_R
   1000002     1.03601090E+03   #  ~u_L
   2000002     1.03654529E+03   #  ~u_R
   1000003     1.03816356E+03   #  ~s_L
   2000003     1.03719659E+03   #  ~s_R
   1000004     1.03601090E+03   #  ~c_L
   2000004     1.03654529E+03   #  ~c_R
   1000005     1.03575995E+03   #  ~b_1
   2000005     1.03959997E+03   #  ~b_2
   1000006     9.60281557E+02   #  ~t_1
   2000006     1.12699626E+03   #  ~t_2
   1000011     1.00077837E+03   #  ~e_L
   2000011     1.00067504E+03   #  ~e_R
   1000012     9.98544999E+02   #  ~nue_L
   1000013     1.00077837E+03   #  ~mu_L
   2000013     1.00067504E+03   #  ~mu_R
   1000014     9.98544999E+02   #  ~numu_L
   1000015     9.99245790E+02   #  ~tau_1
   2000015     1.00220859E+03   #  ~tau_2
   1000016     9.98544999E+02   #  ~nutau_L
   1000021     1.07902758E+03   #  ~g
   1000022    -9.78138073E+01   # neutralino(1)
   1000023    -2.27083370E+02   # neutralino(2)
   1000025     2.27948047E+02   # neutralino(3)
   1000035     3.03709218E+02   # neutralino(4)
   1000045     6.21809001E+02   # neutralino(5)
   1000024    -2.07786084E+02   # chargino(1)
   1000037     6.21777058E+02   # chargino(2)
# 
# Low energy observables
BLOCK LOWEN
# Exp. 2 Sigma: 3.03E-04 < BR(b -> s gamma) < 4.01E-04:
     1     3.63716677E-04   # BR(b -> s gamma)
    11     4.02140234E-04   # (BR(b -> s gamma)+Theor.Err.)
    12     3.05626684E-04   # (BR(b -> s gamma)-Theor.Err.)
# Exp. 2 Sigma: 4.99E-01 < Delta M_d < 5.15E-01:
     2     6.23719593E-01   # Delta M_d in ps^-1
    21     1.08925620E+00   # Delta M_d +Theor.Err.
    22     1.67319352E-01   # Delta M_d -Theor.Err.
# Exp. 2 Sigma: 1.753E+01 < Delta Ms < 1.801E+01:
     3     2.16089907E+01   # Delta M_s in ps^-1
    31     2.85163143E+01   # Delta M_s +Theor.Err.
    32     1.48347615E+01   # Delta M_s -Theor.Err.
# Exp. 95% C.L.: BR(Bs->mu+mu-) < 4.5E-09:
     4     3.66139545E-09   # BR(Bs -> mu+mu-)
    41     6.21881125E-09   # BR(Bs -> mu+mu-)+Theor.Err.
    42     1.77736296E-09   # BR(Bs -> mu+mu-)-Theor.Err.
# Exp. 2 Sigma: 8.90E-05 < BR(B+ > tau+ + nu_tau) < 2.45E-04:
     5     1.31637611E-04   # BR(B+ -> tau+ + nu_tau)
    51     2.63326712E-04   # BR(B+ -> tau+ + nu_tau) + Theor.Err.
    52     5.68116338E-05   # BR(B+ -> tau+ + nu_tau) - Theor.Err.
# BSM contr. to the muon anomalous magn. moment:
     6    -7.72307347E-11   # Del_a_mu
    61     2.07305268E-10   # Del_a_mu + Theor.Err.
    62    -3.61766737E-10   # Del_a_mu - Theor.Err.
# Minimal Exp.-SM (2 sigma):  8.77306222E-10
# Maximal Exp.-SM (2 sigma):  4.61144414E-09
# 
BLOCK HMIX Q=  1.00000000E+03 # (STOP/SBOTTOM MASSES)
     1    -2.00000000E+02   # MUEFF
     2     2.57525562E+00   # TAN(BETA)
     3     2.41822895E+02   # V(Q)
     4     3.25992325E+05   # MA^2
     5     4.23278013E+04   # MP^2
# 
# 3*3 Higgs mixing
BLOCK NMHMIX
  1  1    -1.10229927E-01   # S_(1,1)
  1  2     9.11764186E-02   # S_(1,2)
  1  3     9.89715224E-01   # S_(1,3)
  2  1     3.71533478E-01   # S_(2,1)
  2  2     9.27373795E-01   # S_(2,2)
  2  3    -4.40535945E-02   # S_(2,3)
  3  1     9.21852612E-01   # S_(3,1)
  3  2    -3.62856315E-01   # S_(3,2)
  3  3     1.36099438E-01   # S_(3,3)
# 
# 3*3 Pseudoscalar Higgs mixing
BLOCK NMAMIX
  1  1     1.40953764E-01   # P_(1,1)
  1  2     5.42129860E-02   # P_(1,2)
  1  3     9.88526937E-01   # P_(1,3)
  2  1     9.22640612E-01   # P_(2,1)
  2  2     3.54861774E-01   # P_(2,2)
  2  3    -1.51044664E-01   # P_(2,3)
# 
# 3rd generation sfermion mixing
BLOCK STOPMIX  # Stop mixing matrix
  1  1    -7.08179389E-01   # Rst_(1,1)
  1  2     7.06032544E-01   # Rst_(1,2)
  2  1    -7.06032544E-01   # Rst_(2,1)
  2  2    -7.08179389E-01   # Rst_(2,2)
BLOCK SBOTMIX  # Sbottom mixing matrix
  1  1    -6.16007858E-01   # Rsb_(1,1)
  1  2     7.87740007E-01   # Rsb_(1,2)
  2  1    -7.87740007E-01   # Rsb_(2,1)
  2  2    -6.16007858E-01   # Rsb_(2,2)
BLOCK STAUMIX  # Stau mixing matrix
  1  1    -6.94666701E-01   # Rsl_(1,1)
  1  2     7.19331756E-01   # Rsl_(1,2)
  2  1    -7.19331756E-01   # Rsl_(2,1)
  2  2    -6.94666701E-01   # Rsl_(2,2)
# 
# Gaugino-Higgsino mixing
BLOCK NMIX  # 5*5 Neutralino Mixing Matrix
  1  1    -4.40029145E-02   # N_(1,1)
  1  2     4.58056753E-02   # N_(1,2)
  1  3    -1.40922328E-02   # N_(1,3)
  1  4     4.28128247E-01   # N_(1,4)
  1  5     9.01372951E-01   # N_(1,5)
  2  1    -6.84791003E-02   # N_(2,1)
  2  2     8.00337876E-02   # N_(2,2)
  2  3    -7.08726134E-01   # N_(2,3)
  2  4     6.22764805E-01   # N_(2,4)
  2  5    -3.14287243E-01   # N_(2,5)
  3  1    -2.00332521E-01   # N_(3,1)
  3  2     6.77415257E-02   # N_(3,2)
  3  3     6.99124361E-01   # N_(3,3)
  3  4     6.16063116E-01   # N_(3,4)
  3  5    -2.94905632E-01   # N_(3,5)
  4  1     9.76225036E-01   # N_(4,1)
  4  2     3.68650304E-02   # N_(4,2)
  4  3     9.32201135E-02   # N_(4,3)
  4  4     1.87574227E-01   # N_(4,4)
  4  5    -4.18517399E-02   # N_(4,5)
  5  1    -1.50305121E-02   # N_(5,1)
  5  2     9.92747948E-01   # N_(5,2)
  5  3     6.61923090E-03   # N_(5,3)
  5  4    -1.18963645E-01   # N_(5,4)
  5  5     5.42516847E-03   # N_(5,5)
# 
BLOCK UMIX  # Chargino U Mixing Matrix
  1  1     9.83153370E-03   # U_(1,1)
  1  2    -9.99951669E-01   # U_(1,2)
  2  1     9.99951669E-01   # U_(2,1)
  2  2     9.83153370E-03   # U_(2,2)
# 
BLOCK VMIX  # Chargino V Mixing Matrix
  1  1     1.67489961E-01   # V_(1,1)
  1  2    -9.85873781E-01   # V_(1,2)
  2  1     9.85873781E-01   # V_(2,1)
  2  2     1.67489961E-01   # V_(2,2)
# 
# Higgs reduced couplings
# (as compared to a SM Higgs with same mass)
BLOCK REDCOUP
# H1
  1  1     9.76877354E-02   # U-type fermions
  1  2    -3.07065045E-01   # D-type fermions
  1  3     4.55288720E-02   # W,Z bosons
  1  4     1.76381708E-01   # Gluons
  1  5     1.56830906E-01   # Photons
# H2
  2  1     9.93601715E-01   # U-type fermions
  2  2     1.03497251E+00   # D-type fermions
  2  3     9.98933003E-01   # W,Z bosons
  2  4     9.95003391E-01   # Gluons
  2  5     9.80739552E-01   # Photons
# H3
  3  1    -3.88769511E-01   # U-type fermions
  3  2     2.56798422E+00   # D-type fermions
  3  3    -7.74454525E-03   # W,Z bosons
  3  4     3.90873519E-01   # Gluons
  3  5     1.62126172E+00   # Photons
# A1
  4  1     5.80845784E-02   # U-type fermions
  4  2     3.92651750E-01   # D-type fermions
  4  3     0.00000000E+00   # W,Z bosons
  4  4     5.03803300E-02   # Gluons
  4  5     3.15079603E-01   # Photons
# A2
  5  1     3.80204044E-01   # U-type fermions
  5  2     2.57017934E+00   # D-type fermions
  5  3     0.00000000E+00   # W,Z bosons
  5  4     3.83981580E-01   # Gluons
  5  5     3.68438393E-01   # Photons
# 
# GAUGE AND YUKAWA COUPLINGS AT THE SUSY SCALE
BLOCK GAUGE Q=  1.00000000E+03 # (SUSY SCALE)
     1     3.62459603E-01   # g1(Q,DR_bar)
     2     6.42566822E-01   # g2(Q,DR_bar)
     3     1.05976273E+00   # g3(Q,DR_bar)
BLOCK YU Q=  1.00000000E+03 # (SUSY SCALE)
  3  3     9.25551242E-01   # HTOP(Q,DR_bar)
BLOCK YD Q=  1.00000000E+03 # (SUSY SCALE)
  3  3     3.93503431E-02   # HBOT(Q,DR_bar)
BLOCK YE Q=  1.00000000E+03 # (SUSY SCALE)
  3  3     2.78125732E-02   # HTAU(Q,DR_bar)
# 
# SOFT TRILINEAR COUPLINGS AT THE SUSY SCALE
BLOCK AU Q=  1.00000000E+03 # (SUSY SCALE)
  3  3     1.15244910E+03   # ATOP
BLOCK AD Q=  1.00000000E+03 # (SUSY SCALE)
  3  3     1.15244910E+03   # ABOT
BLOCK AE Q=  1.00000000E+03 # (SUSY SCALE)
  2  2     1.15244910E+03   # AMUON
  3  3     1.15244910E+03   # ATAU
# 
# SOFT MASSES AT THE SUSY SCALE
BLOCK MSOFT Q=  1.00000000E+03 # (SUSY SCALE)
     1     3.00000000E+02   # M1
     2     6.00000000E+02   # M2
     3     1.00000000E+03   # M3
    21     2.36941814E+05   # M_HD^2
    22     2.69117786E+04   # M_HU^2
    31     1.00000000E+03   # M_eL
    32     1.00000000E+03   # M_muL
    33     1.00000000E+03   # M_tauL
    34     1.00000000E+03   # M_eR
    35     1.00000000E+03   # M_muR
    36     1.00000000E+03   # M_tauR
    41     1.00000000E+03   # M_q1L
    42     1.00000000E+03   # M_q2L
    43     1.00000000E+03   # M_q3L
    44     1.00000000E+03   # M_uR
    45     1.00000000E+03   # M_cR
    46     1.00000000E+03   # M_tR
    47     1.00000000E+03   # M_dR
    48     1.00000000E+03   # M_sR
    49     1.00000000E+03   # M_bR
# 
# NMSSM SPECIFIC PARAMETERS THE SUSY SCALE
BLOCK NMSSMRUN Q=  1.00000000E+03 # (SUSY SCALE)
     1     6.00000000E-01   # LAMBDA(Q,DR_bar)
     2     1.20000000E-01   # KAPPA(Q,DR_bar)
     3    -5.10000000E+02   # ALAMBDA
     4     2.53576314E+02   # AKAPPA
     5    -2.00000000E+02   # MUEFF
    10     6.88950449E+03   # MS^2
# 
# GAUGE AND YUKAWA COUPLINGS AT THE GUT SCALE
BLOCK GAUGE Q=  1.96152990E+16 # (GUT SCALE)
     1     7.11402404E-01   # g1(MGUT,DR_bar), GUT normalization
     2     7.11402404E-01   # g2(MGUT,DR_bar)
     3     7.02978759E-01   # g3(MGUT,DR_bar)
BLOCK YU Q=  1.96152990E+16 # (GUT SCALE)
  3  3     8.29138698E-01   # HTOP(MGUT,DR_bar)
BLOCK YD Q=  1.96152990E+16 # (GUT SCALE)
  3  3     1.80992961E-02   # HBOT(MGUT,DR_bar)
BLOCK YE Q=  1.96152990E+16 # (GUT SCALE)
  3  3     2.17551441E-02   # HTAU(MGUT,DR_bar)
# 
# SOFT TRILINEAR COUPLINGS AT THE GUT SCALE
BLOCK AU Q=  1.96152990E+16 # (GUT SCALE)
  3  3     1.03219932E+04   # ATOP
BLOCK AD Q=  1.96152990E+16 # (GUT SCALE)
  3  3     4.19765001E+03   # ABOT
BLOCK AE Q=  1.96152990E+16 # (GUT SCALE)
  2  2     2.05580582E+03   # AMUON
  3  3     2.08192180E+03   # ATAU
# 
# SOFT MASSES SQUARED AT THE GUT SCALE
BLOCK MSOFT Q=  1.96152990E+16 # (GUT SCALE)
     1     7.30616214E+02   # M1
     2     7.87545760E+02   # M2
     3     4.67968179E+02   # M3
    21     5.49987063E+06   # M_HD^2
    22     4.16597270E+07   # M_HU^2
    31     7.64565523E+05   # M_eL^2
    32     7.64565523E+05   # M_muL^2
    33     7.65648351E+05   # M_tauL^2
    34     9.24331870E+05   # M_eR^2
    35     9.24331870E+05   # M_muR^2
    36     9.26505956E+05   # M_tauR^2
    41     5.39134028E+04   # M_q1L^2
    42     5.39134028E+04   # M_q2L^2
    43     1.13848984E+07   # M_q3L^2
    44     2.54532965E+05   # M_uR^2
    45     2.54532965E+05   # M_cR^2
    46     2.33904330E+07   # M_tR^2
    47     2.57203664E+05   # M_dR^2
    48     2.57203664E+05   # M_sR^2
    49     2.61662825E+05   # M_bR^2
# 
# NMSSM SPECIFIC PARAMETERS AT THE GUT SCALE
BLOCK NMSSMRUN Q=  1.96152990E+16 # (GUT SCALE)
     1     1.14613216E+00   # LAMBDA(MGUT,DR_bar)
     2     2.70925807E-01   # KAPPA(MGUT,DR_bar)
     3     5.38560716E+03   # ALAMBDA
     4     2.99377697E+03   # AKAPPA
    10     1.15542135E+07   # MS^2
# 
# FINE-TUNING parameter d(ln Mz^2)/d(ln PS^2)
         1     3.22679269E+00   # PS=MHU
         2     4.35756548E+00   # PS=MHD
         3     1.37385654E-01   # PS=MS
         4    -4.88426936E+00   # PS=ALAMBDA
         5    -1.01132811E-01   # PS=AKAPPA
         6    -0.00000000E+00   # PS=XIF
         7    -0.00000000E+00   # PS=XIS
         8     0.00000000E+00   # PS=MUP
         9     0.00000000E+00   # PS=MSP
        10    -0.00000000E+00   # PS=M3H
        11     7.74726147E-01   # PS=LAMBDA
        12    -4.27749974E-01   # PS=KAPPA
        13     6.79516122E-01   # PS=HTOP
        14    -6.86734234E-01   # PS=G
        15     4.88426936E+00   # MAX
        16                  4   # IMAX
# 
# REDUCED CROSS SECTIONS AT LHC
        11     2.14102795E-03   # VBF -> H1 -> tautau
        12     0.00000000E+00   # ggF -> H1 -> ZZ
        13     0.00000000E+00   # ggF -> H1 -> WW
        14     8.38269250E-03   # ggF -> H1 -> gammagamma
        15     5.58534790E-04   # VBF -> H1 -> gammagamma
        21     7.00556314E-02   # VBF -> H2 -> tautau
        22     6.47492207E-02   # ggF -> H2 -> ZZ
        23     6.47492207E-02   # ggF -> H2 -> WW
        24     6.24158021E-02   # ggF -> H2 -> gammagamma
        25     6.29097787E-02   # VBF -> H2 -> gammagamma
        31     5.46542314E-03   # VBF -> H3 -> tautau
        32     1.26622705E-04   # ggF -> H3 -> ZZ
        33     1.26622705E-04   # ggF -> H3 -> WW
        34     5.54946806E+00   # ggF -> H3 -> gammagamma
        35     2.17856590E-03   # VBF -> H3 -> gammagamma
# HIGGS + TOP BRANCHING RATIOS IN SLHA FORMAT
# Info about decay package
BLOCK DCINFO   # Program information
     1   NMSSMTools # Decay package
     2   3.2.0      # Version number
#           PDG          Width
DECAY        25     6.93423599E-05   # Lightest neutral Higgs scalar
     4.50492057E-03    2          21        21   # BR(H_1 -> gluon gluon)
     2.49055276E-04    2          13       -13   # BR(H_1 -> muon muon)
     6.83275415E-02    2          15       -15   # BR(H_1 -> tau tau)
     7.33727882E-04    2           3        -3   # BR(H_1 -> s sbar)
     4.00267165E-03    2           4        -4   # BR(H_1 -> c cbar)
     9.22163202E-01    2           5        -5   # BR(H_1 -> b bbar)
     0.00000000E+00    2           6        -6   # BR(H_1 -> t tbar)
     0.00000000E+00    2          24       -24   # BR(H_1 -> W+ W-)
     0.00000000E+00    2          23        23   # BR(H_1 -> Z Z)
     1.88810084E-05    2          22        22   # BR(H_1 -> gamma gamma)
     0.00000000E+00    2          23        22   # BR(H_1 -> Z gamma)
DECAY        35     6.04596322E-02   # 2nd neutral Higgs scalar
     3.58897528E-03    2          21        21   # BR(H_2 -> gluon gluon)
     1.62660267E-05    2          13       -13   # BR(H_2 -> muon muon)
     4.59528735E-03    2          15       -15   # BR(H_2 -> tau tau)
     3.42428371E-05    2           3        -3   # BR(H_2 -> s sbar)
     1.90769331E-03    2           4        -4   # BR(H_2 -> c cbar)
     4.35440407E-02    2           5        -5   # BR(H_2 -> b bbar)
     0.00000000E+00    2           6        -6   # BR(H_2 -> t tbar)
     1.32289693E-02    2          24       -24   # BR(H_2 -> W+ W-)
     1.45595168E-03    2          23        23   # BR(H_2 -> Z Z)
     1.49609490E-04    2          22        22   # BR(H_2 -> gamma gamma)
     1.06132256E-04    2          23        22   # BR(H_2 -> Z gamma)
     9.31372832E-01    2          25        25   # BR(H_2 -> H_1 H_1)
DECAY        45     7.35790595E+00   # 3rd neutral Higgs scalar
     7.02407319E-04    2          21        21   # BR(H_3 -> gluon gluon)
     3.78590437E-06    2          13       -13   # BR(H_3 -> muon muon)
     1.07077596E-03    2          15       -15   # BR(H_3 -> tau tau)
     5.96235645E-06    2           3        -3   # BR(H_3 -> s sbar)
     1.14446816E-04    2           4        -4   # BR(H_3 -> c cbar)
     7.87837347E-03    2           5        -5   # BR(H_3 -> b bbar)
     3.83642904E-01    2           6        -6   # BR(H_3 -> t tbar)
     4.56110135E-04    2          24       -24   # BR(H_3 -> W+ W-)
     2.20603749E-04    2          23        23   # BR(H_3 -> Z Z)
     3.02775769E-06    2          22        22   # BR(H_3 -> gamma gamma)
     7.92129655E-07    2          23        22   # BR(H_3 -> Z gamma)
     2.02529861E-02    2          25        25   # BR(H_3 -> H_1 H_1)
     1.39913711E-01    2          25        35   # BR(H_3 -> H_1 H_2)
     1.14961851E-04    2          35        35   # BR(H_3 -> H_2 H_2)
     1.53439759E-05    2          36        36   # BR(H_3 -> A_1 A_1)
     1.20148940E-01    2          23        36   # BR(H_3 -> A_1 Z)
     1.01617473E-01    2     1000022   1000022   # BR(H_3 -> neu_1 neu_1)
     1.13426165E-01    2     1000022   1000023   # BR(H_3 -> neu_1 neu_2)
     1.01364362E-02    2     1000022   1000025   # BR(H_3 -> neu_1 neu_3)
     8.47315945E-03    2     1000022   1000035   # BR(H_3 -> neu_1 neu_4)
     2.13963922E-02    2     1000023   1000023   # BR(H_3 -> neu_2 neu_2)
     4.70523269E-02    2     1000023   1000025   # BR(H_3 -> neu_2 neu_3)
     1.47229980E-02    2     1000023   1000035   # BR(H_3 -> neu_2 neu_4)
     6.04345281E-03    2     1000025   1000025   # BR(H_3 -> neu_3 neu_3)
     2.41726200E-03    2     1000025   1000035   # BR(H_3 -> neu_3 neu_4)
     1.69202435E-04    2     1000024  -1000024   # BR(H_3 -> cha_1 cha_1bar)
DECAY        36     1.02533738E-03   # Lightest pseudoscalar
     5.00307291E-03    2          21        21   # BR(A_1 -> gluon gluon)
     2.12601789E-04    2          13       -13   # BR(A_1 -> muon muon)
     6.01239002E-02    2          15       -15   # BR(A_1 -> tau tau)
     4.05073418E-04    2           3        -3   # BR(A_1 -> s sbar)
     1.15273205E-03    2           4        -4   # BR(A_1 -> c cbar)
     5.25544486E-01    2           5        -5   # BR(A_1 -> b bbar)
     0.00000000E+00    2           6        -6   # BR(A_1 -> t tbar)
     6.72127541E-04    2          22        22   # BR(A_1 -> gamma gamma)
     2.70287404E-06    2          23        22   # BR(A_1 -> Z gamma)
     4.06883303E-01    2          23        25   # BR(A_1 -> Z H_1)
DECAY        46     8.72154153E+00   # 2nd pseudoscalar
     9.61932924E-04    2          21        21   # BR(A_2 -> gluon gluon)
     3.20378409E-06    2          13       -13   # BR(A_2 -> muon muon)
     9.06167916E-04    2          15       -15   # BR(A_2 -> tau tau)
     5.09433513E-06    2           3        -3   # BR(A_2 -> s sbar)
     1.53964741E-04    2           4        -4   # BR(A_2 -> c cbar)
     6.72501740E-03    2           5        -5   # BR(A_2 -> b bbar)
     4.53946291E-01    2           6        -6   # BR(A_2 -> t tbar)
     4.13520360E-06    2          22        22   # BR(A_2 -> gamma gamma)
     1.18559127E-06    2          23        22   # BR(A_2 -> Z gamma)
     1.53048163E-02    2          36        25   # BR(A_2 -> A_1 H_1)
     1.04614374E-01    2          36        35   # BR(A_2 -> A_1 H_2)
     1.19864230E-01    2          23        25   # BR(A_2 -> Z H_1)
     1.07707336E-03    2          23        35   # BR(A_2 -> Z H_2)
     1.20928098E-01    2     1000022   1000022   # BR(A_2 -> neu_1 neu_1)
     6.82699243E-03    2     1000022   1000023   # BR(A_2 -> neu_1 neu_2)
     8.19502226E-02    2     1000022   1000025   # BR(A_2 -> neu_1 neu_3)
     8.25626451E-03    2     1000022   1000035   # BR(A_2 -> neu_1 neu_4)
     7.13991837E-03    2     1000023   1000023   # BR(A_2 -> neu_2 neu_2)
     2.00080125E-02    2     1000023   1000025   # BR(A_2 -> neu_2 neu_3)
     1.96269482E-03    2     1000023   1000035   # BR(A_2 -> neu_2 neu_4)
     3.51484889E-02    2     1000025   1000025   # BR(A_2 -> neu_3 neu_3)
     1.40365680E-02    2     1000025   1000035   # BR(A_2 -> neu_3 neu_4)
     1.75252608E-04    2     1000024  -1000024   # BR(A_2 -> cha_1 cha_1bar)
DECAY        37     8.06322124E+00   # Charged Higgs
     3.47313159E-06    2         -13        14   # BR(H+ -> muon nu_muon)
     9.82350185E-04    2         -15        16   # BR(H+ -> tau nu_tau)
     2.64920446E-07    2           2        -3   # BR(H+ -> u sbar)
     1.05933060E-05    2           4        -3   # BR(H+ -> c sbar)
     1.12210610E-07    2           2        -5   # BR(H+ -> u bbar)
     1.12306353E-05    2           4        -5   # BR(H+ -> c bbar)
     4.69020926E-01    2           6        -5   # BR(H+ -> t bbar)
     1.26436200E-01    2          24        25   # BR(H+ -> W+ H_1)
     1.13132304E-03    2          24        35   # BR(H+ -> W+ H_2)
     1.05887241E-01    2          24        36   # BR(H+ -> W+ A_1)
     2.32198530E-01    2     1000024   1000022   # BR(H+ -> cha_1 neu_1)
     1.88217599E-02    2     1000024   1000023   # BR(H+ -> cha_1 neu_2)
     3.01239205E-02    2     1000024   1000025   # BR(H+ -> cha_1 neu_3)
     1.53720752E-02    2     1000024   1000035   # BR(H+ -> cha_1 neu_4)
DECAY         6     1.38766019E+00   # Top Quark
     1.00000000E+00    2           5        24   # BR(t ->  b    W+)
#         PDG            Width
DECAY        24     2.08500000E+00   # W+ (measured)
     1.16500000E-01    2         -11        12   # BR(W+ -> e+ nu_e)
     1.16500000E-01    2         -13        14   # BR(W+ -> mu+ nu_mu)
     1.12000000E-01    2         -15        16   # BR(W+ -> tau+ nu_tau)
     3.65000000E-01    2           2        -1   # BR(W+ -> u db)
     3.10000000E-01    2           4        -3   # BR(W+ -> c sb)
#         PDG            Width
DECAY        23     2.49520000E+00   # Z (measured)
     2.00000000E-01    2         -12        12   # BR(Z -> invisible)
     3.36500000E-02    2         -11        11   # BR(Z -> e+ e-)
     3.36500000E-02    2         -13        13   # BR(Z -> mu+ mu-)
     3.37000000E-02    2         -15        15   # BR(Z -> tau+ tau-)
     1.11000000E-01    2           2        -2   # BR(Z -> u ub)
     1.58500000E-01    2           1        -1   # BR(Z -> d db)
     1.58500000E-01    2           3        -3   # BR(Z -> s sb)
     1.20000000E-01    2           4        -4   # BR(Z -> c cb)
     1.51000000E-01    2           5        -5   # BR(Z -> b bb)
#         PDG            Width
DECAY   1000024     1.95835259E-01   # chargino1
#                    chargino1 2-body decays
#          BR         NDA      ID1       ID2
     1.00000000E+00    2     1000022        24   # BR(~chi_1+ -> ~chi_10  W+)
#         PDG            Width
DECAY   1000037     2.89304455E+00   # chargino2
#                    chargino2 2-body decays
#          BR         NDA      ID1       ID2
     2.60474069E-01    2     1000024        23   # BR(~chi_2+ -> ~chi_1+  Z )
     1.03251493E-01    2     1000022        24   # BR(~chi_2+ -> ~chi_10  W+)
     1.95590500E-01    2     1000023        24   # BR(~chi_2+ -> ~chi_20  W+)
     1.82870512E-01    2     1000025        24   # BR(~chi_2+ -> ~chi_30  W+)
     3.53139828E-02    2     1000035        24   # BR(~chi_2+ -> ~chi_40  W+)
     2.79530234E-03    2     1000024        25   # BR(~chi_2+ -> ~chi_1+  H_1 )
     2.19253328E-01    2     1000024        35   # BR(~chi_2+ -> ~chi_1+  H_2 )
     4.50814023E-04    2     1000024        36   # BR(~chi_2+ -> ~chi_1+  A_1 )
#         PDG            Width
DECAY   1000022     0.00000000E+00   # neutralino1
#         PDG            Width
DECAY   1000023     3.18128882E-01   # neutralino2
#                    neutralino2 2-body decays
#          BR         NDA      ID1       ID2
     5.33189046E-01    2     1000022        23   # BR(~chi_20 -> ~chi_10   Z )
     3.71729479E-01    2     1000022        25   # BR(~chi_20 -> ~chi_10   H_1 )
     9.50814757E-02    2     1000022        35   # BR(~chi_20 -> ~chi_10   H_2 )
#         PDG            Width
DECAY   1000025     1.01094460E-01   # neutralino3
#                    neutralino3 2-body decays
#          BR         NDA      ID1       ID2
     6.25304485E-01    2     1000022        23   # BR(~chi_30 -> ~chi_10   Z )
     3.49602482E-01    2     1000022        25   # BR(~chi_30 -> ~chi_10   H_1 )
     2.50930327E-02    2     1000022        35   # BR(~chi_30 -> ~chi_10   H_2 )
#         PDG            Width
DECAY   1000035     9.90031372E-02   # neutralino4
#                    neutralino4 2-body decays
#          BR         NDA      ID1       ID2
     3.42104751E-01    2     1000022        23   # BR(~chi_40 -> ~chi_10   Z )
     1.80091579E-01    2     1000024       -24   # BR(~chi_40 -> ~chi_1+   W-)
     1.80091579E-01    2    -1000024        24   # BR(~chi_40 -> ~chi_1-   W+)
     3.90955420E-03    2     1000022        25   # BR(~chi_40 -> ~chi_10   H_1 )
     6.02259430E-04    2     1000022        35   # BR(~chi_40 -> ~chi_10   H_2 )
     3.11297585E-02    2     1000022        36   # BR(~chi_40 -> ~chi_10   A_1 )
     9.10306887E-04    2     1000023        25   # BR(~chi_40 -> ~chi_20   H_1 )
     2.61160212E-01    2     1000025        25   # BR(~chi_40 -> ~chi_30   H_1 )
#         PDG            Width
DECAY   1000045     2.89752023E+00   # neutralino5
#                    neutralino5 2-body decays
#          BR         NDA      ID1       ID2
     6.33112028E-02    2     1000022        23   # BR(~chi_50 -> ~chi_10   Z )
     7.93200941E-02    2     1000023        23   # BR(~chi_50 -> ~chi_20   Z )
     1.12593927E-01    2     1000025        23   # BR(~chi_50 -> ~chi_30   Z )
     6.89352755E-03    2     1000035        23   # BR(~chi_50 -> ~chi_40   Z )
     2.58485414E-01    2     1000024       -24   # BR(~chi_50 -> ~chi_1+   W-)
     2.58485414E-01    2    -1000024        24   # BR(~chi_50 -> ~chi_1-   W+)
     9.57767327E-04    2     1000022        25   # BR(~chi_50 -> ~chi_10   H_1 )
     3.37803528E-02    2     1000022        35   # BR(~chi_50 -> ~chi_10   H_2 )
     7.90204767E-04    2     1000022        36   # BR(~chi_50 -> ~chi_10   A_1 )
     1.16419727E-03    2     1000023        25   # BR(~chi_50 -> ~chi_20   H_1 )
     9.07296401E-02    2     1000023        35   # BR(~chi_50 -> ~chi_20   H_2 )
     5.30381824E-05    2     1000023        36   # BR(~chi_50 -> ~chi_20   A_1 )
     3.97645128E-04    2     1000025        25   # BR(~chi_50 -> ~chi_30   H_1 )
     6.57691569E-02    2     1000025        35   # BR(~chi_50 -> ~chi_30   H_2 )
     8.28558424E-05    2     1000025        36   # BR(~chi_50 -> ~chi_30   A_1 )
     2.67586450E-04    2     1000035        25   # BR(~chi_50 -> ~chi_40   H_1 )
     2.69111753E-02    2     1000035        35   # BR(~chi_50 -> ~chi_40   H_2 )
     6.80016114E-06    2     1000035        36   # BR(~chi_50 -> ~chi_40   A_1 )
#         PDG            Width
DECAY   1000021     1.50796157E+00   # gluino
#                    gluino 2-body decays
#          BR         NDA      ID1       ID2
     4.13793003E-02    2     1000001        -1   # BR(~g -> ~d_L  db)
     4.13793003E-02    2    -1000001         1   # BR(~g -> ~d_L* d )
     4.33212075E-02    2     2000001        -1   # BR(~g -> ~d_R  db)
     4.33212075E-02    2    -2000001         1   # BR(~g -> ~d_R* d )
     4.57605556E-02    2     1000002        -2   # BR(~g -> ~u_L  ub)
     4.57605556E-02    2    -1000002         2   # BR(~g -> ~u_L* u )
     4.46532073E-02    2     2000002        -2   # BR(~g -> ~u_R  ub)
     4.46532073E-02    2    -2000002         2   # BR(~g -> ~u_R* u )
     4.13793003E-02    2     1000003        -3   # BR(~g -> ~s_L  sb)
     4.13793003E-02    2    -1000003         3   # BR(~g -> ~s_L* s )
     4.33212075E-02    2     2000003        -3   # BR(~g -> ~s_R  sb)
     4.33212075E-02    2    -2000003         3   # BR(~g -> ~s_R* s )
     4.57605556E-02    2     1000004        -4   # BR(~g -> ~c_L  cb)
     4.57605556E-02    2    -1000004         4   # BR(~g -> ~c_L* c )
     4.46532073E-02    2     2000004        -4   # BR(~g -> ~c_R  cb)
     4.46532073E-02    2    -2000004         4   # BR(~g -> ~c_R* c )
     5.05129557E-02    2     1000005        -5   # BR(~g -> ~b_1  bb)
     5.05129557E-02    2    -1000005         5   # BR(~g -> ~b_1* b )
     3.42876439E-02    2     2000005        -5   # BR(~g -> ~b_2  bb)
     3.42876439E-02    2    -2000005         5   # BR(~g -> ~b_2* b )
#                    gluino 3-body decays
#           BR         NDA      ID1       ID2       ID3
     1.81071798E-02    3     1000022         6        -6   # BR(~g -> ~chi_10 t  tb)
     2.97839961E-02    3     1000023         6        -6   # BR(~g -> ~chi_20 t  tb)
     3.25857777E-02    3     1000025         6        -6   # BR(~g -> ~chi_30 t  tb)
     1.03830739E-02    3     1000035         6        -6   # BR(~g -> ~chi_40 t  tb)
     1.88859736E-03    3     1000045         6        -6   # BR(~g -> ~chi_50 t  tb)
     1.60591626E-02    3     1000024         5        -6   # BR(~g -> ~chi_1+ b  tb)
     1.60591626E-02    3    -1000024         6        -5   # BR(~g -> ~chi_1- t  bb)
     2.50088464E-03    3     1000037         5        -6   # BR(~g -> ~chi_2+ b  tb)
     2.50088464E-03    3    -1000037         6        -5   # BR(~g -> ~chi_2- t  bb)
     3.64995263E-05    3     1000006        -5       -24   # BR(~g -> ~t_1    bb W-)
     3.64995263E-05    3    -1000006         5        24   # BR(~g -> ~t_1*   b  W+)
#         PDG            Width
DECAY   1000011     5.78663686E+00   # selectron_L
#                    selectron_L 2-body decays
#          BR         NDA      ID1       ID2
     3.06852872E-04    2     1000022        11   # BR(~e_L -> ~chi_10 e-)   
     1.09569421E-03    2     1000023        11   # BR(~e_L -> ~chi_20 e-)   
     1.30819805E-03    2     1000025        11   # BR(~e_L -> ~chi_30 e-)  
     2.02127959E-01    2     1000035        11   # BR(~e_L -> ~chi_40 e-)  
     2.59433557E-01    2     1000045        11   # BR(~e_L -> ~chi_50 e-)  
     1.25739781E-04    2    -1000024        12   # BR(~e_L -> ~chi_1- nu_e)
     5.35601999E-01    2    -1000037        12   # BR(~e_L -> ~chi_2- nu_e)
#         PDG            Width
DECAY   2000011     4.32983431E+00   # selectron_R
#                    selectron_R 2-body decays
#          BR         NDA      ID1       ID2
     2.29457555E-03    2     1000022        11   # BR(~e_R -> ~chi_10 e-)
     5.09644980E-03    2     1000023        11   # BR(~e_R -> ~chi_20 e-)
     4.35807438E-02    2     1000025        11   # BR(~e_R -> ~chi_30 e-)
     9.48925398E-01    2     1000035        11   # BR(~e_R -> ~chi_40 e-)
     1.02832819E-04    2     1000045        11   # BR(~e_R -> ~chi_50 e-)
#         PDG            Width
DECAY   1000013     5.78663686E+00   # smuon_L
#                    smuon_L 2-body decays
#          BR         NDA      ID1       ID2
     3.06852872E-04    2     1000022        13   # BR(~mu_L -> ~chi_10 mu-)
     1.09569421E-03    2     1000023        13   # BR(~mu_L -> ~chi_20 mu-)
     1.30819805E-03    2     1000025        13   # BR(~mu_L -> ~chi_30 mu-)
     2.02127959E-01    2     1000035        13   # BR(~mu_L -> ~chi_40 mu-)
     2.59433557E-01    2     1000045        13   # BR(~mu_L -> ~chi_50 mu-)
     1.25739781E-04    2    -1000024        14   # BR(~mu_L -> ~chi_1- nu_mu)
     5.35601999E-01    2    -1000037        14   # BR(~mu_L -> ~chi_2- nu_mu)
#         PDG            Width
DECAY   2000013     4.32983431E+00   # smuon_R
#                    smuon_R 2-body decays
#          BR         NDA      ID1       ID2
     2.29457555E-03    2     1000022        13   # BR(~mu_R -> ~chi_10 mu-)
     5.09644980E-03    2     1000023        13   # BR(~mu_R -> ~chi_20 mu-)
     4.35807438E-02    2     1000025        13   # BR(~mu_R -> ~chi_30 mu-)
     9.48925398E-01    2     1000035        13   # BR(~mu_R -> ~chi_40 mu-)
     1.02832819E-04    2     1000045        13   # BR(~mu_R -> ~chi_50 mu-)
#         PDG            Width
DECAY   1000015     5.03156061E+00   # stau_1
#                    stau1 2-body decays
#          BR         NDA      ID1       ID2
     1.14186586E-03    2     1000022        15   # BR(~tau_1 -> ~chi_10  tau-)
     4.79066718E-04    2     1000023        15   # BR(~tau_1 -> ~chi_20  tau-)
     2.71054790E-02    2     1000025        15   # BR(~tau_1 -> ~chi_30  tau-)
     5.31169018E-01    2     1000035        15   # BR(~tau_1 -> ~chi_40  tau-)
     1.43366118E-01    2     1000045        15   # BR(~tau_1 -> ~chi_50  tau-)
     8.82065449E-04    2    -1000024        16   # BR(~tau_1 -> ~chi_1-  nu_tau)
     2.95856387E-01    2    -1000037        16   # BR(~tau_1 -> ~chi_2-  nu_tau)
#         PDG            Width
DECAY   2000015     4.34604583E+00   # stau_2
#                    stau_2 2-body decays
#          BR         NDA      ID1       ID2
     1.37428162E-03    2     1000022        15   # BR(~tau_2 -> ~chi_10  tau-)
     9.20765668E-03    2     1000023        15   # BR(~tau_2 -> ~chi_20  tau-)
     1.68826586E-02    2     1000025        15   # BR(~tau_2 -> ~chi_30  tau-)
     5.99653922E-01    2     1000035        15   # BR(~tau_2 -> ~chi_40  tau-)
     1.79484751E-01    2     1000045        15   # BR(~tau_2 -> ~chi_50  tau-)
     2.39283431E-03    2    -1000024        16   # BR(~tau_2 -> ~chi_1-  nu_tau)
     3.70488646E-01    2    -1000037        16   # BR(~tau_2 -> ~chi_2-  nu_tau)
#         PDG            Width
DECAY   1000012     5.82409806E+00   # snu_eL
#                    snu_eL 2-body decays
#          BR         NDA      ID1       ID2
     3.44541021E-03    2     1000022        12   # BR(~nu_eL -> ~chi_10 nu_e)
     8.91602588E-03    2     1000023        12   # BR(~nu_eL -> ~chi_20 nu_e)
     2.06692014E-02    2     1000025        12   # BR(~nu_eL -> ~chi_30 nu_e)
     1.53093689E-01    2     1000035        12   # BR(~nu_eL -> ~chi_40 nu_e)
     2.64584107E-01    2     1000045        12   # BR(~nu_eL -> ~chi_50 nu_e)
     3.61604589E-02    2     1000024        11   # BR(~nu_eL -> ~chi_1+ e-)
     5.13131108E-01    2     1000037        11   # BR(~nu_eL -> ~chi_2+ e-)
#         PDG            Width
DECAY   1000014     5.82409806E+00   # snu_muL
#                    snu_muL 2-body decays
#          BR         NDA      ID1       ID2
     3.44541021E-03    2     1000022        14   # BR(~nu_muL -> ~chi_10 nu_mu)
     8.91602588E-03    2     1000023        14   # BR(~nu_muL -> ~chi_20 nu_mu)
     2.06692014E-02    2     1000025        14   # BR(~nu_muL -> ~chi_30 nu_mu)
     1.53093689E-01    2     1000035        14   # BR(~nu_muL -> ~chi_40 nu_mu)
     2.64584107E-01    2     1000045        14   # BR(~nu_muL -> ~chi_50 nu_mu)
     3.61604589E-02    2     1000024        13   # BR(~nu_muL -> ~chi_1+ mu-)
     5.13131108E-01    2     1000037        13   # BR(~nu_muL -> ~chi_2+ mu-)
#         PDG            Width
DECAY   1000016     5.83820352E+00   # snu_tauL
#                    sbu_tauL 2-body decays
#          BR         NDA      ID1       ID2
     3.43708589E-03    2     1000022        16   # BR(~nu_tauL -> ~chi_10 nu_tau)
     8.89448421E-03    2     1000023        16   # BR(~nu_tauL -> ~chi_20 nu_tau)
     2.06192633E-02    2     1000025        16   # BR(~nu_tauL -> ~chi_30 nu_tau)
     1.52723805E-01    2     1000035        16   # BR(~nu_tauL -> ~chi_40 nu_tau)
     2.63944855E-01    2     1000045        16   # BR(~nu_tauL -> ~chi_50 nu_tau)
     3.84961084E-02    2     1000024        15   # BR(~nu_tauL -> ~chi_1+ tau-)
     5.11884398E-01    2     1000037        15   # BR(~nu_tauL -> ~chi_2+ tau-)
#         PDG            Width
DECAY   1000002     5.73689803E+00   # sup_L
#                    sup_L 2-body decays
#          BR         NDA      ID1       ID2
     9.95251694E-04    2     1000022         2   # BR(~u_L -> ~chi_10 u)
     2.97343563E-03    2     1000023         2   # BR(~u_L -> ~chi_20 u)
     5.95852740E-04    2     1000025         2   # BR(~u_L -> ~chi_30 u)
     2.97748093E-02    2     1000035         2   # BR(~u_L -> ~chi_40 u)
     3.11048068E-01    2     1000045         2   # BR(~u_L -> ~chi_50 u)
     3.75280105E-02    2     1000024         1   # BR(~u_L -> ~chi_1+ d)
     6.17084572E-01    2     1000037         1   # BR(~u_L -> ~chi_2+ d)
#         PDG            Width
DECAY   2000002     1.99702651E+00   # sup_R
#                    sup_R 2-body decays
#          BR         NDA      ID1       ID2
     2.22404067E-03    2     1000022         2   # BR(~u_R -> ~chi_10 u)
     5.02648420E-03    2     1000023         2   # BR(~u_R -> ~chi_20 u)
     4.29887112E-02    2     1000025         2   # BR(~u_R -> ~chi_30 u)
     9.49644060E-01    2     1000035         2   # BR(~u_R -> ~chi_40 u)
     1.16703919E-04    2     1000045         2   # BR(~u_R -> ~chi_50 u)
#         PDG            Width
DECAY   1000001     5.64341310E+00   # sdown_L
#                    sdown_L 2-body decays
#          BR         NDA      ID1       ID2
     2.10434144E-03    2     1000022         1   # BR(~d_L -> ~chi_10 d)
     5.79758593E-03    2     1000023         1   # BR(~d_L -> ~chi_20 d)
     7.45741543E-03    2     1000025         1   # BR(~d_L -> ~chi_30 d)
     1.34387635E-02    2     1000035         1   # BR(~d_L -> ~chi_40 d)
     3.21776483E-01    2     1000045         1   # BR(~d_L -> ~chi_50 d)
     1.31720061E-04    2    -1000024         2   # BR(~d_L -> ~chi_1- u)
     6.49293690E-01    2    -1000037         2   # BR(~d_L -> ~chi_2- u)
#         PDG            Width
DECAY   2000001     4.99627626E-01   # sdown_R
#                    sdown_R 2-body decays
#          BR         NDA      ID1       ID2
     2.22360749E-03    2     1000022         1   # BR(~d_R -> ~chi_10 d)
     5.02599170E-03    2     1000023         1   # BR(~d_R -> ~chi_20 d)
     4.29845402E-02    2     1000025         1   # BR(~d_R -> ~chi_30 d)
     9.49649028E-01    2     1000035         1   # BR(~d_R -> ~chi_40 d)
     1.16832598E-04    2     1000045         1   # BR(~d_R -> ~chi_50 d)
#         PDG            Width
DECAY   1000004     5.73689803E+00   # scharm_L
#                    scharm_L 2-body decays
#          BR         NDA      ID1       ID2
     9.95251694E-04    2     1000022         4   # BR(~c_L -> ~chi_10 c)
     2.97343563E-03    2     1000023         4   # BR(~c_L -> ~chi_20 c)
     5.95852740E-04    2     1000025         4   # BR(~c_L -> ~chi_30 c)
     2.97748093E-02    2     1000035         4   # BR(~c_L -> ~chi_40 c)
     3.11048068E-01    2     1000045         4   # BR(~c_L -> ~chi_50 c)
     3.75280105E-02    2     1000024         3   # BR(~c_L -> ~chi_1+ s)
     6.17084572E-01    2     1000037         3   # BR(~c_L -> ~chi_2+ s)
#         PDG            Width
DECAY   2000004     1.99702651E+00   # scharm_R
#                    scharm_R 2-body decays
#          BR         NDA      ID1       ID2
     2.22404067E-03    2     1000022         4   # BR(~c_R -> ~chi_10 c)
     5.02648420E-03    2     1000023         4   # BR(~c_R -> ~chi_20 c)
     4.29887112E-02    2     1000025         4   # BR(~c_R -> ~chi_30 c)
     9.49644060E-01    2     1000035         4   # BR(~c_R -> ~chi_40 c)
     1.16703919E-04    2     1000045         4   # BR(~c_R -> ~chi_50 c)
#         PDG            Width
DECAY   1000003     5.64341310E+00   # sstrange_L
#                    sstrange_L 2-body decays
#          BR         NDA      ID1       ID2
     2.10434144E-03    2     1000022         3   # BR(~s_L -> ~chi_10 s)
     5.79758593E-03    2     1000023         3   # BR(~s_L -> ~chi_20 s)
     7.45741543E-03    2     1000025         3   # BR(~s_L -> ~chi_30 s)
     1.34387635E-02    2     1000035         3   # BR(~s_L -> ~chi_40 s)
     3.21776483E-01    2     1000045         3   # BR(~s_L -> ~chi_50 s)
     1.31720061E-04    2    -1000024         4   # BR(~s_L -> ~chi_1- c)
     6.49293690E-01    2    -1000037         4   # BR(~s_L -> ~chi_2- c)
#         PDG            Width
DECAY   2000003     4.99627626E-01   # sstrange_R
#                    sstrange_R 2-body decays
#          BR         NDA      ID1       ID2
     2.22360749E-03    2     1000022         3   # BR(~s_R -> ~chi_10 s)
     5.02599170E-03    2     1000023         3   # BR(~s_R -> ~chi_20 s)
     4.29845402E-02    2     1000025         3   # BR(~s_R -> ~chi_30 s)
     9.49649028E-01    2     1000035         3   # BR(~s_R -> ~chi_40 s)
     1.16832598E-04    2     1000045         3   # BR(~s_R -> ~chi_50 s)
#         PDG            Width
DECAY   1000006     2.18944264E+01   # stop1
#                    stop1 2-body decays
#          BR         NDA      ID1       ID2
     1.09912477E-01    2     1000022         6   # BR(~t_1 -> ~chi_10 t )
     1.96163329E-01    2     1000023         6   # BR(~t_1 -> ~chi_20 t )
     2.17642262E-01    2     1000025         6   # BR(~t_1 -> ~chi_30 t )
     8.77834169E-02    2     1000035         6   # BR(~t_1 -> ~chi_40 t )
     4.56499826E-02    2     1000045         6   # BR(~t_1 -> ~chi_50 t )
     2.52074872E-01    2     1000024         5   # BR(~t_1 -> ~chi_1+ b )
     9.07736609E-02    2     1000037         5   # BR(~t_1 -> ~chi_2+ b )
#         PDG            Width
DECAY   2000006     3.21963098E+01   # stop2
#                    stop2 2-body decays
#          BR         NDA      ID1       ID2
     1.10849439E-01    2     1000022         6   # BR(~t_2 -> ~chi_10 t )
     2.28919114E-01    2     1000023         6   # BR(~t_2 -> ~chi_20 t )
     2.07556523E-01    2     1000025         6   # BR(~t_2 -> ~chi_30 t )
     2.98910194E-02    2     1000035         6   # BR(~t_2 -> ~chi_40 t )
     2.13145108E-02    2     1000045         6   # BR(~t_2 -> ~chi_50 t )
     3.26169902E-01    2     1000024         5   # BR(~t_2 -> ~chi_1+ b )
     3.69385241E-02    2     1000037         5   # BR(~t_2 -> ~chi_2+ b )
     6.25419060E-08    2     1000006        25   # BR(~t_2 -> ~t_1    H1 )
     3.95342636E-07    2     1000006        35   # BR(~t_2 -> ~t_1    H2 )
     3.54933804E-02    2     1000006        23   # BR(~t_2 -> ~t_1    Z )
     1.57237423E-03    2     1000005        24   # BR(~t_2 -> ~b_1    W+)
     1.29475441E-03    2     2000005        24   # BR(~t_2 -> ~b_2    W+)
#         PDG            Width
DECAY   1000005     7.91241548E+00   # sbottom1
#                    sbottom1 2-body decays
#          BR         NDA      ID1       ID2
     5.94550399E-04    2     1000022         5   # BR(~b_1 -> ~chi_10 b )
     1.60789517E-04    2     1000023         5   # BR(~b_1 -> ~chi_20 b )
     1.03677709E-02    2     1000025         5   # BR(~b_1 -> ~chi_30 b )
     3.88362111E-02    2     1000035         5   # BR(~b_1 -> ~chi_40 b )
     7.88297180E-02    2     1000045         5   # BR(~b_1 -> ~chi_50 b )
     7.01755450E-01    2    -1000024         6   # BR(~b_1 -> ~chi_1- t )
     1.69455510E-01    2    -1000037         6   # BR(~b_1 -> ~chi_2- t )
#         PDG            Width
DECAY   2000005     1.27186372E+01   # sbottom2
#                    sbottom2 2-body decays
#          BR         NDA      ID1       ID2
     6.44124575E-04    2     1000022         5   # BR(~b_2 -> ~chi_10 b )
     4.84349389E-03    2     1000023         5   # BR(~b_2 -> ~chi_20 b )
     6.47748025E-04    2     1000025         5   # BR(~b_2 -> ~chi_30 b )
     1.83041601E-02    2     1000035         5   # BR(~b_2 -> ~chi_40 b )
     8.44702142E-02    2     1000045         5   # BR(~b_2 -> ~chi_50 b )
     7.08770621E-01    2    -1000024         6   # BR(~b_2 -> ~chi_1- t )
     1.81711698E-01    2    -1000037         6   # BR(~b_2 -> ~chi_2- t )
#
# Dummy alpha block (for Prospino compatibility only - not used)
BLOCK ALPHA
	0.1000E+00
"""

  f = open("%s/src/WorkingPoint_mH1_25_mH2_125p3_MSUSY_1000.slha" % os.environ['CMSSW_BASE'],"w")
  f.write(slhacontent)
  f.close()
  
  return process