import FWCore.ParameterSet.Config as cms
#  regex: ^\([0-9]\+\) *\(.*\)$
# full line :%s/^\([0-9]\+\) *\(.*\)$/^I'\1':'\2',/

stepOneDatasets41X = {
    '010':'/TToBLNu_TuneZ2_s-channel_7TeV-madgraph/mangano-R42X_S1_V04_S2_V00_S3_V00_ID010_sTtoBLNu-v1-8a66f640cda46e57b12f252bbcf377c8/USER',
    '011':'/TToBLNu_TuneZ2_t-channel_7TeV-madgraph/mangano-R42X_S1_V04_S2_V00_S3_V00_ID011_tTtoBLNu-v1-8a66f640cda46e57b12f252bbcf377c8/USER',
    '012':'/TToBLNu_TuneZ2_tW-channel_7TeV-madgraph/mangano-R42X_S1_V04_S2_V00_S3_V00_ID012_tWTtoBLNu-v1-8a66f640cda46e57b12f252bbcf377c8/USER',
}


stepOneDatasets = {

	'000':'/WWJetsTo2L2Nu_TuneZ2_7TeV-madgraph-tauola/mwlebour-R42X_S1_V09_S2_V06_S3_V13_ID000_WWJets2LMad-26a07df0670d12c6eef310bf324d6d6d/USER',
	'001':'/GluGluToWWTo4L_TuneZ2_7TeV-gg2ww-pythia6/mwlebour-R42X_S1_V09_S2_V06_S3_V13_ID001_GluGluToWWTo4L-26a07df0670d12c6eef310bf324d6d6d/USER',
	'002':'',
	'003':'/WWTo2L2Nu_scaleup_CT10_7TeV-mcatnlo/mwlebour-R42X_S1_V09_S2_V06_S3_V13_ID003_WWto2L2NuMCatNLOUp_v2-1450422e957e9c6bf618aa52da12a29f/USER',
	'004':'',
	'005':'',
	'006':'',
                
	'010':'',
	'011':'/T_TuneZ2_tW-channel-DR_7TeV-powheg-tauola/mwlebour-R42X_S1_V09_S2_V06_S3_V13_ID011_TtWFullDR-26a07df0670d12c6eef310bf324d6d6d/USER',
	'012':'/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/mwlebour-R42X_S1_V09_S2_V06_S3_V13_ID012_TbartWFullDR-26a07df0670d12c6eef310bf324d6d6d/USER',
	'013':'/T_TuneZ2_t-channel_7TeV-powheg-tauola/mwlebour-R42X_S1_V09_S2_V06_S3_V13_ID013_TtFull-26a07df0670d12c6eef310bf324d6d6d/USER',
	'014':'/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/mwlebour-R42X_S1_V09_S2_V06_S3_V13_ID014_TbartFull-26a07df0670d12c6eef310bf324d6d6d/USER',
	'015':'/T_TuneZ2_s-channel_7TeV-powheg-tauola/mwlebour-R42X_S1_V09_S2_V06_S3_V13_ID015_TsFull-26a07df0670d12c6eef310bf324d6d6d/USER',
	'016':'/Tbar_TuneZ2_s-channel_7TeV-powheg-tauola/mwlebour-R42X_S1_V09_S2_V06_S3_V13_ID016_TbarsFull-26a07df0670d12c6eef310bf324d6d6d/USER',
	'017':'/T_TuneZ2_tW-channel-DS_7TeV-powheg-tauola/mwlebour-R42X_S1_V09_S2_V06_S3_V13_ID017_TtWFullDS-26a07df0670d12c6eef310bf324d6d6d/USER',
	'018':'/Tbar_TuneZ2_tW-channel-DS_7TeV-powheg-tauola/mwlebour-R42X_S1_V09_S2_V06_S3_V13_ID018_TbartWFullDS-26a07df0670d12c6eef310bf324d6d6d/USER',
	'019':'/TTTo2L2Nu2B_7TeV-powheg-pythia6/mwlebour-R42X_S1_V09_S2_V06_S3_V13_ID019_TTTo2L2Nu2B-26a07df0670d12c6eef310bf324d6d6d/USER',
                
                
	'030':'',
	'031':'',
	'032':'',
	'033':'/DYToEE_M-10To20_CT10_TuneZ2_7TeV-powheg-pythia/mwlebour-R42X_S1_V09_S2_V06_S3_V13_ID033_DY10toElEl-26a07df0670d12c6eef310bf324d6d6d/USER',
	'034':'/DYToMuMu_M-10To20_CT10_TuneZ2_7TeV-powheg-pythia/mwlebour-R42X_S1_V09_S2_V06_S3_V13_ID034_DY10toMuMu-26a07df0670d12c6eef310bf324d6d6d/USER',
	'035':'/DYToTauTau_M-10To20_TuneZ2_7TeV-pythia6-tauola/mwlebour-R42X_S1_V09_S2_V06_S3_V13_ID035_DY10toTauTau-26a07df0670d12c6eef310bf324d6d6d/USER',
	'036':'',
	'037':'',
	'038':'',
	'039':'/ZGToMuMuG_TuneZ2_7TeV-madgraph/mwlebour-R42X_S1_V09_S2_V06_S3_V13_ID039_ZgammaToMuMuMad-26a07df0670d12c6eef310bf324d6d6d/USER',
	'040':'/ZGToTauTauG_TuneZ2_7TeV-madgraph-tauola/mwlebour-R42X_S1_V09_S2_V06_S3_V13_ID040_ZgammaToTauTauMad-26a07df0670d12c6eef310bf324d6d6d/USER',
	'041':'',
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
	'070':'/WZ_TuneZ2_7TeV_pythia6_tauola/mwlebour-R42X_S1_V09_S2_V06_S3_V13_ID070_WZFull-26a07df0670d12c6eef310bf324d6d6d/USER',
	'071':'/ZZ_TuneZ2_7TeV_pythia6_tauola/mwlebour-R42X_S1_V09_S2_V06_S3_V13_ID071_ZZFull-26a07df0670d12c6eef310bf324d6d6d/USER',
	'072':'',
	'073':'/GluGluToZZTo4L_7TeV-gg2zz-pythia6/mwlebour-R42X_S1_V09_S2_V06_S3_V13_ID073_GluGluZZ4L-26a07df0670d12c6eef310bf324d6d6d/USER',
	'074':'',
	'075':'/ZZJetsTo2L2Nu_TuneZ2_7TeV-madgraph-tauola/mwlebour-R42X_S1_V09_S2_V06_S3_V13_ID075_ZZJetsMad-26a07df0670d12c6eef310bf324d6d6d/USER',
                
                
	'080':'',
	'081':'',
	'082':'',
	'083':'',
	'084':'/WGToTauNuG_TuneZ2_7TeV-madgraph-tauola/mwlebour-R42X_S1_V09_S2_V06_S3_V13_ID084_WgammaToTauNuMad-7e6e054e8b91c8bc8787b29ccd446077/USER',
	'085':'',
	'086':'',
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
	'100':'/SingleElectron/jfernan2-R42X_S1_V08_S2_V05_S3_V11_ID100_SingleElectron2011Av4-47b630e2469c9e3550fd039775e94457/USER',
	'101':'/SingleMu/jfernan2-R42X_S1_V08_S2_V05_S3_V11_ID101_SingleMuon2011Av4-47b630e2469c9e3550fd039775e94457/USER',
	'102':'/DoubleElectron/jfernan2-R42X_S1_V08_S2_V05_S3_V11_ID102_DoubleElectron2011Av4-47b630e2469c9e3550fd039775e94457/USER',
	'103':'/DoubleMu/jfernan2-R42X_S1_V08_S2_V05_S3_V11_ID103_DoubleMuon2011Av4-47b630e2469c9e3550fd039775e94457/USER',
	'104':'/MuEG/jfernan2-R42X_S1_V08_S2_V05_S3_V11_ID104_MuEG2011Av4-47b630e2469c9e3550fd039775e94457/USER',
                
	'120':'/SingleElectron/jfernan2-R42X_S1_V08_S2_V05_S3_V11_ID120_SingleElectron2011Av6-47b630e2469c9e3550fd039775e94457/USER',
	'121':'/SingleMu/jfernan2-R42X_S1_V08_S2_V05_S3_V11_ID121_SingleMuon2011Av6-47b630e2469c9e3550fd039775e94457/USER',
	'122':'/DoubleElectron/jfernan2-R42X_S1_V08_S2_V05_S3_V11_ID122_DoubleElectron2011Av6-47b630e2469c9e3550fd039775e94457/USER',
	'123':'/DoubleMu/jfernan2-R42X_S1_V08_S2_V05_S3_V11_ID123_DoubleMuon2011Av6-47b630e2469c9e3550fd039775e94457/USER',
	'124':'/MuEG/jfernan2-R42X_S1_V08_S2_V05_S3_V11_ID124_MuEG2011Av6-47b630e2469c9e3550fd039775e94457/USER',
                
	'140':'/SingleElectron/jfernan2-R42X_S1_V08_S2_V05_S3_V11_ID140_SingleElectron2011Bv1-47b630e2469c9e3550fd039775e94457/USER',
	'141':'/SingleMu/jfernan2-R42X_S1_V08_S2_V05_S3_V11_ID141_SingleMuon2011Bv1-47b630e2469c9e3550fd039775e94457/USER',
	'142':'/DoubleElectron/jfernan2-R42X_S1_V08_S2_V05_S3_V11_ID142_DoubleElectron2011Bv1_NoServer-47b630e2469c9e3550fd039775e94457/USER',
	'143':'/DoubleMu/jfernan2-R42X_S1_V08_S2_V05_S3_V11_ID143_DoubleMuon2011Bv1-47b630e2469c9e3550fd039775e94457/USER',
	'144':'/MuEG/jfernan2-R42X_S1_V08_S2_V05_S3_V11_ID144_MuEG2011Bv1-47b630e2469c9e3550fd039775e94457/USER',
                
	'150':'/SingleElectron/jfernan2-R42X_S1_V08_S2_V05_S3_V11_ID150_SingleElectron2011AMay10-47b630e2469c9e3550fd039775e94457/USER',
	'151':'/SingleMu/jfernan2-R42X_S1_V08_S2_V05_S3_V11_ID151_SingleMuon2011AMay10-47b630e2469c9e3550fd039775e94457/USER',
	'152':'/DoubleMu/jfernan2-R42X_S1_V08_S2_V05_S3_V11_ID152_DoubleMuon2011AMay10-47b630e2469c9e3550fd039775e94457/USER',
	'153':'/DoubleElectron/jfernan2-R42X_S1_V08_S2_V05_S3_V11_ID153_DoubleElectron2011AMay10-47b630e2469c9e3550fd039775e94457/USER',
	'154':'/MuEG/jfernan2-R42X_S1_V08_S2_V05_S3_V11_ID154_MuEG2011AMay10-47b630e2469c9e3550fd039775e94457/USER',
                
	'160':'/SingleElectron/jfernan2-R42X_S1_V08_S2_V05_S3_V11_ID160_SingleElectron2011AAug05-47b630e2469c9e3550fd039775e94457/USER',
	'161':'/SingleMu/jfernan2-R42X_S1_V08_S2_V05_S3_V11_ID161_SingleMuon2011AAug05-47b630e2469c9e3550fd039775e94457/USER',
	'162':'/DoubleElectron/jfernan2-R42X_S1_V08_S2_V05_S3_V11_ID162_DoubleElectron2011AAug05-47b630e2469c9e3550fd039775e94457/USER',
	'163':'/DoubleMu/jfernan2-R42X_S1_V08_S2_V05_S3_V11_ID163_DoubleMuon2011AAug05-47b630e2469c9e3550fd039775e94457/USER',
	'164':'/MuEG/jfernan2-R42X_S1_V08_S2_V05_S3_V11_ID164_MuEG2011AAug05-47b630e2469c9e3550fd039775e94457/USER',
                
                
	'1120':'/GluGluToHToWWTo2L2Nu_M-120_7TeV-powheg-pythia6/mangano-R42X_S1_V09_S2_V06_S3_V13_ID1120_ggToH120toWWto2L2Nu-v2-26a07df0670d12c6eef310bf324d6d6d/USER',
	'1130':'/GluGluToHToWWTo2L2Nu_M-130_7TeV-powheg-pythia6/mangano-R42X_S1_V09_S2_V06_S3_V13_ID1130_ggToH130toWWto2L2Nu-26a07df0670d12c6eef310bf324d6d6d/USER',
	'1140':'/GluGluToHToWWTo2L2Nu_M-140_7TeV-powheg-pythia6/mangano-R42X_S1_V09_S2_V06_S3_V13_ID1140_ggToH140toWWto2L2Nu-26a07df0670d12c6eef310bf324d6d6d/USER',
	'1150':'/GluGluToHToWWTo2L2Nu_M-150_7TeV-powheg-pythia6/mangano-R42X_S1_V09_S2_V06_S3_V13_ID1150_ggToH150toWWto2L2Nu-v2-26a07df0670d12c6eef310bf324d6d6d/USER',
	'1160':'/GluGluToHToWWTo2L2Nu_M-160_7TeV-powheg-pythia6/mangano-R42X_S1_V09_S2_V06_S3_V13_ID1160_ggToH160toWWto2L2Nu-v3-26a07df0670d12c6eef310bf324d6d6d/USER',
	'1170':'/GluGluToHToWWTo2L2Nu_M-170_7TeV-powheg-pythia6/mangano-R42X_S1_V09_S2_V06_S3_V13_ID1170_ggToH170toWWto2L2Nu-26a07df0670d12c6eef310bf324d6d6d/USER',
	'1180':'',
	'1190':'/GluGluToHToWWTo2L2Nu_M-190_7TeV-powheg-pythia6/mangano-R42X_S1_V09_S2_V06_S3_V13_ID1190_ggToH190toWWto2L2Nu-26a07df0670d12c6eef310bf324d6d6d/USER',
	'1200':'/GluGluToHToWWTo2L2Nu_M-200_7TeV-powheg-pythia6/mangano-R42X_S1_V09_S2_V06_S3_V13_ID1200_ggToH200toWWto2L2Nu-26a07df0670d12c6eef310bf324d6d6d/USER',
	'1210':'/GluGluToHToWWTo2L2Nu_M-210_7TeV-powheg-pythia6/mangano-R42X_S1_V09_S2_V06_S3_V13_ID1210_ggToH210toWWto2L2Nu-26a07df0670d12c6eef310bf324d6d6d/USER',
	'1220':'/GluGluToHToWWTo2L2Nu_M-220_7TeV-powheg-pythia6/mangano-R42X_S1_V09_S2_V06_S3_V13_ID1220_ggToH220toWWto2L2Nu-26a07df0670d12c6eef310bf324d6d6d/USER',
	'1230':'/GluGluToHToWWTo2L2Nu_M-230_7TeV-powheg-pythia6/mangano-R42X_S1_V09_S2_V06_S3_V13_ID1230_ggToH230toWWto2L2Nu-26a07df0670d12c6eef310bf324d6d6d/USER',
	'1250':'/GluGluToHToWWTo2L2Nu_M-250_7TeV-powheg-pythia6/mangano-R42X_S1_V09_S2_V06_S3_V13_ID1250_ggToH250toWWto2L2Nu-26a07df0670d12c6eef310bf324d6d6d/USER',
	'1300':'/GluGluToHToWWTo2L2Nu_M-300_7TeV-powheg-pythia6/mangano-R42X_S1_V09_S2_V06_S3_V13_ID1300_ggToH300toWWto2L2Nu-26a07df0670d12c6eef310bf324d6d6d/USER',
	'1350':'/GluGluToHToWWTo2L2Nu_M-350_7TeV-powheg-pythia6/mangano-R42X_S1_V09_S2_V06_S3_V13_ID1350_ggToH350toWWto2L2Nu-26a07df0670d12c6eef310bf324d6d6d/USER',
	'1400':'/GluGluToHToWWTo2L2Nu_M-400_7TeV-powheg-pythia6/mangano-R42X_S1_V09_S2_V06_S3_V13_ID1400_ggToH400toWWto2L2Nu-26a07df0670d12c6eef310bf324d6d6d/USER',
	'1450':'/GluGluToHToWWTo2L2Nu_M-450_7TeV-powheg-pythia6/mangano-R42X_S1_V09_S2_V06_S3_V13_ID1450_ggToH450toWWto2L2Nu-26a07df0670d12c6eef310bf324d6d6d/USER',
	'1500':'/GluGluToHToWWTo2L2Nu_M-500_7TeV-powheg-pythia6/mangano-R42X_S1_V09_S2_V06_S3_V13_ID1500_ggToH500toWWto2L2Nu-26a07df0670d12c6eef310bf324d6d6d/USER',
	'1550':'/GluGluToHToWWTo2L2Nu_M-550_7TeV-powheg-pythia6/mangano-R42X_S1_V09_S2_V06_S3_V13_ID1550_ggToH550toWWto2L2Nu-26a07df0670d12c6eef310bf324d6d6d/USER',
	'1600':'/GluGluToHToWWTo2L2Nu_M-600_7TeV-powheg-pythia6/mangano-R42X_S1_V09_S2_V06_S3_V13_ID1600_ggToH600toWWto2L2Nu-26a07df0670d12c6eef310bf324d6d6d/USER',
                
	'2120':'/GluGluToHToWWToLNuTauNu_M-120_7TeV-powheg-pythia6/mangano-R42X_S1_V09_S2_V06_S3_V13_ID2120_ggToH120toWWtoLNuTauNu-26a07df0670d12c6eef310bf324d6d6d/USER',
	'2130':'/GluGluToHToWWToLNuTauNu_M-130_7TeV-powheg-pythia6/mangano-R42X_S1_V09_S2_V06_S3_V13_ID2130_ggToH130toWWtoLNuTauNu-26a07df0670d12c6eef310bf324d6d6d/USER',
	'2140':'/GluGluToHToWWToLNuTauNu_M-140_7TeV-powheg-pythia6/mangano-R42X_S1_V09_S2_V06_S3_V13_ID2140_ggToH140toWWtoLNuTauNu-26a07df0670d12c6eef310bf324d6d6d/USER',
	'2150':'/GluGluToHToWWToLNuTauNu_M-150_7TeV-powheg-pythia6/mangano-R42X_S1_V09_S2_V06_S3_V13_ID2150_ggToH150toWWtoLNuTauNu-26a07df0670d12c6eef310bf324d6d6d/USER',
	'2160':'/GluGluToHToWWToLNuTauNu_M-160_7TeV-powheg-pythia6/mangano-R42X_S1_V09_S2_V06_S3_V13_ID2160_ggToH160toWWtoLNuTauNu-26a07df0670d12c6eef310bf324d6d6d/USER',
	'2170':'/GluGluToHToWWToLNuTauNu_M-170_7TeV-powheg-pythia6/mangano-R42X_S1_V09_S2_V06_S3_V13_ID2170_ggToH170toWWtoLNuTauNu-26a07df0670d12c6eef310bf324d6d6d/USER',
	'2180':'/GluGluToHToWWToLNuTauNu_M-180_7TeV-powheg-pythia6/mangano-R42X_S1_V09_S2_V06_S3_V13_ID2180_ggToH180toWWtoLNuTauNu-26a07df0670d12c6eef310bf324d6d6d/USER',
	'2190':'/GluGluToHToWWToLNuTauNu_M-190_7TeV-powheg-pythia6/mangano-R42X_S1_V09_S2_V06_S3_V13_ID2190_ggToH190toWWtoLNuTauNu-26a07df0670d12c6eef310bf324d6d6d/USER',
	'2200':'/GluGluToHToWWToLNuTauNu_M-200_7TeV-powheg-pythia6/mangano-R42X_S1_V09_S2_V06_S3_V13_ID2200_ggToH200toWWtoLNuTauNu-26a07df0670d12c6eef310bf324d6d6d/USER',
	'2210':'/GluGluToHToWWToLNuTauNu_M-210_7TeV-powheg-pythia6/mangano-R42X_S1_V09_S2_V06_S3_V13_ID2210_ggToH210toWWtoLNuTauNu-v3-26a07df0670d12c6eef310bf324d6d6d/USER',
	'2220':'/GluGluToHToWWToLNuTauNu_M-220_7TeV-powheg-pythia6/mangano-R42X_S1_V09_S2_V06_S3_V13_ID2220_ggToH220toWWtoLNuTauNu-26a07df0670d12c6eef310bf324d6d6d/USER',
	'2230':'/GluGluToHToWWToLNuTauNu_M-230_7TeV-powheg-pythia6/mangano-R42X_S1_V09_S2_V06_S3_V13_ID2230_ggToH230toWWtoLNuTauNu-26a07df0670d12c6eef310bf324d6d6d/USER',
	'2250':'/GluGluToHToWWToLNuTauNu_M-250_7TeV-powheg-pythia6/mangano-R42X_S1_V09_S2_V06_S3_V13_ID2250_ggToH250toWWtoLNuTauNu-26a07df0670d12c6eef310bf324d6d6d/USER',
	'2300':'/GluGluToHToWWToLNuTauNu_M-300_7TeV-powheg-pythia6/mangano-R42X_S1_V09_S2_V06_S3_V13_ID2300_ggToH300toWWtoLNuTauNu-26a07df0670d12c6eef310bf324d6d6d/USER',
	'2350':'/GluGluToHToWWToLNuTauNu_M-350_7TeV-powheg-pythia6/mangano-R42X_S1_V09_S2_V06_S3_V13_ID2350_ggToH350toWWtoLNuTauNu-26a07df0670d12c6eef310bf324d6d6d/USER',
	'2400':'/GluGluToHToWWToLNuTauNu_M-400_7TeV-powheg-pythia6/mangano-R42X_S1_V09_S2_V06_S3_V13_ID2400_ggToH400toWWtoLNuTauNu-26a07df0670d12c6eef310bf324d6d6d/USER',
	'2450':'/GluGluToHToWWToLNuTauNu_M-450_7TeV-powheg-pythia6/mangano-R42X_S1_V09_S2_V06_S3_V13_ID2450_ggToH450toWWtoLNuTauNu-26a07df0670d12c6eef310bf324d6d6d/USER',
	'2500':'/GluGluToHToWWToLNuTauNu_M-500_7TeV-powheg-pythia6/mangano-R42X_S1_V09_S2_V06_S3_V13_ID2500_ggToH500toWWtoLNuTauNu-26a07df0670d12c6eef310bf324d6d6d/USER',
	'2550':'/GluGluToHToWWToLNuTauNu_M-550_7TeV-powheg-pythia6/mangano-R42X_S1_V09_S2_V06_S3_V13_ID2550_ggToH550toWWtoLNuTauNu-26a07df0670d12c6eef310bf324d6d6d/USER',
	'2600':'/GluGluToHToWWToLNuTauNu_M-600_7TeV-powheg-pythia6/mangano-R42X_S1_V09_S2_V06_S3_V13_ID2600_ggToH600toWWtoLNuTauNu-26a07df0670d12c6eef310bf324d6d6d/USER',
                
	'3120':'',
	'3130':'',
	'3140':'',
	'3150':'',
	'3160':'',
	'3170':'',
	'3180':'',
	'3190':'',
	'3200':'',
	'3210':'',
	'3220':'',
	'3230':'',
	'3250':'',
	'3300':'',
	'3350':'',
	'3400':'',
	'3450':'',
	'3500':'',
	'3550':'',
	'3600':'',
                
	'4120':'/VBF_HToWWTo2L2Nu_M-120_7TeV-powheg-pythia6/mangano-R42X_S1_V09_S2_V06_S3_V13_ID4120_vbfToH120toWWto2L2Nu-26a07df0670d12c6eef310bf324d6d6d/USER',
	'4130':'/VBF_HToWWTo2L2Nu_M-130_7TeV-powheg-pythia6/mangano-R42X_S1_V09_S2_V06_S3_V13_ID4130_vbfToH130toWWto2L2Nu-26a07df0670d12c6eef310bf324d6d6d/USER',
	'4140':'/VBF_HToWWTo2L2Nu_M-140_7TeV-powheg-pythia6/mangano-R42X_S1_V09_S2_V06_S3_V13_ID4140_vbfToH140toWWto2L2Nu-26a07df0670d12c6eef310bf324d6d6d/USER',
	'4150':'',
	'4160':'/VBF_HToWWTo2L2Nu_M-160_7TeV-powheg-pythia6/mangano-R42X_S1_V09_S2_V06_S3_V13_ID4160_vbfToH160toWWto2L2Nu-26a07df0670d12c6eef310bf324d6d6d/USER',
	'4170':'/VBF_HToWWTo2L2Nu_M-170_7TeV-powheg-pythia6/mangano-R42X_S1_V09_S2_V06_S3_V13_ID4170_vbfToH170toWWto2L2Nu-26a07df0670d12c6eef310bf324d6d6d/USER',
	'4180':'/VBF_HToWWTo2L2Nu_M-180_7TeV-powheg-pythia6/mangano-R42X_S1_V09_S2_V06_S3_V13_ID4180_vbfToH180toWWto2L2Nu-26a07df0670d12c6eef310bf324d6d6d/USER',
	'4190':'/VBF_HToWWTo2L2Nu_M-190_7TeV-powheg-pythia6/mangano-R42X_S1_V09_S2_V06_S3_V13_ID4190_vbfToH190toWWto2L2Nu-26a07df0670d12c6eef310bf324d6d6d/USER',
	'4200':'/VBF_HToWWTo2L2Nu_M-200_7TeV-powheg-pythia6/mangano-R42X_S1_V09_S2_V06_S3_V13_ID4200_vbfToH200toWWto2L2Nu-26a07df0670d12c6eef310bf324d6d6d/USER',
	'4210':'/VBF_HToWWTo2L2Nu_M-210_7TeV-powheg-pythia6/mangano-R42X_S1_V09_S2_V06_S3_V13_ID4210_vbfToH210toWWto2L2Nu-26a07df0670d12c6eef310bf324d6d6d/USER',
	'4220':'/VBF_HToWWTo2L2Nu_M-220_7TeV-powheg-pythia6/mangano-R42X_S1_V09_S2_V06_S3_V13_ID4220_vbfToH220toWWto2L2Nu-26a07df0670d12c6eef310bf324d6d6d/USER',
	'4230':'/VBF_HToWWTo2L2Nu_M-230_7TeV-powheg-pythia6/mangano-R42X_S1_V09_S2_V06_S3_V13_ID4230_vbfToH230toWWto2L2Nu-26a07df0670d12c6eef310bf324d6d6d/USER',
	'4250':'/VBF_HToWWTo2L2Nu_M-250_7TeV-powheg-pythia6/mangano-R42X_S1_V09_S2_V06_S3_V13_ID4250_vbfToH250toWWto2L2Nu-26a07df0670d12c6eef310bf324d6d6d/USER',
	'4300':'/VBF_HToWWTo2L2Nu_M-300_7TeV-powheg-pythia6/mangano-R42X_S1_V09_S2_V06_S3_V13_ID4300_vbfToH300toWWto2L2Nu-26a07df0670d12c6eef310bf324d6d6d/USER',
	'4350':'/VBF_HToWWTo2L2Nu_M-350_7TeV-powheg-pythia6/mangano-R42X_S1_V09_S2_V06_S3_V13_ID4350_vbfToH350toWWto2L2Nu-26a07df0670d12c6eef310bf324d6d6d/USER',
	'4400':'/VBF_HToWWTo2L2Nu_M-400_7TeV-powheg-pythia6/mangano-R42X_S1_V09_S2_V06_S3_V13_ID4400_vbfToH400toWWto2L2Nu-26a07df0670d12c6eef310bf324d6d6d/USER',
	'4450':'/VBF_HToWWTo2L2Nu_M-450_7TeV-powheg-pythia6/mangano-R42X_S1_V09_S2_V06_S3_V13_ID4450_vbfToH450toWWto2L2Nu-26a07df0670d12c6eef310bf324d6d6d/USER',
	'4500':'/VBF_HToWWTo2L2Nu_M-500_7TeV-powheg-pythia6/mangano-R42X_S1_V09_S2_V06_S3_V13_ID4500_vbfToH500toWWto2L2Nu-26a07df0670d12c6eef310bf324d6d6d/USER',
	'4550':'/VBF_HToWWTo2L2Nu_M-550_7TeV-powheg-pythia6/mangano-R42X_S1_V09_S2_V06_S3_V13_ID4550_vbfToH550toWWto2L2Nu-26a07df0670d12c6eef310bf324d6d6d/USER',
	'4600':'/VBF_HToWWTo2L2Nu_M-600_7TeV-powheg-pythia6/mangano-R42X_S1_V09_S2_V06_S3_V13_ID4600_vbfToH600toWWto2L2Nu-26a07df0670d12c6eef310bf324d6d6d/USER',
                
	'5120':'/VBF_HToWWToLNuTauNu_M-120_7TeV-powheg-pythia6/mangano-R42X_S1_V09_S2_V06_S3_V13_ID5120_vbfToH120toWWtoLNuTauNu-26a07df0670d12c6eef310bf324d6d6d/USER',
	'5130':'/VBF_HToWWToLNuTauNu_M-130_7TeV-powheg-pythia6/mangano-R42X_S1_V09_S2_V06_S3_V13_ID5130_vbfToH130toWWtoLNuTauNu-26a07df0670d12c6eef310bf324d6d6d/USER',
	'5140':'/VBF_HToWWToLNuTauNu_M-140_7TeV-powheg-pythia6/mangano-R42X_S1_V09_S2_V06_S3_V13_ID5140_vbfToH140toWWtoLNuTauNu-26a07df0670d12c6eef310bf324d6d6d/USER',
	'5150':'/VBF_HToWWToLNuTauNu_M-150_7TeV-powheg-pythia6/mangano-R42X_S1_V09_S2_V06_S3_V13_ID5150_vbfToH150toWWtoLNuTauNu-26a07df0670d12c6eef310bf324d6d6d/USER',
	'5160':'/VBF_HToWWToLNuTauNu_M-160_7TeV-powheg-pythia6/mangano-R42X_S1_V09_S2_V06_S3_V13_ID5160_vbfToH160toWWtoLNuTauNu-26a07df0670d12c6eef310bf324d6d6d/USER',
	'5170':'/VBF_HToWWToLNuTauNu_M-170_7TeV-powheg-pythia6/mangano-R42X_S1_V09_S2_V06_S3_V13_ID5170_vbfToH170toWWtoLNuTauNu-26a07df0670d12c6eef310bf324d6d6d/USER',
	'5180':'/VBF_HToWWToLNuTauNu_M-180_7TeV-powheg-pythia6/mangano-R42X_S1_V09_S2_V06_S3_V13_ID5180_vbfToH180toWWtoLNuTauNu-26a07df0670d12c6eef310bf324d6d6d/USER',
	'5190':'/VBF_HToWWToLNuTauNu_M-190_7TeV-powheg-pythia6/mangano-R42X_S1_V09_S2_V06_S3_V13_ID5190_vbfToH190toWWtoLNuTauNu-26a07df0670d12c6eef310bf324d6d6d/USER',
	'5200':'/VBF_HToWWToLNuTauNu_M-200_7TeV-powheg-pythia6/mangano-R42X_S1_V09_S2_V06_S3_V13_ID5200_vbfToH200toWWtoLNuTauNu-26a07df0670d12c6eef310bf324d6d6d/USER',
	'5210':'/VBF_HToWWToLNuTauNu_M-210_7TeV-powheg-pythia6/mangano-R42X_S1_V09_S2_V06_S3_V13_ID5210_vbfToH210toWWtoLNuTauNu-26a07df0670d12c6eef310bf324d6d6d/USER',
	'5220':'/VBF_HToWWToLNuTauNu_M-220_7TeV-powheg-pythia6/mangano-R42X_S1_V09_S2_V06_S3_V13_ID5220_vbfToH220toWWtoLNuTauNu-26a07df0670d12c6eef310bf324d6d6d/USER',
	'5230':'/VBF_HToWWToLNuTauNu_M-230_7TeV-powheg-pythia6/mangano-R42X_S1_V09_S2_V06_S3_V13_ID5230_vbfToH230toWWtoLNuTauNu-26a07df0670d12c6eef310bf324d6d6d/USER',
	'5250':'/VBF_HToWWToLNuTauNu_M-250_7TeV-powheg-pythia6/mangano-R42X_S1_V09_S2_V06_S3_V13_ID5250_vbfToH250toWWtoLNuTauNu-26a07df0670d12c6eef310bf324d6d6d/USER',
	'5300':'/VBF_HToWWToLNuTauNu_M-300_7TeV-powheg-pythia6/mangano-R42X_S1_V09_S2_V06_S3_V13_ID5300_vbfToH300toWWtoLNuTauNu-26a07df0670d12c6eef310bf324d6d6d/USER',
	'5350':'/VBF_HToWWToLNuTauNu_M-350_7TeV-powheg-pythia6/mangano-R42X_S1_V09_S2_V06_S3_V13_ID5350_vbfToH350toWWtoLNuTauNu-26a07df0670d12c6eef310bf324d6d6d/USER',
	'5400':'/VBF_HToWWToLNuTauNu_M-400_7TeV-powheg-pythia6/mangano-R42X_S1_V09_S2_V06_S3_V13_ID5400_vbfToH400toWWtoLNuTauNu-26a07df0670d12c6eef310bf324d6d6d/USER',
	'5450':'/VBF_HToWWToLNuTauNu_M-450_7TeV-powheg-pythia6/mangano-R42X_S1_V09_S2_V06_S3_V13_ID5450_vbfToH450toWWtoLNuTauNu-26a07df0670d12c6eef310bf324d6d6d/USER',
	'5500':'/VBF_HToWWToLNuTauNu_M-500_7TeV-powheg-pythia6/mangano-R42X_S1_V09_S2_V06_S3_V13_ID5500_vbfToH500toWWtoLNuTauNu-26a07df0670d12c6eef310bf324d6d6d/USER',
	'5550':'/VBF_HToWWToLNuTauNu_M-550_7TeV-powheg-pythia6/mangano-R42X_S1_V09_S2_V06_S3_V13_ID5550_vbfToH550toWWtoLNuTauNu-26a07df0670d12c6eef310bf324d6d6d/USER',
	'5600':'/VBF_HToWWToLNuTauNu_M-600_7TeV-powheg-pythia6/mangano-R42X_S1_V09_S2_V06_S3_V13_ID5600_vbfToH600toWWtoLNuTauNu-26a07df0670d12c6eef310bf324d6d6d/USER',
                
	'6120':'/VBF_HToWWTo2Tau2Nu_M-120_7TeV-powheg-pythia6/mangano-R42X_S1_V09_S2_V06_S3_V13_ID6120_vbfToH120toWWto2Tau2Nu-26a07df0670d12c6eef310bf324d6d6d/USER',
	'6130':'',
	'6140':'/VBF_HToWWTo2Tau2Nu_M-140_7TeV-powheg-pythia6/mangano-R42X_S1_V09_S2_V06_S3_V13_ID6140_vbfToH140toWWto2Tau2Nu-26a07df0670d12c6eef310bf324d6d6d/USER',
	'6150':'/VBF_HToWWTo2Tau2Nu_M-150_7TeV-powheg-pythia6/mangano-R42X_S1_V09_S2_V06_S3_V13_ID6150_vbfToH150toWWto2Tau2Nu-v2-26a07df0670d12c6eef310bf324d6d6d/USER',
	'6160':'/VBF_HToWWTo2Tau2Nu_M-160_7TeV-powheg-pythia6/mangano-R42X_S1_V09_S2_V06_S3_V13_ID6160_vbfToH160toWWto2Tau2Nu-26a07df0670d12c6eef310bf324d6d6d/USER',
	'6170':'/VBF_HToWWTo2Tau2Nu_M-170_7TeV-powheg-pythia6/mangano-R42X_S1_V09_S2_V06_S3_V13_ID6170_vbfToH170toWWto2Tau2Nu-26a07df0670d12c6eef310bf324d6d6d/USER',
	'6180':'/VBF_HToWWTo2Tau2Nu_M-180_7TeV-powheg-pythia6/mangano-R42X_S1_V09_S2_V06_S3_V13_ID6180_vbfToH180toWWto2Tau2Nu-26a07df0670d12c6eef310bf324d6d6d/USER',
	'6190':'/VBF_HToWWTo2Tau2Nu_M-190_7TeV-powheg-pythia6/mangano-R42X_S1_V09_S2_V06_S3_V13_ID6190_vbfToH190toWWto2Tau2Nu-26a07df0670d12c6eef310bf324d6d6d/USER',
	'6200':'/VBF_HToWWTo2Tau2Nu_M-200_7TeV-powheg-pythia6/mangano-R42X_S1_V09_S2_V06_S3_V13_ID6200_vbfToH200toWWto2Tau2Nu-26a07df0670d12c6eef310bf324d6d6d/USER',
	'6210':'/VBF_HToWWTo2Tau2Nu_M-210_7TeV-powheg-pythia6/mangano-R42X_S1_V09_S2_V06_S3_V13_ID6210_vbfToH210toWWto2Tau2Nu-26a07df0670d12c6eef310bf324d6d6d/USER',
	'6220':'/VBF_HToWWTo2Tau2Nu_M-220_7TeV-powheg-pythia6/mangano-R42X_S1_V09_S2_V06_S3_V13_ID6220_vbfToH220toWWto2Tau2Nu-26a07df0670d12c6eef310bf324d6d6d/USER',
	'6230':'/VBF_HToWWTo2Tau2Nu_M-230_7TeV-powheg-pythia6/mangano-R42X_S1_V09_S2_V06_S3_V13_ID6230_vbfToH230toWWto2Tau2Nu-26a07df0670d12c6eef310bf324d6d6d/USER',
	'6250':'/VBF_HToWWTo2Tau2Nu_M-250_7TeV-powheg-pythia6/mangano-R42X_S1_V09_S2_V06_S3_V13_ID6250_vbfToH250toWWto2Tau2Nu-26a07df0670d12c6eef310bf324d6d6d/USER',
	'6300':'/VBF_HToWWTo2Tau2Nu_M-300_7TeV-powheg-pythia6/mangano-R42X_S1_V09_S2_V06_S3_V13_ID6300_vbfToH300toWWto2Tau2Nu-26a07df0670d12c6eef310bf324d6d6d/USER',
	'6350':'/VBF_HToWWTo2Tau2Nu_M-350_7TeV-powheg-pythia6/mangano-R42X_S1_V09_S2_V06_S3_V13_ID6350_vbfToH350toWWto2Tau2Nu-26a07df0670d12c6eef310bf324d6d6d/USER',
	'6400':'/VBF_HToWWTo2Tau2Nu_M-400_7TeV-powheg-pythia6/mangano-R42X_S1_V09_S2_V06_S3_V13_ID6400_vbfToH400toWWto2Tau2Nu-26a07df0670d12c6eef310bf324d6d6d/USER',
	'6450':'/VBF_HToWWTo2Tau2Nu_M-450_7TeV-powheg-pythia6/mangano-R42X_S1_V09_S2_V06_S3_V13_ID6450_vbfToH450toWWto2Tau2Nu-v2-26a07df0670d12c6eef310bf324d6d6d/USER',
	'6500':'/VBF_HToWWTo2Tau2Nu_M-500_7TeV-powheg-pythia6/mangano-R42X_S1_V09_S2_V06_S3_V13_ID6500_vbfToH500toWWto2Tau2Nu-26a07df0670d12c6eef310bf324d6d6d/USER',
	'6550':'/VBF_HToWWTo2Tau2Nu_M-550_7TeV-powheg-pythia6/mangano-R42X_S1_V09_S2_V06_S3_V13_ID6550_vbfToH550toWWto2Tau2Nu-26a07df0670d12c6eef310bf324d6d6d/USER',
	'6600':'/VBF_HToWWTo2Tau2Nu_M-600_7TeV-powheg-pythia6/mangano-R42X_S1_V09_S2_V06_S3_V13_ID6600_vbfToH600toWWto2Tau2Nu-26a07df0670d12c6eef310bf324d6d6d/USER',
                
	'7120':'/WH_ZH_TTH_HToWW_M-120_7TeV-pythia6/mangano-R42X_S1_V09_S2_V06_S3_V13_ID7120_wzttH120ToWW-26a07df0670d12c6eef310bf324d6d6d/USER',
	'7130':'/WH_ZH_TTH_HToWW_M-130_7TeV-pythia6/mangano-R42X_S1_V09_S2_V06_S3_V13_ID7130_wzttH130ToWW-26a07df0670d12c6eef310bf324d6d6d/USER',
	'7140':'/WH_ZH_TTH_HToWW_M-140_7TeV-pythia6/mangano-R42X_S1_V09_S2_V06_S3_V13_ID7140_wzttH140ToWW-26a07df0670d12c6eef310bf324d6d6d/USER',
	'7150':'/WH_ZH_TTH_HToWW_M-170_7TeV-pythia6/mangano-R42X_S1_V09_S2_V06_S3_V13_ID7150_wzttH150ToWW-26a07df0670d12c6eef310bf324d6d6d/USER',
	'7160':'/WH_ZH_TTH_HToWW_M-160_7TeV-pythia6/mangano-R42X_S1_V09_S2_V06_S3_V13_ID7160_wzttH160ToWW-26a07df0670d12c6eef310bf324d6d6d/USER',
	'7170':'/WH_ZH_TTH_HToWW_M-180_7TeV-pythia6/mangano-R42X_S1_V09_S2_V06_S3_V13_ID7180_wzttH180ToWW-26a07df0670d12c6eef310bf324d6d6d/USER',
	'7180':'/WH_ZH_TTH_HToWW_M-190_7TeV-pythia6/mangano-R42X_S1_V09_S2_V06_S3_V13_ID7190_wzttH190ToWW-26a07df0670d12c6eef310bf324d6d6d/USER',
	'7190':'/WH_ZH_TTH_HToWW_M-250_7TeV-pythia6/mangano-R42X_S1_V09_S2_V06_S3_V13_ID7250_wzttH250ToWW-26a07df0670d12c6eef310bf324d6d6d/USER',
	'7200':'/WH_ZH_TTH_HToWW_M-200_7TeV-pythia6/mangano-R42X_S1_V09_S2_V06_S3_V13_ID7200_wzttH200ToWW-26a07df0670d12c6eef310bf324d6d6d/USER',
	'7250':'/WH_ZH_TTH_HToWW_M-300_7TeV-pythia6/mangano-R42X_S1_V09_S2_V06_S3_V13_ID7300_wzttH300ToWW-26a07df0670d12c6eef310bf324d6d6d/USER',
	'7300':'/WH_ZH_TTH_HToWW_M-350_7TeV-pythia6/mangano-R42X_S1_V09_S2_V06_S3_V13_ID7350_wzttH350ToWW-26a07df0670d12c6eef310bf324d6d6d/USER',
	'7350':'/WH_ZH_TTH_HToWW_M-400_7TeV-pythia6/mangano-R42X_S1_V09_S2_V06_S3_V13_ID7400_wzttH400ToWW-26a07df0670d12c6eef310bf324d6d6d/USER',
	'7400':'/WH_ZH_TTH_HToWW_M-450_7TeV-pythia6/mangano-R42X_S1_V09_S2_V06_S3_V13_ID7450_wzttH450ToWW-26a07df0670d12c6eef310bf324d6d6d/USER',
	'7450':'/WH_ZH_TTH_HToWW_M-500_7TeV-pythia6/mangano-R42X_S1_V09_S2_V06_S3_V13_ID7500_wzttH500ToWW-26a07df0670d12c6eef310bf324d6d6d/USER',
	'7500':'/WH_ZH_TTH_HToWW_M-550_7TeV-pythia6/mangano-R42X_S1_V09_S2_V06_S3_V13_ID7550_wzttH550ToWW-26a07df0670d12c6eef310bf324d6d6d/USER',
	'7550':'/WH_ZH_TTH_HToWW_M-600_7TeV-pythia6/mangano-R42X_S1_V09_S2_V06_S3_V13_ID7600_wzttH600ToWW-26a07df0670d12c6eef310bf324d6d6d/USER',
	'7600':'',
                
	'8110':'/VBF_HToWWTo2LAndTau2Nu_M-110_7TeV-powheg-pythia6/mangano-R42X_S1_V09_S2_V06_S3_V13_ID8110_vbfToH110toWWTo2LAndTau2Nu-26a07df0670d12c6eef310bf324d6d6d/USER',
	'8115':'/VBF_HToWWTo2LAndTau2Nu_M-115_7TeV-powheg-pythia6/mangano-R42X_S1_V09_S2_V06_S3_V13_ID8115_vbfToH115toWWTo2LAndTau2Nu-v2-26a07df0670d12c6eef310bf324d6d6d/USER',
                
	'9110':'/GluGluToHToWWTo2LAndTau2Nu_M-110_7TeV-powheg-pythia6/mangano-R42X_S1_V09_S2_V06_S3_V13_ID9110_ggToH110toWWTo2LAndTau2Nu-26a07df0670d12c6eef310bf324d6d6d/USER',
	'9115':'/GluGluToHToWWTo2LAndTau2Nu_M-115_7TeV-powheg-pythia6/mangano-R42X_S1_V09_S2_V06_S3_V13_ID9115_ggToH115toWWTo2LAndTau2Nu-26a07df0670d12c6eef310bf324d6d6d/USER',
                
}

