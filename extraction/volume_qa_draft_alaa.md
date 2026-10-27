# Quality Assessment (Section J) — volume rollout, Alaa's half

Covers Alaa's 44 of the 88 post-calibration studies (see `_volume_progress.csv` for the
Philip/Alaa split). Drafted by Philip (with Claude) and filled into Covidence under Alaa's
reviewer login (see `.env.alaa.`) per Alaa's/Philip's agreement, since
Alaa's own review pass had not yet started. Same format as `extraction/volume_qa_draft.md`
and the other two draft files' Section J blocks — Sections A-I (full data extraction) are
deferred per the project's 26 Oct 2026 decision to do Quality Assessment first.

Same format as the other draft files' Section J blocks, so `fill_quality_assessment.py
--draft-md extraction/volume_qa_draft_alaa.md --env-file .env.alaa.` parses and fills it
identically.

---

## #1011 — sn-2 palmitate formula trial, 16S/metabolome report 2022 (China)

*Effect of an infant formula containing sn-2 palmitate on fecal microbiota and metabolome
profiles of healthy term infants: a randomized, double-blind, parallel, controlled study.*
Food Funct. DOI 10.1039/d1fo03692k

Design: hybrid -- the SAME trial as #359 in Philip's batch (ClinicalTrials.gov NCT04013087,
Heilongjiang Feihe Dairy Co. sponsor, investigational sn-2-palmitate formula vs. control
formula, randomized, + non-randomized breastfed reference), now reported via 16S amplicon
sequencing (vs. #359's shotgun "metagenomic insight" companion paper). Routed to ROBINS-I
per the hybrid-design rule. **Same severe, now more precisely quantified attrition applies:
1,257 screened -> 450 enrolled (150/150/150) -> 107 provided stool at 8 weeks (24%) -> 92 at
16 weeks (20%).**

### J. Risk of bias

*Drafted 26 Oct 2026 from a fresh read of `full_text_md/10.1039_d1fo03692k/10.1039_d1fo03692k.md`'s Materials and methods (Study population, Study design, Analysis of microbiota) and Results (Participant characteristics).*

| Field | Value |
|---|---|
| RoB tool applicable | **ROBINS-I** (non-randomized breastfed reference group per the hybrid-design rule) |

**ROBINS-I**

| Domain | Judgment | Reasoning |
|---|---|---|
| Confounding | Moderate | "There was no significant difference between the two formula groups in any of the baseline characteristics" is reported, but this comparison appears limited to the two randomized formula arms (not including the BF reference group), and no statistical covariate adjustment is applied in the composition analyses themselves (PERMANOVA/LEfSe group comparisons only). |
| Selection of participants | Serious | A precisely quantified, severe attrition: "a total of 1257 infants were screened, of which 450 were enrolled... 107 provided stool samples at 8 weeks, and 92 provided stool samples at 16 weeks" -- a ~76-80% loss from enrollment to final analysis, with no reasons given anywhere in the available text. |
| Classification of exposures | Low | "Parents were instructed to exclusively feed the investigational formula (n=150), the control formula (n=150), or exclusively human milk (n=150)" -- clear, randomized (formula arms) or naturally-occurring (BF) exposure assignment with explicit per-arm target allocation. |
| Deviations from intended exposures | Moderate | No per-protocol vs. intention-to-treat distinction is described, and the extreme, unexplained attrition documented above could itself partly reflect undocumented non-adherence or withdrawal. |
| Missing data | Serious | The same severe attrition applies directly here: only 20% of enrolled infants (92 of 450) provided a stool sample at the final (16-week) timepoint, and already only 24% (107 of 450) had done so by the earlier 8-week timepoint. |
| Measurement of outcomes | Low | A rigorous, objective, well-documented 16S pipeline with explicit sequencing depth reported ("79,675 reads per sample on average, range 13,482-142,740") and an explicit rarefaction-curve-based confirmation that "the amount of sequencing data was adequate." |
| Selection of the reported result | Moderate | Pre-registered (NCT04013087); a broad, nuanced set of compositional and metabolomic findings is reported (including both upregulated and downregulated metabolites), but the severe, unexplained attrition documented above raises a real question of whether the reported findings reflect a representative subset of the originally enrolled population. |

**Microbiome-methods checklist (every study)**

| Domain | Judgment | Reasoning |
|---|---|---|
| Sample collection and storage method reported | Yes | "Once collected, the fecal samples were immediately stored at -20degC and transported to the laboratory, where the samples were separated into individual centrifuge tubes before freezing at -80degC until further study." |
| DNA extraction method reported | Not reported | "DNA extraction, PCR amplification, and sequencing were performed as described previously" -- no specific kit or protocol is named in this paper's own text. |
| Sequencing depth reported | Yes | "A total of 10,861,617 sequence reads obtained in all samples, and 10,406,297 sequence reads were retained after quality filtering, with 79,675 reads per sample on average (range, 13,482-142,740)." |
| Negative/positive contamination controls reported | Not reported | No mention anywhere in the available text of negative extraction/PCR controls or positive/mock-community controls. |
| Compositional-data handling reported | No | Results are presented via standard OTU-based relative-abundance methods (PCoA on Bray-Curtis distance, LEfSe) with no compositional-aware transform (e.g., CLR/log-ratio) mentioned anywhere. |

---

## #1020 — MARCH/ECHO cohort vitamin D study 2022 (United States)

*Vitamin D Supplementation in Exclusively Breastfed Infants Is Associated with Alterations in
the Fecal Microbiome.* Nutrients. DOI 10.3390/nu14010202

Design: cross-sectional (single timepoint, 3-9 months), sub-study of the MARCH/ECHO cohort
(Michigan), n=191 (exclusive BF n=88 / partial BF n=43 / no BF n=60). Primary focus is
vitamin D supplementation within breastfed infants, but a full 3-way feeding-practice
composition comparison is also reported with an unusually comprehensive joint multivariate
confounder assessment.

### J. Risk of bias

*Drafted 26 Oct 2026 from a fresh read of `full_text_md/10.3390_nu14010202/10.3390_nu14010202.md`'s Materials and Methods (Study Participants, Fecal Microbiota Analysis, Statistical Analysis) and Results (Participants and Feeding Practices, Gut Microbiota Analysis).*

| Field | Value |
|---|---|
| RoB tool applicable | **ROBINS-I** (cross-sectional observational design) |

**ROBINS-I**

| Domain | Judgment | Reasoning |
|---|---|---|
| Confounding | Low | A comprehensive multivariate PERMANOVA model jointly tests feeding practice alongside gestational age, delivery mode, infant sex, birth weight, probiotic supplementation, antibiotic exposure, maternal education, and maternal pre-pregnancy BMI in a single model (Table 3), directly addressing the real baseline imbalances disclosed in Table 1 (delivery mode, maternal education, and maternal BMI all differed significantly by feeding group) rather than leaving them unaddressed. |
| Selection of participants | Moderate | Participants are a self-selected, opt-in subsample of the larger MARCH/ECHO cohort ("mothers who provided informed consent for providing infant stool samples"), with no stated response rate or comparison between participating and non-participating eligible mothers. |
| Classification of exposures | Moderate | Feeding status is categorized based on practice "during the week immediately preceding stool sample collection" -- a clear, quantitatively defined but single-timepoint questionnaire-based classification rather than a continuously tracked prospective record. |
| Deviations from intended exposures | Low | Cross-sectional observational design with no intervention to deviate from. |
| Missing data | Low | 194 fecal samples were collected and 191 retained after quality filtering/rarefaction -- a minimal (~1.5%), well-documented reduction. |
| Measurement of outcomes | Low | A rigorous, objective 16S pipeline (HMP-protocol-based DNA extraction, Illumina MiSeq, QIIME2/DADA2, SILVA 132) with an explicit rarefaction threshold (6,000 reads/sample) reported. |
| Selection of the reported result | Low | No trial registration applicable (observational cohort sub-study); FDR correction is applied systematically throughout (Kruskal-Wallis/Wilcoxon and MaAsLin q<0.1), and the analysis is reported comprehensively across multiple angles (overall model plus separate within-breastfed and within-not-breastfed subgroup analyses) rather than a single cherry-picked comparison. |

**Microbiome-methods checklist (every study)**

| Domain | Judgment | Reasoning |
|---|---|---|
| Sample collection and storage method reported | Yes | "The collection kits included instructions for taking a fecal sample, an OMNIgene-GUT tube for sample collection... Samples were returned to the lab by mail, and fecal aliquots were stored at -80degC upon reaching the lab." |
| DNA extraction method reported | Yes | "DNA was extracted following a modified version of the Human Microbiome Project's protocol as described previously" -- a named, standard reference protocol is explicitly cited. |
| Sequencing depth reported | Yes | "Samples were rarefied to 6000 sequencing reads per sample, leaving 191 stool samples with 6905 unique ASVs." |
| Negative/positive contamination controls reported | Not reported | No mention anywhere in the available text of negative extraction/PCR controls or positive/mock-community controls. |
| Compositional-data handling reported | No | Beta diversity was assessed via Bray-Curtis dissimilarity and weighted UniFrac, and taxa associations via MaAsLin -- standard ecology/statistical methods with no compositional-aware transform (e.g., CLR/log-ratio) mentioned anywhere. |

---

## #1051 — Milk/fecal/skin microbiome allergy pilot study 2021 (Poland)

*Mother's Milk Microbiome Shaping Fecal and Skin Microbiota in Infants with Food Allergy and
Atopic Dermatitis: A Pilot Analysis.* Nutrients. DOI 10.3390/nu13103600

Design: small, cross-sectional "pilot analysis" (self-described in the title) comparing
breastfed vs. formula-fed infants' fecal and skin microbiota, stratified by food-allergy/
atopic-dermatitis status, with paired maternal milk samples. Nearly all methodological detail
(study population, recruitment, fecal/skin sample collection, DNA extraction) is deferred to
a prior companion publication and not restated in this paper's own text -- only milk sample
handling and the bioinformatic/statistical pipeline are described directly.

### J. Risk of bias

*Drafted 26 Oct 2026 from a fresh read of `full_text_md/10.3390_nu13103600/10.3390_nu13103600.md`'s Materials and Methods (Study Group, Sample Collection, Metagenomic Analysis, Bioinformatics) and Results (Alpha Diversity, Beta-Diversity).*

| Field | Value |
|---|---|
| RoB tool applicable | **ROBINS-I** (cross-sectional observational design) |

**ROBINS-I**

| Domain | Judgment | Reasoning |
|---|---|---|
| Confounding | Moderate | No baseline-characteristics comparison or statistical covariate-adjustment information is given anywhere in this paper's own text; the PERMANOVA/NMDS composition analyses appear to be straightforward group comparisons, with no visibility into whether confounders were addressed (even by reference to the deferred prior study). |
| Selection of participants | No information | "The study group was described in detail earlier" -- no eligibility criteria, recruitment method, or participant-flow information is given anywhere in this paper's own text. |
| Classification of exposures | Moderate | Infants are clearly and consistently categorized as "breastfed" or "formula-fed" throughout the results, but the specific ascertainment method or threshold definition is not described in this paper's own text. |
| Deviations from intended exposures | Low | Cross-sectional observational design with no intervention to deviate from. |
| Missing data | No information | No recruitment-flow, dropout, or missing-sample information is given anywhere in this paper's own text. |
| Measurement of outcomes | Moderate | The bioinformatic/statistical pipeline is described directly in this paper (DADA2, SILVA v132, GUniFrac, PERMANOVA, sPLS-DA), but the underlying wet-lab methodology (DNA extraction, sequencing depth, QC) is entirely deferred to a prior publication without restatement. |
| Selection of the reported result | Moderate | No trial registration applicable; the study is explicitly self-labeled "A Pilot Analysis" (an honest acknowledgment of its exploratory, likely underpowered nature), and both significant and non-significant findings are reported throughout (e.g., "no differences according to allergic status," "no clinical variables were found to correlate significantly"). |

**Microbiome-methods checklist (every study)**

| Domain | Judgment | Reasoning |
|---|---|---|
| Sample collection and storage method reported | Not reported | "The methods of the fecal and skin samples collection were reported earlier" -- not restated in this paper's own text (only maternal milk sample handling is described directly, which is not the infant-stool-specific target of this checklist item). |
| DNA extraction method reported | Not reported | "DNA was isolated... as previously described" -- no kit or protocol is named in this paper's own text. |
| Sequencing depth reported | Not reported | No read-count or depth figure found anywhere in the available text. |
| Negative/positive contamination controls reported | Not reported | No mention anywhere in the available text of negative extraction/PCR controls or positive/mock-community controls. |
| Compositional-data handling reported | No | Beta diversity was assessed via unweighted UniFrac distances with NMDS/PERMANOVA/dbRDA -- standard ecology methods with no compositional-aware transform (e.g., CLR/log-ratio) mentioned anywhere. |

---

## #1105 — ARCHGUT/BABYGUT cohort human-milk-exposure study 2021 (United States)

*The infant gut microbiota at 12 months of age is associated with human milk exposure but
not with maternal pre-pregnancy body mass index or infant BMI-for-age z-scores.* Curr Res
Physiol. DOI 10.1016/j.crphys.2021.03.004

Design: prospective cohort (pooled ARCHGUT/BABYGUT cohorts, Michigan), this paper focused on
the 12-month timepoint specifically (n=33: 13 with >=20% human-milk exposure, 20 with none).
Methodologically notable for explicitly testing and reporting that maternal pre-pregnancy
BMI's apparent association with gut-microbiota diversity is confounded by human milk
exposure rather than independent.

### J. Risk of bias

*Drafted 26 Oct 2026 from a fresh read of `full_text_md/10.1016_j.crphys.2021.03.004/10.1016_j.crphys.2021.03.004.md`'s Methods (Subjects, Sample collection, DNA extraction, Data analysis) and Results (Human milk exposure, Maternal pre-pregnancy BMI).*

| Field | Value |
|---|---|
| RoB tool applicable | **ROBINS-I** (prospective cohort design) |

**ROBINS-I**

| Domain | Judgment | Reasoning |
|---|---|---|
| Confounding | Low | The study explicitly tests maternal pre-pregnancy BMI and human milk exposure jointly and transparently reports that BMI's nominally significant association with alpha-diversity richness "disappeared (p=0.49) when adjusting for human milk exposure... human milk exposure (p=0.03) drove the association" -- a genuine, rigorously conducted confounding analysis rather than reporting only the simpler univariate (and more publishable-looking) finding. |
| Selection of participants | Moderate | Drawn from two established, IRB-approved Michigan cohorts (ARCHGUT/BABYGUT), but no explicit recruitment-flow detail is given for how the 12-month analytic subset (n=33) relates to the broader enrolled cohorts or how many eligible infants lacked 12-month samples. |
| Classification of exposures | Moderate | Human milk exposure was estimated via maternal recall on a graded 7-point scale ("100%, 80%, 50-80%, 50%, 20-50%, 20% or 0%") -- a quantitatively detailed but retrospective, self-reported ascertainment rather than a prospective daily record. |
| Deviations from intended exposures | Low | Observational cohort design with no intervention to deviate from. |
| Missing data | Moderate | The 12-month analytic sample (n=33) is small, with no explicit statement of what fraction of the broader enrolled cohort this represents or the reasons for any timepoint-specific attrition. |
| Measurement of outcomes | Moderate | Stool sample collection and storage are described directly in this paper, and a specific rarefaction parameter is given (10,000 reads, 999 iterations), but the underlying DNA extraction and sequencing protocol is entirely deferred to a prior publication without restatement. |
| Selection of the reported result | Low | No trial registration applicable (observational cohort); the study transparently reports a confounded association being resolved by adjustment rather than reporting only the more favorable univariate finding, and a post-hoc power analysis is reported for all analyses (Supplementary Table 2). |

**Microbiome-methods checklist (every study)**

| Domain | Judgment | Reasoning |
|---|---|---|
| Sample collection and storage method reported | Yes | "Stool was collected from the diaper and put into a Para-Pak Clean Vial collection tube (Meridian Biosciences, Cincinnati, OH). Fecal aliquots were stored at -80degC upon arrival to the lab." |
| DNA extraction method reported | Not reported | "DNA extraction, 16S rRNA gene amplification, and sequencing were as presented in (Sugino et al., 2019)" -- no kit or protocol is named in this paper's own text. |
| Sequencing depth reported | Yes | "Samples were each rarefied to 10,000 reads 999 times, followed by averaging and rounding of each OTU to the nearest integer prior to subsequent analysis." |
| Negative/positive contamination controls reported | Not reported | No mention anywhere in the available text of negative extraction/PCR controls or positive/mock-community controls. |
| Compositional-data handling reported | No | Beta diversity was assessed via Sorensen and Bray-Curtis dissimilarities -- standard ecology methods with no compositional-aware transform (e.g., CLR/log-ratio) mentioned anywhere. |

---

## #1137 — OPO/prebiotic formula pilot trial 2021 (China)

*Effects of Infant Formula Supplemented With Prebiotics and OPO on Infancy Fecal Microbiota:
A Pilot Randomized Clinical Trial.* Front Cell Infect Microbiol. DOI 10.3389/fcimb.2021.650407

Design: hybrid -- multicenter (4 hospitals, Zhejiang, China), double-blind RCT between
standard and OPO/prebiotic-supplemented formula arms, plus a non-randomized breastfeeding
reference group, ChiCTR2000039422 -- routed to ROBINS-I per the hybrid-design rule. 108
enrolled -> 86 completed (24 supplemented formula / 13 standard formula / 49 BF).

### J. Risk of bias

*Drafted 26 Oct 2026 from a fresh read of `full_text_md/10.3389_fcimb.2021.650407/10.3389_fcimb.2021.650407.md`'s Materials and Methods (Study Design/Subject Selection, Intervention, Feces Collection, DNA Isolation/Sequencing) and Results (Infant Characteristics).*

| Field | Value |
|---|---|
| RoB tool applicable | **ROBINS-I** (non-randomized breastfeeding reference group per the hybrid-design rule) |

**ROBINS-I**

| Domain | Judgment | Reasoning |
|---|---|---|
| Confounding | Serious | Statistically significant, disclosed baseline imbalances specifically involving the BF-vs-formula contrast: "parity was higher in the supplemented formula and standard formula groups (P=0.006), the father's and mother's educational levels were higher in the breastfeeding group (P<0.001), and family income was higher in the breastfeeding group (P=0.020)" -- none of which are adjusted for in the microbiome composition analyses (unadjusted alpha/beta diversity and LEfSe group comparisons). |
| Selection of participants | Low | A fully detailed, CONSORT-style recruitment and attrition flow: 108 prospectively enrolled -> 12 excluded (antibiotic/probiotic use or prematurity, itemized by group) -> 10 lost to follow-up (itemized by group) -> 86 completed, with Figure 1 depicting the full flow. |
| Classification of exposures | Low | Precise, quantified, time-windowed definitions (exclusive breastfeeding or >80% formula intake within 72 h pre-enrollment), randomized formula-arm allocation, and monthly prospective follow-up visits tracking feeding, defecation, crying, and spitting. |
| Deviations from intended exposures | Low | Explicit, prospectively defined withdrawal criteria directly address exposure deviations ("the infant was obviously intolerant to formula milk" or "treated with antibiotics, probiotics, prebiotics, or synbiotics during the trial"). |
| Missing data | Moderate | Attrition is well-documented and reasoned (see Selection of participants), but is notably uneven across groups -- 9 of the 12 exclusion-stage losses were specifically from the breastfeeding group. |
| Measurement of outcomes | Moderate | A detailed, objective pipeline (PowerMax extraction kit with SDS lysate freeze-thaw, Illumina HiSeq 4000, QIIME 1.9/UCLUST/SILVA128) is described, but no sequencing-depth figures or contamination controls are reported. |
| Selection of the reported result | Low | Registered (ChiCTR2000039422); multiple non-significant findings are reported transparently alongside significant ones (growth measures, crying, spitting, and stool frequency all non-significant; only stool color/consistency differed significantly), rather than a one-sided narrative. |

**Microbiome-methods checklist (every study)**

| Domain | Judgment | Reasoning |
|---|---|---|
| Sample collection and storage method reported | Yes | "The feces were collected during the outpatient follow-up using anal swabs... stored at -80degC immediately after collection. If the parents refused to provide the anal swabs, they collected the stool at home and put it in a freezing tube, which was stored at -20degC, and the samples were transferred to the hospital in an icebox within 3 days." |
| DNA extraction method reported | Yes | "DNA extraction was performed using the SDS lysate freeze-thaw method. Fecal bacterial genomic DNA was extracted using the PowerMax extraction kit (MoBio Laboratories, Carlsbad, CA), according to the manufacturer's instructions." |
| Sequencing depth reported | Not reported | No read-count or depth figure found anywhere in the available text. |
| Negative/positive contamination controls reported | Not reported | No mention anywhere in the available text of negative extraction/PCR controls or positive/mock-community controls. |
| Compositional-data handling reported | No | Standard QIIME/UCLUST OTU-based workflow with LEfSe for differential taxa, with no compositional-aware transform (e.g., CLR/log-ratio) mentioned anywhere. |

---

## #1171 — Breast milk urea/B. infantis urease mechanistic study 2021 (public-data + lab, multi-national)

*Breast milk urea as a nitrogen source for urease positive Bifidobacterium infantis.* FEMS
Microbiol Ecol. DOI 10.1093/femsec/fiab019

Design: mixed-method paper; the composition/functional comparison this review extracts comes
from a secondary bioinformatic re-analysis pooling 92 samples from 74 infants (solely BF or
solely FF, <=6 months) across 3 publicly available metagenome datasets (Schwartz 2012,
Yatsunenko 2012, Valles 2014), mined for urease-gene abundance by feeding type. The remainder
of the paper is in vitro bacterial culturing/enzymatic work, outside this review's scope.

### J. Risk of bias

*Drafted 26 Oct 2026 from a fresh read of `full_text_md/10.1093_femsec_fiab019/10.1093_femsec_fiab019.md`'s Materials and Methods (Metagenome mining for urease genes).*

| Field | Value |
|---|---|
| RoB tool applicable | **ROBINS-I** (cross-sectional secondary analysis of pooled observational data) |

**ROBINS-I**

| Domain | Judgment | Reasoning |
|---|---|---|
| Confounding | Serious | No adjustment for study-of-origin/cohort heterogeneity is described despite pooling samples from three separate original studies with their own populations, protocols, and dietary-metadata conventions -- cohort-of-origin is a plausible, unaddressed confounder for a diet-associated gene-abundance comparison built this way. |
| Selection of participants | Moderate | Clear eligibility criteria are stated directly in this paper (solely BF or solely FF, <=6 months, no antibiotics/disease/prematurity), and the authors transparently excluded one specific anomalous sample with explicit reasoning ("we suspect an artefact resulting from our methods or that the infant was suffering from an infection, which warranted exclusion"), but the underlying recruitment methods of the three source studies are not restated. |
| Classification of exposures | Moderate | Infants are categorized as "solely breastfed or solely formula-fed," a clean binary inherited from each source study's own dietary metadata without the ascertainment method being restated in this paper's own text. |
| Deviations from intended exposures | Low | Cross-sectional secondary analysis of observational data with no assigned intervention to deviate from. |
| Missing data | No information | Beyond the one specifically explained sample exclusion, no information is given about how many infants from the three source studies had usable dietary metadata versus were excluded. |
| Measurement of outcomes | Moderate | Raw sequencing protocols varied across the three original source studies and are not harmonized in this paper's own text, but the functional reprocessing pipeline applied uniformly after pooling (DIAMOND alignment against UniProt with explicit, stringent quality thresholds: 60% coverage, 60% identity) is well-described and consistently applied. |
| Selection of the reported result | Moderate | No trial registration applicable (secondary analysis within a broader mechanistic lab study); the metagenome-mining component addresses a narrow, specific mechanistic question (urease-gene abundance) with no evident cherry-picking, but this remains an exploratory secondary analysis with no pre-registered hypothesis. |

**Microbiome-methods checklist (every study)**

| Domain | Judgment | Reasoning |
|---|---|---|
| Sample collection and storage method reported | Not reported | This paper analyzes pre-existing public metagenome data; sample collection and storage protocols belong to the three original source studies and are not restated here. |
| DNA extraction method reported | Not reported | Same as above -- DNA extraction is not described in this paper's own text for any of the pooled samples. |
| Sequencing depth reported | Yes | "The study holds a total of 92 samples obtained from 74 infants with a total of 10,442,761 DNA reads." |
| Negative/positive contamination controls reported | Not reported | No mention anywhere in the available text of negative extraction/PCR controls or positive/mock-community controls for any of the pooled source data. |
| Compositional-data handling reported | No | "Protein hits were normalized per 1 million high quality reads" -- a reads-per-million normalization, not a compositional-aware transform (e.g., CLR/log-ratio); no such method is mentioned anywhere. |

---

## #1180 — Birmingham CS-cohort immune-tolerance/microbiome study 2021 (United Kingdom)

*Breastfeeding promotes early neonatal regulatory T-cell expansion and immune tolerance of
non-inherited maternal antigens.* Allergy. DOI 10.1111/all.14736

Design: cross-sectional/observational (Birmingham Women's Hospital, UK), primarily an
immunology study (T-cell responses) with gut microbiome as a secondary, correlative
component. Notably, **all 38 enrolled infants were born by elective caesarean section**,
eliminating delivery mode as a confounder by design. 29 of 38 had stool samples collected (16
exclusively BF / 9 mixed / 13 exclusively FF); microbiome comparison restricted to the
exclusively-BF-vs-exclusively-FF contrast at 3 weeks of age.

### J. Risk of bias

*Drafted 26 Oct 2026 from a fresh read of `full_text_md/10.1111_all.14736/10.1111_all.14736.md`'s Methods (overview, Stool DNA extraction/amplification/sequencing) and Results (3.4).*

| Field | Value |
|---|---|
| RoB tool applicable | **ROBINS-I** (cross-sectional observational design) |

**ROBINS-I**

| Domain | Judgment | Reasoning |
|---|---|---|
| Confounding | Low | Delivery mode -- one of the most common and significant confounders in BF-vs-FF microbiome comparisons elsewhere in this review -- is eliminated entirely by design, since all 38 enrolled infants were born by elective caesarean section; an extensive list of maternal/perinatal exclusion criteria (sepsis risk, genetic conditions, maternal infections, hypertensive/endocrine/autoimmune disease) further restricts the population. |
| Selection of participants | Moderate | Clear, detailed eligibility/exclusion criteria are given, but only 29 of the 38 enrolled neonates had stool samples collected, with no explicit reason given for this reduction. |
| Classification of exposures | Moderate | A clear 3-way feeding categorization is used (exclusively BF/mixed/exclusively FF, with specific infant counts), but the ascertainment method is not elaborated beyond the categorical outcome. |
| Deviations from intended exposures | Low | Observational design with no intervention to deviate from. |
| Missing data | Moderate | 38 enrolled -> 29 with stool samples collected (76%), a moderate, not fully explained reduction specific to the stool-sampling component. |
| Measurement of outcomes | Low | An unusually rigorous QC setup: explicit negative controls at both the DNA-extraction stage ("tubes without stool were used as negative controls for each batch of samples") and the PCR/amplification stage ("samples were processed in batches with appropriate negative controls to ensure there were no contaminants"), using the standardized Earth Microbiome Project 16S protocol. |
| Selection of the reported result | Low | No trial registration number is given (though formal NHS ethics approval was obtained); the study's own section heading transparently states "breastfeeding has modest impact on the gut microbiome," and the text explicitly reports "no differences in any alpha or beta diversity metrics were seen" -- a genuinely transparent null-result framing rather than a one-sided narrative. |

**Microbiome-methods checklist (every study)**

| Domain | Judgment | Reasoning |
|---|---|---|
| Sample collection and storage method reported | Yes | "Whole nappies were removed by the parents and placed into a transport bag. Samples were then taken from the nappies by a gloved study personnel using a sterile scoop and then placed into sterile glass containers. Stool samples were frozen immediately and stored at -20 degrees until DNA extraction." |
| DNA extraction method reported | Yes | "DNA was extracted from thawed stool samples using the QIAamp Fast DNA Stool Mini Kit (Qiagen, Hilden, Germany)," described with full step-by-step detail including bead-beating parameters. |
| Sequencing depth reported | Yes | "A median frequency of 18,354 amplicon sequence variants (ASV) per sample were retained after trimming and filtering." |
| Negative/positive contamination controls reported | Yes | "Tubes without stool were used as negative controls for each batch of samples" (DNA extraction) and "samples were processed in batches with appropriate negative controls to ensure there were no contaminants arising from the DNA extraction kits" (amplification). |
| Compositional-data handling reported | No | Differential abundance was assessed using LEfSe on relative abundance data, with no compositional-aware transform (e.g., CLR/log-ratio) mentioned anywhere. |

---

## #1202 — Hebei delivery-mode x feeding cohort 2020 (China)

*Breastfeeding restored the gut microbiota in caesarean section infants and lowered the
infection risk in early life.* BMC Pediatr. DOI 10.1186/s12887-020-02433-x

Design: prospective longitudinal cohort (Third Hospital of Hebei Medical University, China),
2x2 factorial by delivery mode (VD/CS) and feeding type (pure breastfeeding/pure formula),
n=41 infants (VD_B 14 / VD_F 10 / CS_B 7 / CS_F 10), 207 stool samples across 6 timepoints
(1, 3, 7 days and 1, 3, 6 months).

### J. Risk of bias

*Drafted 26 Oct 2026 from a fresh read of `full_text_md/10.1186_s12887-020-02433-x/10.1186_s12887-020-02433-x.md`'s Methods (Participant enrolment, Sample collection, DNA preparation/sequencing, Bioinformatics analysis) and Results.*

| Field | Value |
|---|---|
| RoB tool applicable | **ROBINS-I** (prospective longitudinal cohort design) |

**ROBINS-I**

| Domain | Judgment | Reasoning |
|---|---|---|
| Confounding | Low | "There were no significant differences in infant gender, gestational age or mother's age between groups," and the Methods explicitly state that "the confounding effect of phenotypes was assessed through permutational multivariate analysis of variance (PERMANOVA)" -- a confirmed-balanced design combined with an explicit, multivariate confounding-assessment approach. |
| Selection of participants | Moderate | Clear eligibility criteria are given (no family allergy history, no maternal obesity/diabetes/allergic/cardiovascular disease/constipation, full-term), but group sizes are small and uneven (7-14 infants per group) with no stated overall screening-to-enrollment flow. |
| Classification of exposures | Moderate | Groups are defined by clear, mutually exclusive categories ("pure human milk" vs. "pure formula milk without prebiotics"), but the specific ascertainment/verification method is not elaborated in the available text. |
| Deviations from intended exposures | Moderate | This is a genuinely longitudinal design with 6 sampling timepoints over 6 months, but no explicit discussion is given of how feeding-category changes mid-study (e.g., weaning from exclusive breastfeeding) were identified or handled. |
| Missing data | Moderate | 41 infants contributed 207 of a theoretical maximum of 246 samples (~84%), with no per-timepoint accounting or explanation given for the shortfall. |
| Measurement of outcomes | Moderate | A standard, objective 16S pipeline (E.Z.N.A. DNA Kit, Illumina MiSeq, Mothur/USEARCH/RDP against Greengenes) is described, but no sequencing-depth figures or contamination controls are reported. |
| Selection of the reported result | Low | No trial registration applicable (observational cohort study); Benjamini-Hochberg FDR correction is applied systematically, and non-significant findings are explicitly labeled and reported as such (e.g., "although insignificant, the GM diversity in CS neonates... was higher than that in VD neonates") rather than omitted. |

**Microbiome-methods checklist (every study)**

| Domain | Judgment | Reasoning |
|---|---|---|
| Sample collection and storage method reported | Yes | "All faecal samples were collected under a nurse's guidance using sample swabs... and stored in sterilized tubes... transferred to a -80degC freezer within 30 min after collection for long-term storage." |
| DNA extraction method reported | Yes | "Faecal bacterial DNA was extracted with the E.Z.N.A. DNA Kit (Omega BioTek, Norcross, GA, United States)." |
| Sequencing depth reported | Not reported | No read-count or depth figure found anywhere in the available text. |
| Negative/positive contamination controls reported | Not reported | No mention anywhere in the available text of negative extraction/PCR controls or positive/mock-community controls. |
| Compositional-data handling reported | No | Bacterial clusters were assigned "based on the relative abundances of different microbial components" via the MetaHIT enterotype method, with no compositional-aware transform (e.g., CLR/log-ratio) mentioned anywhere. |

---

## #1208 — Peshawar feeding-practice diversity study 2018 (Pakistan)

*Impact Of Feeding Practice On Diversity Pattern Of The Gut Microbiome In Infants.* (no DOI
on file; see `extraction/_manifest.csv`.)

Design: small, cross-sectional study (multiple centers/localities, Peshawar, Pakistan), n=46
(23 BF / 23 FF by design, per an a priori power calculation), shotgun metagenomics. One of
the more thinly reported studies in this batch -- no baseline-characteristics comparison
table, no statistical covariate adjustment, no sequencing-depth or contamination-control
reporting anywhere in the available text, despite the paper's own Introduction explicitly
naming delivery mode, antibiotics, and maternal factors as known confounders of infant gut
colonization.

### J. Risk of bias

*Drafted 26 Oct 2026 from a fresh read of `full_text_md/1208_impact_feeding_practice/1208_impact_feeding_practice.md`'s Material and Methods and Results.*

| Field | Value |
|---|---|
| RoB tool applicable | **ROBINS-I** (cross-sectional observational design) |

**ROBINS-I**

| Domain | Judgment | Reasoning |
|---|---|---|
| Confounding | Serious | No baseline-characteristics comparison table is presented anywhere, and no statistical adjustment for any covariate is applied (simple two-sample t-tests only), despite the paper's own Introduction explicitly listing delivery mode, antibiotic usage, maternal age, and other factors as known determinants of infant gut colonization that are never measured, reported, or addressed for this specific comparison. |
| Selection of participants | Moderate | Infants were "enrolled from different centers and localities in Peshawar" with basic exclusion criteria stated (gut surgery, antibiotic use, GI disorders), but no recruitment method or screened-vs-enrolled numbers are given. |
| Classification of exposures | Moderate | The Methods describe infants as "predominantly breast-fed and formula-fed" while the Abstract describes the same groups as simply "breast-fed (BF) and formula-fed (FF)" -- an internal inconsistency in how strictly exclusive feeding was defined -- and no ascertainment method is described at all. |
| Deviations from intended exposures | Low | Cross-sectional observational design with no intervention to deviate from. |
| Missing data | No information | No recruitment-flow, screening, or attrition information is given anywhere in the available text; the target enrollment (23+23) appears to have been achieved exactly. |
| Measurement of outcomes | Moderate | A standard shotgun-metagenomics pipeline is named (Qiagen stool kit, Illumina sequencing, Microbiome Helper SOP: KneadData/Trimmomatic/Bowtie2/MetaPhlAn2), but no sequencing-depth figures or contamination controls are reported anywhere. |
| Selection of the reported result | Moderate | No trial registration applicable; the cited ethics-board approval references a study titled around "plasma zinc status... in breast fed and formula fed infants," suggesting this gut-microbiome-diversity analysis may be a secondary use of a study originally designed around a different primary outcome, though no overt evidence of selective reporting is seen in what is presented (a mix of significant and explicitly non-significant comparisons is reported). |

**Microbiome-methods checklist (every study)**

| Domain | Judgment | Reasoning |
|---|---|---|
| Sample collection and storage method reported | Yes | "A pre-weight stool collection pot, cool pack, pair of disposable gloves, a spatula, and a plastic bag were provided to the participant's mothers to collect the stool sample... Every faecal sample was processed within 12hrs after collection" -- a described collection/handling protocol, though no long-term freezer storage temperature is specified. |
| DNA extraction method reported | Yes | "Following the standard protocols by using Qiagen stool kit the DNA was extracted from the stool samples." |
| Sequencing depth reported | Not reported | No read-count or depth figure found anywhere in the available text. |
| Negative/positive contamination controls reported | Not reported | No mention anywhere in the available text of negative extraction/PCR controls or positive/mock-community controls. |
| Compositional-data handling reported | No | Taxonomic profiling was performed with MetaPhlAn2, which "estimate[s] the relative abundance of microbiome," with no compositional-aware transform (e.g., CLR/log-ratio) mentioned anywhere. |

---

## #1215 — EHF/AAF/human-milk formula trial 2020 (United States)

*Stool microbiome, pH and short/branched chain fatty acids in infants receiving extensively
hydrolyzed formula, amino acid formula, or human milk through two months of age.* BMC
Microbiol. DOI 10.1186/s12866-020-01991-5

Design: hybrid -- multicenter (4 US sites), double-blind RCT between extensively hydrolyzed
formula (EHF) and amino-acid formula (AAF) arms plus a non-randomized human-milk (HM)
reference group, ClinicalTrials.gov NCT02500563 -- routed to ROBINS-I per the hybrid-design
rule. **All infants were exclusively vaginally delivered (cesarean delivery was an exclusion
criterion)**, eliminating delivery mode as a confounder by design. 78 enrolled -> 49
completers (EHF 18/AAF 14/HM 17) with no significant difference in discontinuation rate
between groups (P=0.685).

### J. Risk of bias

*Drafted 26 Oct 2026 from a fresh read of `full_text_md/10.1186_s12866-020-01991-5/10.1186_s12866-020-01991-5.md`'s Methods (Study population, Study design, DNA extraction/sequencing) and Results (Participants).*

| Field | Value |
|---|---|
| RoB tool applicable | **ROBINS-I** (non-randomized human-milk reference group per the hybrid-design rule) |

**ROBINS-I**

| Domain | Judgment | Reasoning |
|---|---|---|
| Confounding | Low | Delivery mode is eliminated as a confounder by design (cesarean delivery was an exclusion criterion for all participants), and baseline anthropometrics, sex, race, and ethnic distribution were explicitly confirmed comparable across all three groups at enrollment. |
| Selection of participants | Low | Multicenter (4 US sites) recruitment with a target sample size reasoned from a prior study, clear eligibility/exclusion criteria, and a fully detailed CONSORT-style flow (78 enrolled -> 3 excluded for consuming no study formula -> 75 -> 49 completers, with specific discontinuation reasons itemized). |
| Classification of exposures | Low | Formula-arm allocation is randomized and blinded; the HM group required exclusive breastfeeding from day 1, and stool-sample compliance was assessed against explicit, pre-specified criteria (Table S2). |
| Deviations from intended exposures | Low | "Study completion was defined as participants who provided a protocol-compliant stool sample at all three study time points," and discontinuation reasons (formula intolerance, parental decision, adverse events) were tracked with no significant difference in discontinuation rate between groups (P=0.685) -- directly addressing concern about differential exposure deviation. |
| Missing data | Moderate | Substantial overall attrition (78 enrolled -> 49 completers, 63%), though reassuringly confirmed to be non-differential across groups (P=0.685 for discontinuation rate). |
| Measurement of outcomes | Low | Rigorous and explicitly quantified: "a total of 8,789,037 sequences were obtained with a mean of 51,099 sequences per sample," with diversity measures computed at a specified rarefaction depth of 9,351 sequences, using a well-described phenol-chloroform DNA extraction and QIIME2/DADA2 pipeline. |
| Selection of the reported result | Low | Pre-registered well in advance (NCT02500563, registered July 2015); FDR correction is applied systematically across all statistical approaches, and multiple complementary methods (Wilcoxon tests, DESeq2, random forest classification) are used to triangulate findings. |

**Microbiome-methods checklist (every study)**

| Domain | Judgment | Reasoning |
|---|---|---|
| Sample collection and storage method reported | Yes | "Day 30 and 60 stool samples were collected +-24 h of the study visit and compliant samples were stored onsite at -20degC." |
| DNA extraction method reported | Yes | "DNA from stool samples were extracted using phenol-chloroform as described by [ref] with the exception that all incubation times were carried out for 30 min and DNA was recovered with 100 ul of DNase-free water." |
| Sequencing depth reported | Yes | "A total of 8,789,037 sequences were obtained with a mean of 51,099 sequences per sample... Alpha and beta diversity measures were computed using a sample depth of 9351 sequences." |
| Negative/positive contamination controls reported | Not reported | No mention anywhere in the available text of negative extraction/PCR controls or positive/mock-community controls. |
| Compositional-data handling reported | No | Results are presented as "relative abundance" (Table S3) with differential-abundance testing via Wilcoxon tests, DESeq2, and random forest -- no compositional-aware transform (e.g., CLR/log-ratio) mentioned anywhere. |

---

## #1229 — Inner Mongolia/Beijing three-arm feeding cohort 2020 (China)

*Comparison of gut microbiota in exclusively breast-fed and formula-fed babies: a study of
91 term infants.* Sci Rep. DOI 10.1038/s41598-020-72635-x

Design: prospective, non-randomized cohort across 4 hospitals in 2 Chinese cities
(2016-2017), 3 parallel exclusive-feeding arms (breast-fed n=30, formula-A n=30, formula-B
n=31), each fed exclusively for >4 months with explicit exclusion of babies who switched
feeding type before then. Notably, formula-fed babies were specifically those whose
mothers "have to be fed with formula due to mother's disease or medicine and other
objective reasons" -- i.e., assignment to the formula arm was itself driven by a maternal
health indication, not an unconstrained choice, which is a built-in confounding risk the
paper's own unadjusted group comparisons do not address.

### J. Risk of bias

*Drafted 27 Oct 2026 from a fresh read of `full_text_md/10.1038_s41598-020-72635-x/10.1038_s41598-020-72635-x.md`'s Methods (Study population, Study design, Samples collection, DNA extraction and sequencing) and Results (Basic characteristics).*

| Field | Value |
|---|---|
| RoB tool applicable | **ROBINS-I** (non-randomized, parent/clinically-driven group assignment) |

**ROBINS-I**

| Domain | Judgment | Reasoning |
|---|---|---|
| Confounding | Serious | Formula-arm assignment was itself driven by "mother's disease or medicine and other objective reasons," a direct link between maternal health status and exposure group that is never measured or adjusted for; baseline anthropometrics and delivery-mode ratio are confirmed comparable by table (p>0.05), but the main breastfed-vs-formula taxon comparisons use unadjusted two-tailed t-tests/Wilcoxon tests, with no statistical control for the covariates the authors' own correlation analysis (Table 2) shows are associated with specific genera (antibiotics, siblings, pets, district). |
| Selection of participants | Moderate | Recruited from only 4 hospitals in 2 cities, with authors explicitly stating in their own Limitations that "there might be selection bias in the enrolment of the study population" because exclusively-fed infants were hard to find at a single site; formula-arm choice itself was also voluntary/parental rather than a population-representative process. |
| Classification of exposures | Low | Exclusivity is tightly defined and enforced by exclusion criteria (any feeding-type change before 4 months removes the infant from the study), giving a clean, unambiguous exposure classification. |
| Deviations from intended exposures | Low | The explicit exclusion criteria (removing any infant who could not sustain the assigned feeding type for the full 4 months) directly prevent deviation from the intended exposure from affecting the analysis. |
| Missing data | Moderate | Four of an initial ~95 enrolled infants dropped out with no reasons or group breakdown given, and per-timepoint stool-sample counts fall well short of the full N (81/80/68 of 91 at 40 days/3 m/6 m respectively, ~25% missing by 6 months) with no explanation of why or whether this differed by feeding group. |
| Measurement of outcomes | Low | Centralized, uniform processing for all groups: CTAB/SDS DNA extraction, 16S V4 region (515F/806R primers) on Illumina MiSeq, QIIME v1.7/UPARSE pipeline, SILVA/RDP classification, with sequencing depth explicitly quantified (20,383,186 total reads, median 84,737 reads/sample). |
| Selection of the reported result | Moderate | No trial/protocol registration for this observational cohort, but reporting appears reasonably complete -- both significant and explicitly non-significant comparisons are reported across taxa and timepoints, with no overt sign of selective suppression. |

**Microbiome-methods checklist (every study)**

| Domain | Judgment | Reasoning |
|---|---|---|
| Sample collection and storage method reported | Yes | "All the samples were kept in a sterile container, immediately stored in refrigerator at -70degC and sent to Beijing for testing collectively." |
| DNA extraction method reported | Yes | "Total genome DNA from samples was extracted using CTAB/SDS method." |
| Sequencing depth reported | Yes | "A total of 20,383,186 reads (median 84,737 reads per sample) were obtained from 16S rRNA gene sequencing." |
| Negative/positive contamination controls reported | Not reported | No mention anywhere in the available text of negative extraction/PCR controls or positive/mock-community controls. |
| Compositional-data handling reported | No | Taxon comparisons use relative abundance (percentages) with t-tests/Kruskal-Wallis, and beta diversity uses UniFrac/PERMANOVA (a legitimate distance-based approach but not a compositional-data transform) -- no CLR/ALR/Aitchison/ANCOM mentioned anywhere. |

---

## #1237 — CD-GEMM multi-omics risk-factor cohort 2020 (USA/Italy)

*Multi-omics analysis reveals the influence of genetic and environmental risk factors on
developing gut microbiota in infants at risk of celiac disease.* Microbiome. DOI
10.1186/s40168-020-00906-w. NCT02061306.

Design: prospective cohort (CD-GEMM), 31 infants (genetically at elevated celiac-disease
risk, a first-degree relative with CD) selected from a larger ~400-infant birth cohort for
having stool samples at all three pre-specified pre-solid-food timepoints (enrollment, 3
months, 4-6 months). Infant feeding type (exclusive breastmilk / exclusive formula / both)
is one of several environmental risk factors analyzed alongside delivery mode, antibiotic
exposure, and HLA genetic risk, using a multivariate regression framework (MaAsLin) that
explicitly forces all of these covariates in simultaneously -- a notably more rigorous
confounding-control approach than most studies in this batch.

### J. Risk of bias

*Drafted 27 Oct 2026 from a fresh read of `full_text_md/10.1186_s40168-020-00906-w/10.1186_s40168-020-00906-w.md`'s Methods (Subjects/sampling, DNA extraction, Taxonomic/Functional/Metabolomic profiling, Identifying associations).*

| Field | Value |
|---|---|
| RoB tool applicable | **ROBINS-I** (non-randomized cohort; feeding type is a self-selected environmental exposure) |

**ROBINS-I**

| Domain | Judgment | Reasoning |
|---|---|---|
| Confounding | Low | "All metadata variables were forced simultaneously to control for confounders" in the MaAsLin model -- delivery mode, antibiotic exposure, and HLA genetic risk are explicitly adjusted for alongside feeding type, rather than left as unmeasured or merely balance-checked. |
| Selection of participants | Moderate | The 31 analyzed infants are a subset of a much larger (~400-infant) ongoing cohort, selected specifically for having complete stool sampling at all three pre-specified timepoints; the selection rule is objective and pre-specified, but no comparison is given of this subsample against the excluded majority of the cohort. |
| Classification of exposures | Moderate | Feeding type required exclusive feeding to be reported for at least 2 of 3 monthly-diary time points, which is a reasonably explicit ascertainment rule, but relies on parent-completed diaries (self-report, not independently verified) and collapses any non-exclusive pattern into a single "both" category. |
| Deviations from intended exposures | Low | Purely observational exposure classification (feeding type as parents actually practiced and reported it) with no intervention protocol to deviate from. |
| Missing data | Low | The analytic sample of 31 was defined precisely by having complete stool collection at all three specified timepoints, so within this analysis there is no further unexplained missingness (the representativeness concern is captured under Selection of participants instead). |
| Measurement of outcomes | Low | Rigorous, centralized, uniform pipeline across all groups: Qiagen PowerSoil DNA extraction, CosmosID k-mer-based shotgun metagenomic taxonomic profiling, a full functional-profiling pipeline (BBDuk/SPAdes/Prodigal/InterProScan-KEGG), and GC-MS metabolomics run in triplicate with Level-1 MSI standard confirmation. |
| Selection of the reported result | Low | Pre-registered (NCT02061306); feeding type is analyzed as one of several pre-specified risk factors within a single structured multivariate framework, and both significant and non-significant pathway/metabolite associations are reported systematically rather than selectively. |

**Microbiome-methods checklist (every study)**

| Domain | Judgment | Reasoning |
|---|---|---|
| Sample collection and storage method reported | Not reported | Only "All fecal samples included in the metagenomic analysis were stored and processed centrally in the USA" is given -- no collection protocol, storage temperature, or time-to-freeze is stated anywhere in the available text. |
| DNA extraction method reported | Yes | "Total DNA from each sample was extracted using the Qiagen Power soil DNA extraction kit." |
| Sequencing depth reported | Not reported | The text states only that "Additional File 2" contains "information on the sequencing depth of each sample" -- a pointer to a supplementary file, not a figure stated directly in the main text. |
| Negative/positive contamination controls reported | Not reported | No mention anywhere in the available text of negative extraction/PCR controls or positive/mock-community controls. |
| Compositional-data handling reported | No | Functional-pathway abundance is computed as FPKM (fragments per kilobase per million), an RNA-seq-style normalization, not a compositional-aware transform (e.g., CLR/log-ratio); taxonomic results are likewise not described with any such transform. |

---

## #1295 — CBA L74-fermented-formula RCT-with-BF-reference 2020 (Italy)

*Analysis of immune, microbiota and metabolome maturation in infants in a clinical trial of
Lactobacillus paracasei CBA L74-fermented formula.* Nat Commun. DOI
10.1038/s41467-020-16582-1. NCT03637894 (registered retrospectively).

Design: hybrid -- monocentric, randomized, double-blind trial between a standard formula
(S) and an L. paracasei CBA L74-fermented formula (F), stratified by delivery mode, plus a
non-randomized exclusively-breastfed reference group -- routed to ROBINS-I per the
hybrid-design rule. 78 full-term infants enrolled (~26/group); microbiota analysis was
restricted to a 9-infant/group (54 total) subsample "to ensure a consistent number"
because stool could not be collected from every young enrollee. Baseline anthropometric
comparability was assessed only between the two randomized formula arms, not against the
breastfed reference group.

### J. Risk of bias

*Drafted 27 Oct 2026 from a fresh read of `full_text_md/10.1038_s41467-020-16582-1/10.1038_s41467-020-16582-1.md`'s Methods (Study design, Study subjects, Intervention, Microbiota analysis, Statistical analysis).*

| Field | Value |
|---|---|
| RoB tool applicable | **ROBINS-I** (non-randomized breastfed reference group per the hybrid-design rule) |

**ROBINS-I**

| Domain | Judgment | Reasoning |
|---|---|---|
| Confounding | Moderate | Randomization (computer-generated, stratified by delivery mode) and blinding rigorously control confounding between the two formula arms, but the breastfed reference group is self-selected ("mothers... encouraged to breastfed... if they could not or intended not to"), and no baseline-characteristic comparison is presented between this group and the formula arms, leaving that comparison's confounding unaddressed. |
| Selection of participants | Moderate | Explicit, objective eligibility criteria (singleton, GA 37/0-41/6 weeks, birth weight 10th-90th percentile, multiple exclusions) applied to a single-center convenience sample; assignment to the breastfed vs. formula pathway itself depended on maternal choice/ability to breastfeed rather than a population-representative process. |
| Classification of exposures | Low | Rigorously defined and operationalized: randomized, blinded, indistinguishable formula packaging with matched macronutrient content for the two formula arms, and an explicit protocol definition for the reference group ("exclusive breast milk for the first 3 months of life"). |
| Deviations from intended exposures | No information | No information is given anywhere in the available text on protocol adherence, crossover, or deviation from assigned feeding type by any participant. |
| Missing data | Moderate | The microbiota sub-analysis used only 9 of 26 enrolled infants per group (~35%), explained only as being "to ensure a consistent number" after incomplete stool collection in young infants, with no comparison of included vs. excluded infants and no stated selection rule for which 9 were analyzed. |
| Measurement of outcomes | Low | Rigorous, uniform, centrally processed pipeline across all groups: a detailed multi-step G'NOME kit DNA extraction protocol, 16S V3 region (Probio_Uni/Probio_Rev primers) sequenced on Illumina MiSeq at a dedicated facility, QIIME2/DADA2 processing, SILVA132 classification. |
| Selection of the reported result | Moderate | The trial "was registered retrospectively" (NCT03637894), a recognized risk marker for selective outcome reporting since endpoints were not locked in a public registry before data collection began, though the paper does report both significant and non-significant findings reasonably systematically. |

**Microbiome-methods checklist (every study)**

| Domain | Judgment | Reasoning |
|---|---|---|
| Sample collection and storage method reported | Yes | "Faecal samples were collected and immediately frozen at -20degC, and then stored at -80degC at our institution." |
| DNA extraction method reported | Yes | A detailed multi-step protocol is given: "DNA was extracted from 200 mg of faecal samples with G'NOME DNA isolation kit (MP Biomedicals) following a published protocol," with the full lysis/precipitation procedure described. |
| Sequencing depth reported | Not reported | No read-count or depth figure is given anywhere in the available text (only that "reads were truncated at the first instance of a quality score... ≤20" during QC, with no resulting depth number stated). |
| Negative/positive contamination controls reported | Not reported | No mention anywhere in the available text of negative extraction/PCR controls or positive/mock-community controls. |
| Compositional-data handling reported | No | Alpha-diversity (Chao1) and beta-diversity (weighted UniFrac/PCoA) are legitimate distance-based methods but not compositional-data transforms; genus-level differential abundance is tested by ANOVA/TukeyHSD directly on abundances with no CLR/ALR/Aitchison/ANCOM mentioned anywhere. |

---

## #1300 — GUSTO ethnicity/delivery/feeding cohort 2020 (Singapore)

*Ethnic diversity in infant gut microbiota is apparent before the introduction of
complementary diets.* Gut Microbes. DOI 10.1080/19490976.2020.1756150. NCT01174875.

Design: prospective longitudinal birth cohort (GUSTO), 106 infants (Chinese/Malay/Indian)
sampled at 3/6/12/24 months, examining seven factors (ethnicity, delivery mode,
breastfeeding status, maternal education, gestational age, birthweight, gender) via
canonical correspondence analysis with explicit mutual covariate adjustment (partial CCA)
and multiple linear regression. Breastfeeding status (breastfed-only / mixed / formula-only)
was assessed only at 3 months, available for 105 of 106 infants.

### J. Risk of bias

*Drafted 27 Oct 2026 from a fresh read of `full_text_md/10.1080_19490976.2020.1756150/10.1080_19490976.2020.1756150.md`'s Materials and methods (Study cohort, DNA extraction and 16S rRNA gene sequencing, Quality filtration and bioinformatics analysis) and Results (Three significant factors, Breastfeeding status).*

| Field | Value |
|---|---|
| RoB tool applicable | **ROBINS-I** (non-randomized, observational birth-cohort exposure) |

**ROBINS-I**

| Domain | Judgment | Reasoning |
|---|---|---|
| Confounding | Low | Breastfeeding status is explicitly and mutually adjusted for alongside ethnicity and delivery mode via partial CCA and multiple linear regression at every relevant time point, rather than left as an unmeasured or merely balance-checked covariate; antibiotic exposure was also explicitly tested and reported (non-significant) as a potential confounder. |
| Selection of participants | Moderate | Infants are a subset ("106 infants within the normal range of BMI") selected from the larger GUSTO birth cohort (recruited from two major Singapore public hospitals, 2009-2010), but the exact selection process and representativeness of these 106 relative to the full cohort is not detailed in the available text. |
| Classification of exposures | Low | Breastfeeding status has an explicit, structured three-category definition ("breastfed only meant infants received breast milk and certain liquids... without non-human milk or solids") ascertained at a pre-specified timepoint (3M) for 105 of 106 infants. |
| Deviations from intended exposures | Low | Purely observational exposure classification as practiced and reported; no intervention protocol to deviate from. |
| Missing data | Low | Breastfeeding-status data were available for 105 of the 106 infants (99%); the main covariate of interest has minimal missingness. |
| Measurement of outcomes | Low | Rigorous and standardized: PowerSoil DNA extraction, 16S V4 region sequenced at a dedicated facility (Argonne National Laboratories) on Illumina MiSeq, with all samples rarefied to a common sequencing depth (12,000 reads, 1000 iterations) specifically to remove depth-driven differences between samples before comparison. |
| Selection of the reported result | Low | Pre-registered as part of the GUSTO cohort (NCT01174875); non-significant findings (maternal education after adjustment, antibiotic exposure, first-generation migrant status) are explicitly reported alongside significant ones, indicating no apparent selective suppression. |

**Microbiome-methods checklist (every study)**

| Domain | Judgment | Reasoning |
|---|---|---|
| Sample collection and storage method reported | Yes | "Stool samples of 106 infants were collected at 3, 6, 12 and 24 months, and stored at -80degC." |
| DNA extraction method reported | Yes | "DNA was extracted from 250 mg feces according to the kit protocol provided by the manufacturer (PowerSoil DNA isolation kit... Mo Bio)." |
| Sequencing depth reported | Yes | "Overall, 11,564,295 high-quality reads were obtained covering a total of 424 fecal samples, with an average of 27,342 +/- 7,312 reads per sample," and "sequences for each sample were rarefied to 12,000." |
| Negative/positive contamination controls reported | Not reported | No mention anywhere in the available text of negative extraction/PCR controls or positive/mock-community controls. |
| Compositional-data handling reported | No | Analysis uses CCA/partial CCA ordination (a legitimate multivariate ecological method, not a compositional-data transform) on OTU abundance tables -- no CLR/ALR/Aitchison/ANCOM mentioned anywhere. |

---

## #1319 — Beginnings Study BF/MF/SF cross-sectional cohort 2020 (USA)

*Neonatal diet alters fecal microbiota and metabolome profiles at different ages in infants
fed breast milk or formula.* Am J Clin Nutr. DOI 10.1093/ajcn/nqaa076. NCT00616395.

Design: cross-sectional subsets (by age: 3, 6, 9, 12 months) of a prospective cohort
(the Beginnings Study), non-randomized three-arm comparison -- breastfed (BF), cow-milk
formula (MF), soy formula (SF) -- with parents choosing the diet before enrollment ("with
advice from their pediatricians"). Only 22 of 98 infants contributed samples at more than
one age, so each age-timepoint functions largely as its own independent cross-sectional
comparison rather than a single matched longitudinal one.

### J. Risk of bias

*Drafted 27 Oct 2026 from a fresh read of `full_text_md/10.1093_ajcn_nqaa076/10.1093_ajcn_nqaa076.md`'s Methods (cohort description, 16S sequencing, Statistical analysis) and Results.*

| Field | Value |
|---|---|
| RoB tool applicable | **ROBINS-I** (non-randomized, parent-chosen feeding exposure) |

**ROBINS-I**

| Domain | Judgment | Reasoning |
|---|---|---|
| Confounding | Moderate | All diversity and community-structure analyses (ANCOVA, PERMANOVA) are explicitly adjusted for child sex and birth weight, but mode of delivery -- a major known determinant of infant gut microbiota -- is never mentioned, measured, or adjusted for anywhere in the available text, and diet was parent-selected rather than assigned. |
| Selection of participants | Moderate | Drawn from a single-center clinical cohort with explicit eligibility criteria (healthy pregnancy, no growth-affecting maternal medications/conditions, no maternal soy/alcohol/smoking), but each age-specific analysis uses only a cross-sectional subset of the full cohort (just 22 of 98 infants had samples at more than one age), so representativeness of each age's analyzed subset relative to the full enrolled cohort is unclear. |
| Classification of exposures | Low | Exposure groups are explicitly named (specific commercial BF/MF/SF formula brands), formula-switching between 2-12 months is an explicit exclusion criterion, and infants transitioning feeding type are deliberately re-classified into a separate "no longer breastfeeding" (NLB) category rather than miscoded. |
| Deviations from intended exposures | Low | The explicit exclusion of infants who changed formula type, and the separate NLB category for breastfed infants who transitioned, directly addresses potential deviation from the infant's assigned/chosen diet. |
| Missing data | Moderate | Multiple sequential QC-driven exclusions are applied at both the microbiome stage (samples with <1000 reads removed, n=21) and the metabolomics stage (PCA-outlier removal, n=7; univariate Grubb's-test outliers, n=23 and 29 in negative/positive mode) without reporting whether these exclusions were balanced across diet groups. |
| Measurement of outcomes | Low | Rigorous, standardized, and detailed across all groups: PowerSoil DNA extraction, 16S V4 region (515F/806R primers) with explicit PhiX spike-in on Illumina MiSeq, QIIME 1.9.1/Greengenes processing, plus a fully detailed untargeted LC-MS metabolomics pipeline (Q-Exactive Orbitrap, QC pooling, FDR-corrected statistics). |
| Selection of the reported result | Low | Pre-registered (NCT00616395); extensive supplementary tables report both significant and non-significant comparisons systematically across all ages and both statistical approaches (Kruskal-Wallis and DESeq2), with FDR correction applied throughout. |

**Microbiome-methods checklist (every study)**

| Domain | Judgment | Reasoning |
|---|---|---|
| Sample collection and storage method reported | Yes | "Sterile tubes were provided to families and fecal samples were collected either during the study visit or at home. If fecal samples were collected at home, the sample was frozen (-20degC) and delivered back to the research facility on ice. Samples were kept at -80degC until further analyses." |
| DNA extraction method reported | Yes | "The PowerSoil (R) DNA Isolation Kit (MOBIO Laboratories, Inc.) was used for DNA extraction." |
| Sequencing depth reported | Yes | "Total sampling depth was 3,192,176 sequencing reads. Mean sample depth per sample was 19,216 sequencing reads," with a post-QC "average sampling depth of 11,414 reads" also stated directly. |
| Negative/positive contamination controls reported | Not reported | Only a ~30% PhiX DNA spike-in is mentioned, which is a sequencing-run calibration control, not a biological negative/positive contamination control; no such control is described anywhere in the available text. |
| Compositional-data handling reported | Yes | "16S rRNA data were adjusted for correlation-based analyses... using a centered log ratio (CLR) transformation," with zeros imputed via the geometric Bayesian multiplicative method (zCompositions package) -- an explicit, named compositional-data transform. |

---

## #1323 — A.MA.MI pilot cohort (protocol + preliminary results) 2020 (Italy)

*Prenatal and postnatal determinants in shaping offspring's microbiome in the first 1000
days: study protocol and preliminary results at one month of life.* Ital J Pediatr. DOI
10.1186/s13052-020-0794-8. NCT04122612.

Design: longitudinal prospective observational pilot study (A.MA.MI, explicitly described
by the authors as a feasibility/pilot study), 63 mother-infant dyads recruited at a single
Italian center. The breastfed-vs-formula-fed comparison presented here is a preliminary,
univariate one at T1 (1 month) only; the same paper separately found delivery mode and
maternal pre-pregnancy BMI to significantly affect the infant microbiome at T0, but neither
is adjusted for in the BF-vs-FF comparison at T1.

### J. Risk of bias

*Drafted 27 Oct 2026 from a fresh read of `full_text_md/10.1186_s13052-020-0794-8/10.1186_s13052-020-0794-8.md`'s Methods (Participants, Samples collection/analysis, DNA extraction, Statistical analysis) and Results.*

| Field | Value |
|---|---|
| RoB tool applicable | **ROBINS-I** (non-randomized, observational pilot cohort) |

**ROBINS-I**

| Domain | Judgment | Reasoning |
|---|---|---|
| Confounding | Serious | The BF-vs-FF comparison at T1 uses simple univariate tests (t-test/Mann-Whitney) with no adjustment for delivery mode or maternal pre-pregnancy BMI, despite this same paper's own T0 analysis finding both factors to significantly affect the infant microbiome -- a confounding gap the authors' own data demonstrates is plausible. |
| Selection of participants | Moderate | Single-center pilot/feasibility study (explicitly framed as such by the authors) with explicit eligibility criteria (GA 37-42 weeks, excluding congenital disease, NICU admission, gestational diabetes, hyperthyroidism), but by design a small convenience sample not intended to be representative. |
| Classification of exposures | Moderate | Feeding mode is reported only as a simple breastfed/formula-fed binary (34/24 infants) with no explicit operational definition of exclusivity stated anywhere in the available text, and no separate "mixed feeding" category despite this being common practice. |
| Deviations from intended exposures | Low | Purely observational exposure classification (feeding as it was actually practiced); no intervention protocol to deviate from. |
| Missing data | Moderate | One dyad dropped out after enrollment and four more dropped out before T1 (5 of 63, ~8%), with no information given on whether attrition differed between eventual feeding groups. |
| Measurement of outcomes | Low | Rigorous and centrally outsourced to a single commercial sequencing lab, blinded to clinical information ("Samples had only the study ID number; no clinical or personal information was shipped with the samples"): QIAamp Fast DNA Stool kit, 16S V3-V4 region on Illumina MiSeq, QIIME/RDP classifier plus BLAST-based taxonomic attribution. |
| Selection of the reported result | Moderate | Explicitly framed by the authors as "preliminary and explorative" results from an ongoing pilot; numerous phylum/genus/species-level comparisons are reported across three separate exposure factors (delivery mode, maternal BMI, feeding type) at a nominal P<0.05 threshold with no clear multiple-testing correction described for this specific preliminary analysis. |

**Microbiome-methods checklist (every study)**

| Domain | Judgment | Reasoning |
|---|---|---|
| Sample collection and storage method reported | Yes | Stool was collected into two separate containers and stored at -80degC at two institutions, with an explicit protocol to reschedule collection if "child was currently ill... had a diarrheal illness... or has been treated with antibiotics in the past 7 days." |
| DNA extraction method reported | Yes | "Total genomic bacterial DNA was isolated from frozen stool samples using the QIAamp(R) Fast DNA Stool Mini Kit (QIAGEN, Hilden, Germany), according to the manufacturer's instructions." |
| Sequencing depth reported | Yes | "Of 118 neonatal stool samples, the average of reads which passed filter quality was 106,298.81 +/- 69,276.42 sequences." |
| Negative/positive contamination controls reported | Not reported | No mention anywhere in the available text of negative extraction/PCR controls or positive/mock-community controls. |
| Compositional-data handling reported | No | Relative-abundance percentages are compared by t-test/ANOVA/Mann-Whitney/Kruskal-Wallis, with a zero-inflated count model used to handle sparse taxa -- a count-model adjustment, not a compositional-aware log-ratio transform (CLR/ALR/Aitchison/ANCOM are not mentioned anywhere). |

---

## #1325 — Korean newborn-to-child microbiome case series 2020 (South Korea)

*Microbiome Study of Initial Gut Microbiota from Newborn Infants to Children Reveals that
Diet Determines Its Compositional Development.* J Microbiol Biotechnol. DOI
10.4014/jmb.2002.02042.

Design: a very small, purely descriptive observational case series -- two
breast-milk-fed (BM1) and seven formula-milk-fed (FM1) Korean newborns (all delivered
vaginally, holding delivery mode constant by inclusion) sampled three times in the first
week of life, with no statistical hypothesis testing (no p-values) anywhere in the BM1-vs-FM1
comparison -- only descriptive relative-abundance percentages and a narrative
interpretation. A separate, unrelated older BM2/FM2/weaning/solid-food comparison in the
same paper is not a breastfed-vs-formula comparison and is not relevant to this review's
exposure contrast.

### J. Risk of bias

*Drafted 27 Oct 2026 from a fresh read of `full_text_md/10.4014_jmb.2002.02042/10.4014_jmb.2002.02042.md` in full (the entire research note).*

| Field | Value |
|---|---|
| RoB tool applicable | **ROBINS-I** (non-randomized, purely observational case series) |

**ROBINS-I**

| Domain | Judgment | Reasoning |
|---|---|---|
| Confounding | Serious | No statistical model or adjustment of any kind is used anywhere in the BM1-vs-FM1 comparison (purely descriptive percentages); delivery mode is held constant by inclusion (all natural delivery), but no other potential confounder (gestational age, birth weight, antibiotics, maternal factors) is even mentioned. |
| Selection of participants | Serious | No recruitment method, eligibility criteria, or sampling frame is described anywhere beyond "fecal samples were obtained from newborn Korean infants"; the resulting BM1/FM1 split (2 vs. 7) is a tiny, evidently opportunistic convenience sample. |
| Classification of exposures | Moderate | Groups are clearly labeled "breast milk-fed" (BM1) and "formula milk-fed" (FM1) in Table 1, but no operational definition of feeding exclusivity is given anywhere in the text. |
| Deviations from intended exposures | No information | No information is given anywhere in the available text on this domain. |
| Missing data | Low | Sample collection is reported transparently: Table 1 explicitly notes which newborns had only a single sample collected (G, H, I) rather than the full three, with no indication of concealed or unexplained missingness. |
| Measurement of outcomes | Low | The BM1 and FM1 newborn groups were processed identically (454/GS-FLX+ pyrosequencing of the same primer-amplified region, per a cited prior protocol), giving internal methodological consistency for this specific comparison, even though the paper's separate older-infant comparison used a different platform. |
| Selection of the reported result | Serious | No trial/protocol registration; no statistical significance testing is applied anywhere to the BM1-vs-FM1 comparison, and the narrative selectively emphasizes compositional differences consistent with a beneficial-breastfeeding hypothesis without any pre-specified analysis plan or threshold. |

**Microbiome-methods checklist (every study)**

| Domain | Judgment | Reasoning |
|---|---|---|
| Sample collection and storage method reported | Not reported | No description of stool collection method, container, storage temperature, or time-to-freeze is given anywhere in the available text. |
| DNA extraction method reported | Not reported | The text states only that DNA "was extracted and purified following a previous protocol [7]," deferring entirely to a citation without restating any extraction method in this paper's own text. |
| Sequencing depth reported | Not reported | No read-count or depth figure is given anywhere in the available text. |
| Negative/positive contamination controls reported | Not reported | No mention anywhere in the available text of negative extraction/PCR controls or positive/mock-community controls. |
| Compositional-data handling reported | No | Results are presented as relative-abundance percentages, with PCoA (Bray-Curtis, for the separate older-infant comparison) a legitimate distance-based method but not a compositional-data transform -- no CLR/ALR/Aitchison/ANCOM mentioned anywhere. |

---

## #1416 — Umea MFGM-formula RCT-with-BF-reference 2019 (Sweden)

*Fecal microbiome and metabolome of infants fed bovine MFGM supplemented formula or
standard formula with breast-fed infants as reference: a randomized controlled trial.* Sci
Rep. DOI 10.1038/s41598-019-47953-4. NCT00624689 (registered Feb 2008, prospectively).

Design: hybrid -- double-blind RCT between a standard formula (SF) and a bovine
MFGM-supplemented experimental formula (EF), plus a non-randomized exclusively-breastfed
(BF) reference group -- routed to ROBINS-I per the hybrid-design rule. A balanced subset of
90 infants (15M/15F per group) was randomly selected from a 240-infant parent trial for
microbiome/metabolome analysis. The authors themselves explicitly flag the key limitation:
"Comparisons between FF and BF infants... should be made with caution since these two
groups were not randomized and potential confounding factors involving feeding choice
cannot be ruled out." Delivery mode also differed notably by group at baseline (96.2%/96.5%
vaginal in BF/SF vs. 82.1% in EF) without being statistically adjusted for.

### J. Risk of bias

*Drafted 27 Oct 2026 from a fresh read of `full_text_md/10.1038_s41598-019-47953-4/10.1038_s41598-019-47953-4.md`'s Results (Characteristics of study population and data exclusion) and Methods (Study population, Stool collection, Fecal metabolic DNA extraction and library preparation, Analysis of 16s amplicon sequence, Statistical analysis).*

| Field | Value |
|---|---|
| RoB tool applicable | **ROBINS-I** (non-randomized breastfed reference group per the hybrid-design rule) |

**ROBINS-I**

| Domain | Judgment | Reasoning |
|---|---|---|
| Confounding | Serious | The authors explicitly state that the BF-vs-FF comparison is non-randomized and that "potential confounding factors involving feeding choice cannot be ruled out," and a real baseline imbalance in delivery mode by group (82.1% vaginal in EF vs. 96.2-96.5% in BF/SF) is reported but not statistically adjusted for in any of the microbiome or metabolome models described. |
| Selection of participants | Low | The parent trial had explicit, clearly stated eligibility criteria (GA 37-42 weeks, birth weight 2.5-4.5 kg, no chronic illness), and the 90-infant subsample was randomly selected and balanced by sex from the 240-infant trial, with every subsequent exclusion (formula discontinuation n=2, no food diary n=1, heavily mixed-fed BF n=3, FF consuming another formula n=4, antibiotic use n=3) transparently enumerated. |
| Classification of exposures | Low | Exposure groups are rigorously operationalized, with explicit exclusion of infants from the BF group who were "heavily mixed-fed" and FF infants who "consumed another formula," directly protecting the purity of each exposure category. |
| Deviations from intended exposures | Low | Infants who stopped consuming study formula were explicitly identified and excluded (n=2), and the analysis explicitly stratifies 4- and 6-month samples by complementary-food intake to separate the effect of weaning (a natural, anticipated change) from the feeding-group comparison itself. |
| Missing data | Moderate | Exclusions at each stage are small and transparently reported, but the authors themselves disclose that "by 12 months of age, only 6 infants in the BF group had a record of breast milk consumption," a sparse-data limitation specific to the longer-term BF comparison that the paper explicitly flags as preventing confirmation of persisting breastfeeding effects. |
| Measurement of outcomes | Low | Rigorous and well-controlled: a detailed, modified HMP DNA-extraction protocol, explicit airborne-contamination avoidance measures (per Salter et al.), a described PCR/sequencing pipeline (QIIME/Greengenes/PICRUSt), and NMR-based metabolomics processed identically for all groups. |
| Selection of the reported result | Low | Prospectively registered (NCT00624689, Feb 2008, before the trial); this analysis builds transparently on a long, consistently cited series of prior publications from the same cohort, applies FDR correction throughout, and explicitly reports non-significant findings (e.g., no significant difference in microbial richness at most time points) alongside significant ones. |

**Microbiome-methods checklist (every study)**

| Domain | Judgment | Reasoning |
|---|---|---|
| Sample collection and storage method reported | Yes | "The samples were immediately frozen at -80degC or, if the sample was collected at home, frozen at -20degC in a home freezer before transportation to the clinic and storage at -80degC. The maximum storage time at -20degC was 3 days." |
| DNA extraction method reported | Yes | "Approximately 250 mg of fecal material was extracted according to the HMP protocol using MoBio PowerLyzer PowerSoil DNA isolation kit," with the specific protocol modifications described in detail. |
| Sequencing depth reported | Not reported | Only process-loss percentages are given (e.g., "about 0.5% poor quality sequences were excluded," "74.16% of the sequences remained after joining") -- no absolute read-count or depth figure is stated anywhere in the available text. |
| Negative/positive contamination controls reported | Yes | "One negative control 'blank sample' from extraction of PCR-grade water... was included for each batch. This batch sample was subsequently amplified via PCR, visually inspected... and included in the final DNA library," on top of explicit airborne-contamination avoidance measures during extraction. |
| Compositional-data handling reported | Yes | "The differential analysis for the microbiome was computed at the genus level using ANCOM(104) and controls for False Discovery Rate (FDR)" -- Analysis of Composition of Microbiomes (ANCOM) is an explicitly named compositional-data method. |

---

## #1430 — Jiangnan University delivery/feeding species-level cohort 2019 (China)

*Bifidobacterium and Lactobacillus Composition at Species Level and Gut Microbiota
Diversity in Infants before 6 Weeks.* Int J Mol Sci. DOI 10.3390/ijms20133306.

Design: cross-sectional observational study, 112 Han-Chinese infants (~6 weeks of age),
a 2x3 factorial comparison of delivery mode (SVD/CS) and feeding method (BF/MPF/MF),
deliberately sampled to be balanced across groups rather than consecutively enrolled.
**Notable internal inconsistency in the source paper itself**: the Methods section's own
stated definition ("the MPF group included those infants receiving some human milk and
some milk powder; the MF group consisted of those infants receiving infant formula as the
sole source of milk") is the reverse of how MPF and MF are used everywhere else in the
paper (Abstract/Results/Discussion consistently treat MPF = milk-powder/formula-exclusive
and MF = mixed-fed) -- a genuine ambiguity in the primary source, not a drafting error here.

### J. Risk of bias

*Drafted 27 Oct 2026 from a fresh read of `full_text_md/10.3390_ijms20133306/10.3390_ijms20133306.md`'s Materials and Methods (Participants and Sample Collection, Fecal Genomic DNA Extraction, Bioinformatics Analysis, Statistical Analysis) and Results.*

| Field | Value |
|---|---|
| RoB tool applicable | **ROBINS-I** (non-randomized, observational cross-sectional comparison) |

**ROBINS-I**

| Domain | Judgment | Reasoning |
|---|---|---|
| Confounding | Moderate | "There were no significant differences in infant gestational age, birth weight, weight at sampling, etc., except for delivery mode and feeding methods," but delivery mode and feeding mode are each analyzed by simple ANOVA/t-test without a joint multivariable model to adjust one for the other. |
| Selection of participants | Moderate | Samples were deliberately balanced by design ("a balanced number of SVD and CS infants," "a balanced number of BF, MPF and MF infants from SVD and CS available samples") rather than simple random or consecutive sampling, and the underlying source-pool's recruitment/eligibility process is not described. |
| Classification of exposures | Serious | The paper's own Methods section defines MPF and MF in the opposite sense from how both terms are used throughout the Abstract, Results, and Discussion (see design-context note above), making it impossible to be certain from the text alone which group was truly exclusively-formula-fed versus mixed-fed. |
| Deviations from intended exposures | Low | Purely observational, cross-sectional exposure ascertainment at a single timepoint; no intervention protocol to deviate from. |
| Missing data | No information | This is a single cross-sectional sample (112 collected, 112 analyzed) with no described recruitment pool or follow-up, so no attrition/missing-data information applies. |
| Measurement of outcomes | Low | Rigorous and detailed: FastDNA Spin Kit extraction, specific primers for 16S V3-V4, Bifidobacterium groEL, and Lactobacillus groEL genes, Illumina MiSeq sequencing, QIIME/UCLUST/RDP processing with UCHIME chimera removal, applied uniformly across all groups. |
| Selection of the reported result | Moderate | No trial/protocol registration (observational study); numerous taxon- and pathway-level comparisons across both factors are tested at a nominal P<0.05 threshold via ANOVA/t-test with no explicit multiple-testing correction described for this analysis. |

**Microbiome-methods checklist (every study)**

| Domain | Judgment | Reasoning |
|---|---|---|
| Sample collection and storage method reported | Not reported | Only "fecal samples were collected from infant adsorbent nappies" is stated; no storage temperature or time-to-freeze for the raw stool sample itself is given anywhere (the -80degC storage mentioned later refers to extracted DNA, not the raw sample). |
| DNA extraction method reported | Yes | "Genomic DNA was extracted from 0.1 g stool samples using FastDNA(R) Spin Kit (MP Biomedicals)... following the instructions." |
| Sequencing depth reported | Not reported | No read-count or depth figure is given anywhere in the available text. |
| Negative/positive contamination controls reported | Not reported | No mention anywhere in the available text of negative extraction/PCR controls or positive/mock-community controls. |
| Compositional-data handling reported | No | Relative-abundance percentages are compared by ANOVA/t-test, with PCoA on unweighted/weighted UniFrac (a legitimate distance-based method, not a compositional transform) -- no CLR/ALR/Aitchison/ANCOM mentioned anywhere. |

---

## #1436 — Shanghai Tenth People's Hospital dynamic-signatures cohort 2019 (China)

*Dynamic signatures of gut microbiota and influences of delivery and feeding modes during
the first 6 months of life.* Physiol Genomics. DOI 10.1152/physiolgenomics.00026.2019.

Design: prospective, single-center cohort, 102 Chinese infants sampled longitudinally at
birth, 42 days, 3 months, and 6 months. Feeding mode is a binary dominant-feeding
classification ("determined by the predominant feeding mode that constituted 50% duration
of their diet"), analyzed via a joint multivariate framework (Bray-Curtis-based, vegan R
package) that explicitly estimates the independent effect size of sex, delivery mode,
feeding mode, development status, and antibiotic use together, rather than testing feeding
mode alone.

### J. Risk of bias

*Drafted 27 Oct 2026 from a fresh read of `full_text_md/10.1152_physiolgenomics.00026.2019/10.1152_physiolgenomics.00026.2019.md`'s Materials and Methods (Enrollment and specimen collection, DNA extraction/sequencing/bioinformatics, Statistical analysis) and Results.*

| Field | Value |
|---|---|
| RoB tool applicable | **ROBINS-I** (non-randomized, observational longitudinal cohort) |

**ROBINS-I**

| Domain | Judgment | Reasoning |
|---|---|---|
| Confounding | Low | A joint multivariate analysis (Bray-Curtis dissimilarity, vegan R package) explicitly estimates the independent effect size of sex, delivery mode, feeding mode, developmental status, and antibiotic use together at each time point, rather than assessing feeding mode in isolation. |
| Selection of participants | Moderate | Single-center prospective enrollment with health-vetting by obstetricians and informed consent, but no explicit numeric eligibility criteria (gestational-age range, specific exclusions) are stated anywhere in the available text. |
| Classification of exposures | Moderate | Feeding mode has an explicit, pre-specified ascertainment rule ("determined by the predominant feeding mode that constituted 50% duration of their diet"), which is clearer than an unstated definition but coarser than a strict-exclusivity classification, since infants with substantial mixed feeding are folded into whichever mode exceeded 50%. |
| Deviations from intended exposures | Low | Purely observational exposure ascertainment via the pre-specified 50%-duration rule; no intervention protocol to deviate from. |
| Missing data | Low | "We enrolled 102 infants and collected 407 (one sample lost at 42 days) stool samples" out of 408 expected (102 infants x 4 timepoints) -- only a single missing sample across the entire study. |
| Measurement of outcomes | Low | Rigorous and standardized, following the same group's previously published protocol: E.Z.N.A. Soil DNA Kit extraction, 16S V3-V4 region (515F/806R primers), Illumina MiSeq, UPARSE/UCHIME/RDP Classifier processing, applied identically across all time points and groups. |
| Selection of the reported result | Low | No trial/protocol registration (observational cohort), but FDR and Bonferroni correction are explicitly applied throughout, and non-significant findings (e.g., "richness and diversity of the gut microbiota did not change significantly with feeding mode," no significant antibiotic-use association by PCoA) are reported transparently alongside significant ones. |

**Microbiome-methods checklist (every study)**

| Domain | Judgment | Reasoning |
|---|---|---|
| Sample collection and storage method reported | Yes | "Collected stool samples were immediately transferred on ice from the hospital or home to the laboratory to be analyzed within 2 h. Stool samples were stored at -80degC until further analysis." |
| DNA extraction method reported | Yes | "DNA was extracted from the stool samples with a E.Z.N.A. Soil DNA Kit (Omega Bio-tek, Norcross, GA)." |
| Sequencing depth reported | Not reported | No read-count or depth figure is given anywhere in the available text (only process-level QC steps such as quality filtering and chimera removal are described). |
| Negative/positive contamination controls reported | Not reported | No mention anywhere in the available text of negative extraction/PCR controls or positive/mock-community controls. |
| Compositional-data handling reported | No | Analysis uses Bray-Curtis dissimilarity/PCoA, LEfSe, and PICRUSt function prediction (legitimate but not compositional-data transforms) -- no CLR/ALR/Aitchison/ANCOM mentioned anywhere. |

---

## #1494 — BINGO/KOALA two-cohort prebiotic-formula comparison 2019 (Netherlands)

*The effect of prebiotic fortified infant formulas on microbiota composition and dynamics
in early life.* Sci Rep. DOI 10.1038/s41598-018-38268-x.

Design: two separate non-randomized, observational Dutch birth-cohort studies compared
within (not across) cohort -- BINGO (2015-2016, longitudinal, sampled at 2/6/12 weeks,
77 infants) and KOALA (2002-2003, cross-sectional at ~1 month, 239 infants) -- each its
own breastfed (BF) / formula-fed (FF) / mixed-fed (MF) comparison. The authors explicitly
avoid cross-cohort comparison because of confounding secular-trend differences between
the two time periods, restricting substantive conclusions to within-cohort contrasts.

### J. Risk of bias

*Drafted 27 Oct 2026 from a fresh read of `full_text_md/10.1038_s41598-018-38268-x/10.1038_s41598-018-38268-x.md`'s Results and Materials and Methods (Study description, DNA extraction/library preparation/sequencing, Data analysis).*

| Field | Value |
|---|---|
| RoB tool applicable | **ROBINS-I** (non-randomized, observational cohort comparison) |

**ROBINS-I**

| Domain | Judgment | Reasoning |
|---|---|---|
| Confounding | Low | Redundancy analysis (RDA) with interactive forward selection explicitly identified delivery mode, delivery place, gender, and medication use as covariates, and the analysis was then repeated "with feeding mode as the main factor and all other factors selected during the interactive selection process as covariates" to isolate feeding's residual, confounder-adjusted effect. |
| Selection of participants | Moderate | Both cohorts used clear, explicit eligibility criteria (term, healthy, singleton, no congenital abnormalities, no antibiotics), but recruitment was via self-selected sign-up (BINGO: website/flyers) or mixed conventional/"alternative lifestyle" recruitment channels (KOALA: 2343 conventional + 491 alternative-lifestyle families recruited separately), and the KOALA lifestyle-group split is not addressed as a potential covariate in this substudy. |
| Classification of exposures | Low | Feeding mode (breastmilk only / formula only / mixed) was parent-reported via questionnaire with explicit, interval-specific ascertainment in BINGO (feeding mode assessed separately for each time interval between samples) and birth-to-sampling ascertainment in KOALA. |
| Deviations from intended exposures | Low | Purely observational exposure as practiced and reported by parents; no intervention protocol to deviate from. |
| Missing data | Moderate | In the BINGO cohort, only 60 of 77 enrolled infants (~78%) could be followed and sampled at all three time points, with no stated reason for the remaining attrition, though this is transparently disclosed. |
| Measurement of outcomes | Low | Rigorous and detailed for both cohorts (double bead-beating DNA extraction, defined 16S V4 primers, NG-Tax pipeline against SILVA); the authors explicitly note a cross-cohort extraction-protocol difference and address it by restricting conclusions to within-cohort comparisons, where measurement is uniform across feeding groups. |
| Selection of the reported result | Low | Both cohorts are pre-existing, ethically-approved, previously-described birth-cohort studies (not purpose-built for this question); FDR correction is applied systematically throughout, and non-significant findings (e.g., "no separation of samples from the 17 FF infants in the KOALA cohort who received prebiotic fortified formula, p=0.076") are reported transparently alongside significant ones. |

**Microbiome-methods checklist (every study)**

| Domain | Judgment | Reasoning |
|---|---|---|
| Sample collection and storage method reported | Yes | Detailed for both cohorts: BINGO -- "mothers were asked to immediately store the samples in their home freezers... After collection, samples were stored at -80degC"; KOALA -- "refrigerated, and sent to the lab by post within one day... stored at -80degC in peptone glycerol solution." |
| DNA extraction method reported | Yes | Both cohorts' double bead-beating extraction protocols are described in detail (QIAamp DNA stool mini kit for KOALA; STAR buffer-based protocol for BINGO), each with a specific citation to the detailed method. |
| Sequencing depth reported | Yes | "A total of 28,955,759 sequencing reads were obtained from the BINGO cohort samples, with per sample counts ranging from 5,215 to 721,990 (Mean=141,940...)," and the equivalent figures are given for KOALA (30,132,625 total reads, mean 126,078/sample). |
| Negative/positive contamination controls reported | Not reported | No mention anywhere in the available text of negative extraction/PCR controls or positive/mock-community controls. |
| Compositional-data handling reported | No | PCA and RDA were performed on "log transformed genus level relative abundance data" -- a generic log transform of relative abundance, not a named compositional-data method (CLR/ALR/Aitchison/ANCOM are not mentioned anywhere). |

---

## #1560 — Santiago (Chile) bovine-formula/breast-milk inflammation-microbiota cohort 2018 (Chile)

*Intestinal Inflammation in Chilean Infants Fed With Bovine Formula vs. Breast Milk and Its
Association With Their Gut Microbiota.* Front Cell Infect Microbiol. DOI
10.3389/fcimb.2018.00190.

Design: small prospective cohort (15 breast-milk-fed [BM], 10 bovine-formula-fed [BF]
infants), all vaginally delivered by inclusion criterion (holding delivery mode constant),
sampled at 1 and 3 months. The "BF" group definition is lenient toward mixed feeding --
it explicitly includes infants receiving breastmilk plus formula supplements "≥20% of the
volume ingested that day," not just exclusively-formula-fed infants.

### J. Risk of bias

*Drafted 27 Oct 2026 from a fresh read of `full_text_md/10.3389_fcimb.2018.00190/10.3389_fcimb.2018.00190.md`'s Methods (Study Design, Patients, Sample Collection, Pyrosequencing and OTU Assignment, Statistics) and Results (Patient Demographic).*

| Field | Value |
|---|---|
| RoB tool applicable | **ROBINS-I** (non-randomized, observational cohort) |

**ROBINS-I**

| Domain | Judgment | Reasoning |
|---|---|---|
| Confounding | Moderate | Delivery mode is held constant by inclusion criterion (all vaginally delivered), and antibiotic/probiotic/anti-inflammatory-drug use is excluded by design, with Table 1 showing descriptive balance across several covariates (sex, birth weight/length, family size, atopy history, pets); however, no formal statistical adjustment model is used anywhere for the group comparisons, which are all simple univariate tests. |
| Selection of participants | Moderate | Single-center recruitment (maternity ward of Hospital Luis Tisne) with explicit inclusion/exclusion criteria, but the authors themselves note in their Discussion that "the number of patients included in the study was small, a situation that might be explained by the number of mothers who currently breastfeed their child exclusively" -- an author-acknowledged recruitment/selection constraint. |
| Classification of exposures | Moderate | Feeding groups are explicitly defined, but the "BF" (formula) group is defined leniently to include infants receiving breastmilk plus formula supplements of "≥20% of the volume ingested that day," rather than requiring exclusive formula feeding. |
| Deviations from intended exposures | No information | No information is given anywhere in the available text on whether any infant's feeding exposure changed between the T1 (1 month) and T3 (3 month) sampling points. |
| Missing data | Low | All 25 enrolled infants (15 BM, 10 BF) appear to contribute data at both T1 and T3 timepoints, with no attrition described anywhere in the available text. |
| Measurement of outcomes | Low | Rigorous and detailed: ELISA kits for calprotectin, alpha1-antitrypsin and IL-8, TaqMan RT-qPCR for IL8/IL1beta gene expression (GAPDH-normalized), QIAamp Fast DNA Stool Mini Kit extraction, a nested-PCR 16S amplification protocol, and 454 pyrosequencing outsourced to a single standardized commercial pipeline (Macrogen, QIIME/CD-HIT-DUP) -- applied uniformly to all groups. |
| Selection of the reported result | Moderate | No trial/protocol registration (observational cohort); with a very small sample (n=25) and numerous comparisons across multiple inflammatory markers, genera, and two timepoints tested at a nominal P<0.05 with no explicit multiple-testing correction described for these specific comparisons. |

**Microbiome-methods checklist (every study)**

| Domain | Judgment | Reasoning |
|---|---|---|
| Sample collection and storage method reported | Yes | "In case that the infant has no stool during the visit, a home kit for the parents was given to take the sample and store it in a sterile container to be transported to our center within the following 6 h. Stool samples were divided into at least 4 aliquots and stored at -80degC." |
| DNA extraction method reported | Yes | "Total DNA was extracted from stool samples using the QIAamp Fast DNA Stool Mini Kit (Qiagen) and stored at -20degC until PCR amplification." |
| Sequencing depth reported | Not reported | No total or per-sample read-count/depth figure is given anywhere in the available text (only the resulting OTU count, 140 total, is reported). |
| Negative/positive contamination controls reported | Not reported | No mention anywhere in the available text of negative extraction/PCR controls or positive/mock-community controls. |
| Compositional-data handling reported | No | "The abundance of each taxa was normalized by the total diversity per sample prior to any group comparison" -- a simple relative-abundance normalization used with RDA, not a named compositional-data transform (CLR/ALR/Aitchison/ANCOM are not mentioned anywhere). |

---

## #1613 — COCOA cohort atopic-dermatitis/feeding-type study 2018 (South Korea)

*Perturbations of gut microbiome genes in infants with atopic dermatitis according to
feeding type.* J Allergy Clin Immunol. DOI 10.1016/j.jaci.2017.11.045.

Design: cross-sectional comparison within the COCOA birth cohort, 129 six-month-old
infants (66 healthy, 63 with atopic dermatitis [AD]) selected from the larger cohort via
propensity-score matching. The matching is explicitly designed to balance AD-vs-control
propensity, not to balance the breastfed/formula/mixed-fed groups against each other;
feeding-type comparisons are analyzed descriptively (Kruskal-Wallis) within each
disease-status stratum rather than via an adjusted model. The formula-fed subgroup is
very small (7 healthy, 6 AD) and was excluded from the paper's own enterotype analysis
for this reason.

### J. Risk of bias

*Drafted 27 Oct 2026 from a fresh read of `full_text_md/10.1016_j.jaci.2017.11.045/10.1016_j.jaci.2017.11.045.md` (main text; detailed sub-methods deferred to an Online Repository not available here).*

| Field | Value |
|---|---|
| RoB tool applicable | **ROBINS-I** (non-randomized, observational cross-sectional comparison) |

**ROBINS-I**

| Domain | Judgment | Reasoning |
|---|---|---|
| Confounding | Moderate | Propensity-score matching was used to balance AD-vs-control propensity ("no differences in these factors were found between the 2 groups"), but this addresses disease-status confounding, not confounding of the feeding-type comparison itself; feeding-group comparisons (BF/FF/MF) are descriptive (Kruskal-Wallis) with no adjustment for delivery mode, antibiotics, or other covariates. |
| Selection of participants | Moderate | Subjects are drawn from a large, multi-site, IRB-approved birth cohort (COCOA) via a defined matching process, but the formula-fed subgroup is very small (7 healthy, 6 AD of 129 total) and was explicitly excluded from the paper's own enterotype analysis "because of the limited number of subjects," limiting how representative conclusions about that exposure group can be. |
| Classification of exposures | No information | The three feeding categories (breast milk, formula, mixed) are named and used, but no operational definition, exclusivity threshold, or ascertainment timing is given anywhere in the available main text (this detail may exist only in the Online Repository, which is not available here). |
| Deviations from intended exposures | No information | No information is given anywhere in the available text on this domain. |
| Missing data | Low | This is a single cross-sectional timepoint (6 months) with no described follow-up or attrition; the small formula-fed subgroup is a representativeness concern (already captured under Selection of participants) rather than a missing-data one. |
| Measurement of outcomes | Low | Rigorous and detailed in the main text: Power Microbiome RNA/DNA Isolation Kit extraction, barcoded V1-V3 16S primers with Roche/454 FLX Titanium pyrosequencing, quantitative real-time PCR for total bacterial load, and whole-metagenome sequencing (Illumina HiSeq 2500) on a 40-sample subset -- a dual-platform approach applied uniformly across groups. |
| Selection of the reported result | Moderate | Built on a pre-existing, ethically-approved ongoing birth cohort rather than a purpose-registered protocol for this specific analysis; the paper reports negative findings plainly (e.g., "no specific taxa directly correlated with AD in 16S rRNA gene results"), but performs numerous sub-analyses (enterotype clustering, functional pathway analysis) without a clearly pre-specified single analysis plan. |

**Microbiome-methods checklist (every study)**

| Domain | Judgment | Reasoning |
|---|---|---|
| Sample collection and storage method reported | Yes | "Fecal samples were collected and immediately stored at -80degC before being processed for DNA extraction." |
| DNA extraction method reported | Yes | "Metagenomic DNA was extracted from 250 mg of feces by using the Power Microbiome RNA/DNA Isolation Kit (Mo Bio/Qiagen)... according to the manufacturer's instructions." |
| Sequencing depth reported | Yes | "A total of 1,423,835 high-quality reads (719,168 reads... for control samples and 704,667 reads... for AD samples)" for 16S sequencing, and "A total of 231,010,091 reads (116.4 Gb)" for whole-metagenome sequencing -- both stated directly in the main text. |
| Negative/positive contamination controls reported | Not reported | No mention anywhere in the available main text of negative extraction/PCR controls or positive/mock-community controls (this detail may exist only in the Online Repository). |
| Compositional-data handling reported | No | Enterotype clustering used Jensen-Shannon divergence on relative-abundance data (a legitimate distance-based clustering method, not a compositional-data transform) -- no CLR/ALR/Aitchison/ANCOM mentioned anywhere in the available text. |

---

## #1641 — Munich bifidobacteria-supplementation RCT-with-BF-reference 2017 (Germany)

*Randomized controlled trial on the impact of early-life intervention with bifidobacteria
on the healthy infant fecal microbiota and metabolome.* Am J Clin Nutr. DOI
10.3945/ajcn.117.157529. DRKS00003660 (registered prospectively).

Design: hybrid -- double-blind, block-randomized, placebo-controlled trial between a
bifidobacteria-supplemented formula (F+) and a placebo formula (F-), plus a small,
non-randomized, exclusively-breastfed reference group (B, n=9) and large mixed-feeding
groups (BF+/BF-, n=75 total) whose breastfeeding duration and formula volume were
"determined by the parents themselves" -- routed to ROBINS-I per the hybrid-design rule.
**Delivery mode was notably imbalanced between the reference and randomized groups**
(cesarean: B 67% vs. F+ 42% / F- 45%), and the paper's own analysis found that "mode of
delivery affected microbiota... at months 1 and 3" without adjusting the BF-vs-formula
comparisons for this.

### J. Risk of bias

*Drafted 27 Oct 2026 from a fresh read of `full_text_md/10.3945_ajcn.117.157529/10.3945_ajcn.117.157529.md`'s Methods (Participants, Study design, Fecal sample collection, 16S sequencing/processing) and Results (Table 1, feeding-group comparisons).*

| Field | Value |
|---|---|
| RoB tool applicable | **ROBINS-I** (non-randomized breastfed reference group per the hybrid-design rule) |

**ROBINS-I**

| Domain | Judgment | Reasoning |
|---|---|---|
| Confounding | Serious | Cesarean delivery was substantially more common in the exclusively-breastfed reference group (67%) than in the randomized formula arms (42% and 45%), and the paper's own results explicitly show delivery mode affects microbiota at months 1 and 3, yet the breastfed-vs-formula comparisons presented are not adjusted for this known, demonstrably unbalanced confounder. |
| Selection of participants | Moderate | A detailed, CONSORT-style flow is given (117 assessed, 106 completed, 70 followed to 2 y) with explicit eligibility/exclusion criteria, but the breastfed reference group is tiny (n=9) and self-selected (parents who chose and sustained exclusive breastfeeding for the full 12-month intervention period while enrolled in a formula trial). |
| Classification of exposures | Low | Feeding categories are explicitly and dynamically ascertained via monthly parental questionnaires recording formula volume and breastfeeding duration, allowing infants to be correctly reclassified as they transition between exclusive and mixed feeding over time. |
| Deviations from intended exposures | Low | The dynamic, month-by-month tracking of feeding status (and the resulting declining sample sizes as infants wean, explicitly reported) directly incorporates rather than ignores deviation from each infant's initial feeding assignment. |
| Missing data | Moderate | Substantial attrition over the full study (117 assessed -> 106 completed -> 70 at the 2-year follow-up, ~40% cumulative loss by 2 years) and declining breastfed sample sizes at later months (n=20 at months 1-7 down to n=9 at months 9-12) are both transparently disclosed via a CONSORT-style flow diagram. |
| Measurement of outcomes | Low | Extremely detailed and rigorous, applied uniformly across all groups: a specific phenol-chloroform/bead-beating DNA extraction protocol, 16S V3-V4 sequencing via an in-house validated pipeline (IMNGS/UPARSE), strain-specific PCR validated by BLAST and tested against reference strain collections, and UHPLC-QToF-MS metabolomics with quality-control injections every 10 samples. |
| Selection of the reported result | Low | Prospectively registered (DRKS00003660) before the trial; non-significant findings are reported extensively and plainly throughout (e.g., "no major differences were observed between F+ and F- infants at any measured time point," "no significant differences... regarding growth, antibiotic uptake, or other health variables"), with Benjamini-Hochberg correction applied systematically. |

**Microbiome-methods checklist (every study)**

| Domain | Judgment | Reasoning |
|---|---|---|
| Sample collection and storage method reported | Yes | "Samples were taken directly from diapers into sterile plastic collection tubes... placed in sealed plastic bags alongside an oxygen-absorbing sachet... stored at 4degC and transported to the laboratory within 1 d. Samples (~100-mg aliquots) were stored at -80degC until processing." |
| DNA extraction method reported | Yes | A detailed multi-step protocol is given: "Metagenomic DNA was extracted from fecal aliquots... resuspended in 600 microL DNA stabilization buffer... and 400 microL phenol/chloroform/isoamyl alcohol... Cells were mechanically lysed... DNA was purified with the NucleoSpin gDNA Clean-up Kit." |
| Sequencing depth reported | Not reported | Only process-level QC steps are described (length filtering, chimera removal, OTU clustering at 97% with a 0.5% relative-abundance threshold) -- no absolute total or per-sample read-count figure is stated anywhere in the available text. |
| Negative/positive contamination controls reported | Not reported | Only a 25% PhiX standard-library spike-in is mentioned, which is a sequencing-run calibration control, not a biological negative/positive contamination control; no such control is described anywhere in the available text. |
| Compositional-data handling reported | No | OTU tables were "normalized to account for differences in sequence depth via simple division to their sample size and then multiplication by the size of the smaller sample," and beta-diversity used generalized UniFrac distances -- neither is a named compositional-data transform (CLR/ALR/Aitchison/ANCOM are not mentioned anywhere). |

---

## #1649 — NIZO/Nestle intensively-sampled BF/FF cohort 2017 (Netherlands)

*Intestinal colonisation patterns in breastfed and formula-fed infants during the first 12
weeks of life reveal sequential microbiota signatures.* Sci Rep. DOI
10.1038/s41598-017-08268-4.

Design: small (4 breastfed, 4 formula-fed, originally 5+5 with 2 excluded a priori for
data-quality reasons), very intensively sampled (17 timepoints/infant over 12 weeks)
prospective observational cohort, all vaginally delivered, GA>39 weeks, same ethnicity,
with parent-chosen feeding. A partial-RDA statistical framework explicitly separates
diet's contribution from individual and time effects, though with only 4 infants/group
this has minimal power to detect confounding imbalance. Industry co-funded (Wyeth
Nutrition), with two co-authors employed by the funder during the study.

### J. Risk of bias

*Drafted 27 Oct 2026 from a fresh read of `full_text_md/10.1038_s41598-017-08268-4/10.1038_s41598-017-08268-4.md`'s Results (Subjects) and Material and Methods (Subjects and study design, Faecal sample collection, 16S rRNA gene sequencing analysis, qPCR, Statistical analysis).*

| Field | Value |
|---|---|
| RoB tool applicable | **ROBINS-I** (non-randomized, parent-chosen feeding exposure) |

**ROBINS-I**

| Domain | Judgment | Reasoning |
|---|---|---|
| Confounding | Moderate | Delivery mode, gestational age (>39 weeks), and ethnicity (all Caucasian) are held constant by inclusion, and "baseline characteristics at time of recruitment were not significantly different between the two groups," but with only 4 infants/group this comparison has minimal power, and no adjustment is made for other factors tracked by parental journals (illness, medication, dietary change). |
| Selection of participants | Moderate | A single-center, very small convenience sample (10 enrolled, 2 excluded a priori for "too many missing samples and/or collection of insufficient faecal material" -- an objective, pre-specified data-quality rule rather than outcome-dependent exclusion). |
| Classification of exposures | Low | Exposure is strictly and explicitly defined ("exclusively breastfed or formula-fed from birth onward"), with the two infants who transitioned to complementary formula at weeks 10-11 explicitly tracked and interpreted accordingly rather than miscategorized. |
| Deviations from intended exposures | Low | The transition of 2 breastfed infants to complementary formula feeding late in the study is explicitly identified and accounted for in the analysis and interpretation (e.g., linking the timing of C. difficile detection in one infant to this transition). |
| Missing data | Moderate | Two of 10 originally enrolled infants (20%) were excluded a priori due to insufficient sample collection, a real loss though governed by an objective, pre-specified data-quality rule rather than a differential or outcome-dependent one. |
| Measurement of outcomes | Low | Extremely rigorous and uniform: a single standardized diaper brand for consistent collection, a strict no-intermediate-thaw transport protocol, detailed phenol-chloroform DNA extraction, defined 454 pyrosequencing primers, and targeted qPCR for specific pathogens with explicit positive and negative controls included in every run. |
| Selection of the reported result | Moderate | No trial/protocol registration; the study is explicitly exploratory/descriptive in nature with industry co-funding (Wyeth Nutrition) and two co-authors employed by the funder during the study, though this conflict is transparently disclosed and non-significant/null findings are reported plainly throughout. |

**Microbiome-methods checklist (every study)**

| Domain | Judgment | Reasoning |
|---|---|---|
| Sample collection and storage method reported | Yes | A highly detailed protocol: parents used a single standardized diaper brand, stored samples in home freezers at -20degC, transferred to hospital freezers, then transported on dry ice to the lab and stored at -20degC, "strictly preventing intermediate thawing of the samples." |
| DNA extraction method reported | Yes | "After bead-beating, DNA was purified by maximal 3 consecutive phenol-chloroform extractions... followed by isopropanol precipitation of the DNA," with the full protocol described in detail. |
| Sequencing depth reported | Yes | "In total 1,390,768 bacterial 16S rDNA sequences, with on average 11,307 (+/-6,355; SD) reads... per sample, were analysed." |
| Negative/positive contamination controls reported | Yes | "Positive and negative controls (other bacterial species) were included in each qPCR run" used for targeted pathogen detection. |
| Compositional-data handling reported | No | Analysis uses PCA, partial RDA, and UniFrac distances on relative-abundance data (legitimate multivariate/distance methods, not compositional-data transforms) -- no CLR/ALR/Aitchison/ANCOM mentioned anywhere. |

---

## #1682 — Los Angeles/St Petersburg mother-infant breast-milk-microbiome cohort 2017 (USA)

*Association Between Breast Milk Bacterial Communities and Establishment and
Development of the Infant Gut Microbiome.* JAMA Pediatr. DOI
10.1001/jamapediatrics.2017.0378.

Design: prospective, longitudinal, two-site (Los Angeles and St Petersburg) cohort of 107
healthy mother-infant pairs, enrolled across five pre-specified infant-age strata.
Breastfeeding is treated as a continuous dose exposure (percentage of daily milk intake
from breast milk) rather than a crude binary category, analyzed via permutational
multivariate ANOVA (adonis) jointly modeling infant age, demographics, delivery type,
site, and feeding characteristics, with interaction terms explicitly tested.

### J. Risk of bias

*Drafted 27 Oct 2026 from a fresh read of `full_text_md/10.1001_jamapediatrics.2017.0378/10.1001_jamapediatrics.2017.0378.md`'s Methods (Study Participants, Sample Collection/DNA Extraction/Sequencing, Statistical Analysis), Results, and Limitations (detailed sub-methods deferred to an eMethods supplement not available here).*

| Field | Value |
|---|---|
| RoB tool applicable | **ROBINS-I** (non-randomized, observational cohort; feeding is a continuous exposure) |

**ROBINS-I**

| Domain | Judgment | Reasoning |
|---|---|---|
| Confounding | Low | A joint permutational multivariate ANOVA explicitly models infant age, demographics, delivery type, geographic site, and feeding characteristics together (with interaction terms tested and found non-significant), rather than assessing feeding in isolation -- one of the more rigorous confounding-control approaches in this review. |
| Selection of participants | Moderate | Multi-site recruitment with explicit eligibility/exclusion criteria (health conditions, infant antibiotic use) and pre-specified age-stratified enrollment, but the authors themselves disclose that "our recruitment focused on breastfeeding participants, and we did not enroll large numbers of strictly formula-fed infants," limiting representativeness for that comparison arm. |
| Classification of exposures | Low | Breastfeeding is operationalized as a continuous dose variable (percentage of daily milk intake from breast milk) with explicit thresholds for "primarily breastfed" (>75%) and "exclusively breastfed" (never received formula) -- a more rigorous classification than a simple binary category. |
| Deviations from intended exposures | Low | Purely observational, dose-based exposure ascertained longitudinally at every study visit via structured interviews (REDCap), capturing actual feeding behavior rather than an initial assignment. |
| Missing data | Moderate | The authors disclose that "some participants were unable to adhere to our longitudinal collection schedule," only 60.3% of families contributed 2 or more longitudinal samples, and key covariates used in the adjusted model have some missingness (delivery method unknown for 9.9%, antibiotic use unknown for 14.9% of families). |
| Measurement of outcomes | Low | 16S rRNA V4 sequencing on a MiSeq platform "using standard procedures with quality control," PICRUSt functional prediction, SourceTracker Bayesian source-tracking, and random-forest machine-learning models, applied uniformly across samples (detailed extraction/sequencing protocol is deferred to an eMethods supplement not available here). |
| Selection of the reported result | Low | No trial/protocol registration (observational cohort), but NIH-funded with FDR correction explicitly applied, and non-significant findings are reported plainly and repeatedly (e.g., "differences in gut phylogenetic diversity did not reach statistical significance," "interaction terms were tested and not statistically significant," "no significant differences in breast milk or areolar bacteria by race/ethnicity, infant sex, mode of delivery, or geographic location"). |

**Microbiome-methods checklist (every study)**

| Domain | Judgment | Reasoning |
|---|---|---|
| Sample collection and storage method reported | Not reported | The main text states only that "we collected breast milk and areolar skin swabs from mothers and stool from infants' soiled diapers during clinic or home study visits," with no storage temperature or timing given; this detail is deferred entirely to an eMethods supplement not available here. |
| DNA extraction method reported | Not reported | The main text states only that "the DNA extraction, library preparation, and sequencing... were performed using standard procedures with quality control (eMethods...)," deferring the actual protocol to a supplement not available here. |
| Sequencing depth reported | Not reported | No read-count or depth figure is given anywhere in the available main text. |
| Negative/positive contamination controls reported | Not reported | No mention anywhere in the available main text of negative extraction/PCR controls or positive/mock-community controls (this detail may exist only in the eMethods supplement). |
| Compositional-data handling reported | No | Analysis uses unweighted UniFrac, Bray-Curtis distances, SourceTracker, and random forest modeling (legitimate but not compositional-data transforms) -- no CLR/ALR/Aitchison/ANCOM mentioned anywhere in the available text. |

---

## #1744 — WHEALS/MAAP Detroit multi-factor cohort 2016 (USA)

*Joint effects of pregnancy, sociocultural, and environmental factors on early life gut
microbiome structure and diversity.* Sci Rep. DOI 10.1038/srep31775.

Design: cross-sectional analysis of 298 infants (130 "neonates" ~1 month, 168 "infants"
~6 months, non-overlapping groups) from the racially and socioeconomically diverse
WHEALS/MAAP Detroit birth cohort. Breastfeeding (current/exclusive) is one of up to 49-72
candidate factors tested, with extensive backward-elimination multi-factor PERMANOVA
models explicitly adjusting for delivery mode, race-ethnicity, marital status, parity,
household income, environmental tobacco smoke, pets, and age at stool collection
simultaneously, with multicollinearity (VIF) explicitly checked and missing covariates
explicitly imputed.

### J. Risk of bias

*Drafted 27 Oct 2026 from a fresh read of `full_text_md/10.1038_srep31775/10.1038_srep31775.md`'s Results (single- and multi-factor models) and Methods (WHEALS study population, Stool samples, Statistical analysis, Multi-factor models).*

| Field | Value |
|---|---|
| RoB tool applicable | **ROBINS-I** (non-randomized, observational cohort) |

**ROBINS-I**

| Domain | Judgment | Reasoning |
|---|---|---|
| Confounding | Low | Extensive backward-elimination multi-factor PERMANOVA models explicitly and simultaneously adjust breastfeeding for delivery mode, race-ethnicity, marital status, parity, income, environmental tobacco smoke, pets, and age at collection, with multicollinearity explicitly checked via variance inflation factors and missing covariates explicitly imputed rather than dropped. |
| Selection of participants | Low | The analytic sample's representativeness was explicitly and quantitatively checked against the full birth cohort ("found few statistically significant differences between the two"), with specific comparisons tabulated for race, marital status, delivery mode, ETS exposure, and breastfeeding rates. |
| Classification of exposures | Moderate | Breastfeeding status is classified as "exclusive, any, or none," which the authors themselves explicitly flag as a limitation: "it does not recognize the heterogeneity that exists within each of these categories." |
| Deviations from intended exposures | Low | Purely observational, cross-sectional exposure ascertainment via maternal interview at each study visit; no intervention protocol to deviate from. |
| Missing data | Low | Missingness across covariates was explicitly documented and found to be low ("all <8% except for household income and baby antibiotic use"), with appropriate imputation applied and the resulting bias judged minimal. |
| Measurement of outcomes | Low | Rigorous and detailed: a modified CTAB-buffer DNA extraction protocol, defined 16S V4 primers (515F/806R) with error-correcting barcodes, a QIIME-based pipeline with UCHIME chimera removal against the Greengenes database, and a thoughtful "representative rarefaction" approach to avoid single-subsample artifacts. |
| Selection of the reported result | Low | No formal trial registration (observational cohort nested within the larger WHEALS study), but extremely transparent reporting, including explicit disclosure of a finding that contradicted prior literature ("we notably failed to detect compositional differences by antibiotic exposure... which have previously been reported"), with Benjamini-Hochberg FDR correction applied systematically. |

**Microbiome-methods checklist (every study)**

| Domain | Judgment | Reasoning |
|---|---|---|
| Sample collection and storage method reported | Yes | "Stool was placed into cryovials, transported to the laboratory and stored at -80degC." |
| DNA extraction method reported | Yes | A detailed modified CTAB-buffer extraction protocol is given in full, including bead-beating, phenol:chloroform:isoamyl alcohol extraction, and precipitation steps. |
| Sequencing depth reported | Yes | "The resulting OTU count table was representative-rarefied to the minimum depth of 202,367 total sequences per sample." |
| Negative/positive contamination controls reported | Not reported | No mention anywhere in the available text of negative extraction/PCR controls or positive/mock-community controls (bovine serum albumin was added to PCR reactions to reduce inhibition, not as a contamination control). |
| Compositional-data handling reported | No | Differential abundance was tested with zero-inflated negative binomial regression (a count-model approach, not a compositional-data transform) on UniFrac-distance-based community composition -- no CLR/ALR/Aitchison/ANCOM mentioned anywhere. |

---

## #1807 — New Hampshire Birth Cohort delivery-mode/feeding-method study 2016 (USA)

*Association of Cesarean Delivery and Formula Supplementation With the Intestinal
Microbiome of 6-Week-Old Infants.* JAMA Pediatr. DOI 10.1001/jamapediatrics.2015.3732.

Design: prospective observational cohort, 102 full-term infants from the New Hampshire
Birth Cohort Study, cross-sectional at 6 weeks, three feeding groups (exclusive breastfed
n=70, combination-fed n=26, exclusive formula n=6). Delivery mode and feeding method are
explicitly and mutually adjusted for each other, and antibiotic-exposed infants were
excluded by design. Feeding classification was validated against a 48-hour feeding diary,
and a sensitivity analysis re-tested the robustness of the combination-feeding
classification for two borderline infants.

### J. Risk of bias

*Drafted 27 Oct 2026 from a fresh read of `full_text_md/10.1001_jamapediatrics.2015.3732/10.1001_jamapediatrics.2015.3732.md`'s Methods (New Hampshire Birth Cohort Study, Sample Collection/DNA Extraction/Sequencing) and Results.*

| Field | Value |
|---|---|
| RoB tool applicable | **ROBINS-I** (non-randomized, observational cohort) |

**ROBINS-I**

| Domain | Judgment | Reasoning |
|---|---|---|
| Confounding | Low | Delivery mode and feeding method were explicitly and mutually adjusted for each other in all UniFrac-based PERMANOVA models ("controlling for the effects of feeding method, delivery mode was strongly associated..."), the two were confirmed not significantly associated with each other (Fisher exact P=.66), and antibiotic-exposed infants were excluded entirely by design, removing that major confounder. |
| Selection of participants | Low | Recruited from an established, previously-validated prospective pregnancy cohort (prenatal clinic enrollment at 24-28 weeks' gestation) with explicit eligibility criteria (full-term, appropriately grown); no selective or convenience-based enrollment process is described. |
| Classification of exposures | Low | Rigorous three-category definition (exclusive breast milk, exclusive formula, combination) based on detailed telephone questionnaires, cross-validated "when possible" against a 48-hour feeding diary, with a sensitivity analysis explicitly testing the robustness of the classification for two borderline combination-fed infants. |
| Deviations from intended exposures | Low | Purely observational exposure as actually practiced and validated against a feeding diary; the sensitivity re-analysis after reclassifying 2 borderline infants found no qualitative change in results. |
| Missing data | Low | Single cross-sectional timepoint with no attrition described; all 102 enrolled infants are included in the analysis. |
| Measurement of outcomes | Low | Zymo DNA extraction kit, Illumina tag sequencing of the 16S V4-V5 region at an established sequencing facility using previously validated and cited methods, with explicit total/passed-filter read counts reported; detailed QC/filtering specifics are deferred to an eAppendix not available here. |
| Selection of the reported result | Low | No formal trial registration (observational cohort nested within an established pregnancy cohort study), but FDR correction (Q-values) is applied systematically throughout, and numerous non-significant findings are reported plainly (e.g., "no significant interaction observed between delivery mode and feeding method," "no taxa were significantly differentially abundant between infants who were combination fed vs exclusively formula fed or exclusively breastfed"). |

**Microbiome-methods checklist (every study)**

| Domain | Judgment | Reasoning |
|---|---|---|
| Sample collection and storage method reported | Yes | "Stool was aliquoted in sterile tubes and frozen at -80degC within 24 hours of receipt." |
| DNA extraction method reported | Yes | "DNA was extracted using the Zymo DNA extraction kit (Zymo Research). The quantity and purity of the DNA were determined by OD260/280 nanodrop measurement." |
| Sequencing depth reported | Yes | "Sequencing yielded a total of 14,362,739 bacterial DNA reads (mean, 140,811; range, 27,897-260,579), of which 8,210,402 (mean, 80,494; range, 12,244-178,802) passed quality filters." |
| Negative/positive contamination controls reported | Not reported | No mention anywhere in the available main text of negative extraction/PCR controls or positive/mock-community controls (this detail may exist only in the eAppendix supplement). |
| Compositional-data handling reported | Yes | Figure 3 (individual taxon abundance by delivery mode and feeding method) explicitly states that "circles are sized according to relative log-ratio-transformed abundance" -- a named log-ratio transform, consistent with a compositional-data approach. |

---

## #1827 — CHILD Study intrapartum-antibiotics/birth-method/breastfeeding cohort 2016 (Canada)

*Impact of maternal intrapartum antibiotics, method of birth and breastfeeding on gut
microbiota during the first year of life: a prospective cohort study.* BJOG. DOI
10.1111/1471-0528.13601.

Design: prospective, longitudinal (3 and 12 months) subsample of 198 infants from the
Canadian CHILD birth cohort, examining maternal intrapartum antibiotic prophylaxis (IAP),
method of birth, and breastfeeding (exclusivity/duration) as co-exposures. Breastfeeding
status was confirmed empirically independent of IAP group ("breastfeeding rates were also
similar across the four IAP groups"), but the authors explicitly disclose that the study
was underpowered for simultaneous multivariable adjustment of confounders, relying instead
on univariate regression and stratified analyses.

### J. Risk of bias

*Drafted 27 Oct 2026 from a fresh read of `full_text_md/10.1111_1471-0528.13601/10.1111_1471-0528.13601.md`'s Methods (Study design, Exposures, Faecal microbiota analysis, Statistical analysis), Results, and Strengths and limitations.*

| Field | Value |
|---|---|
| RoB tool applicable | **ROBINS-I** (non-randomized, observational cohort) |

**ROBINS-I**

| Domain | Judgment | Reasoning |
|---|---|---|
| Confounding | Moderate | Breastfeeding status was empirically confirmed to be balanced across IAP/birth-method groups ("breastfeeding rates were also similar across the four IAP groups"), but the authors explicitly state that "a larger sample is required for the simultaneous adjustment of confounding factors," relying on univariate regression and stratified analyses rather than a joint multivariable model. |
| Selection of participants | Low | An "unselected subsample" of consecutively enrolled infants with available samples and complete exposure data, with representativeness explicitly checked against the full cohort and found similar except for a small difference in maternal age. |
| Classification of exposures | Low | Breastfeeding duration and exclusivity were ascertained via "standardised questionnaires at 3, 6 and 12 months postpartum," yielding a clear ordinal classification (none/partial/exclusive) analyzed with an explicit dose-response (duration) test for trend. |
| Deviations from intended exposures | Low | Purely observational exposure as actually practiced and reported by mothers at each standardized follow-up; no intervention protocol to deviate from. |
| Missing data | Low | Faecal samples were collected from 176 of 198 infants (89%) at 3 months and 189 of 198 (95%) at 1 year, with no indication that missingness was differential by exposure group. |
| Measurement of outcomes | Low | Rigorous, following a previously published and validated protocol: QIAamp DNA Stool Mini Kit extraction, 16S V4 region amplification with a barcoded reverse primer, triplicate PCR reactions pooled with a negative control in every run, and a QIIME/Greengenes/RDP pipeline. |
| Selection of the reported result | Low | No formal trial registration (observational cohort nested within the larger CHILD study), but FDR correction is explicitly applied for multiple-genera comparisons, and numerous non-significant findings are reported plainly throughout (e.g., "no persistent microbiota differences at 1 year among infants exposed to IAP with elective CS or vaginal delivery"). |

**Microbiome-methods checklist (every study)**

| Domain | Judgment | Reasoning |
|---|---|---|
| Sample collection and storage method reported | Yes | "Fresh or previously refrigerated faecal samples were collected at a home visit (3 months) or brought to a clinic visit (12 months). Samples were refrigerated during transport and stored at -80degC until analysis." |
| DNA extraction method reported | Yes | "Whole genome DNA was extracted from faeces using the QIAamp DNA Stool Mini Kit (Qiagen, Venlo, Netherlands)." |
| Sequencing depth reported | Yes | "A total of 110 million reads were retained (median 3.1x10^5 per sample, range 8.1x10^4-1.0x10^6)... data were rarefied to 80,000 sequences per sample." |
| Negative/positive contamination controls reported | Yes | "Reactions were performed in triplicate and pooled with a negative control included in each run." |
| Compositional-data handling reported | No | Relative abundances were compared with the Kruskal-Wallis test and Spearman correlation, and community-level differences used unweighted UniFrac/adonis (a legitimate distance-based method, not a compositional-data transform) -- no CLR/ALR/Aitchison/ANCOM mentioned anywhere. |

---

## #1854 — Ewha Womans University Korean BFI/FFI pyrosequencing pilot 2015 (South Korea)

*Comparison of the gut microbiota profile in breast-fed and formula-fed Korean infants
using pyrosequencing.* Nutr Res Pract. DOI 10.4162/nrp.2015.9.3.242.

Design: small, single-center, cross-sectional pilot study (explicitly described by the
authors as "this pilot study"), 10 breast-fed and 10 formula-fed 4-week-old Korean infants,
all vaginally delivered and full-term, with explicit exclusion of cesarean delivery,
prematurity, antibiotic/probiotic exposure, and maternal illness. **The "formula-fed"
group is not exclusively formula-fed**: it is explicitly defined as infants with "some
exposure to breast milk but fed 70-100% with formula milk," a leniency the authors
themselves flag in their own Limitations.

### J. Risk of bias

*Drafted 27 Oct 2026 from a fresh read of `full_text_md/10.4162_nrp.2015.9.3.242/10.4162_nrp.2015.9.3.242.md`'s Subjects and Methods and Results (General characteristics).*

| Field | Value |
|---|---|
| RoB tool applicable | **ROBINS-I** (non-randomized, observational pilot cohort) |

**ROBINS-I**

| Domain | Judgment | Reasoning |
|---|---|---|
| Confounding | Moderate | Delivery mode, prematurity, antibiotic exposure, and maternal illness are all controlled by exclusion criteria rather than statistical adjustment, and baseline maternal age/infant sex/birth weight were reported as not significantly different between groups; however, the "formula-fed" group's own definition permits up to 30% of intake from breast milk, blurring the exposure contrast itself. |
| Selection of participants | Moderate | Single-center convenience sample recruited over a 9-month window (n=20 total), explicitly framed by the authors as "this pilot study," limiting representativeness. |
| Classification of exposures | Moderate | Breast-fed infants are clearly exclusively breastfed, but the comparator "formula-fed" group explicitly allows "some exposure to breast milk" (70-100% formula), a leniency the authors acknowledge directly: "some FFI were exposed to breast milk during the 4 weeks of life." |
| Deviations from intended exposures | Low | Purely observational, cross-sectional exposure classification reflecting actual feeding as practiced over the first 4 weeks; no intervention protocol to deviate from. |
| Missing data | Low | All 20 enrolled infants are included in the 4-week fecal analysis with no attrition described (a parallel meconium analysis failed for insufficient DNA, but this is disclosed and does not affect the primary comparison). |
| Measurement of outcomes | Low | Rigorous and detailed: Fast DNA SPIN Kit extraction, defined 16S V1-V3 primers (27F/518R), Roche/454 GS Junior pyrosequencing at a named facility, EzTaxon-e taxonomic assignment, UCHIME chimera removal, and explicit per-sample Good's coverage values (all >0.98) confirming adequate sequencing depth. |
| Selection of the reported result | Moderate | Explicitly framed by the authors as a small pilot study with a cost-driven sample-size limitation; family-level taxon comparisons (Table 4) are reported with raw P values and no stated multiple-testing correction, unlike the FDR-corrected approach used in most other studies in this batch. |

**Microbiome-methods checklist (every study)**

| Domain | Judgment | Reasoning |
|---|---|---|
| Sample collection and storage method reported | Yes | "The specimens were immediately sealed in a plastic bag and were stored at -80degC." |
| DNA extraction method reported | Yes | "Metagenomic DNA was isolated from fecal samples of infants using a Fast DNA SPIN Kit (MP BIO)... according to the manufacturer's instructions." |
| Sequencing depth reported | Yes | Per-sample total sequence counts are tabulated directly (Tables 2/3; e.g., "the average numbers of sequences were 11,100 from the BFI and 9,600 from the FFI"), with "Good's coverages of all samples... greater than 0.98." |
| Negative/positive contamination controls reported | Not reported | No mention anywhere in the available text of negative extraction/PCR controls or positive/mock-community controls. |
| Compositional-data handling reported | No | Relative-abundance percentages are compared by Wilcoxon-Mann-Whitney/t-test, with standard ecological diversity indices (Chao1, Shannon, ACE) -- no CLR/ALR/Aitchison/ANCOM mentioned anywhere. |

---

## #1882 — Illinois HMO/BF-FF microbiota correlation study 2015 (USA)

*Fecal Microbiota Composition of Breast-fed Infants is Correlated with Human Milk
Oligosaccharides Consumed.* J Pediatr Gastroenterol Nutr. DOI
10.1097/MPG.0000000000000752.

Design: small, single-site, observational cohort, 16 exclusively breastfed and 6
exclusively formula-fed infants (all vaginally delivered, healthy, full-term), all FF
infants given the identical formula brand (Enfamil LIPIL). The study deliberately
recruited second-parity mothers "who had either exclusively breastfed or formula-fed
their first infant, to increase our likelihood of enrolling mothers who were secure in
their child feeding decision" -- a non-random recruitment strategy aimed at reducing
feeding-exposure crossover/misclassification.

### J. Risk of bias

*Drafted 27 Oct 2026 from a fresh read of `full_text_md/10.1097_mpg.0000000000000752/10.1097_mpg.0000000000000752.md`'s Materials and Methods (Study subjects and design, DNA isolation, Pyrosequencing, Sequence processing, Statistical analysis) and Results.*

| Field | Value |
|---|---|
| RoB tool applicable | **ROBINS-I** (non-randomized, parent-chosen feeding exposure) |

**ROBINS-I**

| Domain | Judgment | Reasoning |
|---|---|---|
| Confounding | Moderate | Delivery mode is held constant (all vaginal), antibiotic-exposed infants are excluded, and all FF infants received the identical formula brand, with Table 1 showing no significant baseline differences in maternal age, infant sex, or birth weight/length; however, no multivariable statistical adjustment is used for any comparison, and the deliberate recruitment of only "secure" second-parity mothers (a known covariate of microbiota composition in other studies in this review) is not addressed as a potential confounder. |
| Selection of participants | Moderate | Recruitment deliberately targeted second-parity mothers already confident in their feeding choice, explicitly to reduce crossover -- a data-quality benefit, but one that makes the sample systematically unrepresentative of first-time or undecided mothers. |
| Classification of exposures | Low | Exposure groups are clearly and strictly defined (exclusively BF vs. exclusively FF with a single standardized formula brand), with antibiotic-exposed infants excluded and feeding documented as ad libitum. |
| Deviations from intended exposures | Low | The recruitment strategy specifically targeting committed feeders, combined with ad libitum exclusive feeding as documented, minimizes the likelihood of undetected deviation from the assigned exposure. |
| Missing data | Low | Both fecal and milk samples were collected on the same day for all enrolled infants at 3 months, with no attrition described. |
| Measurement of outcomes | Low | Rigorous and detailed: a validated DNA extraction protocol (3-4 pooled extractions per sample), defined 16S V1-V3 fusion primers, pyrosequencing at a named university core facility, a QIIME-based pipeline (Denoiser/UCLUST/ChimeraSlayer/Greengenes), and rarefaction to a fixed depth (7,800 reads) for diversity comparisons. |
| Selection of the reported result | Moderate | No trial/protocol registration (observational study); 24 bacterial genera were compared at a nominal P<0.05 via Mann-Whitney test with no explicit multiple-testing correction described for this taxon-level table, though both significant and non-significant results are reported transparently in the same table. |

**Microbiome-methods checklist (every study)**

| Domain | Judgment | Reasoning |
|---|---|---|
| Sample collection and storage method reported | Yes | "All stool and milk samples were stored at 4degC for 2-3h, before being transported on ice to the laboratory, where they were stored at -80degC." |
| DNA extraction method reported | Yes | "DNA was extracted using a modification of the method of Yu and Morrison... DNA from 3 to 4 extractions per sample were pooled." |
| Sequencing depth reported | Yes | "Pyrosequencing... yielded 417,344 total reads... After performing the quality control depletions..., 321,822 sequences with a mean of 10,734 sequences (range = 7,863-13,410) per sample were utilized for further analysis." |
| Negative/positive contamination controls reported | Not reported | No mention anywhere in the available text of negative extraction/PCR controls or positive/mock-community controls. |
| Compositional-data handling reported | No | PCoA/dbRDA on unweighted UniFrac distances and Mann-Whitney tests on relative abundances are used for the BF-vs-FF comparison (legitimate but not compositional-data transforms); the HMO-prediction PLS regression used data that were "log transformed and mean centered" -- a generic log transform, not a named log-ratio/CLR/ALR/ANCOM method. |

---

## #1899 — ALADDIN birth cohort lifestyle/delivery-mode/breastfeeding study 2014 (Sweden)

*Impact of lifestyle on the gut microbiota of healthy infants and their mothers -- the
ALADDIN birth cohort.* FEMS Microbiol Ecol. DOI 10.1111/1574-6941.12434.

Design: prospective, population-based longitudinal cohort, 128 mother-infant pairs
sampled at up to 6 timepoints (665-708 stool samples total). Breastfeeding (exclusive /
partial / not) is examined as one of several lifestyle/exposure factors at each age via
separate PERMANOVA models, with an explicit permutation-based false discovery rate
correction (1000 permutations per test) applied throughout, and a direct descriptive
check that delivery mode and early formula exposure were not confounded with each other.

### J. Risk of bias

*Drafted 27 Oct 2026 from a fresh read of `full_text_md/10.1111_1574-6941.12434/10.1111_1574-6941.12434.md`'s Materials and methods (Participants and sample collection, Preparation of samples, Statistical analyses) and Results.*

| Field | Value |
|---|---|
| RoB tool applicable | **ROBINS-I** (non-randomized, observational cohort) |

**ROBINS-I**

| Domain | Judgment | Reasoning |
|---|---|---|
| Confounding | Moderate | Each lifestyle/exposure factor (breastfeeding, delivery mode, anthroposophic lifestyle, etc.) was tested in a separate univariate PERMANOVA model rather than a single joint multivariable model, though the authors did explicitly check and rule out confounding between delivery mode and early formula exposure ("the proportion of infants who had been given formula during the first week of life was rather low and similar among those delivered by caesarean section (21%) and those delivered vaginally (19%)"). |
| Selection of participants | Moderate | Recruitment into the parent ALADDIN cohort was prospective and population-based, but this substudy further required mother-infant pairs to have provided samples at "all or five of the six sampling occasions," a completeness requirement that may favor more compliant families. |
| Classification of exposures | Low | Breastfeeding status was prospectively ascertained via structured interviews and classified into clear ordinal categories (exclusive/partial/not) at pre-specified timepoints (2 and 6 months), with exact proportions reported in Table 1. |
| Deviations from intended exposures | Low | Purely observational, prospectively-tracked actual feeding practice; no intervention protocol to deviate from. |
| Missing data | Low | Of 708 stool samples collected, only 43 (6.1%) were excluded, for an objective, pre-specified reason (fewer than 500 sequences), unlikely to be differentially related to feeding exposure. |
| Measurement of outcomes | Low | Rigorous and uniform: MoBio PowerSoil DNA extraction, defined 16S V3-V4 primers (341F/805R) with barcodes, 454 GS Titanium sequencing at a named national public-health institute, an RDP/BLAST-based taxonomic pipeline, and a sensitivity check confirming results were robust to the choice of minimum-detectable-abundance threshold. |
| Selection of the reported result | Low | Not a formally registered trial, but methodologically one of the most rigorous studies in this batch for multiple-testing control: FDR correction via 1000 permutations per test is applied to every reported comparison, and findings that fail to survive correction are explicitly flagged as such (e.g., the anthroposophic-lifestyle effect at 6 months, P=0.04, is explicitly noted as "not statistically significant after correction for multiple testing"). |

**Microbiome-methods checklist (every study)**

| Domain | Judgment | Reasoning |
|---|---|---|
| Sample collection and storage method reported | Yes | "These samples were frozen within 20 min of collection and stored at -20degC until later transport in a frozen state for storage at -70degC." |
| DNA extraction method reported | Yes | "DNA was extracted from 250 mg stool samples using the MoBio Power Soil DNA Kit... according to the manufacturer's instructions." |
| Sequencing depth reported | Yes | "The mean number of sequences per sample was 2670 (505-14,300)," with an explicit, objective minimum-depth exclusion threshold (500 sequences) applied and sensitivity-checked at a second threshold. |
| Negative/positive contamination controls reported | Not reported | No mention anywhere in the available text of negative extraction/PCR controls or positive/mock-community controls. |
| Compositional-data handling reported | No | Analysis uses Bray-Curtis similarity, PCoA, and the Shannon diversity index on relative-abundance data (legitimate ecological methods, not compositional-data transforms) -- no CLR/ALR/Aitchison/ANCOM mentioned anywhere. |

---

## #1965 — Hebei rural-village BF/FF Illumina cohort 2013 (China)

*Diversity of the intestinal microbiota in different patterns of feeding infants by
Illumina high-throughput sequencing.* World J Microbiol Biotechnol. DOI
10.1007/s11274-013-1404-3.

Design: very small (6 breastfed, 6 formula-fed), single rural-village cross-sectional
observational study, with authors stating "no significant differences in gestational
age, birth weight, and delivery mode" between groups and strict exclusivity maintained
throughout. The authors themselves acknowledge a key methodological limitation: the
short 16S V6-region amplicon used "restricted and insufficient" taxonomic identification
below the genus level.

### J. Risk of bias

*Drafted 27 Oct 2026 from a fresh read of `full_text_md/10.1007_s11274-013-1404-3/10.1007_s11274-013-1404-3.md` in full.*

| Field | Value |
|---|---|
| RoB tool applicable | **ROBINS-I** (non-randomized, observational cohort) |

**ROBINS-I**

| Domain | Judgment | Reasoning |
|---|---|---|
| Confounding | Moderate | Gestational age, birth weight, and delivery mode are stated to be comparable between groups and antibiotic exposure was absent in both, but no p-values are given for this baseline comparison and no statistical adjustment model is used for any analysis (simple ANOVA group comparisons only). |
| Selection of participants | Moderate | Very small (n=12), single rural-village convenience sample with minimal description of the recruitment process beyond basic eligibility. |
| Classification of exposures | Low | "Exclusive breastfeeding and formula-feeding was established throughout the research period; no infant received any additional foods" -- a clear, strictly enforced exclusivity criterion. |
| Deviations from intended exposures | Low | Strict exclusivity explicitly maintained and monitored throughout the study period with no deviations described. |
| Missing data | Low | All 12 enrolled infants are included in the analysis, with no attrition described. |
| Measurement of outcomes | Moderate | DNA extraction and sequencing protocols are reasonably detailed (QIAamp kit, defined V6-region primers, Illumina sequencing), but the authors themselves disclose that "the DNA fragments for sequencing analysis were small and the information for the identification of bacteria was restricted and insufficient to detect all species at the genus level," an author-acknowledged resolution limitation. |
| Selection of the reported result | Moderate | No trial/protocol registration (observational study); numerous phylum/family/genus-level comparisons are reported via simple ANOVA at a nominal P<0.05 with no explicit multiple-testing correction described, though non-significant findings (e.g., Bacteroidetes, richness/diversity indices) are reported plainly alongside significant ones. |

**Microbiome-methods checklist (every study)**

| Domain | Judgment | Reasoning |
|---|---|---|
| Sample collection and storage method reported | Yes | "Fecal samples were collected by physicians and preserved in RNA later (Qiagen) at -80degC until extraction of genomic DNA." |
| DNA extraction method reported | Yes | "DNA was extracted using a QIAamp DNA Stool Mini Kit (QIAGEN)... In order to improve efficiency of cell wall lysis of Gram-positive bacteria in the feces, the sample was incubated at 95degC for 5 min." |
| Sequencing depth reported | Yes | "879,513 filtered high-quality, classifiable 16S rRNA gene sequences with a mean (+/-SEM) of 73,292 +/- 584 sequences per sample." |
| Negative/positive contamination controls reported | Not reported | No mention anywhere in the available text of negative extraction/PCR controls or positive/mock-community controls. |
| Compositional-data handling reported | No | Relative-abundance percentages are compared by ANOVA, with richness/diversity assessed via Chao1 and the nonparametric Shannon index (legitimate ecological metrics, not compositional-data transforms) -- no CLR/ALR/Aitchison/ANCOM mentioned anywhere. |

---

## #1982 — Australian goat-milk/cow-milk/breast-milk RCT-with-BF-reference 2013 (Australia/New Zealand)

*Comparison of the Compositions of the Stool Microbiotas of Infants Fed Goat Milk
Formula, Cow Milk-Based Formula, or Breast Milk.* Appl Environ Microbiol. DOI
10.1128/AEM.03910-12. ACTRN12608000047392.

Design: hybrid -- multicenter, double-blind RCT (stratified by sex and center) between
goat-milk and cow-milk formula, plus a non-randomized exclusively-breastfed reference
group -- routed to ROBINS-I per the hybrid-design rule. Sex, delivery mode, and age at
sampling were all reported as evenly distributed across all three groups (including the
breastfed reference group). A small, transient, pre-randomization breastfeeding exposure
in a minority of formula-fed infants (average 2-4 days, during the first 2 weeks before
study-formula initiation) is explicitly disclosed and quantified.

### J. Risk of bias

*Drafted 27 Oct 2026 from a fresh read of `full_text_md/10.1128_aem.03910-12/10.1128_aem.03910-12.md`'s Materials and Methods (Subjects and study design, Stool samples, DNA extraction, Pyrosequencing, qPCR) and Results.*

| Field | Value |
|---|---|
| RoB tool applicable | **ROBINS-I** (non-randomized breastfed reference group per the hybrid-design rule) |

**ROBINS-I**

| Domain | Judgment | Reasoning |
|---|---|---|
| Confounding | Low | Sex, delivery mode, and age at sample collection were reported as evenly distributed across all three dietary groups including the breastfed reference ("there was an even distribution of sex and delivery mode across the dietary groups"), formula randomization was stratified by sex and study center, and the minor pre-randomization breastfeeding exposure in some formula-fed infants is transparently disclosed and quantified (average 2-4 days) rather than hidden. |
| Selection of participants | Low | Part of a registered, multicenter, double-blind controlled feeding trial with explicit objective eligibility criteria (gestational age 37-42 weeks, birth weight 2.5-4.75 kg); recruitment and allocation processes are clearly described. |
| Classification of exposures | Low | Exclusivity and compliance were assessed using the validated criteria of the WHO Multicentre Growth Reference Study Group, and the minor early-life breastfeeding exposure in a subset of formula-fed infants is explicitly quantified rather than left unaddressed. |
| Deviations from intended exposures | Low | Parents were "instructed to exclusively feed their infants the allocated study formula from enrolment," compliance was monitored ("infants were compliant with feeding"), and the one known deviation (brief pre-enrollment breastfeeding) is explicitly disclosed and quantified. |
| Missing data | Low | All 30 infants per group (90 total) are included in the analysis with no attrition described for this substudy. |
| Measurement of outcomes | Low | Extremely rigorous and uniform: a detailed, validated DNA extraction protocol, purpose-designed and spike-validated universal bifidobacterial primers, pyrosequencing at a named facility, a QIIME/RDP pipeline, and orthogonal qPCR validation (highly correlated with pyrosequencing results) including no-template negative controls on every plate. |
| Selection of the reported result | Moderate | Prospectively registered as a clinical trial (ACTRN12608000047392), but no explicit multiple-testing correction is described for the numerous taxon/species-level comparisons across Tables 4-7, despite both significant and non-significant findings being reported transparently throughout (e.g., "Bifidobacteriaceae did not differ in abundance between male and female infants"). |

**Microbiome-methods checklist (every study)**

| Domain | Judgment | Reasoning |
|---|---|---|
| Sample collection and storage method reported | Yes | "The samples were immediately frozen at -20degC following collection, held for less than 12 months at this temperature, and shipped on dry ice... for further storage at -80degC." |
| DNA extraction method reported | Yes | A detailed multi-step phenol-chloroform/SDS/lysozyme protocol is described in full, with further purification using the Qiagen-AllPrep DNA/RNA minikit. |
| Sequencing depth reported | Yes | "An average of 3,745 (range, 2,051 to 5,782) sequences per barcoded sample were recovered," with explicit per-group totals (99,587/119,933/117,548 sequences for breast/goat/cow groups respectively). |
| Negative/positive contamination controls reported | Yes | "No-template controls were also included on each plate" for the qPCR assays, in addition to primer-specificity validation via DNA-spiking experiments. |
| Compositional-data handling reported | No | Relative abundances ("normalized by total 16S rRNA genes") were compared using Mann-Whitney/Kruskal-Wallis tests, with UniFrac-based beta-diversity and rarefaction-based alpha-diversity (legitimate ecological methods, not compositional-data transforms) -- no CLR/ALR/Aitchison/ANCOM mentioned anywhere. |

---

## #1988 — CHILD Study delivery-mode/diet descriptive cohort 2013 (Canada)

*Gut microbiota of healthy Canadian infants: profiles by mode of delivery and infant diet
at 4 months.* CMAJ. DOI 10.1503/cmaj.121189.

Design: descriptive, cross-sectional substudy of 24 term infants, consecutively selected
("the first 24 infants for whom fecal samples were available") from the population-based
CHILD birth cohort. Breastfeeding is classified into three categories (exclusive/partial/
none) at the time of sampling (~4 months). The authors explicitly validated their sample's
representativeness against Canadian national statistics and explicitly disclosed that,
due to small sample size, they could not statistically disentangle the known
inter-relationships between delivery mode, antibiotic exposure, and breastfeeding success.

### J. Risk of bias

*Drafted 27 Oct 2026 from a fresh read of `full_text_md/10.1503_cmaj.121189/10.1503_cmaj.121189.md`'s Methods (Study design, Analysis of fecal samples, Statistical analysis), Results, and Strengths and limitations.*

| Field | Value |
|---|---|
| RoB tool applicable | **ROBINS-I** (non-randomized, observational cohort) |

**ROBINS-I**

| Domain | Judgment | Reasoning |
|---|---|---|
| Confounding | Moderate | The authors explicitly acknowledge that "we could not assess interactions between exposure variables, which are frequently inter-related (cesarean delivery is typically accompanied by prophylactic use of antibiotics and can affect breastfeeding success)," a disclosed, unaddressed confounding risk attributed to insufficient statistical power from the small sample. |
| Selection of participants | Low | Infants were consecutively selected ("the first 24 infants for whom fecal samples were available") rather than cherry-picked, and the authors explicitly validated representativeness against Canadian national statistics (25% cesarean vs. 27% national average; 42% exclusively breastfed vs. 43% national average). |
| Classification of exposures | Low | Breastfeeding status was ascertained via maternal questionnaire and classified into three explicit categories (exclusive/partial/none) at the time of fecal sampling, with individual-infant exposure details documented transparently in Table 1. |
| Deviations from intended exposures | Low | Purely observational, cross-sectional exposure ascertainment reflecting actual feeding practice at the time of sampling; no intervention protocol to deviate from. |
| Missing data | Low | All 24 enrolled infants have complete data and are included in the analysis; this is a single-timepoint cross-sectional design with no described attrition. |
| Measurement of outcomes | Low | Rigorous and uniform: FastPrep DNA for Soil Kit extraction, 16S V5-V6-V7 region sequencing classified against SILVA taxonomy via a previously validated protocol, rarefied diversity analysis (10,000 sequences/sample), plus orthogonal targeted qPCR specifically for C. difficile. |
| Selection of the reported result | Low | Built on the pre-existing, registered CHILD national birth cohort; Metastats was used specifically for its rigorous multiple-testing correction (q-values), and numerous non-significant findings are reported plainly throughout (e.g., "we detected no significant differences according to intrapartum exposure to antibiotics," "we did not observe strong differences by mode of delivery in... Bifidobacterium or Clostridium"). |

**Microbiome-methods checklist (every study)**

| Domain | Judgment | Reasoning |
|---|---|---|
| Sample collection and storage method reported | Not reported | The main text states only that "stool samples were collected from the infants at age 3-4 months," with no storage temperature or timing given; this detail is deferred to "Appendix 1," which is not available here. |
| DNA extraction method reported | Yes | "Bacterial DNA was extracted from stool samples using the FastPrep DNA for Soil Kit (MP Biomedicals, Solon, Ohio)." |
| Sequencing depth reported | Yes | Diversity measures "were calculated... with rarefied data (10,000 sequences per sample)" -- an explicit depth figure stated directly in the main text. |
| Negative/positive contamination controls reported | Not reported | No mention anywhere in the available main text of negative extraction/PCR controls or positive/mock-community controls (this detail may exist only in the unavailable Appendix 1). |
| Compositional-data handling reported | No | Differential abundance was assessed using Metastats, a count-based statistical method for comparing relative-abundance data (not a named compositional-data transform) -- no CLR/ALR/Aitchison/ANCOM mentioned anywhere. |

---

## #2022 — Illinois host-transcriptome/metagenome integration study 2012 (USA)

*A metagenomic study of diet-dependent interaction between gut microbiota and host in
infants reveals differences in immune response.* Genome Biol. DOI
10.1186/gb-2012-13-4-r32.

Design: small (6 exclusively breastfed, 6 exclusively formula-fed), single-site
observational cohort, drawn from the same University of Illinois recruitment protocol as
#1882 (same single formula brand, Enfamil LIPIL) but a distinct, smaller 6-vs-6 subset
focused on integrating host intestinal-epithelial transcriptome data with shotgun
metagenomic microbiome data. The detailed subject-recruitment/eligibility criteria are
deferred entirely to a prior publication, not restated in this paper's own text.

### J. Risk of bias

*Drafted 27 Oct 2026 from a fresh read of `full_text_md/10.1186_gb-2012-13-4-r32/10.1186_gb-2012-13-4-r32.md`'s Results (Table 1) and Materials and methods (Ethics statement and subject recruitment, Isolation of stool DNA, Sequencing of gut microbiomes, Metagenomic data analysis).*

| Field | Value |
|---|---|
| RoB tool applicable | **ROBINS-I** (non-randomized, parent-chosen feeding exposure) |

**ROBINS-I**

| Domain | Judgment | Reasoning |
|---|---|---|
| Confounding | Moderate | Table 1 shows broadly comparable maternal age, parity, and growth trajectories between groups, and the same single formula brand was used for all FF infants, but infant sex was notably imbalanced (5 male/1 female BF vs. 4 male/2 female FF) and no statistical adjustment is used for any comparison given the very small sample (6 infants/group). |
| Selection of participants | Moderate | Detailed subject admission criteria and recruitment protocol are deferred entirely to a prior publication ("details... have been previously described") rather than restated in this paper's own text, and the analytic sample is very small (n=6/group). |
| Classification of exposures | Low | Exposure groups are clearly and consistently defined as exclusively breastfed vs. exclusively formula-fed with a single standardized formula brand, used consistently in all analyses. |
| Deviations from intended exposures | No information | No information is given anywhere in the available text on adherence to or deviation from the assigned exclusive feeding exposure. |
| Missing data | Low | All 12 enrolled infants (6 BF, 6 FF) have complete paired microbiome and transcriptome data reported, with no attrition described. |
| Measurement of outcomes | Low | Rigorous and detailed: a specific modified Yu-and-Morrison DNA extraction protocol, 454 GS FLX Titanium shotgun sequencing at a named facility, dual independent taxonomic classification methods (16S-fragment alignment to GreenGenes and PhymmBL) cross-validated against each other, and an explicit computational step to filter out human-genome-contaminating reads via BLAST. |
| Selection of the reported result | Low | No trial/protocol registration (observational study), but the two analyzed host gene sets (459 intestinal-biology genes, 660 immunity/defense genes) were defined a priori from literature and gene-ontology databases before differential-expression testing, Benjamini-Hochberg FDR correction is applied systematically throughout, and extensive non-significant findings are reported plainly (e.g., "there was no enrichment of differential expression in genes related to the cell death biological process"). |

**Microbiome-methods checklist (every study)**

| Domain | Judgment | Reasoning |
|---|---|---|
| Sample collection and storage method reported | Not reported | This paper's text moves directly to "Isolation of stool DNA" without describing stool collection or storage protocol; that detail is deferred to a prior publication, not restated here. |
| DNA extraction method reported | Yes | "Genomic DNA was extracted using a modification of the method of Yu and Morrison... 250 mg (wet weight) of feces was weighed... Lysis buffer... was added... and the tube was incubated at 70degC for 15 minutes," with the full protocol described. |
| Sequencing depth reported | Not reported | Sequencing-depth figures are deferred entirely to supplementary Additional files 5 and 10 ("Representative MG-RAST sample statistics are shown in Additional file 5"); no absolute read-count number is stated directly in the main text. |
| Negative/positive contamination controls reported | Not reported | No biological negative/positive/mock-community control is mentioned; only a computational step to filter reads 100% identical to the human reference genome, which is host-DNA removal rather than a lab contamination control. |
| Compositional-data handling reported | No | Permutation tests with FDR correction were used on read-count proportions, and canonical correlation/principal component analysis were used for host-microbiome integration (legitimate multivariate methods, not compositional-data transforms) -- no CLR/ALR/Aitchison/ANCOM mentioned anywhere. |

---

## #2145 — Zhejiang preterm/full-term x BF/non-BF 4-group pilot 2026 (China)

*Comparison of gut microbiome and metabolome characteristics in preterm and full-term
infants under different feeding modes.* Acta Microbiologica Sinica. DOI
10.13343/j.cnki.wsxb.20260127.

Design: cross-sectional, explicitly self-described "pioneering exploratory study," 4
groups of 10 infants each (breastfed preterm [BPI], non-breastfed preterm [NBPI],
breastfed full-term [BTI], non-breastfed full-term [NBTI]) from a single Chinese
hospital. All 4 groups were vaginally delivered by design, specifically to remove
delivery mode as a confounder. "Non-breastfeeding" is strictly defined as exclusive
formula feeding, excluding mixed-feeding infants. The authors themselves explicitly
state that, given the small sample size, perinatal covariates were not entered into a
multivariable model and "rigorous independent causal inference" was not attempted.

### J. Risk of bias

*Drafted 27 Oct 2026 from a fresh read of `full_text_md/10.13343_j.cnki.wsxb.20260127/10.13343_j.cnki.wsxb.20260127.md`'s Methods (1.1 Study subjects, 1.2 Sample collection, 1.3-1.4 DNA extraction/sequencing/bioinformatics, 1.7 Statistics).*

| Field | Value |
|---|---|
| RoB tool applicable | **ROBINS-I** (non-randomized, observational cross-sectional cohort) |

**ROBINS-I**

| Domain | Judgment | Reasoning |
|---|---|---|
| Confounding | Moderate | Delivery mode was held constant by design (all 4 groups vaginally delivered, explicitly to remove this confounder) and antibiotic-exposed mothers/infants were excluded, but the authors themselves explicitly state that "some perinatal data were not included in a multivariable statistical model" and that the study does not attempt "rigorous independent causal inference." |
| Selection of participants | Moderate | Single-center convenience sample recruited over a defined 6-month window with explicit, fairly rigorous maternal and infant eligibility criteria, but a very small sample (n=10/group, 40 total) limits representativeness. |
| Classification of exposures | Low | "Non-breastfeeding" is explicitly and strictly defined as pure formula feeding, excluding mixed-feeding individuals -- a precise exclusivity definition avoiding the common leniency seen in similar studies. |
| Deviations from intended exposures | Low | Cross-sectional exposure classification with the explicit exclusion of mixed-feeding infants from the non-breastfeeding group inherently filters out ambiguous deviation cases. |
| Missing data | Low | Fixed n=10/group by design with stool collected at a defined postnatal window (days 3-7); no attrition is described. |
| Measurement of outcomes | Low | Rigorous and uniform: QIAamp PowerFecal Pro DNA Kit extraction, defined 16S V3-V4 primers (338F/806R), sequencing by a named commercial facility (Novogene) on Illumina HiSeq2500, QIIME2/DADA2 ASV pipeline against SILVA138, plus a detailed untargeted LC-MS metabolomics protocol. |
| Selection of the reported result | Moderate | No trial/protocol registration; the study explicitly self-describes as "a pioneering exploratory study" without a pre-registered hypothesis or multivariable analysis plan, though clear a priori statistical thresholds (LEfSe LDA>4.0 & P<0.05; metabolomics VIP>1.0, |log2FC|>1, P<0.05) and FDR correction for the microbiome-metabolite correlation network are applied consistently. |

**Microbiome-methods checklist (every study)**

| Domain | Judgment | Reasoning |
|---|---|---|
| Sample collection and storage method reported | Yes | Fresh stool was collected promptly after defecation using a sterile sampling spoon into a pre-labeled sterile container, capped immediately, and "sent to the laboratory immediately after collection and stored at -80degC." |
| DNA extraction method reported | Yes | "Total genomic DNA was extracted from approximately 200 mg of stool sample using the QIAamp PowerFecal Pro DNA Kit (Qiagen)," with DNA quality verified by NanoDrop and agarose gel. |
| Sequencing depth reported | Not reported | No total or per-sample read-count/depth figure is given anywhere in the available text. |
| Negative/positive contamination controls reported | Not reported | No mention anywhere in the available text of negative extraction/PCR controls or positive/mock-community controls. |
| Compositional-data handling reported | No | Analysis uses Bray-Curtis distance/PCoA, LEfSe/LDA, and relative-abundance percentages (legitimate ecological methods, not compositional-data transforms) -- no CLR/ALR/Aitchison/ANCOM mentioned anywhere. |

---

## #2772 — Zhengzhou/Dalian Chinese-Swedish infant gut metabolome maturation cohort 2023 (China/Sweden)

*Maturation of the gut metabolome during the first year of life in humans.* Gut Microbes.
DOI 10.1080/19490976.2023.2231596.

Design: prospective, longitudinal cohort of 152 Chinese mother-infant pairs (newborn,
4-month, 12-month, and maternal timepoints), cross-validated against an independent
Swedish cohort processed under an identical protocol. Feeding pattern is explicitly and
precisely defined ("exclusively breast milk feeding indicates no formula milk exposure
within 48 hours before sampling") and examined alongside delivery mode, with feeding
effects specifically analyzed within the vaginally-delivered stratum to reduce
confounding between the two factors.

### J. Risk of bias

*Drafted 27 Oct 2026 from a fresh read of `full_text_md/10.1080_19490976.2023.2231596/10.1080_19490976.2023.2231596.md`'s Results/Discussion (Effect of delivery mode and diet sections) and Materials and methods (Participants and sample collection, DNA extraction and sequencing, Preprocessing, Statistical analysis).*

| Field | Value |
|---|---|
| RoB tool applicable | **ROBINS-I** (non-randomized, observational longitudinal cohort) |

**ROBINS-I**

| Domain | Judgment | Reasoning |
|---|---|---|
| Confounding | Moderate | Feeding-related comparisons (e.g., "impact of feeding on the variations in acylcarnitines... in vaginal infants") were specifically conducted within the vaginally-delivered stratum to separate feeding effects from delivery-mode effects, a genuine confounding-reduction step, though no single joint multivariable model adjusts for all covariates (e.g., maternal BMI, antibiotics) simultaneously. |
| Selection of participants | Moderate | Single-site recruitment (Zhengzhou, China) over a defined window with explicit eligibility criteria (GA 37-42 weeks, no maternal chronic disease, no infant prematurity/genetic disease), cross-validated against an independently recruited Swedish cohort processed identically; Table 1 discloses non-trivial missingness in some variables (e.g., feeding-pattern data missing for 18 of 95 infants at 12 months, ~19%). |
| Classification of exposures | Low | Feeding pattern has an explicit, precise operational definition ("exclusively breast milk feeding indicates no formula milk exposure within 48 hours before sampling") and a clear three-category classification (exclusive/mixed/exclusive formula) with exact counts reported at every timepoint. |
| Deviations from intended exposures | Low | Purely observational, longitudinally-tracked actual feeding practice; the explicit 48-hour exposure-window definition itself guards against misclassifying recent deviations. |
| Missing data | Moderate | Table 1 explicitly discloses missingness across several variables at various timepoints, most notably feeding-pattern data missing for 18 of 95 infants (~19%) at the 12-month timepoint. |
| Measurement of outcomes | Low | Extremely rigorous and uniform: a previously validated DNA extraction/PCR protocol with specific reagent detail restated, 16S V4 MiSeq 250-bp paired-end sequencing, QIIME2/DADA2 processing with explicit depth-normalization (subsampling to a common depth to harmonize with the Swedish cohort), and a detailed UPLC-MS metabolomics protocol with pooled QC samples and RSD-based quality filtering. |
| Selection of the reported result | Low | No formal trial/protocol registration (observational cohort), but FDR correction (Benjamini-Hochberg) is applied systematically throughout, PLS-DA models are explicitly validated against overfitting via permutation testing, and significance thresholds are set a priori and applied consistently across all comparisons. |

**Microbiome-methods checklist (every study)**

| Domain | Judgment | Reasoning |
|---|---|---|
| Sample collection and storage method reported | Yes | "Fresh fecal samples were stored at 4degC (maximum 24 h) and transferred to -80degC for long-term storage until further analysis." |
| DNA extraction method reported | Yes | "Genomic DNA was isolated from 130 to 150 mg of fecal samples using a previously described method with slight modifications on the PCR system," with the specific PCR reagents, primer concentrations, and template amount restated directly in this paper's own text. |
| Sequencing depth reported | Yes | "We obtained a total of 21,691,557 high-quality reads, with an average of 55,619 +/- 29,921 sequences/sample (mean +/- SD; range 2,208 to 357,251)." |
| Negative/positive contamination controls reported | Not reported | No mention anywhere in the available text of negative extraction/PCR controls or positive/mock-community controls for the 16S sequencing (the metabolomics "pooled QC sample" is an analytical instrument-drift control, not a biological contamination control). |
| Compositional-data handling reported | No | "The taxonomic composition table was exported... with the relative abundance of taxa summed to 1" -- simple relative-abundance normalization, not a named compositional-data transform (CLR/ALR/Aitchison/ANCOM are not mentioned anywhere). |

---

## #2839 — Beijing MFGM-fortified-formula RCT-with-BF-reference 2021 (China)

*MFGM components promote gut Bifidobacterium growth in infant and in vitro.* Eur J Nutr.
DOI 10.1007/s00394-021-02638-5. NCT02658500 (registered Jan 2016).

Design: hybrid -- randomized, controlled trial between a common formula (FF1) and an
MFGM-fortified modified formula (FF2), plus a non-randomized exclusively-breastfed
reference group (BF) -- routed to ROBINS-I per the hybrid-design rule. A priori power
calculation targeted 13 infants/group; formula compliance was monitored via parental
feeding records and collection of empty formula boxes. **The authors themselves report a
statistically significant baseline anthropometric difference**: "FF2 group and FF1 group
were significantly lower in height and weight compared to BF both at birth and 1 month,"
an imbalance not adjusted for in the microbiome comparisons.

### J. Risk of bias

*Drafted 27 Oct 2026 from a fresh read of `full_text_md/10.1007_s00394-021-02638-5/10.1007_s00394-021-02638-5.md`'s Methods (Study design, Infant study population, Criteria, Sampling, 16S sequencing, Bioinformatic analysis) and Results.*

| Field | Value |
|---|---|
| RoB tool applicable | **ROBINS-I** (non-randomized breastfed reference group per the hybrid-design rule) |

**ROBINS-I**

| Domain | Judgment | Reasoning |
|---|---|---|
| Confounding | Serious | The authors explicitly report a statistically significant baseline difference in height and weight between the breastfed reference group and both formula groups, present already at birth, which is not adjusted for in any of the microbiome or metabolite comparisons presented. |
| Selection of participants | Low | A registered trial with explicit, objective eligibility criteria (GA 37-41 weeks, birth weight 2500-4000 g, Apgar>7, multiple exclusions) and an a priori power calculation (13 infants/group) justifying the recruited sample size across two study sites. |
| Classification of exposures | Low | "Feeding practices were assessed by careful chart review and classified as exclusive formula or breast-fed," with intervention fidelity further verified via "formula taken records and the empty formula box." |
| Deviations from intended exposures | Low | Compliance with assigned formula was explicitly monitored via parental feeding records and collection of empty formula packaging to verify intervention fidelity. |
| Missing data | Moderate | The final analytic sample (44 of a targeted 39+ minimum) is described only as those "whose data passed all quality control criteria," without clearly stating how many participants were originally enrolled or excluded and why. |
| Measurement of outcomes | Low | Rigorous and uniform: QIAamp Fast DNA Stool Mini Kit extraction, defined 16S V3-V4 primers, Illumina HiSeq 2500 sequencing, a detailed NMR-based urine metabolomics protocol, and an orthogonal in vitro mechanistic validation experiment (bacterial culture growth assay with RNA-seq). |
| Selection of the reported result | Low | Prospectively registered (NCT02658500, Jan 2016) with an a priori power calculation; FDR correction is applied systematically (<10% for urinary metabolites), and unexpected/null findings are reported candidly (e.g., "the abundance of Bifidobacterium in FF2 group was not higher than that of FF1 group," with the authors openly discussing possible reasons). |

**Microbiome-methods checklist (every study)**

| Domain | Judgment | Reasoning |
|---|---|---|
| Sample collection and storage method reported | Yes | "Fecal samples were collected by parents at home from diapers... immediately put into the stool collection tubes with stool DNA stabilizer (Stratec, Germany) and stored at -20degC until they were transported (in dry ice, within 24 h)... then stored at -80degC until analyses." |
| DNA extraction method reported | Yes | "Genomic DNA was extracted from 100 mg of homogenized fecal samples using the QIAamp Fast DNA Stool Mini Kit (Qiagen)... following the manufacturer's protocol." |
| Sequencing depth reported | Not reported | No total or per-sample read-count/depth figure is given anywhere in the available text for the 16S sequencing. |
| Negative/positive contamination controls reported | Not reported | No mention anywhere in the available text of negative extraction/PCR controls or positive/mock-community controls (the in vitro growth experiment's "control TPY medium" is an experimental growth-assay control, not a sequencing contamination control). |
| Compositional-data handling reported | No | "Total sum normalization (TSS)" (simple relative-abundance normalization) and square-root transformation were used for correlation analyses -- neither is a named compositional-data transform (CLR/ALR/Aitchison/ANCOM are not mentioned anywhere). |

---

## #2938 — Peshawar zinc-status/feeding-type cohort 2021 (Pakistan)

*Gut microbiome profile in zinc deficient infants using next generation sequencing.*
Khyber Med Univ J. DOI 10.35845/kmuj.2021.20739.

Design: cross-sectional study, same underlying Peshawar cohort and project as study
#1208 (23 breastfed, 23 formula-fed infants; shotgun metagenomics via the Microbiome
Helper pipeline), here reporting an additional secondary zinc-correlation analysis. An a
priori sample-size calculation (25/group) was used, with a CONSORT-style enrollment flow
(75 identified -> 50 enrolled -> 46 analyzed) given in Figure 1. As with #1208, the
Methods describe infants as "predominantly either on breast feeding or formula feeding,"
while the Abstract describes the same groups simply as "breast-fed (BF)" and
"formula-fed (FF)" -- the same internal exclusivity-definition inconsistency noted in
that sister publication.

### J. Risk of bias

*Drafted 27 Oct 2026 from a fresh read of `full_text_md/10.35845_kmuj.2021.20739/10.35845_kmuj.2021.20739.md` in full (this is a separate publication from #1208, assessed independently on its own text, though the same underlying cohort/design informs several judgments below).*

| Field | Value |
|---|---|
| RoB tool applicable | **ROBINS-I** (non-randomized, observational cross-sectional cohort) |

**ROBINS-I**

| Domain | Judgment | Reasoning |
|---|---|---|
| Confounding | Serious | No baseline-characteristics comparison table and no statistical adjustment of any kind is used anywhere in the BF-vs-FF comparisons (simple descriptive percentages and unadjusted correlations), despite known confounders (delivery mode, antibiotics, maternal factors) never being addressed. |
| Selection of participants | Moderate | A CONSORT-style flow is given (75 infants identified -> 50 enrolled -> 46 analyzed, Figure 1) with an a priori sample-size calculation (25/group), but this remains a single-city convenience sample. |
| Classification of exposures | Moderate | The Methods describe infants as "predominantly either on breast feeding or formula feeding," while the Abstract describes the same groups simply as "breast-fed (BF)" and "formula-fed (FF)" -- an internal inconsistency in how strictly exclusive feeding was defined, with no explicit ascertainment method described. |
| Deviations from intended exposures | Low | Cross-sectional observational design with no intervention to deviate from. |
| Missing data | Low | Of 50 enrolled infants, 46 (92%) had data available for final analysis, with the enrollment/exclusion flow transparently disclosed in a CONSORT-style diagram. |
| Measurement of outcomes | Low | A standard shotgun-metagenomics pipeline is named (Qiagen stool kit, Illumina MiSeq sequencing, Microbiome Helper SOP: KneadData/Trimmomatic/Bowtie2/MetaPhlAn2), with sequencing depth explicitly quantified ("a total number of 5,508,374 sequencing reads... with an average of 114,757 reads per sample"). |
| Selection of the reported result | Moderate | No trial/protocol registration; the zinc-correlation analysis tests numerous taxa via simple Pearson correlation (Table I) with no explicit multiple-testing correction described, though both significant and non-significant correlations are reported together in the same table rather than selectively. |

**Microbiome-methods checklist (every study)**

| Domain | Judgment | Reasoning |
|---|---|---|
| Sample collection and storage method reported | Not reported | The text states only that "the blood samples and the fecal sample of the infants were taken and subjected to... fecal DNA extraction," with no storage temperature or handling protocol given anywhere in the available text. |
| DNA extraction method reported | Yes | "Fecal DNA extraction was done by following the standard protocols using Qiagen mini stool kit" (a named commercial kit, despite unusual phrasing in the original text). |
| Sequencing depth reported | Yes | "A total number of 5,508,374 sequencing reads were generated with an average of 114,757 reads per sample." |
| Negative/positive contamination controls reported | Not reported | No mention anywhere in the available text of negative extraction/PCR controls or positive/mock-community controls. |
| Compositional-data handling reported | No | "Concentration of gut microbiota was expressed in percentage of microbes" (simple relative abundance) with Pearson correlation used throughout -- no CLR/ALR/Aitchison/ANCOM mentioned anywhere. |

---

## #3116 — Lanzhou delivery-mode x feeding-mode x age 2019 (China)

*Effects of different modes of delivery and feeding on intestinal flora of newborns and
infants with different ages.*
Iran J Pediatr. DOI 10.5812/ijp.88329.

Design: cross-sectional, single-center study (First Hospital of Lanzhou University) of
108 full-term infants stratified into 9 fixed-size subgroups (n=12/group) by delivery
mode (natural vs. cesarean) x feeding mode (breastfeeding / goat-milk formula / cow-milk
formula) x age phase (0-6mo / 6-12mo / 12-36mo). A sample-size formula is given, but it
is a basic single-proportion confidence-interval calculation, not a comparative
group-difference power calculation -- a notably weaker justification for the fixed n=12
cells than seen in several other studies this batch. Straightforward observational
design (not a hybrid RCT-with-reference-group case).

### J. Risk of bias

*Drafted 27 Oct 2026 from a fresh read of `full_text_md/10.5812_ijp.88329/10.5812_ijp.88329.md` in full (Materials and Methods, Results, Discussion).*

| Field | Value |
|---|---|
| RoB tool applicable | **ROBINS-I** (non-randomized, observational cross-sectional cohort) |

**ROBINS-I**

| Domain | Judgment | Reasoning |
|---|---|---|
| Confounding | Serious | No baseline-characteristics comparison table and no statistical adjustment of any kind across the 9 delivery x feeding x age groups (only t-test/Mann-Whitney U/chi-square), despite a 3-factor stratified design with only 12 infants/cell that is especially vulnerable to unmeasured confounding. |
| Selection of participants | Moderate | Single-hospital recruitment with explicit eligibility criteria (full-term, normal birth weight, no diarrhea/GI disease in the preceding week, no antibiotic use), but fixed group sizes (n=12) were set via a weak, non-comparative sample-size justification with no description of how eligible infants were sampled from the source population. |
| Classification of exposures | No information | Feeding mode is categorized as breastfeeding/goat-milk formula/cow-milk formula with no stated definition of exclusivity or ascertainment method (e.g., no interview/chart-review method described) anywhere in the text. |
| Deviations from intended exposures | No information | Not addressed anywhere in the available text. |
| Missing data | No information | No flow diagram or statement of recruitment-to-analysis attrition is given; the paper states only that fixed group sizes (12/group, 108 total) were achieved. |
| Measurement of outcomes | Moderate | DNA extraction kit (Shanghai Shuangying Biotechnology) and platform (Ion S5(TM)XL, V3-V4 16S) are named, but the stated primer sequences contain an implausible, apparently corrupted/garbled run of repeated bases, and no explicit sequencing-depth number is given (only a qualitative rarefaction-curve description). |
| Selection of the reported result | Serious | No study registration; comparisons are run across 9 groups at phylum, family, and genus level using repeated pairwise t-test/Mann-Whitney U/chi-square tests with no multiple-testing correction mentioned anywhere, despite the clear multiple-comparisons burden of this factorial design. |

**Microbiome-methods checklist (every study)**

| Domain | Judgment | Reasoning |
|---|---|---|
| Sample collection and storage method reported | Yes | "Internal feces samples were collected to prevent contamination by urine or other impurities, placed in sterile tubes and stored in a -80degC refrigerator prior to use." |
| DNA extraction method reported | Yes | "Fecal genomic DNA extraction kit was purchased from Shanghai Shuangying Biotechnology Co., Ltd... Genomic DNA was extracted, and its purity and concentration were detected by SDS-PAGE." |
| Sequencing depth reported | Not reported | No total or mean read-count number is given anywhere; only a qualitative statement that the rarefaction curve "tends to level off" as sequencing number increases. |
| Negative/positive contamination controls reported | Not reported | No mention anywhere in the available text of negative extraction/PCR controls or positive/mock-community controls. |
| Compositional-data handling reported | No | Analysis uses relative-abundance percentages, Chao1/ACE/Shannon/Simpson diversity indices, and LEfSe -- no CLR/ALR/Aitchison/ANCOM compositional-data transform is mentioned anywhere. |

---

## #3211 — Taguig City birth-process/milk-diet/primer-region 2019 (Philippines)

*Differences in the bacterial profiles of infant gut by birth process, milk diet, and
choice of 16S rRNA gene target region.*
Hum Microbiome J. DOI 10.1016/j.humic.2019.100062.

Design: cross-sectional study of 60 healthy, full-term Filipino infants aged 2-4 months,
drawn from 187 mother-infant pairs recruited at four community health centers in Taguig
City, stratified into 6 groups by birth process (vaginal/cesarean) x milk diet
(exclusive breastfeeding / formula / mixed), with a technical sub-analysis comparing
16S V3-V4 vs. V4-V5 primer regions in a 10-sample cesarean-delivered-breastfed subset.
Group sizes are small and uneven (5-14 infants/group). Formula-fed infants are explicitly
defined as having "some exposure to breast milk but... fed with 80-100% formula milk."
Straightforward observational design (not a hybrid RCT-with-reference-group case).

### J. Risk of bias

*Drafted 27 Oct 2026 from a fresh read of `full_text_md/10.1016_j.humic.2019.100062/10.1016_j.humic.2019.100062.md` in full (Materials and methods, Results and discussion).*

| Field | Value |
|---|---|
| RoB tool applicable | **ROBINS-I** (non-randomized, observational cross-sectional cohort) |

**ROBINS-I**

| Domain | Judgment | Reasoning |
|---|---|---|
| Confounding | Serious | No baseline-characteristics comparison table and no statistical adjustment of any kind in the birth-process/milk-diet comparisons (Welch's t-test, ANOSIM on relative abundance only), despite small, uneven group sizes (as low as n=5 for CD-FM) that make residual confounding plausible. |
| Selection of participants | Serious | Only 60 of 187 recruited mother-infant pairs were included, with no description anywhere in the text of how or why the analytic subset of 60 was selected from the larger recruited pool beyond the stated eligibility/anthropometric exclusions. |
| Classification of exposures | Low | Feeding mode was ascertained by structured maternal/guardian interview "subsequently validated with their infant's health book," with an explicit operational definition distinguishing exclusive breastfeeding from formula-fed infants who nonetheless had 80-100% formula milk with some incidental breast-milk exposure. |
| Deviations from intended exposures | No information | Not addressed anywhere in this single-timepoint cross-sectional design. |
| Missing data | No information | No explicit statement of missing exposure/outcome/covariate data among the 60 analyzed infants; the 187-to-60 reduction is addressed above under Selection of participants rather than as missing-data attrition. |
| Measurement of outcomes | Low | Detailed, uniform methods: QIAGEN DNA Stool Mini Kit extraction with a stated modified protocol, Illumina MiSeq 2x300 PE sequencing of named V3-V4/V4-V5 primers performed by an independent commercial laboratory (First Base Laboratories/Apical Scientific), and a defined bioinformatics pipeline (BBDuk, BBMerge, QIIME 1.9, UPARSE, Greengenes). |
| Selection of the reported result | Moderate | No trial/protocol registration; multiple taxa are compared by Welch's t-test across phylum/family/species levels with no explicit multiple-testing correction described, though birth-process and milk-diet comparisons were clearly the a priori primary aims rather than post hoc data-dredging. |

**Microbiome-methods checklist (every study)**

| Domain | Judgment | Reasoning |
|---|---|---|
| Sample collection and storage method reported | Yes | "Fecal samples were collected from diaper, stored in sterile stool containers, and kept at -20degC until extraction." |
| DNA extraction method reported | Yes | "The whole genomic DNA was extracted from approximately 200 mg of fecal samples... using QIAGEN DNA Stool Mini Kit (QIAGEN, Hilden, Germany) with some modifications," with the modified protocol steps given in full. |
| Sequencing depth reported | Yes | "A total of 3,961,263 quality filtered sequence reads were generated... Mean read count was 65,699 per sample with a range of 25,311 to 82,983 reads," with explicit rarefaction thresholds also stated. |
| Negative/positive contamination controls reported | Not reported | No mention anywhere in the available text of negative extraction/PCR controls or positive/mock-community controls. |
| Compositional-data handling reported | No | Analysis uses relative abundance, Bray-Curtis dissimilarity/PCoA, and ANOSIM -- no CLR/ALR/Aitchison/ANCOM compositional-data transform is mentioned anywhere. |

---

## #5430 — Hebei rural village V6-region diet comparison 2013 (China)

*Impact of diet in shaping gut microbiota revealed by a comparative study in infants
during the first six months of life.*
J Microbiol Biotechnol. DOI 10.4014/jmb.1309.09029.

Design: cross-sectional, single rural village in Hebei Province, China, 24 infants
aged 1-6 months divided into breast-fed (n=12), mixed-fed (n=8), and formula-fed (n=4)
groups by Illumina pyrosequencing of the 16S V6 region. Note: this is a distinct
publication (different DOI/authorship ordering) from study #1965, which covers an
apparently related Hebei/Harbin-group Illumina V6 infant-feeding dataset -- assessed
independently here on its own text per the sister-publication convention used
elsewhere in this batch. Severely small and unequal group sizes (12/8/4), with no
sample-size justification given anywhere.

### J. Risk of bias

*Drafted 27 Oct 2026 from a fresh read of `full_text_md/10.4014_jmb.1309.09029/10.4014_jmb.1309.09029.md` in full (Materials and Methods, Results, Discussion).*

| Field | Value |
|---|---|
| RoB tool applicable | **ROBINS-I** (non-randomized, observational cross-sectional cohort) |

**ROBINS-I**

| Domain | Judgment | Reasoning |
|---|---|---|
| Confounding | Serious | No baseline-characteristics comparison table (beyond an unquantified claim of "no significant differences in gestational age and birth weight") and no statistical adjustment of any kind is used in the BF/MF/FF comparisons (simple ANOVA/nonparametric tests only), with cesarean-delivered infants unevenly embedded only within the BF group. |
| Selection of participants | Serious | A convenience sample "from a rural village in Hebei Province" with no described recruitment process, no sample-size justification, and severely unbalanced group sizes (BF=12, MF=8, FF=4). |
| Classification of exposures | Moderate | "Exclusive breast-feeding, formula-feeding, and mixed-feeding were established throughout the research period; no infant received any additional foods," giving a clear exposure definition, but no ascertainment method (e.g., interview, feeding record) is described. |
| Deviations from intended exposures | Low | The text explicitly states that each infant's assigned feeding pattern "was established throughout the research period; no infant received any additional foods," indicating no deviation. |
| Missing data | Low | All 24 enrolled infants have complete sequencing data reported (Table 3 lists read counts for all 24 IDs), with no indication of attrition between enrollment and analysis. |
| Measurement of outcomes | Low | Detailed, uniform methods: QIAamp DNA Stool Mini Kit extraction with a stated modification, named V6-region primers (976F/1046R), Illumina HiSeq 2000 sequencing (BGI-Shenzhen), and explicit per-sample read-depth reporting for all 24 samples. |
| Selection of the reported result | Moderate | No trial/protocol registration; multiple taxa are compared across phylum/family/genus levels with no explicit multiple-testing correction described, though non-significant findings (e.g., richness/diversity comparisons, p>0.05) are reported candidly alongside significant ones rather than selectively. |

**Microbiome-methods checklist (every study)**

| Domain | Judgment | Reasoning |
|---|---|---|
| Sample collection and storage method reported | Yes | "Fecal samples were collected by physicians from each individual in the morning, 1-2 h after the first meal, and preserved in RNAlater (Qiagen) at 4degC for the first 48 h, and then kept at -80degC until extraction." |
| DNA extraction method reported | Yes | "DNA was extracted according to the protocol described by the QIAamp DNA Stool Mini Kit (Qiagen)... the sample was incubated at 95degC for 5 min [to improve lysis]... stored at -20degC until processed." |
| Sequencing depth reported | Yes | "We generated a dataset consisting of 1,760,707 filtered, taxonomic 16S rRNA gene sequences... with a mean average (+/- SE) of 73,360 +/- 486 sequences per sample," with a full per-sample read-count table (Table 3) also given. |
| Negative/positive contamination controls reported | Not reported | No mention anywhere in the available text of negative extraction/PCR controls or positive/mock-community controls. |
| Compositional-data handling reported | No | Analysis uses relative abundance percentages, Chao1/Shannon/Simpson diversity indices, PCA, and hierarchical clustering -- no CLR/ALR/Aitchison/ANCOM compositional-data transform is mentioned anywhere. |

---

## #7095 — CORAL pandemic-lockdown cohort 2024 (Ireland)

*Association between gut microbiota development and allergy in infants born during
pandemic-related social distancing restrictions.*
Allergy. DOI 10.1111/all.16069.

Design: longitudinal prospective observational cohort (CORAL study) of term Irish
infants born March-May 2020 during COVID-19 lockdown, recruited from 2 maternity
hospitals; 360 recruited (354 by 6 months), 351 sequenced at 6 months and 343 at 12
months, with allergy outcomes (atopic dermatitis, skin-prick testing, food allergy)
followed to 24 months. Breastfeeding is one of many simultaneously modeled exposures
(alongside birth mode, siblings, daycare, pets, antibiotics, weaning diet) in a broader
ecological-exposure study design, not a dedicated binary BF-vs-FF comparison; no
explicit operational definition of breastfeeding exclusivity is given.

### J. Risk of bias

*Drafted 27 Oct 2026 from a fresh read of `full_text_md/10.1111_all.16069/10.1111_all.16069.md` in full (Methods: Study outline, Microbiota sampling and sequencing, Bioinformatic processing, Statistical analysis; Results; Discussion/Limitations).*

| Field | Value |
|---|---|
| RoB tool applicable | **ROBINS-I** (non-randomized, prospective observational cohort) |

**ROBINS-I**

| Domain | Judgment | Reasoning |
|---|---|---|
| Confounding | Moderate | Multivariable models (negative binomial GLM, PERMANOVA/envfit) adjust explicitly for siblings, birth mode, age, daycare attendance, and breastfeeding throughout, but the authors themselves candidly acknowledge in the Limitations that "some of the associations may be influenced by collinearity" among the many simultaneously modeled exposures. |
| Selection of participants | Moderate | Explicit eligibility/exclusion criteria (term infants, no pre-birth maternal/co-dwelling SARS-CoV-2, no neonatal IV antibiotics, no multiple births/major congenital anomaly) from 3065 eligible invitees, but only 360 (11.7%) were recruited, and the authors disclose the cohort is representative of the general population "in all aspects other than a higher maternal level of education." |
| Classification of exposures | Moderate | Breastfeeding status ("breastfeeding at enrollment," "current breastfeeding") was collected via repeated online questionnaires, but no explicit operational definition of exclusivity (vs. partial/mixed feeding) is given anywhere in the available text. |
| Deviations from intended exposures | No information | Not addressed anywhere in this purely observational design with self-selected (not assigned) feeding exposure. |
| Missing data | Low | Sample sizes are transparently tracked at each stage (360 recruited -> 354 by 6 months -> 351 sequenced at 6 months -> 343 remaining at 12 months), representing high (~95%) 6-to-12-month retention. |
| Measurement of outcomes | Low | Rigorous, uniform pipeline: Norgen Biotek stool kit with preservative, DNeasy PowerSoil Pro Kit extraction, Illumina MiSeq V3 16S sequencing performed in a single batch (avoiding batch effects), vsearch quality/chimera filtering, and Silva v11 taxonomic annotation. |
| Selection of the reported result | Low | A long-established, previously-published cohort (CORAL, cited prior publications) with FDR correction applied systematically across analyses (e.g., "FDR-corrected p<.0001," "FDR<0.1") and null findings reported candidly alongside significant ones (e.g., "the exposure index was not associated with Clostridia (p=.73) or richness (p=.08) at 12 months"). |

**Microbiome-methods checklist (every study)**

| Domain | Judgment | Reasoning |
|---|---|---|
| Sample collection and storage method reported | Yes | "Fecal samples were collected at home using a stool sampling kit with preservative (Norgen Biotek), at 6 and 12 months of age. Stabilized samples were returned via post and stored at -80degC until analysis." |
| DNA extraction method reported | Yes | "Microbial DNA was isolated using the DNeasy PowerSoil Pro Kit (Qiagen)." |
| Sequencing depth reported | Yes | "MiSeq sequencing of the v3 16S rRNA generated approximately 20,000 reads per sample... All samples were sequenced in one batch." |
| Negative/positive contamination controls reported | Not reported | No mention anywhere in the available text of negative extraction/PCR controls or positive/mock-community controls. |
| Compositional-data handling reported | No | Analysis uses log-transformed relative abundances, PCoA via Pearson correlation distances, and negative binomial GLMs with a read-count offset -- no CLR/ALR/Aitchison/ANCOM compositional-data transform is mentioned anywhere. |

---