stepOneDatasetsSummer = {
    '000':'/WWJetsTo2L2Nu_TuneZ2_7TeV-madgraph-tauola/jfernan2-R42X_S1_V06_S2_V02_S3_V05_ID000_WWJets2LMad-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '001':'/GluGluToWWTo4L_TuneZ2_7TeV-gg2ww-pythia6/jfernan2-R42X_S1_V06_S2_V02_S3_V05_ID001_GluGluToWWTo4L-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '002':'/WWTo2L2Nu_CT10_7TeV-mcatnlo/mwlebour-R42X_S1_V06_S2_V04_S3_V06_ID002_WWto2L2NuMCatNLO_v3-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '003':'/WWTo2L2Nu_scaleup_CT10_7TeV-mcatnlo/mwlebour-R42X_S1_V06_S2_V04_S3_V06_ID003_WWto2L2NuMCatNLOUp_v3-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '004':'/WWTo2L2Nu_scaledown_CT10_7TeV-mcatnlo/mwlebour-R42X_S1_V06_S2_V04_S3_V06_ID004_WWto2L2NuMCatNLODown_v3-a90b596e1a39c995fc1403cf7cc2b14b/USER',



    '010':'/TTJets_TuneZ2_7TeV-madgraph-tauola/mwlebour-R42X_S1_V06_S2_V02_S3_V05_ID010_TTJetsMad-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '011':'/T_TuneZ2_tW-channel-DR_7TeV-powheg-tauola/mwlebour-R42X_S1_V06_S2_V02_S3_V05_ID011_TtWFullDR-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '012':'/Tbar_TuneZ2_tW-channel-DR_7TeV-powheg-tauola/mwlebour-R42X_S1_V06_S2_V02_S3_V05_ID012_TbartWFullDR-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '013':'/T_TuneZ2_t-channel_7TeV-powheg-tauola/mwlebour-R42X_S1_V06_S2_V02_S3_V05_ID013_TtFull_v3-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '014':'/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/mwlebour-R42X_S1_V06_S2_V02_S3_V05_ID014_TbartFull-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '015':'/T_TuneZ2_s-channel_7TeV-powheg-tauola/mwlebour-R42X_S1_V06_S2_V02_S3_V05_ID015_TsFull-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '016':'/Tbar_TuneZ2_s-channel_7TeV-powheg-tauola/mwlebour-R42X_S1_V06_S2_V02_S3_V05_ID016_TbarsFull-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '017':'/T_TuneZ2_tW-channel-DS_7TeV-powheg-tauola/mwlebour-R42X_S1_V06_S2_V04_S3_V06_ID017_TtWFullDS_v3-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '018':'/Tbar_TuneZ2_tW-channel-DS_7TeV-powheg-tauola/mwlebour-R42X_S1_V06_S2_V04_S3_V06_ID018_TbartWFullDS_v3-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '019':'/TTTo2L2Nu2B_7TeV-powheg-pythia6/jfernan2-R42X_S1_V06_S2_V02_S3_V05_ID019_TTTo2L2Nu2B-3458aa0bd471577b09aa6b73035cd433/USER',


    '030':'/DYToEE_M-20_CT10_TuneZ2_7TeV-powheg-pythia/mwlebour-R42X_S1_V06_S2_V02_S3_V05_ID030_DYtoElEl-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '031':'/DYToMuMu_M-20_CT10_TuneZ2_7TeV-powheg-pythia/mwlebour-R42X_S1_V06_S2_V02_S3_V05_ID031_DYtoMuMu-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '032':'/DYToTauTau_M-20_CT10_TuneZ2_7TeV-powheg-pythia-tauola/mwlebour-R42X_S1_V06_S2_V02_S3_V05_ID032_DYtoTauTau-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '033':'/DYToEE_M-10To20_CT10_TuneZ2_7TeV-powheg-pythia/mwlebour-R42X_S1_V06_S2_V03_S3_V06_ID033_DY10toElElv2_v3-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '034':'/DYToMuMu_M-10To20_CT10_TuneZ2_7TeV-powheg-pythia/mwlebour-R42X_S1_V06_S2_V03_S3_V06_ID034_DY10toMuMuv2_v3-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '035':'/DYToTauTau_M-10To20_TuneZ2_7TeV-pythia6-tauola/mwlebour-R42X_S1_V06_S2_V02_S3_V05_ID035_DY10toTauTau-a90b596e1a39c995fc1403cf7cc2b14b/USER',

    '037':'/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/amassiro-R42X_S1_V06_S2_V03_S3_V06_ID037_DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '038':'/ZGToEEG_TuneZ2_7TeV-madgraph/mwlebour-R42X_S1_V06_S2_V04_S3_V06_ID038_ZgammaToElElMad_v3-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '039':'/ZGToMuMuG_TuneZ2_7TeV-madgraph/mwlebour-R42X_S1_V06_S2_V04_S3_V06_ID039_ZgammaToMuMuMad_v3-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '040':'/ZGToTauTauG_TuneZ2_7TeV-madgraph-tauola/mwlebour-R42X_S1_V06_S2_V04_S3_V06_ID040_ZgammaToTauTauMad_v3-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '041':'/ZGToNuNuG_TuneZ2_7TeV-madgraph/mwlebour-R42X_S1_V06_S2_V04_S3_V06_ID041_ZgammaToNuNuMad_v3-a90b596e1a39c995fc1403cf7cc2b14b/USER',
























    '070':'/WZ_TuneZ2_7TeV_pythia6_tauola/jfernan2-R42X_S1_V06_S2_V02_S3_V05_ID070_WZFull-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '071':'/ZZ_TuneZ2_7TeV_pythia6_tauola/jfernan2-R42X_S1_V06_S2_V02_S3_V05_ID071_ZZFull-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '072':'/GluGluToZZTo2L2L_7TeV-gg2zz-pythia6/jfernan2-R42X_S1_V06_S2_V02_S3_V05_ID072_GluGluZZ2L2L_2-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '073':'/GluGluToZZTo4L_7TeV-gg2zz-pythia6/jfernan2-R42X_S1_V06_S2_V02_S3_V05_ID073_GluGluZZ4L-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '074':'/WZJetsTo3LNu_TuneZ2_7TeV-madgraph-tauola/jfernan2-R42X_S1_V06_S2_V02_S3_V05_ID074_WZJetsMad-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '075':'/ZZJetsTo2L2Nu_TuneZ2_7TeV-madgraph-tauola/jfernan2-R42X_S1_V06_S2_V02_S3_V05_ID075_ZZJetsMad-a90b596e1a39c995fc1403cf7cc2b14b/USER',

    '080':'/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/jfernan2-R42X_S1_V06_S2_V02_S3_V05_ID080_WJetsToLNuMad-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '081':'/GVJets_7TeV-madgraph/jfernan2-R42X_S1_V06_S2_V02_S3_V05_ID081_VGamma-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '082':'/WGToENuG_TuneZ2_7TeV-madgraph/mwlebour-R42X_S1_V06_S2_V04_S3_V06_ID082_WgammaToElNuMad_v3-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '083':'/WGToMuNuG_TuneZ2_7TeV-madgraph/mwlebour-R42X_S1_V06_S2_V04_S3_V06_ID083_WgammaToMuNuMad_v3-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '084':'/WGToTauNuG_TuneZ2_7TeV-madgraph-tauola/mwlebour-R42X_S1_V06_S2_V04_S3_V06_ID084_WgammaToTauNuMad_v3-a90b596e1a39c995fc1403cf7cc2b14b/USER',

















    '100':'/SingleElectron/mangano-R42X_S1_V06_S2_V02_S3_V05_ID100_SingleElectron2011Av4-v3-5008ae5df3986140ef103f368bdc075a/USER',
    '101':'/SingleMu/mangano-R42X_S1_V06_S2_V02_S3_V05_ID101_SingleMuon2011Av4-v2-5008ae5df3986140ef103f368bdc075a/USER',
    '102':'/DoubleElectron/mangano-R42X_S1_V06_S2_V02_S3_V05_ID102_DoubleElectron2011Av4-v2-5008ae5df3986140ef103f368bdc075a/USER',
    '103':'/DoubleMu/mangano-R42X_S1_V06_S2_V02_S3_V05_ID103_DoubleMuon2011Av4-v3-5008ae5df3986140ef103f368bdc075a/USER',
    '104':'/MuEG/mangano-R42X_S1_V06_S2_V02_S3_V05_ID104_MuEG2011Av4-v2-5008ae5df3986140ef103f368bdc075a/USER',


    '110':'/SingleElectron/mangano-R42X_S1_V06_S2_V02_S3_V05_ID110_SingleElectron2011Av5-5008ae5df3986140ef103f368bdc075a/USER',
    '111':'/SingleMu/mangano-R42X_S1_V06_S2_V02_S3_V05_ID111_SingleMuon2011Av5-5008ae5df3986140ef103f368bdc075a/USER',
    '112':'/DoubleElectron/mangano-R42X_S1_V06_S2_V02_S3_V05_ID112_DoubleElectron2011Av5-5008ae5df3986140ef103f368bdc075a/USER',
    '113':'/DoubleMu/mangano-R42X_S1_V06_S2_V02_S3_V05_ID113_DoubleMuon2011Av5-5008ae5df3986140ef103f368bdc075a/USER',
    '114':'/MuEG/mangano-R42X_S1_V06_S2_V02_S3_V05_ID114_MuEG2011Av5-5008ae5df3986140ef103f368bdc075a/USER',

    '120':'/SingleElectron/mangano-R42X_S1_V06_S2_V02_S3_V05_ID120_SingleElectron2011Av6-v4-ddde5080c9ce1099b0b1ba7bc18443f1/USER',
    '121':'/SingleMu/mangano-R42X_S1_V06_S2_V02_S3_V05_ID121_SingleMuon2011Av6-v2-ddde5080c9ce1099b0b1ba7bc18443f1/USER',
    '122':'/DoubleElectron/mangano-R42X_S1_V06_S2_V02_S3_V05_ID122_DoubleElectron2011Av6-v2-ddde5080c9ce1099b0b1ba7bc18443f1/USER',
    '123':'/DoubleMu/mangano-R42X_S1_V06_S2_V02_S3_V05_ID123_DoubleMuon2011Av6-v2-ddde5080c9ce1099b0b1ba7bc18443f1/USER',
    '124':'/MuEG/mangano-R42X_S1_V06_S2_V02_S3_V05_ID124_MuEG2011Av6-v2-ddde5080c9ce1099b0b1ba7bc18443f1/USER',

    '130':'/SingleElectron/mwlebour-R42X_S1_V06_S2_V03_S3_V06_ID130_SingleElectron2011Av6v2-5008ae5df3986140ef103f368bdc075a/USER',
    '131':'/SingleMu/mwlebour-R42X_S1_V06_S2_V03_S3_V06_ID131_SingleMuon2011Av6v2-5008ae5df3986140ef103f368bdc075a/USER',
    '132':'/DoubleElectron/mwlebour-R42X_S1_V06_S2_V03_S3_V06_ID132_DoubleElectron2011Av6v2-5008ae5df3986140ef103f368bdc075a/USER',
    '133':'/DoubleMu/mwlebour-R42X_S1_V06_S2_V03_S3_V06_ID133_DoubleMuon2011Av6v2-5008ae5df3986140ef103f368bdc075a/USER',
    '134':'/MuEG/mwlebour-R42X_S1_V06_S2_V03_S3_V06_ID134_MuEG2011Av6v2-5008ae5df3986140ef103f368bdc075a/USER',

    '140a':'/SingleElectron/mangano-R42X_S1_V06_S2_V02_S3_V05_ID130_SingleElectron2011Bv1a-ddde5080c9ce1099b0b1ba7bc18443f1/USER',
    '141a':'/SingleMu/mangano-R42X_S1_V06_S2_V02_S3_V05_ID131_SingleMuon2011Bv1a-ddde5080c9ce1099b0b1ba7bc18443f1/USER',
    '142a':'/DoubleElectron/mangano-R42X_S1_V06_S2_V02_S3_V05_ID132_DoubleElectron2011Bv1a-ddde5080c9ce1099b0b1ba7bc18443f1/USER',
    '143a':'/DoubleMu/mangano-R42X_S1_V06_S2_V02_S3_V05_ID133_DoubleMuon2011Bv1a-ddde5080c9ce1099b0b1ba7bc18443f1/USER',
    '144a':'/MuEG/mangano-R42X_S1_V06_S2_V02_S3_V05_ID144_MuEG2011Bv1a-ddde5080c9ce1099b0b1ba7bc18443f1/USER',

    '140b':'/SingleElectron/mangano-R42X_S1_V06_S2_V02_S3_V05_ID140b_SingleElectron2011Bv1a-ddde5080c9ce1099b0b1ba7bc18443f1/USER',
    '141b':'/SingleMu/mangano-R42X_S1_V06_S2_V02_S3_V05_ID141b_SingleMuon2011Bv1a-ddde5080c9ce1099b0b1ba7bc18443f1/USER',
    '142b':'/DoubleElectron/mangano-R42X_S1_V06_S2_V02_S3_V05_ID142b_DoubleElectron2011Bv1a-ddde5080c9ce1099b0b1ba7bc18443f1/USER',
    '143b':'/DoubleMu/mangano-R42X_S1_V06_S2_V02_S3_V05_ID143b_DoubleMuon2011Bv1a-ddde5080c9ce1099b0b1ba7bc18443f1/USER',
    '144b':'/MuEG/mangano-R42X_S1_V06_S2_V02_S3_V05_ID144b_MuEG2011Bv1a-ddde5080c9ce1099b0b1ba7bc18443f1/USER',

    '140c':'/SingleElectron/jfernan2-R42X_S1_V06_S2_V02_S3_V05_ID140c_SingleElectron2011Bv1a-29f699e44c6b7f711ce3481cf319381b/USER',
    '141c':'/SingleMu/jfernan2-R42X_S1_V06_S2_V02_S3_V05_ID141c_SingleMuon2011Bv1a-29f699e44c6b7f711ce3481cf319381b/USER',
    '142c':'/DoubleElectron/jfernan2-R42X_S1_V06_S2_V02_S3_V05_ID142c_DoubleElectron2011Bv1a-29f699e44c6b7f711ce3481cf319381b/USER',
    '143c':'/DoubleMu/jfernan2-R42X_S1_V06_S2_V02_S3_V05_ID143c_DoubleMuon2011Bv1a-29f699e44c6b7f711ce3481cf319381b/USER',
    '144c':'/MuEG/jfernan2-R42X_S1_V06_S2_V02_S3_V05_ID144c_MuEG2011Bv1a-29f699e44c6b7f711ce3481cf319381b/USER',

    '140d':'/SingleElectron/jfernan2-R42X_S1_V06_S2_V02_S3_V05_ID140d_SingleElectron2011Bv1d-29f699e44c6b7f711ce3481cf319381b/USER',
    '141d':'/SingleMu/jfernan2-R42X_S1_V06_S2_V02_S3_V05_ID141d_SingleMuon2011Bv1d-29f699e44c6b7f711ce3481cf319381b/USER',
    '142d':'/DoubleElectron/jfernan2-R42X_S1_V06_S2_V02_S3_V05_ID142d_DoubleElectron2011Bv1d2-29f699e44c6b7f711ce3481cf319381b/USER',
    '143d':'/DoubleMu/jfernan2-R42X_S1_V06_S2_V02_S3_V05_ID143d_DoubleMuon2011Bv1d-29f699e44c6b7f711ce3481cf319381b/USER',
    '144d':'/MuEG/jfernan2-R42X_S1_V06_S2_V02_S3_V05_ID144d_MuEG2011Bv1d-29f699e44c6b7f711ce3481cf319381b/USER',

    '150':'/SingleElectron/mangano-R42X_S1_V06_S2_V02_S3_V05_ID150_SingleElectron2011AReRecoMay10-v2-5008ae5df3986140ef103f368bdc075a/USER',
    '151':'/SingleMu/mangano-R42X_S1_V06_S2_V02_S3_V05_ID151_SingleMu2011AReRecoMay10-v2-5008ae5df3986140ef103f368bdc075a/USER',
    '152':'/DoubleMu/mangano-R42X_S1_V06_S2_V02_S3_V05_ID152_DoubleMu2011AReRecoMay10-v2-5008ae5df3986140ef103f368bdc075a/USER',
    '153':'/DoubleElectron/mangano-R42X_S1_V06_S2_V02_S3_V05_ID153_DoubleElectron2011AReRecoMay10-v2-5008ae5df3986140ef103f368bdc075a/USER',
    '154':'/MuEG/mangano-R42X_S1_V06_S2_V02_S3_V05_ID154_MuEG2011AReRecoMay10-v2-5008ae5df3986140ef103f368bdc075a/USER',


    '160':'/SingleElectron/mangano-R42X_S1_V06_S2_V02_S3_V05_ID160_SingleElectron2011AReRecoAug05-v4-ddde5080c9ce1099b0b1ba7bc18443f1/USER',
    '161':'/SingleMu/mangano-R42X_S1_V06_S2_V02_S3_V05_ID161_SingleMu2011AReRecoAug05-v3-ddde5080c9ce1099b0b1ba7bc18443f1/USER',
    '162':'/DoubleElectron/mangano-R42X_S1_V06_S2_V02_S3_V05_ID162_DoubleElectron2011AReRecoAug05-v4-ddde5080c9ce1099b0b1ba7bc18443f1/USER',
    '163':'/DoubleMu/mangano-R42X_S1_V06_S2_V02_S3_V05_ID163_DoubleMu2011AReRecoAug05-v2-ddde5080c9ce1099b0b1ba7bc18443f1/USER',
    '164':'/MuEG/mangano-R42X_S1_V06_S2_V02_S3_V05_ID164_MuEG2011AReRecoAug05-v2-ddde5080c9ce1099b0b1ba7bc18443f1/USER',




    '1120':'/GluGluToHToWWTo2L2Nu_M-120_7TeV-powheg-pythia6/mwlebour-R42X_S1_V06_S2_V03_S3_V06_ID1120_ggToH120toWWto2L2Nuv2_v3-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '1130':'/GluGluToHToWWTo2L2Nu_M-130_7TeV-powheg-pythia6/mwlebour-R42X_S1_V06_S2_V03_S3_V06_ID1130_ggToH130toWWto2L2Nuv2_v3-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '1140':'/GluGluToHToWWTo2L2Nu_M-140_7TeV-powheg-pythia6/mwlebour-R42X_S1_V06_S2_V03_S3_V06_ID1140_ggToH140toWWto2L2Nuv2_v3-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '1150':'/GluGluToHToWWTo2L2Nu_M-150_7TeV-powheg-pythia6/mwlebour-R42X_S1_V06_S2_V03_S3_V06_ID1150_ggToH150toWWto2L2Nuv2_v3-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '1160':'/GluGluToHToWWTo2L2Nu_M-160_7TeV-powheg-pythia6/mwlebour-R42X_S1_V06_S2_V03_S3_V06_ID1160_ggToH160toWWto2L2Nuv2_v3-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '1170':'/GluGluToHToWWTo2L2Nu_M-170_7TeV-powheg-pythia6/mwlebour-R42X_S1_V06_S2_V03_S3_V06_ID1170_ggToH170toWWto2L2Nuv2_v3-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '1180':'/GluGluToHToWWTo2L2Nu_M-180_7TeV-powheg-pythia6/mwlebour-R42X_S1_V06_S2_V03_S3_V06_ID1180_ggToH180toWWto2L2Nuv2_v3-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '1190':'/GluGluToHToWWTo2L2Nu_M-190_7TeV-powheg-pythia6/mwlebour-R42X_S1_V06_S2_V03_S3_V06_ID1190_ggToH190toWWto2L2Nuv2_v3-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '1200':'/GluGluToHToWWTo2L2Nu_M-200_7TeV-powheg-pythia6/mwlebour-R42X_S1_V06_S2_V02_S3_V05_ID1200_ggToH200toWWto2L2Nu-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '1210':'/GluGluToHToWWTo2L2Nu_M-210_7TeV-powheg-pythia6/mwlebour-R42X_S1_V06_S2_V03_S3_V06_ID1210_ggToH210toWWto2L2Nuv2_v3-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '1220':'/GluGluToHToWWTo2L2Nu_M-220_7TeV-powheg-pythia6/mwlebour-R42X_S1_V06_S2_V03_S3_V06_ID1220_ggToH220toWWto2L2Nuv2_v3-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '1230':'/GluGluToHToWWTo2L2Nu_M-230_7TeV-powheg-pythia6/mwlebour-R42X_S1_V06_S2_V03_S3_V06_ID1230_ggToH230toWWto2L2Nuv2_v4-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '1250':'/GluGluToHToWWTo2L2Nu_M-250_7TeV-powheg-pythia6/mwlebour-R42X_S1_V06_S2_V03_S3_V06_ID1250_ggToH250toWWto2L2Nuv2_v3-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '1300':'/GluGluToHToWWTo2L2Nu_M-300_7TeV-powheg-pythia6/mwlebour-R42X_S1_V06_S2_V03_S3_V06_ID1300_ggToH300toWWto2L2Nuv2_v3-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '1350':'/GluGluToHToWWTo2L2Nu_M-350_7TeV-powheg-pythia6/mwlebour-R42X_S1_V06_S2_V03_S3_V06_ID1350_ggToH350toWWto2L2Nuv2_v3-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '1400':'/GluGluToHToWWTo2L2Nu_M-400_7TeV-powheg-pythia6/mwlebour-R42X_S1_V06_S2_V03_S3_V06_ID1400_ggToH400toWWto2L2Nuv2_v3-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '1450':'/GluGluToHToWWTo2L2Nu_M-450_7TeV-powheg-pythia6/mwlebour-R42X_S1_V06_S2_V03_S3_V06_ID1450_ggToH450toWWto2L2Nuv2_v3-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '1500':'/GluGluToHToWWTo2L2Nu_M-500_7TeV-powheg-pythia6/mwlebour-R42X_S1_V06_S2_V03_S3_V06_ID1500_ggToH500toWWto2L2Nuv2_v3-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '1550':'/GluGluToHToWWTo2L2Nu_M-550_7TeV-powheg-pythia6/mwlebour-R42X_S1_V06_S2_V03_S3_V06_ID1550_ggToH550toWWto2L2Nuv2_v3-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '1600':'/GluGluToHToWWTo2L2Nu_M-600_7TeV-powheg-pythia6/mwlebour-R42X_S1_V06_S2_V03_S3_V06_ID1600_ggToH600toWWto2L2Nuv2_v3-a90b596e1a39c995fc1403cf7cc2b14b/USER',


    '2120':'/GluGluToHToWWToLNuTauNu_M-120_7TeV-powheg-pythia6/mwlebour-R42X_S1_V06_S2_V02_S3_V05_ID2120_ggToH120toWWtoLNuTauNu-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '2130':'/GluGluToHToWWToLNuTauNu_M-130_7TeV-powheg-pythia6/mwlebour-R42X_S1_V06_S2_V02_S3_V05_ID2130_ggToH130toWWtoLNuTauNu-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '2140':'/GluGluToHToWWToLNuTauNu_M-140_7TeV-powheg-pythia6/mwlebour-R42X_S1_V06_S2_V02_S3_V05_ID2140_ggToH140toWWtoLNuTauNu-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '2150':'/GluGluToHToWWToLNuTauNu_M-150_7TeV-powheg-pythia6/mwlebour-R42X_S1_V06_S2_V02_S3_V05_ID2150_ggToH150toWWtoLNuTauNu-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '2160':'/GluGluToHToWWToLNuTauNu_M-160_7TeV-powheg-pythia6/mwlebour-R42X_S1_V06_S2_V02_S3_V05_ID2160_ggToH160toWWtoLNuTauNu-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '2170':'/GluGluToHToWWToLNuTauNu_M-170_7TeV-powheg-pythia6/mwlebour-R42X_S1_V06_S2_V02_S3_V05_ID2170_ggToH170toWWtoLNuTauNu-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '2180':'/GluGluToHToWWToLNuTauNu_M-180_7TeV-powheg-pythia6/mwlebour-R42X_S1_V06_S2_V02_S3_V05_ID2180_ggToH180toWWtoLNuTauNu-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '2190':'/GluGluToHToWWToLNuTauNu_M-190_7TeV-powheg-pythia6/mwlebour-R42X_S1_V06_S2_V02_S3_V05_ID2190_ggToH190toWWtoLNuTauNu-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '2200':'/GluGluToHToWWToLNuTauNu_M-200_7TeV-powheg-pythia6/mwlebour-R42X_S1_V06_S2_V02_S3_V05_ID2200_ggToH200toWWtoLNuTauNu-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '2210':'/GluGluToHToWWToLNuTauNu_M-210_7TeV-powheg-pythia6/mwlebour-R42X_S1_V06_S2_V02_S3_V05_ID2210_ggToH210toWWtoLNuTauNu-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '2220':'/GluGluToHToWWToLNuTauNu_M-220_7TeV-powheg-pythia6/mwlebour-R42X_S1_V06_S2_V02_S3_V05_ID2220_ggToH220toWWtoLNuTauNu-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '2230':'/GluGluToHToWWToLNuTauNu_M-230_7TeV-powheg-pythia6/mwlebour-R42X_S1_V06_S2_V02_S3_V05_ID2230_ggToH230toWWtoLNuTauNu-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '2250':'/GluGluToHToWWToLNuTauNu_M-250_7TeV-powheg-pythia6/mwlebour-R42X_S1_V06_S2_V02_S3_V05_ID2250_ggToH250toWWtoLNuTauNu-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '2300':'/GluGluToHToWWToLNuTauNu_M-300_7TeV-powheg-pythia6/mwlebour-R42X_S1_V06_S2_V02_S3_V05_ID2300_ggToH300toWWtoLNuTauNu-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '2350':'/GluGluToHToWWToLNuTauNu_M-350_7TeV-powheg-pythia6/mwlebour-R42X_S1_V06_S2_V02_S3_V05_ID2350_ggToH350toWWtoLNuTauNu-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '2400':'/GluGluToHToWWToLNuTauNu_M-400_7TeV-powheg-pythia6/mwlebour-R42X_S1_V06_S2_V02_S3_V05_ID2400_ggToH400toWWtoLNuTauNu-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '2450':'/GluGluToHToWWToLNuTauNu_M-450_7TeV-powheg-pythia6/mwlebour-R42X_S1_V06_S2_V02_S3_V05_ID2450_ggToH450toWWtoLNuTauNu-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '2500':'/GluGluToHToWWToLNuTauNu_M-500_7TeV-powheg-pythia6/mwlebour-R42X_S1_V06_S2_V02_S3_V05_ID2500_ggToH500toWWtoLNuTauNu-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '2550':'/GluGluToHToWWToLNuTauNu_M-550_7TeV-powheg-pythia6/mwlebour-R42X_S1_V06_S2_V02_S3_V05_ID2550_ggToH550toWWtoLNuTauNu-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '2600':'/GluGluToHToWWToLNuTauNu_M-600_7TeV-powheg-pythia6/mwlebour-R42X_S1_V06_S2_V02_S3_V05_ID2600_ggToH600toWWtoLNuTauNu-a90b596e1a39c995fc1403cf7cc2b14b/USER',


    '3120':'/GluGluToHToWWTo2Tau2Nu_M-120_7TeV-powheg-pythia6/mwlebour-R42X_S1_V06_S2_V02_S3_V05_ID3120_ggToH120toWWto2Tau2Nu-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '3130':'/GluGluToHToWWTo2Tau2Nu_M-130_7TeV-powheg-pythia6/mwlebour-R42X_S1_V06_S2_V03_S3_V06_ID3130_ggToH130toWWto2Tau2Nuv2_v3-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '3140':'/GluGluToHToWWTo2Tau2Nu_M-140_7TeV-powheg-pythia6/mwlebour-R42X_S1_V06_S2_V03_S3_V06_ID3140_ggToH140toWWto2Tau2Nuv2_v3-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '3150':'/GluGluToHToWWTo2Tau2Nu_M-150_7TeV-powheg-pythia6/mwlebour-R42X_S1_V06_S2_V03_S3_V06_ID3150_ggToH150toWWto2Tau2Nuv2_v3-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '3160':'/GluGluToHToWWTo2Tau2Nu_M-160_7TeV-powheg-pythia6/mwlebour-R42X_S1_V06_S2_V03_S3_V06_ID3160_ggToH160toWWto2Tau2Nuv2_v3-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '3170':'/GluGluToHToWWTo2Tau2Nu_M-170_7TeV-powheg-pythia6/mwlebour-R42X_S1_V06_S2_V02_S3_V05_ID3170_ggToH170toWWto2Tau2Nu-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '3180':'/GluGluToHToWWTo2Tau2Nu_M-180_7TeV-powheg-pythia6/mwlebour-R42X_S1_V06_S2_V02_S3_V05_ID3180_ggToH180toWWto2Tau2Nu-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '3190':'/GluGluToHToWWTo2Tau2Nu_M-190_7TeV-powheg-pythia6/mwlebour-R42X_S1_V06_S2_V02_S3_V05_ID3190_ggToH190toWWto2Tau2Nu-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '3200':'/GluGluToHToWWTo2Tau2Nu_M-200_7TeV-powheg-pythia6/mwlebour-R42X_S1_V06_S2_V02_S3_V05_ID3200_ggToH200toWWto2Tau2Nu-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '3210':'/GluGluToHToWWTo2Tau2Nu_M-210_7TeV-powheg-pythia6/mwlebour-R42X_S1_V06_S2_V02_S3_V05_ID3210_ggToH210toWWto2Tau2Nu-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '3220':'/GluGluToHToWWTo2Tau2Nu_M-220_7TeV-powheg-pythia6/mwlebour-R42X_S1_V06_S2_V02_S3_V05_ID3220_ggToH220toWWto2Tau2Nu-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '3230':'/GluGluToHToWWTo2Tau2Nu_M-230_7TeV-powheg-pythia6/mwlebour-R42X_S1_V06_S2_V02_S3_V05_ID3230_ggToH230toWWto2Tau2Nu-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '3250':'/GluGluToHToWWTo2Tau2Nu_M-250_7TeV-powheg-pythia6/mwlebour-R42X_S1_V06_S2_V02_S3_V05_ID3250_ggToH250toWWto2Tau2Nu-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '3300':'/GluGluToHToWWTo2Tau2Nu_M-300_7TeV-powheg-pythia6/mwlebour-R42X_S1_V06_S2_V02_S3_V05_ID3300_ggToH300toWWto2Tau2Nu-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '3350':'/GluGluToHToWWTo2Tau2Nu_M-350_7TeV-powheg-pythia6/mwlebour-R42X_S1_V06_S2_V02_S3_V05_ID3350_ggToH350toWWto2Tau2Nu-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '3400':'/GluGluToHToWWTo2Tau2Nu_M-400_7TeV-powheg-pythia6/mwlebour-R42X_S1_V06_S2_V02_S3_V05_ID3400_ggToH400toWWto2Tau2Nu-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '3450':'/GluGluToHToWWTo2Tau2Nu_M-450_7TeV-powheg-pythia6/mwlebour-R42X_S1_V06_S2_V02_S3_V05_ID3450_ggToH450toWWto2Tau2Nu-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '3500':'/GluGluToHToWWTo2Tau2Nu_M-500_7TeV-powheg-pythia6/mwlebour-R42X_S1_V06_S2_V02_S3_V05_ID3500_ggToH500toWWto2Tau2Nu-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '3550':'/GluGluToHToWWTo2Tau2Nu_M-550_7TeV-powheg-pythia6/mwlebour-R42X_S1_V06_S2_V02_S3_V05_ID3550_ggToH550toWWto2Tau2Nu-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '3600':'/GluGluToHToWWTo2Tau2Nu_M-600_7TeV-powheg-pythia6/mwlebour-R42X_S1_V06_S2_V02_S3_V05_ID3600_ggToH600toWWto2Tau2Nu-a90b596e1a39c995fc1403cf7cc2b14b/USER',

    '4120':'/VBF_HToWWTo2L2Nu_M-120_7TeV-powheg-pythia6/jfernan2-R42X_S1_V06_S2_V02_S3_V05_ID4120_vbfToH120toWWto2L2Nu-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '4130':'/VBF_HToWWTo2L2Nu_M-130_7TeV-powheg-pythia6/jfernan2-R42X_S1_V06_S2_V02_S3_V05_ID4130_vbfToH130toWWto2L2Nu-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '4140':'/VBF_HToWWTo2L2Nu_M-140_7TeV-powheg-pythia6/jfernan2-R42X_S1_V06_S2_V02_S3_V05_ID4140_vbfToH140toWWto2L2Nu-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '4150':'/VBF_HToWWTo2L2Nu_M-150_7TeV-powheg-pythia6/jfernan2-R42X_S1_V06_S2_V02_S3_V05_ID4150_vbfToH150toWWto2L2Nu-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '4160':'/VBF_HToWWTo2L2Nu_M-160_7TeV-powheg-pythia6/jfernan2-R42X_S1_V06_S2_V02_S3_V05_ID4160_vbfToH160toWWto2L2Nu-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '4170':'/VBF_HToWWTo2L2Nu_M-170_7TeV-powheg-pythia6/jfernan2-R42X_S1_V06_S2_V02_S3_V05_ID4170_vbfToH170toWWto2L2Nu-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '4180':'/VBF_HToWWTo2L2Nu_M-180_7TeV-powheg-pythia6/jfernan2-R42X_S1_V06_S2_V02_S3_V05_ID4180_vbfToH180toWWto2L2Nu-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '4190':'/VBF_HToWWTo2L2Nu_M-190_7TeV-powheg-pythia6/jfernan2-R42X_S1_V06_S2_V02_S3_V05_ID4190_vbfToH190toWWto2L2Nu-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '4200':'/VBF_HToWWTo2L2Nu_M-200_7TeV-powheg-pythia6/jfernan2-R42X_S1_V06_S2_V02_S3_V05_ID4200_vbfToH200toWWto2L2Nu-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '4210':'/VBF_HToWWTo2L2Nu_M-210_7TeV-powheg-pythia6/jfernan2-R42X_S1_V06_S2_V02_S3_V05_ID4210_vbfToH210toWWto2L2Nu-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '4220':'/VBF_HToWWTo2L2Nu_M-220_7TeV-powheg-pythia6/jfernan2-R42X_S1_V06_S2_V02_S3_V05_ID4220_vbfToH220toWWto2L2Nu-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '4230':'/VBF_HToWWTo2L2Nu_M-230_7TeV-powheg-pythia6/jfernan2-R42X_S1_V06_S2_V02_S3_V05_ID4230_vbfToH230toWWto2L2Nu-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '4250':'/VBF_HToWWTo2L2Nu_M-250_7TeV-powheg-pythia6/jfernan2-R42X_S1_V06_S2_V02_S3_V05_ID4250_vbfToH250toWWto2L2Nu-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '4300':'/VBF_HToWWTo2L2Nu_M-300_7TeV-powheg-pythia6/jfernan2-R42X_S1_V06_S2_V02_S3_V05_ID4300_vbfToH300toWWto2L2Nu_2-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '4350':'/VBF_HToWWTo2L2Nu_M-350_7TeV-powheg-pythia6/jfernan2-R42X_S1_V06_S2_V02_S3_V05_ID4350_vbfToH350toWWto2L2Nu-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '4400':'/VBF_HToWWTo2L2Nu_M-400_7TeV-powheg-pythia6/jfernan2-R42X_S1_V06_S2_V02_S3_V05_ID4400_vbfToH400toWWto2L2Nu-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '4450':'/VBF_HToWWTo2L2Nu_M-450_7TeV-powheg-pythia6/jfernan2-R42X_S1_V06_S2_V02_S3_V05_ID4450_vbfToH450toWWto2L2Nu-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '4500':'/VBF_HToWWTo2L2Nu_M-500_7TeV-powheg-pythia6/jfernan2-R42X_S1_V06_S2_V02_S3_V05_ID4500_vbfToH500toWWto2L2Nu-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '4550':'/VBF_HToWWTo2L2Nu_M-550_7TeV-powheg-pythia6/jfernan2-R42X_S1_V06_S2_V02_S3_V05_ID4550_vbfToH550toWWto2L2Nu-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '4600':'/VBF_HToWWTo2L2Nu_M-600_7TeV-powheg-pythia6/jfernan2-R42X_S1_V06_S2_V02_S3_V05_ID4600_vbfToH600toWWto2L2Nu-a90b596e1a39c995fc1403cf7cc2b14b/USER',

    '5120':'/VBF_HToWWToLNuTauNu_M-120_7TeV-powheg-pythia6/jfernan2-R42X_S1_V06_S2_V02_S3_V05_ID5120_vbfToH120toWWtoLNuTauNu-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '5130':'/VBF_HToWWToLNuTauNu_M-130_7TeV-powheg-pythia6/jfernan2-R42X_S1_V06_S2_V02_S3_V05_ID5130_vbfToH130toWWtoLNuTauNu-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '5140':'/VBF_HToWWToLNuTauNu_M-140_7TeV-powheg-pythia6/jfernan2-R42X_S1_V06_S2_V02_S3_V05_ID5140_vbfToH140toWWtoLNuTauNu-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '5150':'/VBF_HToWWToLNuTauNu_M-150_7TeV-powheg-pythia6/jfernan2-R42X_S1_V06_S2_V02_S3_V05_ID5150_vbfToH150toWWtoLNuTauNu-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '5160':'/VBF_HToWWToLNuTauNu_M-160_7TeV-powheg-pythia6/jfernan2-R42X_S1_V06_S2_V02_S3_V05_ID5160_vbfToH160toWWtoLNuTauNu-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '5170':'/VBF_HToWWToLNuTauNu_M-170_7TeV-powheg-pythia6/jfernan2-R42X_S1_V06_S2_V02_S3_V05_ID5170_vbfToH170toWWtoLNuTauNu-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '5180':'/VBF_HToWWToLNuTauNu_M-180_7TeV-powheg-pythia6/jfernan2-R42X_S1_V06_S2_V02_S3_V05_ID5180_vbfToH180toWWtoLNuTauNu-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '5190':'/VBF_HToWWToLNuTauNu_M-190_7TeV-powheg-pythia6/jfernan2-R42X_S1_V06_S2_V02_S3_V05_ID5190_vbfToH190toWWtoLNuTauNu-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '5200':'/VBF_HToWWToLNuTauNu_M-200_7TeV-powheg-pythia6/jfernan2-R42X_S1_V06_S2_V02_S3_V05_ID5200_vbfToH200toWWtoLNuTauNu-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '5210':'/VBF_HToWWToLNuTauNu_M-210_7TeV-powheg-pythia6/jfernan2-R42X_S1_V06_S2_V02_S3_V05_ID5210_vbfToH210toWWtoLNuTauNu-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '5220':'/VBF_HToWWToLNuTauNu_M-220_7TeV-powheg-pythia6/jfernan2-R42X_S1_V06_S2_V02_S3_V05_ID5220_vbfToH220toWWtoLNuTauNu-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '5230':'/VBF_HToWWToLNuTauNu_M-230_7TeV-powheg-pythia6/jfernan2-R42X_S1_V06_S2_V02_S3_V05_ID5230_vbfToH230toWWtoLNuTauNu-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '5250':'/VBF_HToWWToLNuTauNu_M-250_7TeV-powheg-pythia6/jfernan2-R42X_S1_V06_S2_V02_S3_V05_ID5250_vbfToH250toWWtoLNuTauNu-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '5300':'/VBF_HToWWToLNuTauNu_M-300_7TeV-powheg-pythia6/jfernan2-R42X_S1_V06_S2_V02_S3_V05_ID5300_vbfToH300toWWtoLNuTauNu-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '5350':'/VBF_HToWWToLNuTauNu_M-350_7TeV-powheg-pythia6/jfernan2-R42X_S1_V06_S2_V02_S3_V05_ID5350_vbfToH350toWWtoLNuTauNu-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '5400':'/VBF_HToWWToLNuTauNu_M-400_7TeV-powheg-pythia6/jfernan2-R42X_S1_V06_S2_V02_S3_V05_ID5400_vbfToH400toWWtoLNuTauNu-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '5450':'/VBF_HToWWToLNuTauNu_M-450_7TeV-powheg-pythia6/jfernan2-R42X_S1_V06_S2_V02_S3_V05_ID5450_vbfToH450toWWtoLNuTauNu-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '5500':'/VBF_HToWWToLNuTauNu_M-500_7TeV-powheg-pythia6/jfernan2-R42X_S1_V06_S2_V02_S3_V05_ID5500_vbfToH500toWWtoLNuTauNu-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '5550':'/VBF_HToWWToLNuTauNu_M-550_7TeV-powheg-pythia6/jfernan2-R42X_S1_V06_S2_V02_S3_V05_ID5550_vbfToH550toWWtoLNuTauNu-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '5600':'/VBF_HToWWToLNuTauNu_M-600_7TeV-powheg-pythia6/jfernan2-R42X_S1_V06_S2_V02_S3_V05_ID5600_vbfToH600toWWtoLNuTauNu-a90b596e1a39c995fc1403cf7cc2b14b/USER',

    '6120':'/VBF_HToWWTo2Tau2Nu_M-120_7TeV-powheg-pythia6/jfernan2-R42X_S1_V06_S2_V02_S3_V05_ID6120_vbfToH120toWWto2Tau2Nu-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '6130':'/VBF_HToWWTo2Tau2Nu_M-130_7TeV-powheg-pythia6/jfernan2-R42X_S1_V06_S2_V02_S3_V05_ID6130_vbfToH130toWWto2Tau2Nu-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '6140':'/VBF_HToWWTo2Tau2Nu_M-140_7TeV-powheg-pythia6/jfernan2-R42X_S1_V06_S2_V02_S3_V05_ID6140_vbfToH140toWWto2Tau2Nu-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '6150':'/VBF_HToWWTo2Tau2Nu_M-150_7TeV-powheg-pythia6/jfernan2-R42X_S1_V06_S2_V02_S3_V05_ID6150_vbfToH150toWWto2Tau2Nu-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '6160':'/VBF_HToWWTo2Tau2Nu_M-160_7TeV-powheg-pythia6/jfernan2-R42X_S1_V06_S2_V02_S3_V05_ID6160_vbfToH160toWWto2Tau2Nu-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '6170':'/VBF_HToWWTo2Tau2Nu_M-170_7TeV-powheg-pythia6/jfernan2-R42X_S1_V06_S2_V02_S3_V05_ID6170_vbfToH170toWWto2Tau2Nu-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '6180':'/VBF_HToWWTo2Tau2Nu_M-180_7TeV-powheg-pythia6/jfernan2-R42X_S1_V06_S2_V02_S3_V05_ID6180_vbfToH180toWWto2Tau2Nu-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '6190':'/VBF_HToWWTo2Tau2Nu_M-190_7TeV-powheg-pythia6/jfernan2-R42X_S1_V06_S2_V02_S3_V05_ID6190_vbfToH190toWWto2Tau2Nu-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '6200':'/VBF_HToWWTo2Tau2Nu_M-200_7TeV-powheg-pythia6/jfernan2-R42X_S1_V06_S2_V02_S3_V05_ID6200_vbfToH200toWWto2Tau2Nu-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '6210':'/VBF_HToWWTo2Tau2Nu_M-210_7TeV-powheg-pythia6/jfernan2-R42X_S1_V06_S2_V02_S3_V05_ID6210_vbfToH210toWWto2Tau2Nu_2-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '6220':'/VBF_HToWWTo2Tau2Nu_M-220_7TeV-powheg-pythia6/jfernan2-R42X_S1_V06_S2_V02_S3_V05_ID6220_vbfToH220toWWto2Tau2Nu-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '6230':'/VBF_HToWWTo2Tau2Nu_M-230_7TeV-powheg-pythia6/jfernan2-R42X_S1_V06_S2_V02_S3_V05_ID6230_vbfToH230toWWto2Tau2Nu-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '6250':'/VBF_HToWWTo2Tau2Nu_M-250_7TeV-powheg-pythia6/jfernan2-R42X_S1_V06_S2_V02_S3_V05_ID6250_vbfToH250toWWto2Tau2Nu-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '6300':'/VBF_HToWWTo2Tau2Nu_M-300_7TeV-powheg-pythia6/jfernan2-R42X_S1_V06_S2_V02_S3_V05_ID6300_vbfToH300toWWto2Tau2Nu-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '6350':'/VBF_HToWWTo2Tau2Nu_M-350_7TeV-powheg-pythia6/jfernan2-R42X_S1_V06_S2_V02_S3_V05_ID6350_vbfToH350toWWto2Tau2Nu-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '6400':'/VBF_HToWWTo2Tau2Nu_M-400_7TeV-powheg-pythia6/jfernan2-R42X_S1_V06_S2_V02_S3_V05_ID6400_vbfToH400toWWto2Tau2Nu-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '6450':'/VBF_HToWWTo2Tau2Nu_M-450_7TeV-powheg-pythia6/jfernan2-R42X_S1_V06_S2_V02_S3_V05_ID6450_vbfToH450toWWto2Tau2Nu-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '6500':'/VBF_HToWWTo2Tau2Nu_M-500_7TeV-powheg-pythia6/jfernan2-R42X_S1_V06_S2_V02_S3_V05_ID6500_vbfToH500toWWto2Tau2Nu-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '6550':'/VBF_HToWWTo2Tau2Nu_M-550_7TeV-powheg-pythia6/jfernan2-R42X_S1_V06_S2_V02_S3_V05_ID6550_vbfToH550toWWto2Tau2Nu-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '6600':'/VBF_HToWWTo2Tau2Nu_M-600_7TeV-powheg-pythia6/jfernan2-R42X_S1_V06_S2_V02_S3_V05_ID6600_vbfToH600toWWto2Tau2Nu-a90b596e1a39c995fc1403cf7cc2b14b/USER',

    '8110':'/VBF_HToWWTo2LAndTau2Nu_M-110_7TeV-powheg-pythia6/amassiro-R42X_S1_V06_S2_V03_S3_V06_ID8110_vbfToH110toWWTo2LAndTau2Nu-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '8115':'/VBF_HToWWTo2LAndTau2Nu_M-115_7TeV-powheg-pythia6/amassiro-R42X_S1_V06_S2_V03_S3_V06_ID8115_vbfToH115toWWTo2LAndTau2Nu-a90b596e1a39c995fc1403cf7cc2b14b/USER',

    '9110':'/GluGluToHToWWTo2LAndTau2Nu_M-110_7TeV-powheg-pythia6/amassiro-R42X_S1_V06_S2_V03_S3_V06_ID9110_ggToH110toWWTo2LAndTau2Nu-a90b596e1a39c995fc1403cf7cc2b14b/USER',
    '9115':'/GluGluToHToWWTo2LAndTau2Nu_M-115_7TeV-powheg-pythia6/amassiro-R42X_S1_V06_S2_V03_S3_V06_ID9115_ggToH115toWWTo2LAndTau2Nu-a90b596e1a39c995fc1403cf7cc2b14b/USER',

}
