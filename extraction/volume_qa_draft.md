# Quality Assessment (Section J) — volume rollout, Philip's half

Covers Philip's 44 of the 88 post-calibration studies (see `_volume_progress.csv` for the
Philip/Alaa split). Unlike `extraction_pilot_3studies.md` and `20pct_sample_draft.md`, these
entries carry **Section J only** — Sections A-I (full data extraction) are deferred per the
user's 26 Oct 2026 decision to do Quality Assessment first. Each heading still needs enough of
a read to judge RoB soundly even without a formal A-I writeup: design, population, exposure
ascertainment, covariates, and outcome-measurement method are all noted inline in the
reasoning column rather than in a separate table.

Same format as the other two draft files' Section J blocks, so `fill_quality_assessment.py
--draft-md extraction/volume_qa_draft.md` parses it identically.

---

## #35 — van den Munckhof 2026 (Netherlands)

*Maternal influences on infant gut microbiome and health.* Nature. DOI 10.1038/s41586-026-10922-9

Design: prospective cohort (Lifelines NEXT, LLNEXT) -- 714 mother-infant pairs, 2,939 infant
faecal samples across 10 longitudinal timepoints (2 weeks to 12 months), shotgun metagenomics.
One of the largest and most methodologically rigorous studies in the full 111-study corpus.

### J. Risk of bias

*Drafted 26 Oct 2026 from a fresh read of `full_text_md/10.1038_s41586-026-10922-9/10.1038_s41586-026-10922-9.md`'s Methods section (Study design, Predictors, Sample collection, Microbiome processing and profiling).*

| Field | Value |
|---|---|
| RoB tool applicable | **ROBINS-I** (prospective cohort design) |

**ROBINS-I**

| Domain | Judgment | Reasoning |
|---|---|---|
| Confounding | Low | Among the most rigorous confounding-control approaches in this entire review: 316 cross-sectional and 158 longitudinal predictors were systematically collected, and every microbiome-association model used a base/extended/final-model structure explicitly adjusting for technical covariates (read depth, DNA concentration, batch) plus delivery mode and feeding mode in sequence, rather than a single unadjusted comparison. |
| Selection of participants | Low | "The present study included the first 714 mother-infant pairs recruited between 2016 and 2019" from the much larger Lifelines population cohort -- consecutive/sequential recruitment rather than a selected convenience sample, drawn from a well-characterized 167,729-person parent cohort. |
| Classification of exposures | Low | Feeding mode at birth was obtained from medical birth cards; feeding mode after birth was tracked longitudinally via repeated FFQs, with an explicit, transparently documented imputation rule for missing feeding-mode timepoints based on adjacent-timepoint combinations -- one of the more rigorous, prospectively-recorded exposure ascertainment protocols in this review. |
| Deviations from intended exposures | Low | Purely observational cohort with no assigned intervention; feeding mode is tracked as a naturally occurring, longitudinally measured exposure. |
| Missing data | Moderate | Real longitudinal attrition is present and quantified (e.g., exclusive-BF/FF sample sizes shift substantially across the 7 infant timepoints, and the average infant contributed only ~4 of up to 10 possible samples), but it is explicitly characterized and handled with mixed models (random effects, FDR correction) and methods tolerant of missing timepoints (e.g., MOFA factor analysis) rather than naive complete-case analysis. |
| Measurement of outcomes | Low | State-of-the-art, published, versioned shotgun-metagenomics pipeline (BBDuk adapter trimming, KneadData/Bowtie2 host-read removal, MetaPhlAn4, HUMAnN3, StrainPhlAn4) applied uniformly and objectively, blind to feeding-group status by nature of the lab/bioinformatic workflow. |
| Selection of the reported result | Low | No trial registration applicable (observational cohort); despite testing hundreds of predictor-outcome associations, Benjamini-Hochberg FDR correction is applied systematically throughout every analysis, and reported predictive performance is presented without over-claiming (eczema-prediction AUCs of 0.74/0.68/0.73, not inflated). |

**Microbiome-methods checklist (every study)**

| Domain | Judgment | Reasoning |
|---|---|---|
| Sample collection and storage method reported | Yes | "Parents used stool collection kits provided by the UMCG and froze the faecal samples at home at -20degC within 10 min of stool production... stored in -20degC (short-term) or -80degC (long-term) freezer until DNA extraction." |
| DNA extraction method reported | Yes | "Microbial DNA was isolated from 0.2-0.5 g faecal material using the QIAamp Fast DNA Stool Mini Kit (Qiagen) and the QIAcube (Qiagen), according to the manufacturer's instructions... DNA eluates were stored at -20degC." |
| Sequencing depth reported | Yes | "Sequencing depth" is explicitly measured per sample and used as a named technical covariate in every statistical model throughout the paper (alongside DNA concentration and batch number); ultra-deep sequencing depth is explicitly quantified for the milk/vaginal subsamples ("40 gigabases per sample"). |
| Negative/positive contamination controls reported | Not reported | The only contamination-related step described is computational host-DNA removal (Bowtie2 alignment to GRCh38/hg38) -- a bioinformatic QC step, not a laboratory negative (blank/reagent) or positive (mock-community) sequencing control; no such lab control is mentioned anywhere in the available text. |
| Compositional-data handling reported | Yes | Explicit, detailed CLR transformation applied at the SGB level and higher taxonomic levels throughout ("CLR transformation was then applied... using the geometric mean of the relative abundance of microbial species as the CLR denominator. As CLR transformation cannot be applied to zero values, zeros were adjusted by adding half of the lowest non-zero value"), plus ALR transformation (with documented zero-handling) for MetaCyc pathways, GBMs, and CAZymes -- a textbook compositional-data-aware approach. |

---

## #116 — Brockway/Dai 2026 (Canada, replication in Denmark)

*Breastfeeding may lessen socioeconomic disparities in child health through differences in the
infant gut microbiome.* Cell Reports Medicine. DOI 10.1016/j.xcrm.2026.102755

Design: prospective cohort (CHILD Study, Canada, n=1,479 with microbiome data; replicated in
the independent COPSAC2010 Danish cohort), shotgun metagenomics. Primary research question is
socioeconomic status (SES), with breastfeeding analyzed as a key mediator/exposure.

### J. Risk of bias

*Drafted 26 Oct 2026 from a fresh read of `full_text_md/10.1016_j.xcrm.2026.102755/10.1016_j.xcrm.2026.102755.md`'s STAR Methods (Experimental model, Method details, Quantification and statistical analysis). Checklist judgments are for the CHILD cohort specifically (the primary cohort this review's comparison is drawn from) -- its own sample-collection protocol is deferred to a cited prior publication (Dai et al.) and not restated in this paper's own text, distinct from the independently-described COPSAC2010 replication-cohort protocol.*

| Field | Value |
|---|---|
| RoB tool applicable | **ROBINS-I** (prospective cohort design) |

**ROBINS-I**

| Domain | Judgment | Reasoning |
|---|---|---|
| Confounding | Low | Extensive, systematic covariate adjustment throughout: all microbiome models adjust for stool collection age, processing/shipment time, and study-center strata; the main multi-factor PERMANOVA models breastfeeding alongside 35 other perinatal factors simultaneously (yielding an adjusted partial R2 for breastfeeding specifically); sensitivity analyses additionally adjust for genetic-ancestry principal components. |
| Selection of participants | Moderate | Transparent recruitment flow is given (3,263 eligible families in the general CHILD cohort -> 2,752 with complete SES data -> 1,479 with usable 3-month/1-year microbiome data), but the reduction is substantial, and the authors candidly acknowledge in their Limitations that "the CHILD Study skews toward urban families with higher income and education." |
| Classification of exposures | Moderate | Breastfeeding status is defined with a clear binary rule (actively breastfeeding at the time of stool sample collection vs. never breastfed or stopped by the 3-month visit), but ascertainment method (prospective record vs. questionnaire recall) is not described in further detail in the available text. |
| Deviations from intended exposures | Low | Purely observational cohort design with no intervention to deviate from. |
| Missing data | Moderate | Substantial group-size imbalance exists between BF and No-BF groups at both timepoints (e.g., 3-month n=1,001 BF vs. 159 No-BF), and the authors explicitly flag in their Limitations that "the proportion of missing data for some health outcomes was modestly associated with SES... which could potentially introduce bias" -- a candid acknowledgment of a plausible non-random missingness pattern. |
| Measurement of outcomes | Low | Objective, vendor-generated (Diversigen) shotgun-metagenomics pipeline (bioBakery3/MetaPhlAn4/HUMAnN3) applied uniformly and blind to feeding status; the primary findings are independently replicated in a second cohort (COPSAC2010) using a comparable pipeline, strengthening confidence in the measurement's robustness. |
| Selection of the reported result | Low | No trial registration applicable (observational cohort); the study's central design feature is confirmatory replication of its primary claims in an independent cohort (COPSAC2010), FDR correction is applied systematically throughout, and candid limitations are reported (urban/high-SES recruitment skew, SES-linked missingness, non-independence of the SES and breastfeeding effect estimates) rather than an overstated narrative. |

**Microbiome-methods checklist (every study)**

| Domain | Judgment | Reasoning |
|---|---|---|
| Sample collection and storage method reported | Not reported | CHILD cohort stool samples are cited to a prior publication ("Stool samples \| Dai, D.L.Y. et al." in the REAGENT/RESOURCE table) rather than described in this paper's own Methods text; only the independent COPSAC2010 replication cohort's collection/storage protocol ("mixed on arrival with 1 mL of 10% (v/v) glycerol broth... frozen at -80degC") is given directly. |
| DNA extraction method reported | Yes | "DNA was extracted from fecal samples using the MO Bio PowerSoil Pro with bead beating in 0.1mm glass bead plates" (CHILD cohort, METHOD DETAILS). |
| Sequencing depth reported | Yes | "In CHILD cohort, shotgun metagenomic sequencing data with an average depth of 5 million reads per sample was generated by Diversigen... only samples with at least 100,000 remaining reads or more were retained for downstream analysis." |
| Negative/positive contamination controls reported | Not reported | No mention anywhere in the available text of negative extraction/PCR controls or positive/mock-community sequencing controls for either cohort; only computational host-read removal (Bowtie2, for the COPSAC pipeline) is described, which is a bioinformatic QC step rather than a laboratory contamination control. |
| Compositional-data handling reported | Yes | "Aitchison's distance (''vegan'') was calculated on the modified centered log-ratio (mCLR)-transformed... relative abundance of species," with the zero-handling approach explicitly described ("mCLR transform applies central log transformation to non-zero values and adds a pseudocount of the minimal value... previous exact zero relative abundance entries... remained zero") -- used consistently for both diversity metrics and the MaAsLin2 differential-abundance models. |

---

## #131 — Korean combined birth cohort study 2025 (South Korea)

*Effects of feeding type on gut microbiota and atopic dermatitis in cesarean delivered infants:
a combined birth cohort study.* Maternal-Fetal Medicine / J. Korean Med Sci family journal.
DOI 10.1007/s44463-025-00040-x

Design: retrospective secondary analysis pooling cesarean-delivered infants (n=129) from three
separate Korean prospective birth cohorts, 3-arm feeding comparison: Group A exclusively
breastfed (n=12), Group B standard formula (n=94), Group C probiotic-fortified formula (n=23,
Lotte Wellfood-supplied, not exclusively breastfed).

### J. Risk of bias

*Drafted 26 Oct 2026 from a fresh read of `full_text_md/10.1007_s44463-025-00040-x/10.1007_s44463-025-00040-x.md`'s Materials and methods / Results.*

| Field | Value |
|---|---|
| RoB tool applicable | **ROBINS-I** (non-randomized, retrospective secondary analysis of pooled observational cohort data) |

**ROBINS-I**

| Domain | Judgment | Reasoning |
|---|---|---|
| Confounding | Moderate | A baseline-characteristics table shows no significant between-group differences on sex, gestational age, birth weight, family history of allergic disease, maternal education, household mold, or tobacco exposure, but none of these are entered as statistical covariates in the composition comparisons (simple Kruskal-Wallis/Chi-square tests), and since the three feeding groups are pooled from three separately designed original cohorts (general-population, allergy-risk-stratified, and cesarean-specific), cohort-of-origin itself is a plausible unaddressed confounder not discussed in the available text. |
| Selection of participants | Moderate | Clear inclusion criteria are stated (cesarean delivery, stool sample at 1-2 months, 6-month follow-up completion, family history of allergic disease; antibiotic-treated infants excluded), but this is a retrospective pooling of three differently-designed original cohorts with starkly uneven realized group sizes (12/94/23) and no discussion of how many eligible infants from each original cohort were excluded. |
| Classification of exposures | Moderate | Groups are clearly and mutually-exclusively defined by feeding type (exclusive breastfeeding / standard formula / probiotic-fortified formula), but the ascertainment method (prospective record vs. caregiver report) is not described in the available text. |
| Deviations from intended exposures | Low | Observational design with no randomized intervention; feeding type reflects each family's actual feeding choice. |
| Missing data | No information | No recruitment-flow detail is given for any of the three original cohorts (how many eligible infants were screened, excluded, or lost before reaching the final N=129) -- only the final per-group counts are reported. |
| Measurement of outcomes | Serious | Two materially different sequencing technologies and bioinformatic pipelines were used depending on which original cohort a sample came from -- 16S V3-V4 on Illumina MiSeq/QIIME1.9.1/Greengenes for "a subset of participants" vs. full-length 16S-ITS-23S on Oxford Nanopore MinION/MIrROR for "the remaining samples" -- with no discussion of whether feeding groups were evenly distributed across these two measurement platforms; if platform assignment tracks cohort-of-origin (and feeding-group composition differs by cohort-of-origin, which the Confounding domain above already flags as plausible), this is a real, undiscussed batch-effect risk that could masquerade as a feeding-type difference. |
| Selection of the reported result | Moderate | No trial registration applicable; the headline atopic-dermatitis finding is reported plainly as non-significant despite a large descriptive spread (8.3% vs. 66.7% vs. 25.0%, p=0.793) rather than being spun, which is reassuring, but this is a retrospective secondary analysis repurposing pre-existing cohort data for a comparison not necessarily part of any original pre-specified design, which carries an inherent (if here unevidenced) added risk of post-hoc outcome selection. |

**Microbiome-methods checklist (every study)**

| Domain | Judgment | Reasoning |
|---|---|---|
| Sample collection and storage method reported | Yes | "Fecal samples were collected by caregivers using a stool collection kit capable of preserving at room temperature for up to 8 weeks. Once the study team was notified, samples were promptly delivered to the research facility... and immediately stored at -80degC upon arrival." |
| DNA extraction method reported | Not reported | The methods move directly from sample storage to amplification/sequencing ("the hypervariable V3-V4 regions of the 16S rRNA gene were amplified and sequenced...") with no DNA extraction kit or protocol named anywhere in the available text. |
| Sequencing depth reported | Not reported | No read-count or depth figure found anywhere in the available text for either sequencing platform used. |
| Negative/positive contamination controls reported | Not reported | No mention anywhere in the available text of negative extraction/PCR controls or positive/mock-community controls. |
| Compositional-data handling reported | No | "Relative abundance" is used throughout as the stated basis for all taxonomic comparisons (phylum and genus level), with no compositional-aware transform (e.g., CLR/log-ratio) mentioned anywhere -- a directly observable plain-relative-abundance approach. |

---

## #150 — Zhong 2025 (China)

*Impact of medium- and long-chain triacylglycerols and sn-2 palmitate on temperament
development in term infants: potential role of gut Bifidobacterium.* Food Funct.
DOI 10.1039/d5fo03451e

Design: companion paper to #128 (same trial, ClinicalTrials.gov NCT05295030, Sun Yat-sen
University) -- open-label parallel RCT between two formula arms (IG: MLCT+sn-2 palmitate;
CG: control formula) plus a non-randomized breastfed reference group (BG), routed to
ROBINS-I per the hybrid-design rule for the BF-vs-formula comparison this review extracts.
Unlike #128 (lipidomics-only), this paper reports full alpha/beta diversity and genus-level
composition data.

### J. Risk of bias

*Drafted 26 Oct 2026 from a fresh read of `full_text_md/10.1039_d5fo03451e/10.1039_d5fo03451e.md`'s Methods and Results (Participant characteristics).*

| Field | Value |
|---|---|
| RoB tool applicable | **ROBINS-I** (non-randomized intervention for the BF-vs-formula comparison, per the hybrid-design rule) |

**ROBINS-I**

| Domain | Judgment | Reasoning |
|---|---|---|
| Confounding | Low | An exemplary case: the baseline table explicitly identifies imbalances in gestational age, mode of delivery, and maternal education across the three groups, and all three are then explicitly entered as covariates (alongside infant sex and weight-for-age-z-score change) in every reported statistical model, both for temperament outcomes and for genus-level abundance changes. |
| Selection of participants | Low | A full CONSORT flow diagram is reported: 330 eligible infants -> 179 enrolled (IG 65/CG 48/BG 66) -> specific, individually-counted stool-sample exclusions (diarrhea, antibiotic use, probiotic use) at both baseline and endpoint -> 327 of 354 collected stool samples retained for analysis -- one of the most transparent recruitment-and-exclusion accountings in this review. |
| Classification of exposures | Low | BF defined as exclusive breastfeeding from birth; formula-arm inclusion required objectively verified consumption of >=80% of age-specific recommended daily intake on three consecutive days, with "parents agreeing to maintain this feeding pattern throughout the study" -- a rigorous, prospectively verified ascertainment. |
| Deviations from intended exposures | Low | Infants failing the adherence threshold or developing diarrhea/requiring antibiotics/probiotics were identified and excluded from the relevant analysis (see Selection of participants) rather than analyzed as-assigned regardless, minimizing deviation-driven bias. |
| Missing data | Low | Losses are small, specifically enumerated, and attributable to protocol-consistent clinical reasons (diarrhea, antibiotic/probiotic use) rather than unexplained attrition -- 327 of 354 stool samples (92%) and 177 of 179 participants (99%) retained for their respective analyses. |
| Measurement of outcomes | Low | Detailed, objective 16S pipeline (FastPure Stool DNA kit, Illumina NextSeq 2000, fastp/FLASH/DADA2/QIIME2, SILVA 138) applied uniformly; explicit rarefaction to a fixed depth (228,471 sequences, average Good's coverage 97.90%) specifically to prevent sequencing-depth differences from confounding the diversity comparisons. |
| Selection of the reported result | Low | Pre-registered (ClinicalTrials.gov NCT05295030); null and non-significant findings are reported as plainly as significant ones (e.g., no significant IG-vs-CG difference in Shannon/Chao indices, no baseline difference in *Bifidobacterium*/*Blautia* abundance, no significant weighted-UniFrac separation at all), with no evident selective emphasis. |

**Microbiome-methods checklist (every study)**

| Domain | Judgment | Reasoning |
|---|---|---|
| Sample collection and storage method reported | Yes | "Stool samples were collected at both the baseline and endpoint visits... placed in sterile tubes containing a DNA stabilizing solution and stored at -20degC at the participants' homes. All samples were promptly transported to the laboratory and stored at -80degC for subsequent 16S rRNA amplicon sequencing." |
| DNA extraction method reported | Yes | "Stool samples were processed to extract total microbial genomic DNA using the FastPure Stool DNA Isolation Kit (MJYH, Shanghai, China), following the instructions provided by the manufacturer." |
| Sequencing depth reported | Yes | "To reduce the impact of sequencing depth on both alpha and beta diversity measures, sequences from each sample were rarefied to 228,471, which resulted in an average Good's coverage of 97.90%." |
| Negative/positive contamination controls reported | Not reported | No mention anywhere in the available text of negative extraction/PCR controls or positive/mock-community controls. |
| Compositional-data handling reported | No | "Relative abundance" is used throughout (genus-level comparisons, Table S2, Fig. 3) as the stated basis for all taxonomic results, with no compositional-aware transform (e.g., CLR/log-ratio) mentioned anywhere. |

---

## #182 — Lactoferrin-formula real-world study 2025 (China)

*Associations of Lactoferrin-Fortified Formula with Infant Growth and Gut Microbiota: A
Real-World Observational Study.* Nutrients. DOI 10.3390/nu17243896

Design: real-world observational study, 3-arm hybrid online/clinic recruitment (LF
lactoferrin-fortified formula / CF control formula / BF exclusively breastfed), with formal
propensity-score matching (PSM) applied to the growth-outcome analysis. The 81-infant
microbiome subsample (LF 26/CF 30/BF 25) is explicitly drawn from the **pre-PSM** population.

### J. Risk of bias

*Drafted 26 Oct 2026 from a fresh read of `full_text_md/10.3390_nu17243896/10.3390_nu17243896.md`'s Materials and Methods (2.1-2.8) and Results (3.1, 3.4).*

| Field | Value |
|---|---|
| RoB tool applicable | **ROBINS-I** (fully observational real-world study; no randomized component in any arm) |

**ROBINS-I**

| Domain | Judgment | Reasoning |
|---|---|---|
| Confounding | Moderate | The paper's growth-outcome analysis uses sophisticated confounding control (PSM with 1:1:1 nearest-neighbor matching and Mahalanobis-distance optimization, validated via SMD<0.1, plus a two-tier multivariable regression adjusting for up to 10 maternal/obstetric covariates), but the Methods explicitly state the 81-infant microbiome subsample was drawn from the **pre-PSM** population ("within the pre-PSM population, we additionally collected fecal samples from 81 infants"), meaning the rigorous matching apparatus built for this study may not extend to the composition outcomes this review actually extracts. |
| Selection of participants | Low | An unusually transparent, fully numerically accounted recruitment flow: 584 initially enrolled -> 236 qualified pre-PSM, with each attrition reason individually counted (non-consent n=2, failed questionnaire attention-checks n=119, age>12 months n=120, implausible physical data n=88, implausible age data n=19). |
| Classification of exposures | Moderate | Feeding groups are clearly defined (LF/CF exclusively fed from day 15; BF exclusively breastfed for the first 4 months) and "verified" at enrollment, but ascertainment relies on caregiver self-report and transcription from the Infant Health Handbook via an online questionnaire rather than a prospective daily record. |
| Deviations from intended exposures | Low | "Mixed feeding during the intervention period" was an explicit exclusion criterion, so infants who deviated from their assigned exclusive-feeding category were screened out rather than analyzed as originally assigned. |
| Missing data | Low | Every exclusion at every stage is individually enumerated with a specific, plausible reason (see Selection of participants) -- one of the most transparent accountings of missingness in this review. |
| Measurement of outcomes | Low | Rigorous, detailed, objective pipeline (QIIME2/DADA2/SILVA 138.1) with explicit sequencing-depth reporting and rarefaction, and "all samples were processed in a single batch to minimize technical batch effects." |
| Selection of the reported result | Low | No trial registration applicable (observational RWE study); comprehensive multi-level taxonomic reporting (phylum/genus/species) plus functional (PICRUSt2) analysis, and LEfSe was run at a notably conservative LDA threshold (>4, stricter than this review's more commonly seen LDA>2 cutoff), reducing false-positive differential-taxa risk rather than loosening it to find more "significant" results. |

**Microbiome-methods checklist (every study)**

| Domain | Judgment | Reasoning |
|---|---|---|
| Sample collection and storage method reported | Yes | "Fecal samples were collected in sterile specimen tubes, immediately flash-frozen in liquid nitrogen, and stored at -80degC until analysis." |
| DNA extraction method reported | Not reported | Only a generic statement is given ("Microbial DNA was extracted from the fecal samples") with no kit, reagent, or protocol named in the main text; detail is deferred to "Section C of the Supplementary Materials," not available here. |
| Sequencing depth reported | Yes | "An average sequencing depth of 37.33 million high-quality bases per sample (range: 21.14 to 58.66 million)... an average of 90,019 quality-filtered, non-chimeric reads retained per sample... rarefied to a uniform depth of 46,873 sequences per sample." |
| Negative/positive contamination controls reported | Not reported | No mention anywhere in the available text of negative extraction/PCR controls or positive/mock-community controls. |
| Compositional-data handling reported | No | "Relative abundance" is used throughout (phylum/genus/species-level results, Figure 3) as the stated basis for all taxonomic comparisons, with no compositional-aware transform (e.g., CLR/log-ratio) mentioned anywhere. |

---

## #291 — Capeding/HMO-synbiotic formula trial 2025 (Belgium/France/Germany/Spain)

*Partially hydrolyzed, whey-based infant formula with six human milk oligosaccharides, B.
infantis LMG11588, and B. lactis CNCM I-3446 is safe, well tolerated, and improves gut health:
a staged analysis of a randomized trial.* Front Nutr. DOI 10.3389/fnut.2025.1628847

Design: large (n=313 FAS), 18-center, double-blind RCT between two formula arms (SYN:
HMO+probiotic-supplemented vs. CTRL) with a non-randomized BF reference group -- routed to
ROBINS-I per the hybrid-design rule for the BF-vs-formula comparison. One of the most
methodologically rigorous studies in this review (formal ITT/FAS/PP/SAS analysis populations,
inverse-probability-of-treatment weighting for the BF arm, LinDA compositional-bias
correction).

### J. Risk of bias

*Drafted 26 Oct 2026 from a fresh read of `full_text_md/10.3389_fnut.2025.1628847/10.3389_fnut.2025.1628847.md`'s Participants and methods (2.1-2.16) and Results (3.1-3.2).*

| Field | Value |
|---|---|
| RoB tool applicable | **ROBINS-I** (per the hybrid-design rule: non-randomized BF reference group alongside a randomized SYN-vs-CTRL comparison) |

**ROBINS-I**

| Domain | Judgment | Reasoning |
|---|---|---|
| Confounding | Low | Explicitly handled with inverse probability of treatment weighting (IPTW) "due to the non-randomized nature of the BF arm," with the propensity model incorporating mother's age, delivery method, parental education, household size, smoking status (pregnancy and current), country, and study center -- directly targeting the real baseline imbalances the paper's own Table 2 documents (BF infants significantly older, more educated mothers, lower cesarean rate). All models are additionally adjusted for study center and baseline value. |
| Selection of participants | Low | Full, CONSORT-compliant, numerically detailed recruitment and analysis-population flow across 18 centers in 4 countries (318 screened/enrolled -> 313 FAS -> 227 PP -> 314 SAS), with specific, individually stated exclusion reasons at each step. |
| Classification of exposures | Low | BF required a priori parental intent to continue exclusive breastfeeding through at least 4 months; formula-fed infants required exclusive, tolerated cow's-milk-formula consumption with parents having independently decided against breastfeeding before enrollment; ongoing compliance (>=80% of days on assigned formula/breastmilk) was tracked and used to define the per-protocol population. |
| Deviations from intended exposures | Low | A formal per-protocol population excludes major deviations (non-compliance, concomitant foods, visit-window violations), and a further "sub-PP" sensitivity population additionally excludes prebiotic/probiotic supplement use and any SYN/CTRL infants who also consumed breast milk -- among the most careful deviation-handling protocols in this review. |
| Missing data | Low | 318 enrolled infants -> 258 completing through 4 months (79-84% retention by arm), with explicit, well-characterized ITT/FAS/PP/SAS analysis populations defined specifically to handle different missingness/deviation scenarios appropriately rather than a single undifferentiated analysis set. |
| Measurement of outcomes | Low | Objective, centrally processed shotgun-metagenomics pipeline (NucleoSpin Stool kit DNA extraction, NovaSeq sequencing, CHAMP pipeline) applied uniformly and blind to feeding-group assignment. |
| Selection of the reported result | Low | Pre-registered (ClinicalTrials.gov NCT04962594), CONSORT-checklist-compliant, with formal pre-specified sample-size/power calculations for both the primary (weight-gain) and key secondary (*Bifidobacterium* abundance) endpoints, and Benjamini-Hochberg correction applied to all pairwise group comparisons. |

**Microbiome-methods checklist (every study)**

| Domain | Judgment | Reasoning |
|---|---|---|
| Sample collection and storage method reported | Yes | "Fecal samples were collected at home by the parents using a feces tube with an integrated spatula and without any buffers or additives, frozen in the home freezer (-20degC)... kept frozen at the site at -80degC until transferred every 3-4 months to the central lab for analysis." |
| DNA extraction method reported | Yes | "DNA was extracted from the fecal samples using the NucleoSpin Stool kit (Machery-Nagel) with bead beating at 2700 rpm for 5 min." |
| Sequencing depth reported | Not reported | No read-count or depth figure found anywhere in the available text. |
| Negative/positive contamination controls reported | Not reported | No mention anywhere in the available text of negative extraction/PCR controls or positive/mock-community controls (only computational "adapter and host DNA removal" is described, a bioinformatic QC step rather than a laboratory contamination control). |
| Compositional-data handling reported | Yes | "Microbiome differences... were compared using models... employing a linear regression framework with log-transformed relative abundances and a compositional bias correction based on LinDA" -- an explicitly named, compositional-aware differential-abundance method. |

---

## #324 — Jarman/Torres 2025 (United States)

*Bifidobacterium deficit in United States infants drives prevalent gut dysbiosis.* Commun Biol.
DOI 10.1038/s42003-025-08274-7

Design: cross-sectional (My Baby Biome study, NCT05472688), n=412, decentralized nationwide
US cohort recruited via social media, shotgun metagenomics at 1-3 months of age.

### J. Risk of bias

*Drafted 26 Oct 2026 from a fresh read of `full_text_md/10.1038_s42003-025-08274-7/10.1038_s42003-025-08274-7.md`'s Results (Taxonomic analysis) and Methods (Study population, Stool collection, Sequencing, Microbial classification, Statistics).*

| Field | Value |
|---|---|
| RoB tool applicable | **ROBINS-I** (cross-sectional observational design) |

**ROBINS-I**

| Domain | Judgment | Reasoning |
|---|---|---|
| Confounding | Low | The authors identified that DNA collection/isolation method (raw fecal vs. DNA/RNA Shield tube) significantly affected microbial composition (PERMANOVA p=0.02) and explicitly adjusted for this technical confound in all subsequent models; the key breastfed-vs-non-breastfed comparison (Fig. 1E) is further adjusted for birth mode via ANCOVA. |
| Selection of participants | Moderate | A decentralized, social-media-recruited nationwide cohort was deliberately curated for demographic representativeness ("racial and ethnic diversity comparable to the United States as well as representative levels of birth and feeding modes," cross-checked against CDC data) -- a genuine strength -- but the design is inherently self-selected (opt-in via social media) and no response/completion rate from initial consent to the final n=412 sample is given. |
| Classification of exposures | Moderate | Feeding method (strictly breastfed / strictly formula-fed / combination-fed) is ascertained via "an in-depth questionnaire at the time of stool collection" -- a single cross-sectional parental report rather than a prospective daily record. |
| Deviations from intended exposures | Low | Cross-sectional observational design with no intervention to deviate from. |
| Missing data | No information | No recruitment-flow detail is given (how many caregivers consented, how many kits were returned, how many samples failed QC) -- only the final analytic N=412 is reported. |
| Measurement of outcomes | Low | A custom Kraken2/Bracken taxonomic classifier was built and explicitly validated using simulated mock communities, with a quantified classification-noise floor (0.5%) used as the detection threshold -- an unusually rigorous and transparent measurement-validation approach. |
| Selection of the reported result | Low | Formally registered (NCT05472688) with Benjamini-Hochberg FDR correction applied throughout; the paper reports a counter-intuitive finding (breastfeeding associated with *decreased* infant *Bifidobacterium* specifically in cesarean-born infants, opposite the expected direction) rather than only the anticipated effect, a good-faith transparency signal. |

**Microbiome-methods checklist (every study)**

| Domain | Judgment | Reasoning |
|---|---|---|
| Sample collection and storage method reported | Yes | "Fecal samples were collected at home with stool sampling kits that contained Covidien Precision Stool Collector cups and spoons, ice packs to keep the sample cool, and a DNA/RNA Shield Fecal Collection Tube... Aliquots were labeled and frozen at -80degC for long-term storage." |
| DNA extraction method reported | Yes | "Total genomic DNA was extracted from a fecal PBS aliquot using the MagAttract PowerMicrobiome DNA/RNA kit (Qiagen)... For samples obtained from DNA/RNA Shield Fecal Collection Tubes, the DNA was extracted and purified using the Zymobiomics DNA Miniprep Kit." |
| Sequencing depth reported | Not reported | No read-count or depth figure found anywhere in the available text. |
| Negative/positive contamination controls reported | Yes | "Mock communities were simulated to validate this classification method, demonstrating increased accuracy at the subspecies level compared to the standard GTDB classification. The classification noise for this custom classifier was measured to be 0.5%." |
| Compositional-data handling reported | Yes | "The centered log-ratio (CLR) transformation was applied to species relative abundance after imputation of zero values using multiplicative replacement" -- an explicit, properly zero-handled compositional transform. |

---

## #359 — sn-2 palmitate metagenomic trial 2025 (China)

*Role of sn-2 palmitate on the development of the infant gut microbiome: A metagenomic
insight.* Food Research International. DOI 10.1016/j.foodres.2025.116488

Design: double-blind RCT between two formula arms (investigational high-sn-2-palmitate vs.
control) plus a non-randomized breastfed reference group, ClinicalTrials.gov NCT04013087 --
routed to ROBINS-I per the hybrid-design rule. **Notable limitation: 450 infants enrolled
(300 formula + 150 BF) but only 92 completed the full study duration**, with no stated reasons
or per-group breakdown anywhere in the available text.

### J. Risk of bias

*Drafted 26 Oct 2026 from a fresh read of `full_text_md/10.1016_j.foodres.2025.116488/10.1016_j.foodres.2025.116488.md`'s Materials and methods (2.1-2.3) and Results (3.1).*

| Field | Value |
|---|---|
| RoB tool applicable | **ROBINS-I** (non-randomized BF reference group per the hybrid-design rule) |

**ROBINS-I**

| Domain | Judgment | Reasoning |
|---|---|---|
| Confounding | Moderate | "No significant differences were observed in demographic or clinical characteristics among the three groups" (Table S1), but it is unclear whether this balance check was performed on the original 450 enrollees or only the 92 completers, and no statistical covariate adjustment is applied in any of the composition/diversity comparisons (simple group comparisons only). |
| Selection of participants | Serious | Of 450 infants enrolled (300 formula-fed, 150 breastfed), only 92 "completed the full study duration" -- a ~80% loss with no stated reasons, no per-group breakdown, and no discussion of whether completion was related to feeding tolerance or other factors that could plausibly also relate to the microbiome outcome. |
| Classification of exposures | Low | Investigational/control formula groups are randomized and blinded; BF is clearly defined as exclusive breastfeeding with mothers "predetermined not to breastfeed" for the formula arms -- standard, reasonably rigorous RCT-grade ascertainment. |
| Deviations from intended exposures | Moderate | No per-protocol vs. intention-to-treat distinction is described, and the extreme, unexplained attrition (see Selection of participants) could itself partly reflect undocumented non-adherence or withdrawal, though no direct evidence of a differential co-intervention is present either. |
| Missing data | Serious | The same ~80% loss from enrollment (n=450) to final analysis (n=92) applies here directly -- one of the largest, least-explained attrition rates in this entire review's sample. |
| Measurement of outcomes | Low | Objective, standard shotgun-metagenomics pipeline (MetaPhlAn4 taxonomic profiling, Illumina NovaSeq, an established published protocol) applied uniformly across groups. |
| Selection of the reported result | Moderate | Pre-registered (NCT04013087), and null findings are reported plainly (e.g., "no significant differences... in microbial community structure between groups"), which is reassuring against overt cherry-picking of results -- but the severe, unexplained attrition raises a real question of whether the reported findings reflect a representative subset of the originally enrolled population. |

**Microbiome-methods checklist (every study)**

| Domain | Judgment | Reasoning |
|---|---|---|
| Sample collection and storage method reported | Yes | "Immediately after collection, fecal samples were stored at -20degC and transported to the laboratory where the samples were dispensed into individual centrifuge tubes and then frozen at -80degC for subsequent analysis." |
| DNA extraction method reported | Yes | "Fecal DNA was extracted using the Fast DNA Spin Kit for feces (MP Biomedicals), with quantity and quality assessed via NanoDrop2000 spectrophotometer." |
| Sequencing depth reported | Not reported | No read-count or depth figure found anywhere in the available text. |
| Negative/positive contamination controls reported | Not reported | No mention anywhere in the available text of negative extraction/PCR controls or positive/mock-community controls. |
| Compositional-data handling reported | No | "Relative abundance" is used throughout (e.g., "species which average relative abundance above 0.1%," "representing over 60% of total relative abundance") as the stated basis for all taxonomic results, with no compositional-aware transform mentioned anywhere. |

---

## #413 — AIMS cohort B. longum study 2025 (Netherlands, pooled with 4 public datasets)

*Priority effects, nutrition and milk glycan-metabolic potential drive Bifidobacterium longum
subspecies dynamics in the infant gut microbiome.* PeerJ. DOI 10.7717/peerj.18602

Design: prospective cohort (Amsterdam Infant Microbiome Study, AIMS; n=24 mother-infant
pairs), shotgun metagenomics, pooled with four external public metagenomic datasets
(Chu 2017, Ferretti 2018, Shao 2019, Yassour 2018) for a combined n=125-sample analysis.
Milk-feeding type is one of several candidate predictors tested via LASSO feature selection
for *B. longum* (sub)species abundance, alongside maternal/temporal and HMO-utilization-
potential features -- a narrower, more specialized design than most studies in this review.

### J. Risk of bias

*Drafted 26 Oct 2026 from a fresh read of `full_text_md/10.7717_peerj.18602/10.7717_peerj.18602.md`'s Material and methods (cohort, sample collection, DNA extraction/sequencing, public data acquisition, modeling).*

| Field | Value |
|---|---|
| RoB tool applicable | **ROBINS-I** (prospective cohort design) |

**ROBINS-I**

| Domain | Judgment | Reasoning |
|---|---|---|
| Confounding | Moderate | A sophisticated LASSO feature-selection approach jointly models maternal/temporal effects, nutrition, and HMO-utilization-potential features together, which implicitly nets out confounding among included candidates -- but the pooled public datasets differ substantially in protocol and quality (MAG QC failure rate 27% for AIMS vs. an average 69% for the public datasets) and in exact sampling age (21-40 days vs. AIMS' ~1 month), with no explicit cohort-of-origin covariate included to address this heterogeneity. |
| Selection of participants | Moderate | AIMS recruitment criteria are only generally described (pregnant women in Amsterdam districts, mid-pregnancy recruitment, no stated exclusion criteria), the AIMS analytic sample is very small (24 pairs, 72 samples), and the public-dataset portion is a post-hoc curated combination selected by matching criteria (vaginal delivery, full-term, healthy, no antibiotics, ~1 month age) rather than a single coherent sampling frame. |
| Classification of exposures | Moderate | Milk-feeding type/frequency for AIMS was collected via "validated questionnaires," but the ascertainment method is not restated for the pooled public-dataset samples, which rely on each original study's own (undescribed here) protocol. |
| Deviations from intended exposures | Low | Observational cohort design with no intervention to deviate from. |
| Missing data | Moderate | Data loss is substantial but transparently quantified at each stage (72 AIMS samples -> 57 with acceptable DNA input; MAG QC failure of 27% for AIMS and an average 69% for the public datasets), ending in 125 pooled samples and 34 *B. longum* MAGs. |
| Measurement of outcomes | Low | Rigorous, modern, consistently applied metagenomic/pangenomic pipeline (BBDuk/BBMap/SPAdes assembly, sylph and MetaPhlAn4/StrainPhlAn4 profiling, Anvi'o pangenomics) with explicit, documented MAG quality thresholds (>=90% completeness, <=5% redundancy). |
| Selection of the reported result | Low | No trial registration applicable (observational genomics study); false discovery rate correction is systematically applied "in all instances where multiple testing occurred," and LASSO is used for feature selection (a comparatively conservative, shrinkage-based approach) rather than post-hoc selective hypothesis testing. |

**Microbiome-methods checklist (every study)**

| Domain | Judgment | Reasoning |
|---|---|---|
| Sample collection and storage method reported | Yes | "Samples were deposited in appropriate buffer-containing test tubes and stored in household freezers at -18/-20degC... transported in a mobile freezer (-4degC)... and stored at -80degC until DNA extraction." |
| DNA extraction method reported | Yes | "DNA was extracted using the ZY-D4306 ZymoBIOMICS-96 Magbead DNA Kit (with the use of the KingFisher Flex Purification System for high throughput) following BaseClear protocols." |
| Sequencing depth reported | Yes | "Shotgun metagenomics (mean depth: 38.8M reads per sample)." |
| Negative/positive contamination controls reported | Not reported | No mention anywhere in the available text of negative extraction/PCR controls or positive/mock-community controls. |
| Compositional-data handling reported | No | The LASSO models explicitly "used corresponding relative abundances as response variables" with no compositional-aware transform (e.g., CLR/log-ratio) described anywhere for the abundance-modeling approach. |

---

## #415 — STRONG Kids 2 mixed-feeding study 2025 (United States)

*Fecal Microbiome and Metabolomic Profiles of Mixed-Fed Infants Are More Similar to
Formula-Fed than Breastfed Infants.* Microorganisms. DOI 10.3390/microorganisms13010166

Design: cross-sectional sub-study (n=75; BF/FF/MF, n=25 each, each further split ~13 VD/12 CS)
drawn from the registered STRONG Kids 2 birth cohort (NCT03341858, parent cohort n=468),
shotgun metagenomics + UPLC-MS/MS metabolomics, with a deliberate, disclosed stratified
oversampling of MF/FF and cesarean-delivered infants relative to the parent cohort's natural
distribution.

### J. Risk of bias

*Drafted 26 Oct 2026 from a fresh read of `full_text_md/10.3390_microorganisms13010166/10.3390_microorganisms13010166.md`'s Materials and Methods (2.1-2.6) and Results (3.1).*

| Field | Value |
|---|---|
| RoB tool applicable | **ROBINS-I** (cross-sectional observational sub-study) |

**ROBINS-I**

| Domain | Judgment | Reasoning |
|---|---|---|
| Confounding | Moderate | Delivery mode is handled rigorously as a full factorial design factor (feeding x delivery interaction explicitly tested in both the alpha-diversity model and the MaAsLin2 differential-abundance model), and most baseline variables are balanced across feeding groups -- but the one variable that IS significantly imbalanced (maternal age, p=0.003, BF mothers older than FF) is not entered as a covariate anywhere in the microbiome models. |
| Selection of participants | Low | A deliberately stratified subsample from a well-characterized, registered parent cohort (STRONG Kids 2, n=468), with the oversampling of MF/FF and cesarean-delivered infants relative to the parent cohort's natural distribution explicitly disclosed with exact percentages -- a transparent, methodologically justified balanced-group design rather than an undocumented selection effect. |
| Classification of exposures | Moderate | BF/FF are defined as exclusive; MF intake is quantified via a 7-day parental recall question on feeding frequency, with the actual %-breastmilk-intake reported for the MF subgroups (46.4%/61.6%) -- a reasonably clear, quantitatively granular definition, though based on recall rather than a prospective daily record. |
| Deviations from intended exposures | Low | Observational cross-sectional design with no intervention to deviate from; feeding status reflects actual practice at the time of sampling. |
| Missing data | Low | The planned recruitment target (25 per feeding group, ~13 VD/12 CS each) matches the realized analytic sample with no indication of attrition. |
| Measurement of outcomes | Low | Detailed, objective, centrally processed shotgun-metagenomics pipeline (QIAamp Fast DNA Stool kit, Illumina NovaSeq 6000, Trimmomatic/KneadData/MetaPhlAn2/HUMAnN2) applied uniformly across groups. |
| Selection of the reported result | Low | Drawn from a registered parent cohort (NCT03341858); comprehensive reporting across diversity, taxonomic, functional, and metabolomic domains with systematic Benjamini-Hochberg FDR correction (q<0.10) throughout, with no evident selective emphasis. |

**Microbiome-methods checklist (every study)**

| Domain | Judgment | Reasoning |
|---|---|---|
| Sample collection and storage method reported | Yes | "Tubes were then placed into the storage box... stored in the participant's home freezer (-20degC). Samples were picked up within 2 to 24 h of collection and stored at -80degC until further processing." |
| DNA extraction method reported | Yes | "DNA was extracted from ~200 mg of feces by the QIAamp Fast DNA Stool Mini Kit (Qiagen, Valencia, CA, USA) in combination with bead beating on the FastPrep-24 System." |
| Sequencing depth reported | Not reported | No read-count or depth figure found anywhere in the available text. |
| Negative/positive contamination controls reported | Not reported | The paper describes process blanks and QC standards, but exclusively for the separate UPLC-MS/MS metabolomics workflow ("extracted water samples served as process blanks... a cocktail of quality control (QC) standards that were spiked into every analyzed sample") -- no negative/positive control is described anywhere for the 16S/shotgun sequencing workflow itself. |
| Compositional-data handling reported | No | "The relative abundance of data was arcsine-square root transformed" for the MaAsLin2 models -- a variance-stabilizing transform for proportions, not a compositional-data-aware method (e.g., CLR/log-ratio); no such method is mentioned anywhere. |

---

## #420 — IGram cohort antibiotics/breastfeeding study 2025 (United States)

*Antibiotic exposure is associated with minimal gut microbiome perturbations in healthy term
infants.* Microbiome. DOI 10.1186/s40168-024-01999-3

Design: prospective longitudinal birth cohort (IGram, African American mother-infant pairs,
Philadelphia; main cohort n=323 at 4/12/24 months, nested short-term antibiotic substudy
n=39), shotgun metagenomics. Primary exposure of interest is antibiotic timing, but
breastfeeding ("any amount of breastmilk" vs. none) is treated as a fixed effect in every
model and is reported as having a far larger, more consistent microbiome association than
antibiotic exposure itself -- a genuine, richly reported BF-vs-not-BF composition comparison.

### J. Risk of bias

*Drafted 26 Oct 2026 from a fresh read of `full_text_md/10.1186_s40168-024-01999-3/10.1186_s40168-024-01999-3.md`'s Methods (Study design, Microbiome sequencing, Statistical analysis) and Results.*

| Field | Value |
|---|---|
| RoB tool applicable | **ROBINS-I** (prospective longitudinal cohort design) |

**ROBINS-I**

| Domain | Judgment | Reasoning |
|---|---|---|
| Confounding | Low | Breastfeeding status "was included in all statistical models" alongside the primary antibiotic-exposure variable, with extensive sensitivity analyses additionally testing for intrapartum antibiotics, delivery mode, and gestational age as covariates, and explicit confirmation that no batch effects were detected (PERMANOVA on visit, breastfeeding status, and sequencing run number). |
| Selection of participants | Moderate | Clear eligibility criteria are described (3rd-trimester pregnant women, healthy-weight/obese BMI, uncomplicated term pregnancies, 2014-2017 recruitment), but detailed recruitment-flow numbers (screened vs. enrolled) are deferred to an unavailable supplement. |
| Classification of exposures | Low | Feeding mode was ascertained via structured parental interview conducted monthly (then quarterly after age 1) throughout follow-up -- a genuinely prospective, repeated-measurement ascertainment rather than retrospective recall, with a simple, consistently applied breastfeeding definition ("any amount of breastmilk, regardless of formula supplementation"). |
| Deviations from intended exposures | Low | Purely observational cohort design with no intervention to deviate from. |
| Missing data | Moderate | Breastfeeding prevalence genuinely declines over time (32% at 4 months, 19% at 12 months, 5% at 24 months) reflecting population-level weaning rather than missing data, but no explicit recruitment-to-final-analysis attrition numbers are given in the available text for the main longitudinal cohort. |
| Measurement of outcomes | Low | One of the most rigorous microbiome QC setups in this review: three distinct types of negative controls (clean swab, empty well, DNA-free water) plus a positive mock-community control, explicit rarefaction to a fixed depth, and a standardized, published (Sunbeam) bioinformatic pipeline. |
| Selection of the reported result | Low | Findings for the main (breastfeeding-relevant) comparisons were confirmed across four independent statistical approaches (log-linear models, CLR-transformed models, beta regression, quasibinomial GLMs on raw counts), extensive sensitivity analyses were run, FDR correction was applied throughout, and null findings are reported as plainly as positive ones (e.g., "no effect of antibiotic exposure on the overall taxonomic composition"). |

**Microbiome-methods checklist (every study)**

| Domain | Judgment | Reasoning |
|---|---|---|
| Sample collection and storage method reported | Yes | "Stool samples were collected at 4, 12, and 24 months, stored on ice, then aliquoted and stored at -80degC." |
| DNA extraction method reported | Yes | "DNA was extracted from fecal and negative control samples using the PowerSoil-htp kit (MO BIO Laboratories, Carlsbad, CA)." |
| Sequencing depth reported | Yes | "Taxonomic and KEGG ortholog tables were rarefied to 50,000 counts per sample to calculate beta diversity using Bray-Curtis dissimilarity." |
| Negative/positive contamination controls reported | Yes | "Three types of negative controls were added to each plate... Clean swab and empty well samples were used to assess environmental and reagent contamination. DNA-free water was used to assess potential PCR contamination. A mock community consisting of *Vibrio campbellii* and Lambda phage were included as positive controls." |
| Compositional-data handling reported | Yes | "Linear models on log-transformed bacterial abundances for the main cohort were confirmed with additional tests: linear models on centered log ratio (clr) transformed data, beta regression on proportions, and generalized linear models on the read count data with a quasibinomial link function" -- CLR explicitly used as a confirmatory compositional-aware method. |

---

## #438 — Neumann/TRAMIC oral-GIT cohort 2025 (Austria)

*First-year dynamics of the anaerobic microbiome and archaeome in infants' oral and
gastrointestinal systems.* mSystems. DOI 10.1128/msystems.01071-24

Design: small (n=30), single-center prospective pilot cohort (Graz, Austria), 16S rRNA
amplicon sequencing of oral + stool samples at up to 14 timepoints (day 1 to 12 months), plus
a limited shotgun-metagenomics sub-analysis. BF/NBF status is reassessed at every single
timepoint rather than fixed at baseline -- a notably rigorous, time-varying exposure design.

### J. Risk of bias

*Drafted 26 Oct 2026 from a fresh read of `full_text_md/10.1128_msystems.01071-24/10.1128_msystems.01071-24.md`'s Materials and methods (Study design, Sample collection, PCR, sequencing/bioinformatics) and Results (Overview on the study population).*

| Field | Value |
|---|---|
| RoB tool applicable | **ROBINS-I** (prospective observational cohort design) |

**ROBINS-I**

| Domain | Judgment | Reasoning |
|---|---|---|
| Confounding | Moderate | Baseline comparability was checked and confirmed for adjacent stratifications (delivery-mode groups differ only in gestational age; BF-duration subgroups differ only in formula feeding), but no explicit baseline-balance statement or statistical covariate adjustment is reported for the core BF-vs-NBF comparison itself (ALDEx2/PERMANOVA group comparisons are not covariate-adjusted), though the very small sample size (n=30) would limit the value of formal adjustment regardless. |
| Selection of participants | Low | A fully accounted, transparent recruitment flow: 32 mother-infant pairs enrolled -> 2 women withdrew during the study -> 30 infants completed the full sampling protocol, with the single stated reason (maternal discontinuation) given. |
| Classification of exposures | Low | Breastfeeding status was reassessed at every single monthly timepoint for each infant individually, producing dynamic group membership that changes over time as infants wean, rather than a single fixed baseline label carried through all of follow-up -- one of the more methodologically sophisticated exposure-ascertainment approaches in this review. |
| Deviations from intended exposures | Low | Observational cohort design with no intervention to deviate from. |
| Missing data | Moderate | The core 16S-amplicon-based taxonomic composition data appears essentially complete across all 30 infants, but the separate shotgun-metagenomics/functional sub-analysis was severely limited ("metagenomic data could only be obtained for nine oral samples in total due to the challenging nature of buccal mucosa samples"), a real, specific, and transparently documented data-completeness gap for that component. |
| Measurement of outcomes | Low | Detailed, rigorous DNA extraction protocol (enzymatic lysozyme/mutanolysin pretreatment plus mechanical bead-beating lysis, appropriate for Gram-positive cell walls) with negative controls and mock-community positive controls run alongside every extraction batch. |
| Selection of the reported result | Low | No trial registration applicable (observational pilot study); null findings are reported as plainly as positive ones (e.g., "we did not find significant differences in the relative abundance of *Staphylococcus* between BF and NBF infants... P>0.05"), with FDR (q-value) correction applied systematically throughout. |

**Microbiome-methods checklist (every study)**

| Domain | Judgment | Reasoning |
|---|---|---|
| Sample collection and storage method reported | Yes | "All samples were refrigerated, transported to the laboratory on ice and stored at -80degC until further processing." |
| DNA extraction method reported | Yes | Detailed, kit-specific protocols given for both sample types: "Genomic DNA was extracted from the oral swabs utilizing the QIAamp DNA Mini Kit (QIAGEN)..." and "Stool samples were processed utilizing the QIAamp DNA Stool Mini Kit (QIAGEN)...", each with enzymatic and mechanical lysis steps specified. |
| Sequencing depth reported | Not reported | No read-count or depth figure is given in the paper's own text (rarefaction values for the source-tracking analysis are deferred to an external GitHub repository table, not stated in the manuscript itself). |
| Negative/positive contamination controls reported | Yes | "Throughout the DNA extraction procedure, negative controls and mock communities as positive controls were incorporated and processed concurrently." |
| Compositional-data handling reported | Yes | Differential abundance was determined using ALDEx2 (an inherently CLR-based compositional method), and "the data of relative abundance were first CLR transformed in R" explicitly for visualization. |

---

## #468 — IGraM cohort metal/microbiome study 2025 (United States)

*Metal availability shapes early life microbial ecology and community succession.* mBio.
DOI 10.1128/mbio.01534-24

Design: companion paper to #420 (same IGraM prospective cohort, Philadelphia). Sub-study 2
(n=30; 17 breastfed, 13 formula-fed) provides the BF-vs-FF microbiome/metals comparison this
review extracts.

### J. Risk of bias

*Drafted 26 Oct 2026 from a fresh read of `full_text_md/10.1128_mbio.01534-24/10.1128_mbio.01534-24.md`'s Materials and methods (Human subjects, Shotgun metagenomic DNA sequencing, Statistical analysis) and Results.*

| Field | Value |
|---|---|
| RoB tool applicable | **ROBINS-I** (prospective cohort design) |

**ROBINS-I**

| Domain | Judgment | Reasoning |
|---|---|---|
| Confounding | Moderate | Unlike the companion paper #420 (which explicitly included breastfeeding in every model alongside extensive sensitivity analyses), this paper's BF-vs-FF comparisons are simpler group tests (two-way ANOVA with Geisser-Greenhouse correction for metals; linear mixed-effects modeling for microbiome taxa) with no additional covariates (e.g., delivery mode, gestational age) described. |
| Selection of participants | Moderate | Drawn from the same well-described IGraM prospective cohort as #420, with clear sub-study structure (sub-study 1 n=17 weekly through 1 month then 4/12 months; sub-study 2 n=30 at birth/1/4/12 months), but detailed recruitment-flow and eligibility-criteria numbers are deferred to a prior cohort publication not available here. |
| Classification of exposures | Moderate | Feeding-mode ascertainment methodology is not restated in this paper's own text (likely the same monthly-interview protocol described in the companion paper #420, but not repeated here). |
| Deviations from intended exposures | Low | Observational cohort design with no intervention to deviate from. |
| Missing data | Low | Sub-study 2's BF/FF composition analysis (n=17+13=30) accounts for the full sub-study 2 sample with no apparent loss. |
| Measurement of outcomes | Low | Same rigorous, objective pipeline as the companion paper (PowerSoil-htp extraction, Sunbeam/MetaPhlAn2), with 15 explicitly described negative control samples (diaper blank, blank swabs, library negative controls) processed alongside extraction. |
| Selection of the reported result | Low | FDR correction applied throughout; non-significant findings are reported as plainly as significant ones (e.g., "potassium, sodium, sulfur, selenium, and chromium did not differ between breast- and formula-fed infants"). |

**Microbiome-methods checklist (every study)**

| Domain | Judgment | Reasoning |
|---|---|---|
| Sample collection and storage method reported | Not reported | The Methods move directly from cohort description to DNA extraction ("DNA was extracted from fecal samples using the PowerSoil-htp kit...") with no stool-collection or storage protocol restated in this paper's own text. |
| DNA extraction method reported | Yes | "DNA was extracted from fecal samples using the PowerSoil-htp kit (MO BIO Laboratories, Carlsbad, CA), following the manufacturer's instructions, with the optional heating step included." |
| Sequencing depth reported | Not reported | No read-count or depth figure found anywhere in the available text. |
| Negative/positive contamination controls reported | Yes | "Fifteen negative control samples were included: one sample of unsoiled diaper (diaper blank), five unused swab tip samples (blank swabs), and nine samples of DNA-free water added to the NexteraXT library preparation kit instead of DNA (library negative controls)." |
| Compositional-data handling reported | Yes | Figure 4's gene-abundance heatmap is explicitly described as "mean clr transformed abundance of metal import genes," confirming CLR transformation was used for at least part of the paper's abundance analyses. |

---

## #497 — Hong Kong feeding-practices cohort 2024 (China)

*Influence of Feeding Practices on Intestinal Microbiota Composition in Healthy Chinese
Infants: A Prospective Cohort Study.* J Pediatr Health Care. DOI 10.1016/j.pedhc.2024.06.015

Design: prospective cohort (Hong Kong), 3-arm (direct breastfeeding n=83 / predominantly
expressed breastmilk >70% n=50 / exclusive formula n=84), recruitment halted early by the
COVID-19 pandemic (home-visit stool collection became impossible). DNA
extraction/sequencing/QC protocol details are deferred to an unavailable supplement
("eMethods in supplement").

### J. Risk of bias

*Drafted 26 Oct 2026 from a fresh read of `full_text_md/10.1016_j.pedhc.2024.06.015/10.1016_j.pedhc.2024.06.015.md`'s Methods (Study Setting and Design, Collection/DNA extraction/Sequencing, Statistical Analysis) and Results.*

| Field | Value |
|---|---|
| RoB tool applicable | **ROBINS-I** (prospective cohort design) |

**ROBINS-I**

| Domain | Judgment | Reasoning |
|---|---|---|
| Confounding | Moderate | Delivery mode was identified as significantly imbalanced (formula-fed infants more likely born by cesarean) and was explicitly adjusted for, along with sex and age, in the PERMANOVA/beta-diversity community-structure models -- but the headline taxon-specific findings (e.g., the *Bifidobacterium*/*Bacteroides* vs. *Streptococcus*/*Enterococcus* ratio) use unadjusted Dunn's/Kruskal-Wallis tests. |
| Selection of participants | Low | Clear eligibility criteria and a pre-specified sample-size target (84/group) are given, with a transparent, plausibly non-differential external reason for falling short of that target in one arm (COVID-19 halted home-visit stool collection, leaving the expressed-milk group at 50 of a planned 84). |
| Classification of exposures | Low | Three explicitly and operationally defined categories (direct breastfeeding / predominantly expressed breastmilk, >70% threshold / exclusive formula), confirmed by telephone contact at 6 weeks -- a notably granular distinction (direct vs. expressed breastmilk) that few other studies in this review capture. |
| Deviations from intended exposures | Low | Infants receiving both formula and breast milk were excluded by design, reducing the risk that exposure deviations blur the comparison groups. |
| Missing data | Low | The realized sample (217; 83/50/84 per group) reflects actual achieved recruitment before a well-explained external halt (COVID-19), not an unexplained loss of already-enrolled participants. |
| Measurement of outcomes | Moderate | DNA extraction, sequencing platform details, and QC measures are deferred to an unavailable supplement ("eMethods in supplement"), so the specific rigor of the measurement protocol cannot be verified from this paper's own text beyond the general approach (MiSeq, 16S V3-V4). |
| Selection of the reported result | Low | A sample-size/power calculation with a pre-specified, Bonferroni-corrected significance threshold (alpha=0.0167 for 3-group comparisons) was set a priori; FDR correction is applied throughout, and a nuanced, non-oversimplified result is reported transparently (individual *Bifidobacterium* and *Bacteroides* differences were non-significant, but their combined ratio reached significance) rather than only the more favorable framing. |

**Microbiome-methods checklist (every study)**

| Domain | Judgment | Reasoning |
|---|---|---|
| Sample collection and storage method reported | Yes | "The liner diaper was placed in a collection bag, sealed, and kept in a refrigerator until collection... immediately transported to the laboratory with frozen ice blocks and stored at -80degC prior to analysis." |
| DNA extraction method reported | Not reported | "DNA extraction, library preparation, and sequencing... were performed on a MiSeq sequencer (Illumina Inc.) with quality control measures in place (eMethods in supplement)" -- no specific kit or protocol is named in the main text itself. |
| Sequencing depth reported | Not reported | No read-count or depth figure found anywhere in the available text; detail is deferred to the unavailable supplement. |
| Negative/positive contamination controls reported | Not reported | Only a vague reference to "quality control measures in place (eMethods in supplement)" is given, with no specific negative or positive control described in the main text. |
| Compositional-data handling reported | No | "Relative abundance" (log10-transformed for visualization, Figure 1) is used throughout as the stated basis for all taxonomic comparisons, with no compositional-aware transform (e.g., CLR/log-ratio) mentioned anywhere. |

---

## #572 — INCA cohort bifidobacterial longitudinal study 2025 (Netherlands)

*Longitudinal changes in bifidobacterial population during the first two years of life.*
Beneficial Microbes. DOI 10.1163/18762891-bja00012

Design: prospective, registered (ClinicalTrials.gov NCT02536560), 4-center Dutch cohort
(INCA cohort). 450 planned -> 436 recruited -> 196 selected for this sub-analysis (>5 faecal
samples, exclusively breast- or formula-fed), 1,654 samples across 9 timepoints (1 day to
2 years), using specialized ITS-*Bifidobacterium* sequencing rather than general 16S/shotgun.

### J. Risk of bias

*Drafted 26 Oct 2026 from a fresh read of `full_text_md/10.1163_18762891-bja00012/10.1163_18762891-bja00012.md`'s Materials and methods (Study design, Bifidobacterial population profiling, Statistical analysis) and Results.*

| Field | Value |
|---|---|
| RoB tool applicable | **ROBINS-I** (prospective observational cohort design) |

**ROBINS-I**

| Domain | Judgment | Reasoning |
|---|---|---|
| Confounding | Low | A multivariate canonical correspondence analysis (CCA) jointly partitions variance in the bifidobacterial population across sampling timepoint, antibiotic(s) intake, delivery mode, feeding mode, and subject identity simultaneously, rather than assessing feeding mode in isolation. |
| Selection of participants | Moderate | A transparent flow is given (450 planned -> 436 recruited -> 196 selected for this analysis based on providing >5 faecal samples and having exclusive feeding status), but the sample-richness-based selection criterion could itself introduce a selection effect if infants able to provide many samples over two years differ systematically from those who could not. |
| Classification of exposures | Low | Feeding mode was tracked via daily parental checklists plus an online questionnaire throughout follow-up -- a genuinely prospective, continuously recorded ascertainment rather than retrospective recall. |
| Deviations from intended exposures | Low | Observational cohort design with no intervention to deviate from. |
| Missing data | Moderate | Per-timepoint sample sizes vary meaningfully within the 196-infant cohort (n=120 to n=189 across the first year, n=123 at 2 years), reflecting openly disclosed "deviations in the timepoints" due to practical sample-collection limitations -- real but transparently acknowledged incompleteness. |
| Measurement of outcomes | Low | A specialized, externally validated ITS-*Bifidobacterium* sequencing method (Milani et al. protocol) was used, with the reference database's quality validated against genomes of the dominant infant-gut bifidobacterial species. |
| Selection of the reported result | Low | Pre-registered (NCT02536560); Benjamini-Hochberg FDR correction applied throughout; comprehensive, nuanced findings are reported across many (sub)species and timepoints, including numerous explicitly non-significant comparisons, rather than only the significant results. |

**Microbiome-methods checklist (every study)**

| Domain | Judgment | Reasoning |
|---|---|---|
| Sample collection and storage method reported | Yes | "Collected faecal materials were directly frozen at -18 to -20degC until analysis." |
| DNA extraction method reported | Yes | "Total DNA was extracted from faeces using the QIAmp DNA Stool Mini Kit following the manufacturer's instructions (Qiagen, Hilden, Germany)." |
| Sequencing depth reported | Not reported | No read-count or depth figure found anywhere in the available text. |
| Negative/positive contamination controls reported | Not reported | No mention anywhere in the available text of negative extraction/PCR controls or positive/mock-community controls. |
| Compositional-data handling reported | No | "Relative abundance" is used throughout as the stated basis for every reported comparison, with no compositional-aware transform (e.g., CLR/log-ratio) mentioned anywhere. |

---

## #632 — OPO/MFGM fortified formula trial 2024 (China)

*Comparative evaluation of enriched formula milk powder with OPO and MFGM vs. breastfeeding
and regular formula milk powder in full-term infants: a comprehensive study on gut
microbiota, neurodevelopment, and growth.* Food Funct. DOI 10.1039/d3fo03392a

Design: hybrid -- single-blind RCT between two formula arms (FFG: OPO+MFGM-fortified vs.
RFG: regular formula) plus a non-randomized breastfeeding reference group (BMG), Peking
University Third Hospital -- routed to ROBINS-I per the hybrid-design rule. Final analytic
groups: BMG n=50, FFG n=17, RFG n=12 (of 81 enrolled, 79 completed).

### J. Risk of bias

*Drafted 26 Oct 2026 from a fresh read of `full_text_md/10.1039_d3fo03392a/10.1039_d3fo03392a.md`'s Materials & methods (Study design, Collection, Sequencing/Bioinformatics, Statistical analysis) and Results (Demographic and clinical information).*

| Field | Value |
|---|---|
| RoB tool applicable | **ROBINS-I** (non-randomized breastfeeding reference group per the hybrid-design rule) |

**ROBINS-I**

| Domain | Judgment | Reasoning |
|---|---|---|
| Confounding | Moderate | An unusually comprehensive baseline-characteristics table confirms no significant differences across a wide range of variables (gestational age, sex, birth weight/length/head circumference, maternal age, delivery mode, parental education, household income, pregnancy complications, twin status), but none of these are entered as formal covariates in the actual composition-comparison models (simple Kruskal-Wallis/PERMANOVA group tests). |
| Selection of participants | Low | Clear eligibility criteria and a transparent, CONSORT-style flow (81 enrolled -> 79 completed, with the 2 losses specifically attributed to loss to follow-up, one each from FFG and RFG); the markedly uneven final group sizes (BMG 50, FFG 17, RFG 12) reflect the study's natural-feeding-method-based BMG assignment plus 1:1 randomization only within the formula arms, not an undisclosed selection process. |
| Classification of exposures | Moderate | Groups are clearly defined (BMG by "natural feeding methods," FFG/RFG by randomized, single-blind formula assignment), but the ascertainment method for the breastfeeding group specifically is not elaborated beyond this categorical description. |
| Deviations from intended exposures | Low | Single-blind randomization (parents unaware of formula type) for the formula arms, combined with minimal, well-documented loss to follow-up. |
| Missing data | Low | Minimal, specifically attributed loss to follow-up (2 of 81 enrolled, one each from FFG and RFG). |
| Measurement of outcomes | Low | Standard, consistently applied 16S pipeline (QIIME2/deblur-DADA2, Silva reference database, PICRUSt2 functional prediction) applied uniformly across groups. |
| Selection of the reported result | Moderate | No trial registration number is given anywhere in the available text (unlike several other hybrid-design studies in this review); a pre-specified sample-size/power calculation is reported and met (minimum 9/group for *Bifidobacterium* differences), and non-significant findings for growth and neurodevelopment outcomes are reported plainly and repeatedly rather than downplayed. |

**Microbiome-methods checklist (every study)**

| Domain | Judgment | Reasoning |
|---|---|---|
| Sample collection and storage method reported | Yes | "Parents collected the samples at home and placed them in stool tubes with preservation solution. The tubes were stored at -20degC before being transferred to the hospital's refrigerated facility. All samples in the hospital were stored below -80degC until further analysis." |
| DNA extraction method reported | Yes | "The SDS method was employed to extract total genomic DNA from the samples." |
| Sequencing depth reported | Not reported | No read-count or depth figure found anywhere in the available text. |
| Negative/positive contamination controls reported | Not reported | No mention anywhere in the available text of negative extraction/PCR controls or positive/mock-community controls. |
| Compositional-data handling reported | No | Results are presented throughout as "relative abundance" (phylum/genus level, Figure 3; functional protein abundance, Figure 6) with no compositional-aware transform (e.g., CLR/log-ratio) mentioned anywhere. |

---

## #640 — San Luis Potosi feeding-practices study 2023 (Mexico)

*Influence of feeding practices in the composition and functionality of infant gut
microbiota and its relationship with health.* PLOS ONE. DOI 10.1371/journal.pone.0294494

Design: cross-sectional (San Luis Potosi, Mexico; 2017-2019 recruitment), 3-arm (BF n=20 /
FF n=16 / combined-fed CF n=19 for growth/biomarker outcomes). The 16S sequencing subsample
was deliberately restricted to only 6 infants per group, all vaginally delivered with
mothers of healthy BMI, as a confounding-control-by-restriction strategy.

### J. Risk of bias

*Drafted 26 Oct 2026 from a fresh read of `full_text_md/10.1371_journal.pone.0294494/10.1371_journal.pone.0294494.md`'s Materials and methods (Registration, DNA extraction, Sequencing, Bioinformatic/statistical analyses) and Results.*

| Field | Value |
|---|---|
| RoB tool applicable | **ROBINS-I** (cross-sectional observational design) |

**ROBINS-I**

| Domain | Judgment | Reasoning |
|---|---|---|
| Confounding | Moderate | The 16S-sequenced subsample was deliberately restricted to infants "born by vaginal delivery, and their mothers had healthy BMI" -- a genuine, explicit confounding-control-by-restriction strategy for two specific factors -- but no statistical adjustment is used in the actual composition comparisons (NMDS/PERMANOVA group tests), and other plausible confounders (maternal age, socioeconomic status) are not addressed. |
| Selection of participants | Moderate | Recruitment was by volunteer self-selection ("lactating mothers were asked about their willingness to participate") with no stated response rate, and the 16S-sequenced subsample (6 of each group's larger enrolled N) was further narrowed with no described selection method beyond the delivery-mode/maternal-BMI restriction criteria. |
| Classification of exposures | Moderate | Three feeding groups (BF/FF/combined-fed) are defined, and the study explicitly notes "no advice or recommendations about feeding practices were expressed to the participants" (reducing risk of study-induced behavior change), but the specific ascertainment method (recall vs. prospective record) is not clearly detailed in the available text. |
| Deviations from intended exposures | Low | Cross-sectional observational design with no intervention to deviate from. |
| Missing data | No information | No recruitment-flow detail is given (how many eligible mothers were approached or declined) over the 2-year recruitment window -- only the final per-group analytic Ns are reported. |
| Measurement of outcomes | Low | A detailed, objective, consistently applied 16S pipeline (Illumina MiSeq, Mothur SOP, Silva v123, 97% OTU clustering) with triplicate technical PCR replicates per sample. |
| Selection of the reported result | Low | No trial registration applicable (observational cross-sectional study); non-significant findings are reported plainly (e.g., a fecal-fat-detection trend with "no statistical significance was found") rather than only the significant results. |

**Microbiome-methods checklist (every study)**

| Domain | Judgment | Reasoning |
|---|---|---|
| Sample collection and storage method reported | Yes | "Infant feces samples were collected in commercial diapers. The samples were separated into four portions and frozen at -60degC until used." |
| DNA extraction method reported | Yes | A detailed phenol-chloroform protocol is given: "The feces stored at -60degC were thawed and suspended in 1.5 mL suspension buffer... An extraction with phenol-chloroform was performed... The obtained pellet was washed with ethanol (70%)." |
| Sequencing depth reported | Not reported | No read-count or depth figure found anywhere in the available text. |
| Negative/positive contamination controls reported | Not reported | The only sequencing-related control mentioned is "PhiX sequencing control (Illumina) represented 30% of the pooled library" -- a standard Illumina run-calibration spike-in, not a laboratory negative (blank/reagent) or positive (mock-community) contamination control; no such control is described anywhere. |
| Compositional-data handling reported | No | "Read count matrixes were normalized by a square root transformation" for the Bray-Curtis-based NMDS/PERMANOVA analyses -- a variance-stabilizing transform, not a compositional-data-aware method (e.g., CLR/log-ratio); no such method is mentioned anywhere. |

---

## #701 — MicrobeMom secondary analysis 2023 (Ireland)

*Maternal breastfeeding is associated with offspring microbiome diversity; a secondary
analysis of the MicrobeMom randomized control trial.* Front Microbiol.
DOI 10.3389/fmicb.2023.1154114

Design: secondary (observational) analysis of breastfeeding within the MicrobeMom RCT cohort
(ISRCTN53023014, Dublin, Ireland) -- the trial's actual randomized intervention was a
prenatal probiotic vs. placebo, not feeding mode; breastfeeding itself was never
randomized. Routed to ROBINS-I. n=118 mother-infant pairs with microbial diversity outcomes.

### J. Risk of bias

*Drafted 26 Oct 2026 from a fresh read of `full_text_md/10.3389_fmicb.2023.1154114/10.3389_fmicb.2023.1154114.md`'s Methods (MicrobeMom, Breastfeeding, Infant microbiome diversity, Statistical analysis) and Results (Baseline information, Breastfeeding).*

| Field | Value |
|---|---|
| RoB tool applicable | **ROBINS-I** (breastfeeding is an observational, non-randomized exposure within this RCT cohort) |

**ROBINS-I**

| Domain | Judgment | Reasoning |
|---|---|---|
| Confounding | Low | Confounders were "determined a priori" (maternal age, maternal early-pregnancy BMI, probiotic-vs-placebo trial group, mode of delivery, antibiotics during delivery) and explicitly entered into adjusted regression models for the breastfeeding-microbiome associations, with Benjamini-Hochberg correction applied to the adjusted analyses -- a pre-specified, causally-reasoned adjustment strategy rather than one driven only by observed imbalance. |
| Selection of participants | Moderate | This secondary analysis is restricted to "118 mother-infant pairs... based on the presence of infant microbial diversity outcomes," but the relationship between this analytic subset and the full originally-randomized MicrobeMom cohort (how many lacked usable microbiome data and why) is not given in the available text. |
| Classification of exposures | Low | Breastfeeding status was recorded from hospital records at discharge (yes/no, exclusive yes/no) and reassessed via direct participant questioning at the 1-month follow-up -- a dual-source, two-timepoint ascertainment. |
| Deviations from intended exposures | Low | Breastfeeding was never an assigned/randomized exposure in this trial (the actual randomized intervention was prenatal probiotic vs. placebo), so there is no assigned-vs-received distinction to track for this naturally occurring exposure. |
| Missing data | Moderate | The 118-pair analytic sample reflects some reduction from the full MicrobeMom RCT cohort (to those with usable microbial diversity outcomes), but the magnitude of and reasons for this reduction are not given in the available text. |
| Measurement of outcomes | Low | Detailed, objective, consistently applied pipeline (AllPrep DNA/RNA kit, Illumina NextSeq shotgun metagenomics, MetaPhlAn3), with an explicit sample-inclusion threshold of >100,000 reads to ensure adequate depth for rarefaction. |
| Selection of the reported result | Moderate | The parent trial is registered (ISRCTN53023014), but this specific breastfeeding-microbiome relationship is explicitly framed as a "secondary analysis" not itself independently pre-registered as a primary hypothesis -- though the a priori confounder specification and systematic FDR correction partially offset this. |

**Microbiome-methods checklist (every study)**

| Domain | Judgment | Reasoning |
|---|---|---|
| Sample collection and storage method reported | Yes | "There was 1g of infant stool in one stool pot, fixed with 7mL of RNAlater and frozen on site at -80degC." |
| DNA extraction method reported | Yes | "DNA and RNA extraction using the AllPrep DNA/RNA kit (Qiagen)." |
| Sequencing depth reported | Yes | "Only samples with more than 100,000 reads were included and the rarefaction demonstrates sufficient representation of microbial diversity." |
| Negative/positive contamination controls reported | Not reported | No negative or positive control is described in this paper's own text; sequencing and quality-filtering methods are deferred to companion papers ("the employed methods were previously described in detail"). |
| Compositional-data handling reported | No | Alpha/beta diversity were analyzed via standard ecology methods (Simpson/Shannon indices, Bray-Curtis dissimilarity with PCA, vegan's Adonis function) with no compositional-aware transform (e.g., CLR/log-ratio) mentioned anywhere; "compositional profile" refers only to MetaPhlAn3's taxonomic output, not a CoDA statistical method. |

---

## #718 — Shanghai intestinal-pharyngeal microbiota study 2023 (China)

*The correlation of the intestinal with pharyngeal microbiota in early neonates.*
Front Microbiol. DOI 10.3389/fmicb.2023.1225352

Design: small (n=20), registered (ChiCTR2200056782), tightly eligibility-restricted
observational study, Shanghai, comparing exclusive breastfeeding (n=8) vs. limited formula
feeding (40-60% of intake, n=12) alongside its primary intestinal-vs-oropharyngeal-microbiota
comparison. Delivery mode (vaginal only), antibiotics, and probiotics are controlled by
strict exclusion criteria rather than statistical adjustment.

### J. Risk of bias

*Drafted 26 Oct 2026 from a fresh read of `full_text_md/10.3389_fmicb.2023.1225352/10.3389_fmicb.2023.1225352.md`'s Methods (Study design and population, Collection, DNA extraction, Sequencing, Bioinformatics) and Results (3.1, 3.2).*

| Field | Value |
|---|---|
| RoB tool applicable | **ROBINS-I** (observational comparison; feeding status reflects naturally occurring maternal milk-supply circumstances, not an assigned intervention) |

**ROBINS-I**

| Domain | Judgment | Reasoning |
|---|---|---|
| Confounding | Low | An explicit baseline table confirms no significant differences between the exclusive-breastfeeding and limited-formula groups on gestational age, birth weight, sex, Apgar scores, maternal weight gain, and maternal age, while delivery mode, antibiotic exposure, and probiotic/prebiotic exposure are controlled by strict inclusion/exclusion criteria (100% vaginal delivery, zero antibiotic/probiotic exposure in both groups) rather than merely statistical balance. |
| Selection of participants | Low | A fully transparent, numerically explicit recruitment funnel is given: "of the 1,262 newborns screened, 20 met the inclusion and exclusion criteria," with specific, pre-stated eligibility and exclusion criteria (including explicit exclusion of infants with incomplete paired samples), leaving no evidence that selection was differentially related to both exposure and outcome. |
| Classification of exposures | Low | "Limited formula feeding" is operationalized with a specific, quantified threshold (40-60% of intake), a notably precise definition distinguishing partial supplementation from full formula feeding. |
| Deviations from intended exposures | Low | Observational design; feeding status reflects actual, naturally occurring maternal milk-supply circumstances rather than an assigned exposure. |
| Missing data | Low | Infants with "incomplete collection of paired samples or incomplete data of important clinical information" were excluded by design at enrollment, so the analyzed 20 infants all have complete data. |
| Measurement of outcomes | Low | Rigorous, objective, well-documented 16S pipeline (Usearch 97% OTU clustering, RDP classifier) with explicit, detailed sequencing-depth and coverage statistics reported. |
| Selection of the reported result | Low | Registered (ChiCTR2200056782); the headline finding is a null result (no significant effect of limited formula feeding on microbiota composition), reported prominently and plainly as a central conclusion rather than downplayed or omitted. |

**Microbiome-methods checklist (every study)**

| Domain | Judgment | Reasoning |
|---|---|---|
| Sample collection and storage method reported | Yes | "The first meconium of 3-5 g and fresh feces... were placed in sterile lyophilization tubes... The samples were stored at -40degC before being transferred to the temperature of -80degC within 1 week until DNA extraction." |
| DNA extraction method reported | Yes | "Total genomic DNA was extracted from the fecal and oropharynx swab samples using E.Z.N.A Mag-Bind Soil DNA Kit (OMEGA, M5635-02), according to the manufacturer's instructions." |
| Sequencing depth reported | Yes | "5,099,357 sequencing reads were obtained. After the filtering process... 4,031,740 final valid sequences for subsequent analysis... The sequence depth was sufficient to obtain a high degree of sequence coverage for all samples (mean: 0.998; median: 0.999; range: 0.988-0.999)." |
| Negative/positive contamination controls reported | Not reported | No mention anywhere in the available text of negative extraction/PCR controls or positive/mock-community controls. |
| Compositional-data handling reported | No | Results are presented as "relative abundance histograms" with no compositional-aware transform (e.g., CLR/log-ratio) mentioned anywhere. |

---

## #720 — CARE cohort Peptostreptococcaceae/lactate study 2023 (Switzerland)

*Breastfeeding and the major fermentation metabolite lactate determine occurrence of
Peptostreptococcaceae in infant feces.* Gut Microbes. DOI 10.1080/19490976.2023.2241209

Design: prospective cohort (CARE, St. Gallen, Switzerland; n=69 mother-infant pairs), a
secondary re-analysis of 16S/qPCR/metabolite data originally generated by a companion paper
(Appert et al.) for a new, targeted hypothesis about *Peptostreptococcaceae*/*Clostridiaceae*
and lactate. 3-arm breastfeeding comparison at 4 months: Exclusively-BF n=38, Partially-BF
n=17, Non-BF n=14. DNA extraction and sequencing-protocol specifics are deferred to the
companion paper and not restated here.

### J. Risk of bias

*Drafted 26 Oct 2026 from a fresh read of `full_text_md/10.1080_19490976.2023.2241209/10.1080_19490976.2023.2241209.md`'s Results (Baseline breastfeeding and delivery characteristics) and Materials and methods (Cohort and sample collection, Analysis of microbial composition).*

| Field | Value |
|---|---|
| RoB tool applicable | **ROBINS-I** (prospective observational cohort design) |

**ROBINS-I**

| Domain | Judgment | Reasoning |
|---|---|---|
| Confounding | Moderate | Delivery mode was explicitly checked and confirmed balanced across the three feeding groups (74%/86%/82% vaginal), but this is the only covariate explicitly checked, and no statistical adjustment is applied to the composition analyses themselves (unadjusted alpha/beta-diversity group comparisons). |
| Selection of participants | Moderate | Clear eligibility criteria are given (all healthy babies born at the Cantonal Hospital St. Gallen with at least one German-speaking parent, with specific congenital/chronic-disease exclusions), but no screened-vs-enrolled recruitment-flow numbers are given beyond the final n=69. |
| Classification of exposures | Low | Feeding status was tracked via "weekly food diaries until the end of year 1," with detailed, quantified breastfeeding-duration data (median weeks with IQR) reported per group -- one of the more rigorous, continuously prospective exposure-ascertainment protocols in this review. |
| Deviations from intended exposures | Low | Observational cohort design with no intervention to deviate from. |
| Missing data | Low | Per-timepoint sample sizes are specifically quantified and only modestly reduced relative to the full group sizes (e.g., at 3 months: 34/16/13 vs. the full 38/17/14). |
| Measurement of outcomes | Moderate | DNA extraction and the full sequencing protocol are deferred to a companion paper ("methods are described in detail in Appert et al.") and not restated here, though this paper adds its own BLASTn-supplemented taxonomic identification specifically for the taxa of interest. |
| Selection of the reported result | Moderate | No trial registration applicable; this is explicitly a secondary re-analysis of previously collected cohort data for a new, narrowly targeted hypothesis (not itself independently pre-registered), though it draws on an established, separately peer-reviewed companion dataset. |

**Microbiome-methods checklist (every study)**

| Domain | Judgment | Reasoning |
|---|---|---|
| Sample collection and storage method reported | Not reported | Fecal sample collection/storage is deferred entirely to the companion paper ("fecal samples... were transferred to the laboratory as described by Appert et al.") and not restated in this paper's own text (only the breast-milk sample-handling protocol is given directly). |
| DNA extraction method reported | Not reported | DNA extraction is not described in this paper's own text; "methods are described in detail in Appert et al." |
| Sequencing depth reported | Yes | "We calculated alpha-diversity at an initial subsampling of ASVs higher than 15,000 reads or more." |
| Negative/positive contamination controls reported | Not reported | No negative or positive control is described in this paper's own text; sequencing methodology is deferred to the companion paper. |
| Compositional-data handling reported | No | "Beta-diversity was calculated with all the entire gene catalog using Bray-Curtis dissimilarity matrix" -- a standard ecology approach with no compositional-aware transform (e.g., CLR/log-ratio) mentioned anywhere. |

---

## #725 — 5HMO-mix formula trial 2023 (Germany/Italy/Spain)

*Infant Formula Supplemented with Five Human Milk Oligosaccharides Shifts the Fecal
Microbiome of Formula-Fed Infants Closer to That of Breastfed Infants.* Nutrients.
DOI 10.3390/nu15143087

Design: hybrid -- RCT between two formula arms (5HMO-mix vs. infant-formula control) plus a
non-randomized breastmilk (BM) reference group, 12 sites across 3 countries, N=311,
ClinicalTrials.gov NCT03513744 -- routed to ROBINS-I per the hybrid-design rule. **Notable
limitation: the BM group's 6-month timepoint has only N=2 samples**, explicitly attributed to
COVID-19-related remote-visit disruptions preventing fecal sample collection at some sites.

### J. Risk of bias

*Drafted 26 Oct 2026 from a fresh read of `full_text_md/10.3390_nu15143087/10.3390_nu15143087.md`'s Materials and Methods (Cohort Characteristics, Sample Collection, DNA Extraction/Sequencing, Taxonomic/Functional Annotation, Statistical Analysis).*

| Field | Value |
|---|---|
| RoB tool applicable | **ROBINS-I** (non-randomized breastmilk reference group per the hybrid-design rule) |

**ROBINS-I**

| Domain | Judgment | Reasoning |
|---|---|---|
| Confounding | Moderate | Randomization balances the two formula arms, but the BM reference group is a non-randomized natural comparator with no statistical covariate adjustment described for the composition analyses (PERMANOVA uses feeding group alone as the explanatory variable). |
| Selection of participants | Low | Large (n=311), multi-site (12 sites, 3 countries), registered trial with clear eligibility/exclusion criteria, and a specific, plausible, externally-driven explanation for reduced sample availability (COVID-19 remote-visit restrictions). |
| Classification of exposures | Moderate | Formula-arm assignment is randomized and controlled; the BM group's ascertainment method (how exclusive breastfeeding was verified) is not detailed in the available text. |
| Deviations from intended exposures | Low | "Subjects were excluded if parents were not prepared to feed the subject solely within the assigned study group" -- a design feature specifically intended to minimize exposure-group contamination. |
| Missing data | Serious | The BM group's 6-month sample count collapses to N=2 (from 80-90 at earlier timepoints), explicitly attributed to COVID-19-related remote-visit restrictions preventing fecal sample collection -- a well-explained but severe, specific gap that effectively precludes any meaningful BM comparison at the 6-month timepoint. |
| Measurement of outcomes | Low | A sophisticated, modern shotgun-metagenomics pipeline (metagenomic species (MGS) profiling against a large in-house gene catalog, CheckM-validated taxonomic annotation, strict mapping-quality thresholds) applied uniformly. |
| Selection of the reported result | Low | Pre-registered (NCT03513744); Benjamini-Hochberg FDR correction (<=10%) applied systematically, with effect sizes (Cliff's delta) reported alongside p-values. |

**Microbiome-methods checklist (every study)**

| Domain | Judgment | Reasoning |
|---|---|---|
| Sample collection and storage method reported | Not reported | Collection logistics relative to study visits are described ("fecal samples were voluntarily collected by the parents"), but no storage temperature or preservation method is stated anywhere in the available text. |
| DNA extraction method reported | Yes | "Microbial DNA was extracted from ~0.1 g aliquots of fecal samples using a NucleoSpin 96 Soil kit (Macherey-Nagel) with horizontal bead beating in a Vortex-Genie 2 at 2700 rpm for 5 min." |
| Sequencing depth reported | Not reported | No read-count or depth figure found anywhere in the available text. |
| Negative/positive contamination controls reported | Not reported | No mention anywhere in the available text of negative extraction/PCR controls or positive/mock-community controls (only computational host-DNA removal via Bowtie2 is described, a bioinformatic QC step rather than a laboratory contamination control). |
| Compositional-data handling reported | No | "The MGS count matrix was normalized according to effective gene length and normalized sample-wise to relative abundance estimates for each MGS" -- a directly observable plain-relative-abundance approach, with no compositional-aware transform (e.g., CLR/log-ratio) mentioned anywhere. |

---

## #733 — Lotte probiotic-fortified formula study 2023 (South Korea)

*Effect of Probiotic-Fortified Infant Formula on Infant Gut Health and Microbiota
Modulation.* Food Sci Anim Resour. DOI 10.5851/kosfa.2023.e26

Design: described as a "randomized, double-blind, placebo-controlled study" among three
groups -- breast milk (BF), probiotic formula (PF), and placebo formula (FF) -- at postnatal
care centers in Seoul (n=118 total). **Note: the paper's own text states BF itself was part
of the randomization ("participants were assigned into the following three groups: breast
milk (BF), probiotic formula (PF), and placebo formula-fed group (FF)"), which is not
logically coherent for a breastfeeding exposure (infant feeding by breast milk cannot be
randomly assigned) -- almost certainly BF was in fact a non-randomized natural comparator,
with only PF-vs-FF truly randomized, but the text itself does not clarify this.** Routed to
ROBINS-I per the hybrid-design rule, given this ambiguity.

### J. Risk of bias

*Drafted 26 Oct 2026 from a fresh read of `full_text_md/10.5851_kosfa.2023.e26/10.5851_kosfa.2023.e26.md`'s Materials and methods (Infant cohort study, Treatment protocol, Fecal sample collection, DNA extraction/sequencing, Bioinformatics) and Results.*

| Field | Value |
|---|---|
| RoB tool applicable | **ROBINS-I** (BF almost certainly non-randomized despite the paper's ambiguous phrasing; hybrid-design rule applies) |

**ROBINS-I**

| Domain | Judgment | Reasoning |
|---|---|---|
| Confounding | Moderate | Only a vague statement is given that "individual differences in gestational period and infant body weight were minimized among the three groups," with no baseline-characteristics table or statistical test shown to confirm this, and no covariate adjustment used in the composition analyses (one-way ANOVA with Duncan's/Tukey's post hoc tests only). |
| Selection of participants | Moderate | Clear overall eligibility/exclusion criteria are given (118 total participants recruited from postnatal care centers), but no per-group sample sizes or recruitment-flow/attrition numbers are reported anywhere in the available text. |
| Classification of exposures | Moderate | The paper's own description of how the BF group was formed is internally inconsistent (stated as part of a randomization process alongside the two formula arms, which is not coherent for a breastfeeding exposure), making it unclear how BF-group assignment was actually determined. |
| Deviations from intended exposures | Moderate | No per-protocol vs. intention-to-treat distinction or exposure-deviation handling is discussed anywhere in the available text. |
| Missing data | No information | No recruitment flow, dropout, or missing-sample information is given anywhere in the available text. |
| Measurement of outcomes | Low | A detailed, objective 16S pipeline (QIAamp DNA stool kit, DADA2, SILVA v128) with explicit, rigorous negative and positive (mock-community) controls run alongside extraction, library preparation, and sequencing. |
| Selection of the reported result | Moderate | No trial registration number is given anywhere in the available text despite being described as a formal RCT, though a mix of significant and explicitly non-significant findings is reported transparently throughout (e.g., "iso-butyrate concentration showed no considerable difference," "stool IgA levels... did not show any significant difference"). |

**Microbiome-methods checklist (every study)**

| Domain | Judgment | Reasoning |
|---|---|---|
| Sample collection and storage method reported | Yes | "Collected samples were then stored at [-]80degC until analysis in the microbiology lab." |
| DNA extraction method reported | Yes | A detailed, step-by-step QIAamp DNA stool kit (Qiagen) protocol is given, including buffer volumes, centrifugation steps, and incubation conditions. |
| Sequencing depth reported | Yes | "Data on low-quality samples with <10,000 observed OTUs were removed from the sample set." |
| Negative/positive contamination controls reported | Yes | "The mock DNA library was prepared using the ZymoBiomics microbial community DNA standard... Negative control was established by following the same DNA extraction procedure without feces. The final elute of the DNA extraction negative control was used as the template for PCR negative control... We confirmed that the samples were not contaminated during DNA extraction or library preparation." |
| Compositional-data handling reported | No | Results are presented throughout as "relative abundance" (phylum/class/order/family/genus level, Figure 5) with no compositional-aware transform (e.g., CLR/log-ratio) mentioned anywhere. |

---

## #771 — INNOVA 2020 formula trial 2023 (Spain)

*Innova 2020: A Follow-Up Study of the Fecal Microbiota of Infants Using a Novel Infant
Formula between 6 Months and 12 Months of Age.* Int J Mol Sci. DOI 10.3390/ijms24087392

Design: hybrid -- multicenter (21 sites), randomized, double-blind RCT between two formula
arms (INN vs. STD) plus an unblinded, deliberately matched-recruitment breastfed (BF)
exploratory reference group ("for every two infants supplemented with infant formula, a
candidate BF subject was recruited at each center"), ClinicalTrials.gov NCT05303077 --
routed to ROBINS-I per the hybrid-design rule.

### J. Risk of bias

*Drafted 26 Oct 2026 from a fresh read of `full_text_md/10.3390_ijms24087392/10.3390_ijms24087392.md`'s Materials and Methods (Design of the Trial, Characteristics of the Formula, Sampling, DNA Extraction, Sequencing/Bioinformatics, Rivera-Pinto Analysis).*

| Field | Value |
|---|---|
| RoB tool applicable | **ROBINS-I** (unblinded, non-randomized BF reference group per the hybrid-design rule) |

**ROBINS-I**

| Domain | Judgment | Reasoning |
|---|---|---|
| Confounding | Low | A deliberate, matched-recruitment design was used specifically to balance the BF-vs-formula comparison: "for every two infants supplemented with infant formula, a candidate BF subject was recruited at each center... in order to maintain balance between the three arms of the study" -- a proactive, by-design confounding-control strategy rather than post hoc statistical adjustment alone. |
| Selection of participants | Low | A fully itemized, CONSORT-style recruitment flow across 21 centers via "active and consecutive recruitment methods" (217 signed consent -> 145 randomized, with 3 randomization failures and 2 screening failures itemized -> 140 meeting all inclusion/exclusion criteria). |
| Classification of exposures | Moderate | BF is defined as "exclusively BF infants," and formula-arm allocation is randomized and blinded, but the specific ascertainment method for confirming exclusive breastfeeding status is not elaborated in the available text beyond the recruitment-matching description. |
| Deviations from intended exposures | Low | Dropouts are specifically itemized per arm (25 BF, 8 INN, 5 STD) rather than left as an undifferentiated total, reflecting transparent tracking of exposure-group attrition. |
| Missing data | Moderate | Per-arm dropout counts are transparently disclosed, but the BF group's dropout count (25) is notably higher in proportion than either formula arm (8 and 5), a real asymmetry that is disclosed but not further explained. |
| Measurement of outcomes | Low | A rigorous, well-validated pipeline (QIAmp Power Fecal Kit with explicit Nanodrop DNA-quality QC, Illumina NovaSeq 6000, DADA2/QIIME2) with two independently described negative controls (water-only and empty-collector-tube DNA), both confirmed negative. |
| Selection of the reported result | Low | Pre-registered (NCT05303077) with a separately published trial-protocol paper cited for full methods (Ruiz-Ojeda et al., 2022); the Rivera-Pinto/Selbal microbial-signature method is a principled, systematic variable-selection approach rather than ad hoc post hoc taxon selection. |

**Microbiome-methods checklist (every study)**

| Domain | Judgment | Reasoning |
|---|---|---|
| Sample collection and storage method reported | Yes | "ADM-Biopolis provided a kit that included a buffer for sample stabilization... DNA remains stable at room temperature (15-25degC) for several months and at -20degC or -80degC indefinitely." |
| DNA extraction method reported | Yes | "An optimized DNA extraction protocol was applied using the QIAmp Power Fecal Kit (Qiagen, Hilden, Germany)," with explicit A260/230 and A260/280 DNA-quality QC. |
| Sequencing depth reported | Yes | "Samples with fewer than 10,000 reads were excluded from the data filtering process. No samples were excluded from our study." |
| Negative/positive contamination controls reported | Yes | "A negative control containing water was obtained to confirm that there was no contamination. Furthermore, a second negative control consisting of DNA isolated from a collector tube without a sample was sequenced as a control, and the results were also negative." |
| Compositional-data handling reported | Yes | The Rivera-Pinto method / Selbal algorithm is explicitly used to identify microbial "balances... calculated" from geometric means of taxa groups -- a genuine, named compositional-data-analysis (CoDA) technique, the most sophisticated compositional approach seen in this batch. |

---

## #800 — START-Canada South Asian cohort 2023 (Canada)

*The Relationship Between Diet, Gut Microbiota, and Serum Metabolome of South Asian Infants
at 1 Year.* J Nutr. DOI 10.1016/j.tjnut.2022.12.016

Design: prospective cohort (South Asian Birth Cohort, START-Canada, parent N=1012), a
secondary analysis reprocessing 16S data from a prior study for 182 1-year-olds with both
diet and microbiota data, with independent replication of the serum-metabolome findings in a
subset of the CHILD Cohort Study (n=81, White European). Stool collection and DNA extraction
protocol specifics are deferred to the prior study and not restated here.

### J. Risk of bias

*Drafted 26 Oct 2026 from a fresh read of `full_text_md/10.1016_j.tjnut.2022.12.016/10.1016_j.tjnut.2022.12.016.md`'s Methods (Study design/participants, Dietary data collection, Gut microbiota stool analysis, Association of diet..., Independent cohort replication).*

| Field | Value |
|---|---|
| RoB tool applicable | **ROBINS-I** (prospective cohort design) |

**ROBINS-I**

| Domain | Judgment | Reasoning |
|---|---|---|
| Confounding | Low | A multivariable "envfit" model jointly adjusts diet variables alongside a comprehensive set of participant characteristics (maternal vegetarianism, gestational diabetes, intrapartum antibiotics, mother's years living in Canada, delivery mode, gestational age, infant sex, birth weight, weight gain, infant age) simultaneously for the beta-diversity association -- one of the most comprehensive multivariate confounding-adjustment approaches in this review. |
| Selection of participants | Moderate | Only 182 of the full 1012-infant START-Canada cohort had both dietary and microbiota data collected at 1 year, with no explicit reason given in the available text for why the remainder were not included. |
| Classification of exposures | Moderate | Breastfeeding and formula-feeding status were tracked at four repeated timepoints (birth, 3, 6, and 12 months) to construct a longitudinal "milk diet" variable -- a reasonably rigorous, repeated-measures approach, though based on questionnaire/FFQ report rather than a prospective daily diary. |
| Deviations from intended exposures | Low | Observational cohort design with no intervention to deviate from. |
| Missing data | Serious | The reduction from the full 1012-infant parent cohort to the 182-infant analytic sample with both diet and microbiota data represents an 82% loss, with no reason given in the available text for this large gap. |
| Measurement of outcomes | Low | A rigorous, appropriately compositional-aware bioinformatic pipeline (DADA2, SILVA v132, an explicit sequencing-depth threshold, Aitchison-distance beta-diversity) is described, even though the underlying stool-collection and DNA-extraction protocols are deferred to a prior publication. |
| Selection of the reported result | Low | No trial registration applicable (observational cohort); the study specifically undertook independent replication of its serum-metabolome findings in a separate cohort (CHILD), used a systematic, pre-specified collinearity-handling procedure for its multivariable models, and applied FDR correction to metabolite associations. |

**Microbiome-methods checklist (every study)**

| Domain | Judgment | Reasoning |
|---|---|---|
| Sample collection and storage method reported | Not reported | "Stool sample collection methods and DNA extraction methods are described elsewhere" (a prior study) and are not restated in this paper's own text. |
| DNA extraction method reported | Not reported | Deferred to the same prior study citation, with no kit or protocol named in this paper's own text. |
| Sequencing depth reported | Yes | "Samples with a sequence depth of 40,000 reads were maintained." |
| Negative/positive contamination controls reported | Not reported | No negative or positive control is described anywhere in the available text for the 16S sequencing workflow (a pooled QC sample is described only for the separate serum-metabolomics analysis). |
| Compositional-data handling reported | Yes | "Between-community diversity analyses were based on the Aitchison distance, calculated using the Euclidean distance of centre-log-transformed ASV concentration count data" -- an explicit, properly described CLR-based compositional approach. |

---

## #811 — Combiotic-Study (GOLFIII) synbiotic formula trial 2023 (France/Belgium)

*Early life gut microbiota profiles linked to synbiotic formula effects: a randomized
clinical trial in European infants.* Am J Clin Nutr. DOI 10.1016/j.ajcnut.2022.11.012

Design: hybrid -- large (n=540), multicenter (41 sites), double-blind RCT between two
formula arms (CF vs. IF, dynamically randomized stratified by birth mode and breastfeeding
history) plus a non-randomized, unblinded human-milk (HM) reference group (n=80),
ClinicalTrials.gov NCT02221687 ("The Combiotic-Study, GOLFIII") -- routed to ROBINS-I per the
hybrid-design rule. Explicitly stated by the authors: "the group of breastfed infants, which
was not blinded and randomized, was used as the reference for assessing the effects of the
formulae."

### J. Risk of bias

*Drafted 26 Oct 2026 from a fresh read of `full_text_md/10.1016_j.ajcnut.2022.11.012/10.1016_j.ajcnut.2022.11.012.md`'s Methods (Study design, Sample collection, Stool DNA extraction, 16S processing, Statistical analysis) and Results (Figure 1 legend).*

| Field | Value |
|---|---|
| RoB tool applicable | **ROBINS-I** (non-randomized, unblinded HM reference group, explicitly acknowledged by the authors) |

**ROBINS-I**

| Domain | Judgment | Reasoning |
|---|---|---|
| Confounding | Moderate | Dynamic randomization stratified by birth mode and breastfeeding history at inclusion provides strong balance between the two formula arms, but no equivalent statistical adjustment or baseline comparison is described between the non-randomized HM reference group and the formula arms. |
| Selection of participants | Low | Large (n=540 formula + n=80 HM), multicenter (41 sites across France and Belgium) registered trial with clear eligibility/exclusion criteria and a referenced CONSORT flow chart. |
| Classification of exposures | Low | Formula-arm eligibility required confirmed exclusive formula feeding at randomization; the HM group is defined by a precise, quantified operational threshold ("a maximum of 1 formula meal per 24 h and willingness of the mother to continue breastfeeding until at least the age of 4 mo"). |
| Deviations from intended exposures | Low | Concomitant antibiotic treatment during the study was tracked and explicitly confirmed not to differ significantly between formula groups. |
| Missing data | Moderate | Sample sizes decline over the three visits (M4 n=419, M12 n=379, M24 n=297, from an initial 620 enrolled across all three groups), consistent with ordinary longitudinal attrition, though the magnitude is not further broken down or explained in the available text. |
| Measurement of outcomes | Low | A rigorous, detailed, objective pipeline (Maxwell 16 automated DNA extraction with dual mechanical/chemical lysis, UNOISE3/USEARCH11 denoising, SILVA 138 reference, the Rhea statistical pipeline) applied uniformly across groups. |
| Selection of the reported result | Low | Pre-registered (NCT02221687); pre-specified prevalence/abundance thresholds were applied before statistical testing to limit the scope of taxa tested, and Benjamini-Hochberg correction was applied systematically across all analyses. |

**Microbiome-methods checklist (every study)**

| Domain | Judgment | Reasoning |
|---|---|---|
| Sample collection and storage method reported | Yes | "Jars with stool samples were placed in airtight bags and refrigerated at +2degC to +8degC for a maximum of 24 h... Microtubes were stored at -20degC until shipment to the major laboratory. Samples were then further stored [at] -20degC until analysis." |
| DNA extraction method reported | Yes | "DNA was extracted from stool samples using the Maxwell 16 Tissue DNA Purification kit (Promega) following a protocol with dual cell lysis (mechanical and chemical)," described in full step-by-step detail. |
| Sequencing depth reported | Not reported | No read-count or depth figure found anywhere in the available text (normalization is described only as "division to minimal sampling size," with no specific number given). |
| Negative/positive contamination controls reported | Not reported | The only control described is a "TaqMan Exogenous Internal Positive Control Reagent" used to confirm the absence of PCR inhibitors -- a PCR-inhibition QC check, not a laboratory negative (blank/reagent) or positive (mock-community) contamination control; no such contamination control is described anywhere. |
| Compositional-data handling reported | No | Taxonomic composition data were normalized "relative to 100" (plain relative abundance) via the Rhea pipeline, with no compositional-aware transform (e.g., CLR/log-ratio) mentioned anywhere. |

---

## #822 — INNOVA 2020, 0-6 month report 2023 (Spain)

*Effects of a Novel Infant Formula on the Fecal Microbiota in the First Six Months of Life:
The INNOVA 2020 Study.* Int J Mol Sci. DOI 10.3390/ijms24033034

Design: companion paper to #771 -- same trial (INNOVA 2020, NCT05303077, 21 Spanish centers),
same hybrid design (randomized INN-vs-STD formula arms + unblinded, deliberately
matched-recruitment BF exploratory reference group) and same matched-recruitment strategy
("one candidate breastfeeding subject was recruited at each center for every two infants
supplemented with infant formula"). This paper covers the earlier visits (21 days, 2 months,
6 months) rather than #771's 6-12 month follow-up.

### J. Risk of bias

*Drafted 26 Oct 2026 from a fresh read of `full_text_md/10.3390_ijms24033034/10.3390_ijms24033034.md`'s Materials and Methods (Trial Design, Study Groups, Inclusion/Exclusion Criteria, Sampling, DNA Extraction, Sequencing/Bioinformatic Analysis, Rivera-Pinto Analysis).*

| Field | Value |
|---|---|
| RoB tool applicable | **ROBINS-I** (unblinded, non-randomized BF reference group per the hybrid-design rule, same as companion paper #771) |

**ROBINS-I**

| Domain | Judgment | Reasoning |
|---|---|---|
| Confounding | Low | Same deliberate, by-design matched-recruitment strategy as #771, specifically intended "to keep the three arms of the trial balanced" between the BF reference group and the formula arms, rather than relying on post hoc statistical adjustment alone. |
| Selection of participants | Low | Same fully itemized recruitment flow as #771 (217 signed consent -> 145 randomized), across 21 centers via active, consecutive recruitment, with the same detailed inclusion/exclusion criteria (gestational age, birth weight, maternal BMI, antibiotic history, etc.) explicitly listed. |
| Classification of exposures | Moderate | Same as #771: BF/formula groups are clearly named, but the specific ascertainment method for confirming exclusive breastfeeding status is not elaborated in the available text beyond the recruitment-matching description. |
| Deviations from intended exposures | Low | Same trial-wide design as #771; no evidence of differential handling of exposure deviations for this earlier-timepoint report. |
| Missing data | Moderate | This paper's own text does not restate the trial-wide per-arm dropout counts given in companion paper #771 (25 BF, 8 INN, 5 STD); given the same underlying cohort and the same asymmetric attrition pattern documented there, the same caution applies here. |
| Measurement of outcomes | Low | Same rigorous pipeline as #771 (QIAmp Power Fecal Kit with explicit Nanodrop DNA-quality QC, Illumina NovaSeq 6000, DADA2/QIIME2, SILVA 16S V3-V4), with one negative control described here (water-only), confirming no contamination. |
| Selection of the reported result | Low | Pre-registered (NCT05303077) with a separately published trial-protocol paper cited for full methods; the Rivera-Pinto/Selbal microbial-signature method is again used, a principled, systematic variable-selection approach. |

**Microbiome-methods checklist (every study)**

| Domain | Judgment | Reasoning |
|---|---|---|
| Sample collection and storage method reported | Yes | "Fecal samples were collected at 21 days, 2 and 6 months using a collection kit provided by ADM-Biopolis (Valencia, Spain), which included a sample-stabilizing buffer to ensure its stability." |
| DNA extraction method reported | Yes | "DNA extraction was carried out using a previously optimized protocol, which includes a combination of beads beating and enzymatic lysis... applying the QIAmp Power Fecal Kit (Qiagen, Germany)," with explicit A260/230 and A260/280 DNA-quality QC. |
| Sequencing depth reported | Yes | "As part of the data filtering process, samples with fewer than 10,000 reads were excluded." |
| Negative/positive contamination controls reported | Yes | "A negative control containing water was obtained to confirm the absence of contamination." |
| Compositional-data handling reported | Yes | The Rivera-Pinto method / Selbal algorithm is again used (Section 4.10) to identify microbial balances from geometric means of taxa groups -- the same genuine CoDA technique used in companion paper #771. |

---

## #830 — VDAART offspring cohort microbial maturation/asthma study 2023 (United States)

*Environmental and genetic associations with aberrant early-life gut microbial maturation in
childhood asthma.* J Allergy Clin Immunol. DOI 10.1016/j.jaci.2023.01.006

Design: secondary analysis of offspring from VDAART, a prospective, randomized,
double-blinded, placebo-controlled trial of prenatal vitamin D supplementation
(NCT00920621; 3 US clinical centers). Breastfeeding (exclusive >=4 months) is an
observational covariate within this cohort, not the trial's randomized exposure, so this
review's comparison routes to ROBINS-I. An unusually transparent included-vs-excluded
comparison (Table E1) is provided.

### J. Risk of bias

*Drafted 26 Oct 2026 from a fresh read of `full_text_md/10.1016_j.jaci.2023.01.006/10.1016_j.jaci.2023.01.006.md`'s Methods (Study design/participants, Covariate ascertainment, Fecal microbiome profiling, Data analysis) and Table E1.*

| Field | Value |
|---|---|
| RoB tool applicable | **ROBINS-I** (breastfeeding is an observational, non-randomized covariate within this RCT cohort) |

**ROBINS-I**

| Domain | Judgment | Reasoning |
|---|---|---|
| Confounding | Low | A comprehensive, a priori-specified covariate list is used throughout: "child sex, child race and ethnicity, and study enrollment site were selected a priori as relevant covariates," alongside exclusive breastfeeding, pet ownership, daycare attendance, number of older siblings, birth mode, and perinatal antibiotic exposure. |
| Selection of participants | Moderate | An unusually transparent included-vs-excluded comparison (Table E1) is provided, but it reveals genuine, statistically significant differences between the 463 included and 343 excluded offspring on study site (P<.001), daycare attendance by age 1 (P=.01), and dog ownership (P=.001) -- real, disclosed evidence of non-random selection into the analytic sample. |
| Classification of exposures | Moderate | "Exclusive breast-feeding for at least the first 4 months of life" is ascertained via participant questionnaires, a clear operational definition, though the ascertainment is not described as prospective or diary-based in the available text. |
| Deviations from intended exposures | Low | Breastfeeding is an observational, non-randomized covariate with no assigned exposure to deviate from. |
| Missing data | Moderate | Small, specifically quantified exclusions for insufficient sequencing depth (n=10 at 3-6 months, n=5 at 1 year) are transparently reported, but this sits alongside the larger, non-random included-vs-excluded gap already flagged under Selection of participants. |
| Measurement of outcomes | Low | A rigorous, well-described pipeline (Skewer, QIIME2, DADA2, SILVA 138) with an explicit, confirmed test for batch effects (PERMANOVA testing batch against Bray-Curtis dissimilarity, P=.70, finding none) -- a genuinely rigorous QC step rarely performed elsewhere in this review. |
| Selection of the reported result | Low | The parent VDAART trial is registered (NCT00920621); this secondary analysis is not itself separately registered, but a dedicated sensitivity analysis was performed to test whether repeated-measures inclusion biased the results (a single-timepoint-per-subject reanalysis, reported as highly correlated with and showing similar associations to the main model), a strong robustness-checking signal. |

**Microbiome-methods checklist (every study)**

| Domain | Judgment | Reasoning |
|---|---|---|
| Sample collection and storage method reported | Not reported | Sample collection and storage detail is not given; "DNA extraction and sequencing... were done... as previously described," deferring to a cited prior publication not available here. |
| DNA extraction method reported | Not reported | Deferred to the same prior-publication citation, with no kit or protocol named in this paper's own text. |
| Sequencing depth reported | Yes | "Samples with read depth less than 1000 were not analyzed (n=10 at age 3-6 months and n=5 at age 1 year), leading to final sample sizes of 255 subjects... and 431 subjects." |
| Negative/positive contamination controls reported | Not reported | No negative or positive control is described anywhere in the available text. |
| Compositional-data handling reported | No | For the MAZ-score algorithm, "ASVs were collapsed to the species taxonomic level and log-transformed" -- a plain log transform, not a compositional-aware method (e.g., CLR/log-ratio with a geometric-mean denominator); no such method is described anywhere. |

---

## #837 — GDM postpartum women and offspring cohort 2023 (Brazil)

*The gut microbiome of obese postpartum women with and without previous gestational
diabetes mellitus and the gut microbiota of their babies.* Diabetol Metab Syndr.
DOI 10.1186/s13098-022-00954-2

Design: prospective cohort (São Paulo, Brazil; pregnant women followed from pregnancy
through 2-6 months postpartum), primary comparison is GDM vs. control; breastfeeding
(exclusive/predominant, 2-6 months) is a secondary offspring-level exposure, with N=91
offspring stool samples (45 GDM-exposed, 46 control-exposed) after a transparently
documented exclusion flow.

### J. Risk of bias

*Drafted 26 Oct 2026 from a fresh read of `full_text_md/10.1186_s13098-022-00954-2/10.1186_s13098-022-00954-2.md`'s Methods (Design and study population, Standardized questionnaires, Fecal sample collection, Analytic methods, Bioinformatics analysis) and Results (Offspring).*

| Field | Value |
|---|---|
| RoB tool applicable | **ROBINS-I** (prospective cohort design) |

**ROBINS-I**

| Domain | Judgment | Reasoning |
|---|---|---|
| Confounding | Moderate | Strict eligibility and exclusion criteria (overweight/obese pre-pregnancy mothers only; exclusion of recent antibiotic/laxative/probiotic use) control several potential confounders by design for the overall cohort, but no statistical adjustment or baseline-comparability check specific to the breastfeeding-vs-not contrast is reported (the breastfeeding-abundance association uses unadjusted DESeq2 differential-abundance testing). |
| Selection of participants | Low | A fully transparent, numerically explicit recruitment and exclusion flow: 143 pregnant women enrolled -> 101 evaluated postpartum -> 98 collected stool -> 84 retained after excluding recent antibiotic/laxative/probiotic use -> 91 offspring stool samples with DNA extracted, each step with a specific stated reason. |
| Classification of exposures | Moderate | Breastfeeding is defined clearly ("exclusive or predominant... breastfeeding were considered as 'yes'") but ascertained via a single postpartum-visit questionnaire rather than a prospective daily record. |
| Deviations from intended exposures | Low | Observational cohort design with no intervention to deviate from. |
| Missing data | Low | The same transparent, fully-accounted exclusion flow documented under Selection of participants applies here. |
| Measurement of outcomes | Low | A reasonably rigorous, objective 16S pipeline (QIAamp DNA Stool Mini Kit, Illumina MiSeq V4 amplicon sequencing, DADA2, tag.me taxonomic classifier) with an explicit negative control included in PCR runs. |
| Selection of the reported result | Low | No trial registration applicable (observational cohort); the paper's own abstract and Results prominently and transparently report the headline null finding (no difference in offspring microbiota by GDM status or delivery mode) rather than downplaying it, alongside the positive breastfeeding association. |

**Microbiome-methods checklist (every study)**

| Domain | Judgment | Reasoning |
|---|---|---|
| Sample collection and storage method reported | Yes | "A researcher followed standardized procedures, including antiseptic handling, collection of aliquots in sterile cryotubes, and immediate freezing at -20degC. Aliquots were then stored at -80degC on the same sampling day until DNA extraction." |
| DNA extraction method reported | Yes | "Bacterial DNA from stool samples was extracted using the QIAamp DNA Stool Mini Kit (Qiagen)." |
| Sequencing depth reported | Not reported | No read-count or depth figure found anywhere in the available text. |
| Negative/positive contamination controls reported | Yes | "Negative controls with a buffer from the DNA extraction kit were included in the PCR runs." |
| Compositional-data handling reported | No | "Considering the relative abundance" is used throughout to describe taxonomic findings, and beta diversity was calculated via Jensen-Shannon Divergence/PCoA -- standard ecology methods with no compositional-aware transform (e.g., CLR/log-ratio) mentioned anywhere. |

---

## #838 — DIPP/EHF mother-infant multi-omics study 2023 (Finland)

*Mobile genetic elements from the maternal microbiome shape infant gut microbial assembly
and metabolism.* Cell. DOI 10.1016/j.cell.2022.11.023

Design: hybrid -- nested within a randomized, blinded clinical trial (regular vs. extensively
hydrolyzed formula, EHF) in HLA-genotype-selected infants at risk for type 1 diabetes
(DIPP study, Finland), with mothers "encouraged to breastfeed" as the natural, non-randomized
comparator. n=74 infants analyzed, longitudinal shotgun metagenomics + metabolomics from
late pregnancy to 1 year. Routed to ROBINS-I per the hybrid-design rule.

### J. Risk of bias

*Drafted 26 Oct 2026 from a fresh read of `full_text_md/10.1016_j.cell.2022.11.023/10.1016_j.cell.2022.11.023.md`'s Results (infant diet confounders) and STAR+METHODS (Cohort recruitment, Trial design, Sample collection/DNA extraction, Metagenome sequencing, statistical analysis).*

| Field | Value |
|---|---|
| RoB tool applicable | **ROBINS-I** (non-randomized breastfeeding exposure within a randomized-formula trial, per the hybrid-design rule) |

**ROBINS-I**

| Domain | Judgment | Reasoning |
|---|---|---|
| Confounding | Low | "Delivery mode, breastfeeding, use and type of infant formula, and prior antibiotics significantly influenced infant microbiomes or metabolomes... These factors were considered as confounders in subsequent analyses" -- all of these (plus infant age and sex) were then systematically included as fixed effects in every downstream MaAsLin2 model, with participant identity as a random effect to account for the longitudinal/repeated-measures structure -- an exceptionally comprehensive and consistently applied adjustment strategy. |
| Selection of participants | Moderate | The parent trial restricted eligibility to infants with an HLA genotype conferring increased type 1 diabetes risk, a deliberate enrichment criterion that may limit generalizability of the breastfeeding-microbiome findings beyond this genetically selected population, though detailed per-group sample accounting is otherwise provided (e.g., 27 regular-formula infants/111 samples vs. 23 hydrolyzed-formula infants/107 samples). |
| Classification of exposures | Low | "Study formula use, food consumption frequency, and compliance to the intervention diet were monitored with frequent dietary questionnaires and interviews" at 2 weeks, monthly through 9 months, and at 12 months -- a genuinely frequent, prospective, repeated-measures ascertainment of actual (not just assigned) feeding status. |
| Deviations from intended exposures | Low | Analyses incorporate actual "use and type of infant formula" as a time-varying exposure rather than treating infants solely by original randomization assignment, reflecting a sophisticated as-fed analytic approach. |
| Missing data | Moderate | Detailed per-analysis sample/infant counts are given throughout, but no single overall CONSORT-style flow diagram or total attrition accounting is visible in the available text for this complex, multi-omics, multi-timepoint design. |
| Measurement of outcomes | Low | State-of-the-art shotgun metagenomics (Illumina HiSeq 2500, Nextera XT library prep, explicit target depth of 2.5 Gb per sample) combined with large-scale untargeted and targeted metabolomics, applied uniformly across groups. |
| Selection of the reported result | Low | The parent randomized trial is described as previously published and registered; a pre-specified FDR threshold (q<0.25) is applied systematically to all MaAsLin2 analyses, and the paper reports counter-to-expectation findings plainly (e.g., fecal calprotectin "tended to be elevated in breastfed infants," an inflammation marker one might expect to be lower) rather than only favorable associations. |

**Microbiome-methods checklist (every study)**

| Domain | Judgment | Reasoning |
|---|---|---|
| Sample collection and storage method reported | Yes | "Infant stool samples were collected by the mothers at home and stored in the household freezer (-20degC)... shipped on dry ice to the EDIA Core Laboratory... stored at -80degC until shipping to Tampere University for DNA extraction." |
| DNA extraction method reported | Yes | "DNA extractions from 0.2 g of stool were carried out using the vacuum protocol of PowerSoil DNA Isolation Kit (MoBio Laboratories, Inc.)." |
| Sequencing depth reported | Yes | "Metagenomic libraries were sequenced on the Illumina HiSeq 2500 platform, targeting 2.5 Gb of sequence per sample with 101 bp paired end reads." |
| Negative/positive contamination controls reported | Not reported | No mention anywhere in the available text of negative extraction/PCR controls or positive/mock-community controls. |
| Compositional-data handling reported | No | "Relative abundance" is used throughout (e.g., Figure 2A, 3A) as the stated basis for taxonomic results, with no compositional-aware transform (e.g., CLR/log-ratio) mentioned anywhere. |

---

## #839 — West China breast milk/infant gut microbiota study 2022 (China)

*The Effect of Breast Milk Microbiota on the Composition of Infant Gut Microbiota: A Cohort
Study.* Nutrients. DOI 10.3390/nu14245397

Design: small (n=23 mother-infant pairs), single-center cohort study (Chengdu, China),
sampled at days 0 and 30, comparing a breastfeeding group (BF, n=13, breastfed >=25 of the
first 30 days) against a mixed/formula-predominant group (MF, n=10, formula-fed >=25 of the
first 30 days).

### J. Risk of bias

*Drafted 26 Oct 2026 from a fresh read of `full_text_md/10.3390_nu14245397/10.3390_nu14245397.md`'s Materials and Methods (Subjects Selection, Sample Collection, DNA Extraction, Sequencing/Bioinformatics, Statistical Analysis) and Results.*

| Field | Value |
|---|---|
| RoB tool applicable | **ROBINS-I** (observational cohort design) |

**ROBINS-I**

| Domain | Judgment | Reasoning |
|---|---|---|
| Confounding | Moderate | Maternal antibiotic/probiotic/prebiotic use in the month before delivery is controlled by exclusion, but no other covariates (e.g., delivery mode, maternal age) are compared between groups or adjusted for in the BF-vs-MF composition comparisons (simple t-test/ANOVA/Kruskal-Wallis group tests only). |
| Selection of participants | Moderate | Clear eligibility and exclusion criteria are given, but this is a small, single-center convenience sample (23 pairs) with no stated recruitment-flow numbers (how many eligible infants were approached vs. included). |
| Classification of exposures | Moderate | Groups are defined by a specific, quantified threshold (breastfed or formula-fed for >=25 of the first 30 days), but the paper's own description is somewhat confusingly worded regarding how mixed the "BF" group's feeding actually was ("since the newborns would not have been fed only formula, they were more or less breastfed"). |
| Deviations from intended exposures | Low | Observational cohort design with no intervention to deviate from. |
| Missing data | Moderate | "A total of 58 fecal samples and 25 breast milk samples were finally collected" from 23 pairs at 2 timepoints, a figure that does not map cleanly onto the theoretical maximum (46 possible of each), with no explicit accounting or reason given for the shortfall/discrepancy. |
| Measurement of outcomes | Moderate | A standard, objective 16S pipeline (E.Z.N.A. Stool DNA Kit, SILVA 128 reference) is described, but with limited methodological transparency overall (no sequencing depth, no contamination controls reported) and an unusually strict 100%-similarity OTU-clustering threshold stated without further explanation. |
| Selection of the reported result | Moderate | No trial registration applicable (small observational cohort study); the headline comparison is reported as a plain null result ("no statistical difference in breast milk microbiota was observed between the 30-days BF group... and the 30-days MF group"), a good transparency signal despite the study's otherwise modest methodological detail. |

**Microbiome-methods checklist (every study)**

| Domain | Judgment | Reasoning |
|---|---|---|
| Sample collection and storage method reported | Yes | "All samples were stored at -20degC immediately after collection and transferred to a -80degC refrigerator for measurement within 24 h." |
| DNA extraction method reported | Yes | "Fecal and breast milk bacterial genomic DNA extraction kit E.Z.N.A. Stool DNA Kit (D4015, Omega, Inc., Norwalk, CT, USA)," with explicit Nanodrop DNA-quality QC (concentration >5 ng/uL, OD260/280 between 1.7-1.9). |
| Sequencing depth reported | Not reported | No read-count or depth figure found anywhere in the available text. |
| Negative/positive contamination controls reported | Not reported | No mention anywhere in the available text of negative extraction/PCR controls or positive/mock-community controls. |
| Compositional-data handling reported | No | "Relative abundance" is used throughout (phylum and genus level, Figure 1) as the stated basis for all taxonomic comparisons, with no compositional-aware transform (e.g., CLR/log-ratio) mentioned anywhere. |

---

## #849 — Wageningen fructoselysine degradation study 2022 (Netherlands)

*Differences in gut microbial fructoselysine degradation activity between breast-fed and
formula-fed infants.* FEMS Microbiol Ecol. DOI 10.1093/femsec/fiac145

Design: small (n=20; 10 BF, 10 FF), cross-sectional mechanistic study (Wageningen,
Netherlands) combining 16S composition profiling with a novel in vitro fructoselysine-
degradation functional assay, plus a secondary metagenomic re-analysis of a public dataset
(Backhed et al. 2015). Eligibility restricted to vaginally delivered, antibiotic-naive
infants.

### J. Risk of bias

*Drafted 26 Oct 2026 from a fresh read of `full_text_md/10.1093:femsec:fiac145/10.1093:femsec:fiac145.md`'s Materials and methods (Collection and processing, DNA isolation/sequencing/qPCR) and Results (Bacterial composition, Fructoselysine degradation).*

| Field | Value |
|---|---|
| RoB tool applicable | **ROBINS-I** (cross-sectional observational design) |

**ROBINS-I**

| Domain | Judgment | Reasoning |
|---|---|---|
| Confounding | Moderate | Delivery mode (vaginal only) and antibiotic exposure are controlled by strict exclusion criteria, but the BF and FF groups differ somewhat in mean age at sampling (16 vs. 13 weeks) with no statistical adjustment for this, and no other covariates are addressed. |
| Selection of participants | Moderate | Clear eligibility criteria are given, but this is a small (n=20), single-region convenience sample with no recruitment-flow numbers (how many eligible infants were approached vs. included). |
| Classification of exposures | Moderate | Groups are clearly labeled "exclusively BF" and "exclusively FF," but the specific ascertainment method (prospective record vs. parental report) is not described in the available text. |
| Deviations from intended exposures | Low | Cross-sectional observational design with no intervention to deviate from. |
| Missing data | Low | All 20 collected samples are accounted for in the composition analysis (with 2 individuals flagged, not excluded, as possible outliers for one taxon), and specific, individually-named outlier exclusions from the in vitro kinetics analysis are transparently reported with clear criteria. |
| Measurement of outcomes | Low | Rigorous, detailed methodology for both the 16S/qPCR quantitative microbiome profiling (NG-Tax 2.0, SILVA 132, qPCR-normalized absolute abundance) and a validated, specialized in vitro LC-MS/MS fructoselysine-degradation assay run in technical duplicate and repeated at least three times. |
| Selection of the reported result | Low | No trial registration applicable (small mechanistic/observational study); a clearly non-significant composition finding is reported prominently and transparently (overall fecal bacterial composition did not differ between BF and FF by Bray-Curtis dissimilarity, and LEfSe found no significantly different taxa) alongside the significant functional (fructoselysine-degradation) finding, rather than forcing the composition data to match the functional narrative. |

**Microbiome-methods checklist (every study)**

| Domain | Judgment | Reasoning |
|---|---|---|
| Sample collection and storage method reported | Yes | "Fecal samples were scooped from the diaper into a sterile 50 ml filter top tube, which was directly stored in a BD GasPak EZ Anaerobe gas generating pouch system... transferred to the fridge (+-4degC). Within 24 h, the fecal sample was further processed to fecal slurry under anaerobic conditions and stored at -80degC." |
| DNA extraction method reported | Yes | "DNA was isolated from the fecal samples with a bead-beating procedure combined with the customized MaxWell 16 Tissue LEV Total RNA Purification Kit." |
| Sequencing depth reported | Not reported | No read-count or depth figure found anywhere in the available text. |
| Negative/positive contamination controls reported | Not reported | No mention anywhere in the available text of negative extraction/PCR controls or positive/mock-community controls. |
| Compositional-data handling reported | No | The study instead uses a quantitative microbiome profiling (absolute-abundance) approach -- "multiplying the relative abundance of a taxa within one sample with the corresponding total bacterial load as quantified by qPCR" -- a legitimate alternative to compositional-data analysis, but not a CLR/log-ratio transform; no such compositional-aware method is mentioned anywhere. |

---

## #878 — 2'-FL fortified formula trial 2022 (United States)

*Effects of addition of 2-fucosyllactose to infant formula on growth and specific pathways
of utilization by Bifidobacterium in healthy term infants.* Front Nutr.
DOI 10.3389/fnut.2022.961526

Design: hybrid -- double-blind RCT between two formula arms (2'FL-supplemented test vs.
control, n=66 each) plus a non-randomized breastfed reference group (n=89), N=221 enrolled.
No trial registration number is given anywhere in the available text. Routed to ROBINS-I per
the hybrid-design rule.

### J. Risk of bias

*Drafted 26 Oct 2026 from a fresh read of `full_text_md/10.3389_fnut.2022.961526/10.3389_fnut.2022.961526.md`'s Materials and methods (Subjects and formulas, Sample size statistics, Fecal samples, Microbiome, Microbiome statistics) and Results.*

| Field | Value |
|---|---|
| RoB tool applicable | **ROBINS-I** (non-randomized breastfed reference group per the hybrid-design rule) |

**ROBINS-I**

| Domain | Judgment | Reasoning |
|---|---|---|
| Confounding | Moderate | A baseline-characteristics comparison across all three groups found "most" characteristics comparable, but with a disclosed minor difference specifically involving the BF group (delivery mode "similar proportion between formula groups but slightly less than among infants who were breastfed"), and no statistical adjustment is used in the composition analyses themselves (Mann-Whitney U test only). |
| Selection of participants | Low | Large (n=221), rigorous pre-specified sample-size/power calculation, with detailed, itemized accounting of discontinuation reasons (parent request, lost to follow-up, adverse events, protocol violations, COVID-19). |
| Classification of exposures | Moderate | Formula-arm allocation is randomized and blinded; the BF reference group's specific ascertainment/verification method is not elaborated in the available text beyond being described as "reference breastfed infants." |
| Deviations from intended exposures | Low | Feeding compliance was tracked via caregiver diary during in-person visits and phone/electronic contact at scheduled intervals. |
| Missing data | Serious | Discontinuation was markedly and unevenly higher in the control-formula group (37.9%) compared with the BF reference group (11.2%) and test-formula group (15.2%) -- a substantial, disclosed, cross-group asymmetric attrition pattern (>3-fold higher in control formula vs. BF), even though individual reasons are well itemized. |
| Measurement of outcomes | Low | A rigorous, modern shotgun-metagenomics pipeline (NucleoSpin 96 Soil DNA extraction, Illumina sequencing, Clinical Microbiomics' metagenomic-species (MGS) profiling against a large curated database) applied uniformly. |
| Selection of the reported result | Moderate | No trial registration number is given anywhere in the available text, a notable gap for a trial of this scale and otherwise-detailed reporting; adverse-event and discontinuation reporting is itself highly transparent and itemized by group. |

**Microbiome-methods checklist (every study)**

| Domain | Judgment | Reasoning |
|---|---|---|
| Sample collection and storage method reported | Yes | "After obtaining informed consent on day 1, if a stool sample was available, 1 g of stool was collected and was subsequently frozen-stored (-20degC). Day 112 samples were brought to study site fresh, were coded, and frozen until shipment to Clinical Microbiomics." |
| DNA extraction method reported | Yes | "DNA was extracted from ~0.1 g aliquots of the fecal samples using the NucleoSpin 96 Soil (Macherey-Nagel) kit." |
| Sequencing depth reported | Not reported | No read-count or depth figure found anywhere in the available text. |
| Negative/positive contamination controls reported | Not reported | No mention anywhere in the available text of negative extraction/PCR controls or positive/mock-community controls. |
| Compositional-data handling reported | No | Microbiome statistics used "the Mann-Whitney U test" and "generalized fold change in gene-level abundances," with no compositional-aware transform (e.g., CLR/log-ratio) mentioned anywhere. |

---

## #880 — Public-data metagenome re-analysis 2022 (multi-national, pooled)

*Gut microbe metabolism of small molecules supports human development across the early
stages of life.* Front Microbiol. DOI 10.3389/fmicb.2022.1006721

Design: a fundamentally different study type from the rest of this batch -- a secondary
bioinformatic re-analysis pooling 6,617 publicly available shotgun metagenomic samples from
4,062 infants and 2,555 adults, drawn from 63 different SRA BioProjects (i.e., 63 separate
original studies with heterogeneous populations, countries, and protocols). The BF-vs-FF
comparison this review extracts uses 250 breastfed and 217 formula-fed samples from this
pooled dataset. No sample collection, DNA extraction, sequencing-depth, or contamination-
control detail is restated in this paper's own text for the underlying raw data -- only the
taxonomic/functional reprocessing pipeline applied uniformly after retrieval is described.

### J. Risk of bias

*Drafted 26 Oct 2026 from a fresh read of `full_text_md/10.3389_fmicb.2022.1006721/10.3389_fmicb.2022.1006721.md`'s Materials and methods (Sample collection, Data processing, Statistical analyses) and Results (Early infant feeding practices...).*

| Field | Value |
|---|---|
| RoB tool applicable | **ROBINS-I** (cross-sectional secondary analysis of pooled observational data) |

**ROBINS-I**

| Domain | Judgment | Reasoning |
|---|---|---|
| Confounding | Serious | No adjustment for study-of-origin/cohort/batch heterogeneity is described anywhere despite pooling samples from 63 different original BioProjects/studies, each with its own population, country, and protocol -- cohort-of-origin is a large, highly plausible, and entirely unaddressed confounder for a diet-associated comparison built this way. |
| Selection of participants | Serious | Samples were included based on availability and metadata completeness in public repositories rather than a prospectively designed sampling frame -- an inherently opportunistic selection process across 63 heterogeneous source studies, even though basic eligibility criteria (healthy, term, no antibiotics) are stated. |
| Classification of exposures | Serious | Feeding status was taken from each original study's own associated metadata, and this paper's own text uses the qualifying language "assumed or did not breast milk," signaling real uncertainty/imprecision in how consistently feeding status was defined and ascertained across 63 different source studies. |
| Deviations from intended exposures | Low | Cross-sectional secondary analysis of observational data with no assigned intervention to deviate from. |
| Missing data | No information | No information is given about how many of the underlying infants/samples had usable feeding-status metadata versus were excluded for missing or ambiguous metadata. |
| Measurement of outcomes | Moderate | Raw sequencing protocols varied across the 63 original source studies and are not harmonized or described in this paper's own text, but the taxonomic and functional reprocessing pipeline applied uniformly to all pooled reads after retrieval (METAnnotatorX2, Megablast with consistent alignment thresholds) is itself well-described and consistently applied. |
| Selection of the reported result | Moderate | No trial registration applicable (secondary meta-analytic study); results are reported with some complexity rather than a one-sided narrative (e.g., 64% of profiled GO terms were found to be more abundant in formula-fed rather than breastfed infants), but this is an inherently exploratory secondary analysis with no pre-registered hypothesis. |

**Microbiome-methods checklist (every study)**

| Domain | Judgment | Reasoning |
|---|---|---|
| Sample collection and storage method reported | Not reported | This paper analyzes pre-existing public sequencing data; sample collection and storage protocols belong to each of the 63 original source studies and are not restated here. |
| DNA extraction method reported | Not reported | Same as above -- DNA extraction is not described in this paper's own text for any of the pooled samples. |
| Sequencing depth reported | Not reported | No read-count or depth figure is given for the pooled dataset in this paper's own text. |
| Negative/positive contamination controls reported | Not reported | No mention anywhere in the available text of negative extraction/PCR controls or positive/mock-community controls for any of the pooled source data. |
| Compositional-data handling reported | No | Beta-diversity analyses used Bray-Curtis dissimilarity with PCoA/PERMANOVA/ANOSIM -- standard ecology methods with no compositional-aware transform (e.g., CLR/log-ratio) mentioned anywhere. |

---

## #913 — 5-HMO blend formula trial 2022 (Bulgaria/Hungary/Poland)

*Infant Formula With a Specific Blend of Five Human Milk Oligosaccharides Drives the Gut
Microbiota Development and Improves Gut Maturation Markers: A Randomized Controlled Trial.*
Front Nutr. DOI 10.3389/fnut.2022.920362

Design: hybrid -- large (n=789 enrolled), 32-site, double-blind RCT among three randomized
formula arms (CG, TG1 1.5 g/L 5-HMO, TG2 2.5 g/L 5-HMO) plus a non-randomized human-milk
reference group (HMG), ClinicalTrials.gov NCT03722550 -- routed to ROBINS-I per the
hybrid-design rule. This report covers secondary (microbiome) endpoints of a trial powered
for different co-primary endpoints.

### J. Risk of bias

*Drafted 26 Oct 2026 from a fresh read of `full_text_md/10.3389_fnut.2022.920362/10.3389_fnut.2022.920362.md`'s Subject and Methods (Study Design, Study Participants, Interventions, Microbiome Analysis, Statistics) and Results (Participants).*

| Field | Value |
|---|---|
| RoB tool applicable | **ROBINS-I** (non-randomized HMG reference group per the hybrid-design rule) |

**ROBINS-I**

| Domain | Judgment | Reasoning |
|---|---|---|
| Confounding | Moderate | Baseline characteristics were "largely comparable... except for longer maternal and paternal education and slightly older gestational age at birth in HMG compared with the formula-fed groups" -- a disclosed, real imbalance specifically involving the breastfed comparison group -- and no statistical adjustment for this is applied in the composition-comparison analyses (Kruskal-Wallis/PERMANOVA unadjusted), although baseline-adjusted ANCOVA is used for the separate fecal-biomarker analyses. |
| Selection of participants | Low | A transparent, CONSORT-referenced flow (Figure 1) explains the reduction from 789 enrolled to 535 analyzed via two explicit, methodologically reasoned criteria: a deliberate "first-in, first-served" random subsampling for stool collection (not all parents were asked to provide samples) and a precise, pre-specified >=80%-days feeding-compliance requirement for inclusion in the microbiota dataset. |
| Classification of exposures | Low | HMG required exclusive human milk from birth to enrollment with parental intent to continue to at least 4 months, and feeding compliance was tracked with an explicit, age-window-specific operational definition (>=80% of days compliant). |
| Deviations from intended exposures | Low | The >=80%-compliance requirement for inclusion in the microbiota dataset directly screens out infants with major exposure deviations, a methodologically sound as-fed (not purely as-randomized) analytic approach. |
| Missing data | Moderate | The reduction from 789 enrolled to 535 analyzed is substantial (32%), though transparently attributed to the deliberate stool-subsampling design and compliance filter rather than an unexplained loss. |
| Measurement of outcomes | Low | A rigorous, consistently applied shotgun-metagenomics pipeline (metagenomic species (MGS) profiling, phylogenetic-tree-based Faith's PD and weighted UniFrac diversity, rarefied abundances), though specific DNA-extraction-kit and sequencing-depth details are deferred to a prior publication. |
| Selection of the reported result | Low | Pre-registered (NCT03722550); the authors explicitly and candidly disclose that "this article reports the secondary endpoints of a study for which the sample size calculation was based on the two co-primary endpoints... therefore, no sample size calculation is available for the endpoints reported herein" -- transparent about this analysis's exploratory/underpowered status rather than presenting it as confirmatory. |

**Microbiome-methods checklist (every study)**

| Domain | Judgment | Reasoning |
|---|---|---|
| Sample collection and storage method reported | Yes | "Parents were instructed to immediately freeze the collected fecal samples in their freezer at home (~-20degC) and to bring them within 3 days to the study site where samples were frozen at -80degC until analysis. Transport to the study sites was done in cooling bags containing sufficient cool packs to keep samples frozen." |
| DNA extraction method reported | Not reported | "Microbial DNA was extracted from frozen feces, purified, and shotgun sequenced... as described previously" -- no specific kit or protocol is named in this paper's own text. |
| Sequencing depth reported | Not reported | Only "rarefied abundances" is mentioned generically, with no specific rarefaction threshold or read-count figure given anywhere in the available text. |
| Negative/positive contamination controls reported | Not reported | No mention anywhere in the available text of negative extraction/PCR controls or positive/mock-community controls. |
| Compositional-data handling reported | No | Beta diversity was calculated as "weighted UniFrac distance" with PCoA, a standard ecology approach with no compositional-aware transform (e.g., CLR/log-ratio) mentioned anywhere. |

---

## #926 — COGNIS study, synbiotic/LC-PUFA/MFGM formula trial 2022 (Spain)

*A synbiotics, long chain polyunsaturated fatty acids, and milk fat globule membranes
supplemented formula modulates microbiota maturation and neurodevelopment.* Clin Nutr.
DOI 10.1016/j.clnu.2022.05.013

Design: hybrid -- double-blind RCT between two formula arms (SF standard vs. EF
synbiotic/LC-PUFA/MFGM-supplemented, randomized 1:1) plus a non-randomized exclusively
breastfed reference group (n=50), COGNIS study, University of Granada, ClinicalTrials.gov
NCT02094547 -- routed to ROBINS-I per the hybrid-design rule. The authors' own Discussion
candidly acknowledges that "BF infants were not randomized for ethical reasons which may
explain their higher parental educational levels."

### J. Risk of bias

*Drafted 26 Oct 2026 from a fresh read of `full_text_md/10.1016_j.clnu.2022.05.013/10.1016_j.clnu.2022.05.013.md`'s Materials & methods (Subjects/design, DNA extraction, Sequencing, Statistical analysis) and Results/Discussion (Baseline characteristics, Limitations).*

| Field | Value |
|---|---|
| RoB tool applicable | **ROBINS-I** (non-randomized BF reference group, explicitly acknowledged by the authors) |

**ROBINS-I**

| Domain | Judgment | Reasoning |
|---|---|---|
| Confounding | Moderate | A real, disclosed imbalance exists ("maternal IQ and parent's educational level were significantly higher in BF than in formula groups, p<0.01"), explicitly tied by the authors to BF's non-randomized status; differential-abundance testing is generically described as "adjusted for covariates" (DESeq2) and broader variable effects assessed via envfit/collinearity-corrected logistic regression, but it is not explicit whether the specific IQ/education imbalance itself was among the adjustment covariates for the composition analyses. |
| Selection of participants | Moderate | A rigorous a priori power calculation (85 infants/formula group accounting for 20% dropout) and detailed eligibility criteria are given, but the authors themselves disclose "lower recruitment of BF infants used as reference group" and an inability to statistically examine exclusive formula feeding "due to low recruitment." |
| Classification of exposures | Low | Feeding groups are defined by specific, quantified thresholds (BF >=2 months exclusive; formula groups >70% or >4 doses/day), ascertained in part via a 3-day dietary record collecting quantitative feeding data -- a genuinely rigorous ascertainment approach. |
| Deviations from intended exposures | Low | Exclusion criteria specifically remove infants who deviated from their assigned feeding category ("exclusively breastfed infants who received formula for more than 25% of milk intake after the initial month 2 till month 6" were excluded). |
| Missing data | Moderate | A 20% dropout rate was anticipated in the sample-size design, and the authors specifically disclose that among dropout subjects, EF infants showed higher birth weight and length than SF ones (p=0.012; p=0.023) -- a specific, transparently reported signal of potentially non-random attrition. |
| Measurement of outcomes | Moderate | A reasonably described 16S pipeline (Illumina MiSeq, V1-V2 region, RDP classification) is used, but the authors themselves candidly note as a limitation that "species-level differences were not captured due to limitations of 16S rRNA sequencing with Illumina technology," and no sequencing-depth figures or contamination controls are reported. |
| Selection of the reported result | Low | Pre-registered (NCT02094547); the Discussion/Limitations section is unusually candid and self-critical, explicitly acknowledging the inability to examine exclusive formula feeding due to low recruitment, the non-randomized nature of the BF group and its likely confounding effect, and the species-level resolution limits of the sequencing method -- a notably transparent self-assessment. |

**Microbiome-methods checklist (every study)**

| Domain | Judgment | Reasoning |
|---|---|---|
| Sample collection and storage method reported | Yes | "Fresh stool samples were collected in sterile bottles at home by the parents... stored at -20degC for a maximum of 24 h until delivery to the laboratory, where they were stored [at] -80degC." |
| DNA extraction method reported | Not reported | "Genomic DNA was extracted from faecal bacteria as previously described" -- no specific kit or protocol is named in this paper's own text. |
| Sequencing depth reported | Not reported | No read-count or depth figure found anywhere in the available text. |
| Negative/positive contamination controls reported | Not reported | No mention anywhere in the available text of negative extraction/PCR controls or positive/mock-community controls. |
| Compositional-data handling reported | No | DESeq2 was used on "non-normalized raw count tables," and the text refers generically to "gut microbial compositional changes" without naming any compositional-aware transform (e.g., CLR/log-ratio) anywhere. |

---

## #937 — Inner Mongolia/Beijing delivery-mode x feeding-type cohort 2022 (China)

*Comparison of the Gut Microbiota in Healthy Infants With Different Delivery Modes and
Feeding Types: A Cohort Study.* Front Microbiol. DOI 10.3389/fmicb.2022.868227

Design: prospective cohort (4 sites, Beijing/Inner Mongolia, China), 2x2 factorial by
delivery mode (VD/CS) and feeding type (BF/FF >4 months), small and uneven group sizes
(VD-br n=10, VD-fo n=17, CS-br n=8, CS-fo n=27), sampled at 40 days, 3 months, and 6 months.

### J. Risk of bias

*Drafted 26 Oct 2026 from a fresh read of `full_text_md/10.3389_fmicb.2022.868227/10.3389_fmicb.2022.868227.md`'s Patients and Methods (Study Population, Study Design, Sample Collection, DNA Extraction/Sequencing, Statistical Analysis) and Results (Basic Characteristics).*

| Field | Value |
|---|---|
| RoB tool applicable | **ROBINS-I** (prospective cohort design) |

**ROBINS-I**

| Domain | Judgment | Reasoning |
|---|---|---|
| Confounding | Moderate | A formal baseline-comparison table found no statistically significant differences among the four groups, but antibiotic usage shows a numerically substantial and borderline-significant imbalance (CS-fo 10/27 exposed vs. CS-br 0/8; p=0.064) that is disclosed but not adjusted for in any subsequent microbiome analysis (unadjusted group comparisons only). |
| Selection of participants | Moderate | Clear eligibility/exclusion criteria are given, but group sizes are small and markedly uneven (10/17/8/27), and no original screening-to-enrollment flow is provided (only the later "64 followed up -> 62 included" step is detailed). |
| Classification of exposures | Moderate | BF/FF groups are clearly operationalized (BF: exclusive breastfeeding >4 months; FF: formula use "due to mother's disease or medicine, and other objective reasons"), ascertained prospectively through structured follow-up visits, though the heterogeneous reasons underlying formula-group assignment add some definitional variability. |
| Deviations from intended exposures | Low | Exclusion criteria specifically remove infants whose feeding deviated from their assigned category (BF infants unable to sustain exclusive breastfeeding to 4 months, or formula infants who changed formula before 4 months, were excluded). |
| Missing data | Moderate | "Among 64 infants who were followed up... two patients dropped. Finally, [62] babies were included" -- a small, specifically documented loss at this stage, though the original screening/enrollment flow leading to the 64 followed-up infants is not detailed. |
| Measurement of outcomes | Low | A rigorous, objective, well-documented 16S pipeline (CTAB/SDS DNA extraction, Illumina MiSeq, QIIME/Uparse, SILVA/RDP classification) with an explicit sequencing-depth figure reported. |
| Selection of the reported result | Moderate | No trial registration applicable (observational cohort study); the basic-characteristics table is reported candidly, including the borderline antibiotic-usage imbalance, rather than omitted, though this remains a small, exploratory, non-registered study. |

**Microbiome-methods checklist (every study)**

| Domain | Judgment | Reasoning |
|---|---|---|
| Sample collection and storage method reported | Yes | "All the samples were kept in a sterile container, immediately stored in a refrigerator at -70degC, and sent to Beijing for testing collectively." |
| DNA extraction method reported | Yes | "Total genome DNA from samples was extracted using the CTAB/SDS method. DNA concentration and purity were monitored on 1% agarose gels." |
| Sequencing depth reported | Yes | "A total of 20,383,186 reads (median 84,737 reads per sample) were obtained from 16S rRNA gene sequencing." |
| Negative/positive contamination controls reported | Not reported | No mention anywhere in the available text of negative extraction/PCR controls or positive/mock-community controls. |
| Compositional-data handling reported | No | "The relative abundance of operational taxonomic units (OTUs) was assessed" throughout, with beta diversity via unweighted/weighted UniFrac PCoA -- standard ecology methods with no compositional-aware transform (e.g., CLR/log-ratio) mentioned anywhere. |

---

## #959 — L. paracasei F19 formula trial 2022 (China/United States)

*Metabolic Phenotype and Microbiome of Infants Fed Formula Containing Lactobacillus
paracasei Strain F-19.* Front Pediatr. DOI 10.3389/fped.2022.856951

Design: hybrid -- multicenter (Nanjing/Shanghai/Beijing), double-blind RCT between two
formula arms (SF standard vs. F19 probiotic-supplemented) plus a non-randomized exclusively
breastfed reference group (BF), ClinicalTrials.gov NCT01755481 -- routed to ROBINS-I per the
hybrid-design rule. An exceptionally detailed, multi-stage exclusion flow is given
specifically for the 151-infant microbiome sub-cohort.

### J. Risk of bias

*Drafted 26 Oct 2026 from a fresh read of `full_text_md/10.3389_fped.2022.856951/10.3389_fped.2022.856951.md`'s Results (Study Participants) and Materials and Methods (Subjects, Fecal Microbiome Sequencing, Statistical Analysis).*

| Field | Value |
|---|---|
| RoB tool applicable | **ROBINS-I** (non-randomized BF reference group per the hybrid-design rule) |

**ROBINS-I**

| Domain | Judgment | Reasoning |
|---|---|---|
| Confounding | Moderate | The authors disclose that "a greater number of infants were delivered vaginally in the BF group compared to the F19 or SF groups, and the F19 group had a greater number of vaginally born infants compared to the SF group" -- a real, acknowledged imbalance -- and while the companion serum-metabolome analysis explicitly adjusts for "diet, sex, region, hospital, and mode of delivery" via two-way ANOVA, the microbiome composition analysis itself (PERMANOVA/Kruskal-Wallis/ANCOM) does not appear to apply the same covariate adjustment. |
| Selection of participants | Low | An exceptionally detailed, multi-stage, numerically explicit exclusion flow is given specifically for the microbiome sub-cohort: 151 randomly selected (51 BF/50 SF/50 F19) -> excluded for qPCR-negative probiotic status (1), non-exclusive breastfeeding (13), and antibiotic treatment during the intervention (3 BF/9 SF/6 F19) -> final 37 BF/43 F19/41 SF. |
| Classification of exposures | Low | BF required documented parental intent to breastfeed for at least 5 months with >=80% of calories from breast milk, verified via "a monthly three-day intake record" -- a quantified, periodically-reverified ascertainment protocol. |
| Deviations from intended exposures | Low | The 13 non-exclusively-breastfed infants identified in the nominal BF group were specifically identified and excluded from the microbiome analysis, directly addressing exposure deviations rather than analyzing by nominal group alone. |
| Missing data | Low | The same detailed, transparent exclusion accounting documented under Selection of participants applies directly here. |
| Measurement of outcomes | Low | Rigorous, objective, well-validated methodology throughout, including confirmatory quantitative PCR to verify actual F19 probiotic strain presence in stool (rather than relying on assigned group alone) and standardized NMR-based serum metabolomics with internal standards. |
| Selection of the reported result | Low | Pre-registered (NCT01755481) with a previously published companion clinical-outcomes paper establishing the trial design in advance of this sub-analysis; non-significant findings are reported transparently (e.g., "we did not find any difference in the frequency of antibiotic use or diarrheal episodes among groups," and a metabolome finding explicitly noted as "not significant for the subset of infants used for microbiota analysis"). |

**Microbiome-methods checklist (every study)**

| Domain | Judgment | Reasoning |
|---|---|---|
| Sample collection and storage method reported | Yes | "Placed in a freezer bag and stored at -20degC in a home freezer until the hospital visit. At the hospital, samples were placed in a -20degC freezer and stored until transport on dry ice." |
| DNA extraction method reported | Not reported | "DNA from fecal samples was isolated and V4 hypervariable region... was amplified... as described" -- no specific kit or protocol is named in this paper's own text. |
| Sequencing depth reported | Not reported | No read-count or depth figure found anywhere in the available text. |
| Negative/positive contamination controls reported | Not reported | "48 quality control samples" are mentioned as having been pre-processed alongside the study samples, but the text does not specify whether these were negative (blank/reagent) or positive (mock-community) contamination controls versus another kind of technical QC sample, so this cannot be confidently credited as a contamination control. |
| Compositional-data handling reported | Yes | "Differential abundance analysis of each taxon was determined using ANCOM (Analysis of composition of microbiomes)" -- an explicitly named, genuine compositional-data-analysis method. |

---

## #961 — INCA cohort antibiotics/feeding-mode study 2022 (Netherlands)

*Effect of antibiotics in the first week of life on faecal microbiota development.* Arch Dis
Child Fetal Neonatal Ed. DOI 10.1136/archdischild-2021-322861

Design: prospective cohort (INCA study, Netherlands; NCT02536560, same registered cohort as
companion paper #572), subset of 182 infants (1,128 samples) exclusively BF or FF in the
first 3 months. Primary exposure is early-life antibiotic use, with feeding mode analyzed
as an effect-modifier/stratification variable for antibiotic-associated microbiota
deviations, following a sophisticated data-driven, AIC/BIC-guided confounder-selection
approach.

### J. Risk of bias

*Drafted 26 Oct 2026 from a fresh read of `full_text_md/10.1136_archdischild-2021-322861/10.1136_archdischild-2021-322861.md`'s Materials and Methods (Study design, Data/faeces collection, 16S sequencing, statistical analysis) and Results.*

| Field | Value |
|---|---|
| RoB tool applicable | **ROBINS-I** (prospective cohort design) |

**ROBINS-I**

| Domain | Judgment | Reasoning |
|---|---|---|
| Confounding | Low | A genuinely data-driven, principled approach: alpha-diversity models were "corrected for the baseline characteristic that differed significantly between" exposure groups (gestational age, birth weight), and relative-abundance models explicitly tested delivery mode, feeding mode, and additional antibiotic exposure as candidate covariates via AIC/BIC-based model selection rather than an ad hoc inclusion decision. |
| Selection of participants | Moderate | A clearly defined cohort subset (182 infants, 1,128 samples) with a referenced sample-selection flow diagram (online supplemental figure 1, not visible in this extraction), but the flow itself cannot be directly verified from the available text. |
| Classification of exposures | Low | "Feeding mode was reported monthly during the first year of life" -- a genuinely prospective, continuously repeated-measures ascertainment, among the more rigorous approaches in this review. |
| Deviations from intended exposures | Low | Observational cohort design with no intervention to deviate from. |
| Missing data | Low | The authors transparently restricted their reported feeding/delivery-mode-stratified analyses to samples from 1 week onward specifically "due to the relatively low number of faecal samples in the first week per feeding and delivery type," a responsible handling of data sparsity rather than reporting unreliable early-timepoint estimates. |
| Measurement of outcomes | Low | A rigorous, extensively validated pipeline (QIAamp DNA Stool Mini kit, explicit sequencing depth of ~44,934 reads/sample, NG-Tax 2.0, SILVA v128) with two synthetic mock communities sequenced as positive controls. |
| Selection of the reported result | Low | Registered (NCT02536560) as part of a previously described cohort protocol; extensive null and mixed findings are reported transparently across many sub-analyses (e.g., "AB exposure... did not alter microbial alpha diversity," "ABAMX not deviating from AB-baseline," "no AB-mediated deviations were noted between C-section born infants") rather than a one-sided narrative. |

**Microbiome-methods checklist (every study)**

| Domain | Judgment | Reasoning |
|---|---|---|
| Sample collection and storage method reported | Yes | "Until discharge from the hospital, faeces were sampled from diapers by hospital staff and immediately frozen at -20degC. Sampling continued at home by the parents, using sampling instructions and freezer storage... At the hospital, all samples were stored at -20degC." |
| DNA extraction method reported | Yes | "DNA was extracted from a maximum of 200 mg of the homogenised faecal sample at GenProbio srl (Parma, Italy) with the QIAamp DNA Stool Mini kit according to manufacturer's instructions." |
| Sequencing depth reported | Yes | "Sequencing resulted in ~44,934 (SD 17,205) reads per sample." |
| Negative/positive contamination controls reported | Yes | "Two synthetic mock communities were sequenced as positive controls." |
| Compositional-data handling reported | No | Beta diversity was calculated via weighted/unweighted UniFrac distances and relative abundances were modeled with beta regression -- standard ecology methods with no compositional-aware transform (e.g., CLR/log-ratio) mentioned anywhere. |

---

## #985 — LIFE study prebiotic/postbiotic formula trial 2021 (Netherlands)

*Early-life fecal microbiome and metabolome dynamics in response to an intervention with
infant formula containing specific prebiotics and postbiotics.* Am J Physiol Gastrointest
Liver Physiol. DOI 10.1152/ajpgi.00079.2021

Design: hybrid -- randomized, double-blind RCT (LIFE study, Netherlands Trial Register
NTR3455) between an experimental scGOS/lcFOS-prebiotic-plus-Lactofidus-postbiotic formula and
a non-fermented control formula, plus a non-randomized exclusively breastfed reference arm.
A deliberately balanced 90-subject subgroup (30/arm) was selected with vaginal-delivery-only
and antibiotic/probiotic/laxative-exclusion criteria. Routed to ROBINS-I per the
hybrid-design rule.

### J. Risk of bias

*Drafted 26 Oct 2026 from a fresh read of `full_text_md/10.1152_ajpgi.00079.2021/10.1152_ajpgi.00079.2021.md`'s Materials and Methods (trial description, DNA Extraction, Amplicon Sequencing Analysis).*

| Field | Value |
|---|---|
| RoB tool applicable | **ROBINS-I** (non-randomized breastfed reference group per the hybrid-design rule) |

**ROBINS-I**

| Domain | Judgment | Reasoning |
|---|---|---|
| Confounding | Low | A deliberately balanced subgroup (30 infants per arm) was selected, with baseline characteristics (gestational age, birth weight, maternal age, ethnicity, number of siblings) explicitly checked and confirmed "balanced over the study groups," and delivery mode, antibiotic use, probiotic use, and laxative use were all controlled by exclusion criteria for this specific subgroup. |
| Selection of participants | Moderate | The subgroup-selection criteria (vaginal delivery, no probiotics/antibiotics/laxatives) are clearly stated, but the relationship between this 90-subject subgroup and the full LIFE trial population (how many were eligible vs. excluded) is not detailed in the available text. |
| Classification of exposures | Moderate | Formula-arm allocation is randomized and double-blind; the BF group's specific ascertainment/verification method is not elaborated in the available text beyond being described as "exclusively breast-fed." |
| Deviations from intended exposures | Low | "There was no use of concomitant drinks or foods before 17 wk of age in the study population," explicitly confirming protocol adherence regarding complementary feeding timing. |
| Missing data | Low | Attrition is minor and specifically quantified (Table 2 gives exact per-arm, per-timepoint sample counts, e.g., 27-30 of 30 target for 16S sequencing at each timepoint), attributed to insufficient fecal mass for some analyses rather than unexplained loss. |
| Measurement of outcomes | Moderate | A reasonably described 16S pipeline (QIAmp DNA Stool Mini Kit, 454 pyrosequencing, QIIME 1.8.0, USEARCH 97% OTU clustering, RDP/SILVA classification) is used, though no sequencing-depth figures or contamination controls are reported, and the sequencing platform (454 FLX) is older relative to more recent Illumina-based studies in this review. |
| Selection of the reported result | Low | Registered (NTR3455) with the trial design and primary clinical outcomes previously published separately, reducing concern about post hoc outcome-switching for this microbiome/metabolome sub-analysis. |

**Microbiome-methods checklist (every study)**

| Domain | Judgment | Reasoning |
|---|---|---|
| Sample collection and storage method reported | Yes | "Samples were collected from the diaper in a 10-mL sterile collection tube (no preservatives) at home and were frozen at -12degC or colder immediately... stored at -18degC or, if possible, at -80degC... shipped on dry ice... and stored at -80degC for later analysis." |
| DNA extraction method reported | Yes | "DNA extraction from stool samples was performed with the QIAmp DNA Stool Mini Kit (Qiagen) according to the manufacturer's protocol except for the addition of two bead-beating steps," described in full detail. |
| Sequencing depth reported | Not reported | No read-count or depth figure found anywhere in the available text. |
| Negative/positive contamination controls reported | Not reported | No mention anywhere in the available text of negative extraction/PCR controls or positive/mock-community controls for the 16S workflow (the metabolomics section describes internal-standard/pooled-sample QC, a different purpose). |
| Compositional-data handling reported | No | Standard QIIME 1.8.0 OTU-based relative-abundance workflow with no compositional-aware transform (e.g., CLR/log-ratio) mentioned anywhere. |

---

## #989 — Nemours/CHOP metagenomics feeding study 2022 (United States)

*Impact of Early Feeding: Metagenomics Analysis of the Infant Gut Microbiome.* Front Cell
Infect Microbiol. DOI 10.3389/fcimb.2022.816601

Design: small (n=34; 24 BF, 10 FF), single-center, cross-sectional shotgun-metagenomics study
(Nemours/Children's Hospital of Philadelphia), variable age at sampling (5-100 days).
Exceptionally rigorous contamination-control and orthogonal-validation methodology.

### J. Risk of bias

*Drafted 26 Oct 2026 from a fresh read of `full_text_md/10.3389_fcimb.2022.816601/10.3389_fcimb.2022.816601.md`'s Materials and Methods (Subject Enrollment, Sample Collection, DNA Extraction/Sequencing, Direct PCR Validation) and Results (Patient Demographics).*

| Field | Value |
|---|---|
| RoB tool applicable | **ROBINS-I** (cross-sectional observational design) |

**ROBINS-I**

| Domain | Judgment | Reasoning |
|---|---|---|
| Confounding | Serious | The authors explicitly report "no statistical differences... between the BF and FF cohort except for delivery method (p-value <0.01)" -- a real, disclosed, statistically significant imbalance -- but no statistical adjustment for delivery mode is applied in the differential-abundance analyses (edgeR/DESeq2 group comparisons). |
| Selection of participants | Moderate | Clear eligibility/exclusion criteria are given (no antibiotic exposure, no GI disease, no dietary restrictions), but this is a small, single-center convenience sample with no recruitment-flow numbers (how many eligible infants were approached vs. enrolled). |
| Classification of exposures | Moderate | Groups are clearly labeled "exclusively breast fed" and "exclusively formula fed," but the specific ascertainment method is not elaborated in the available text. |
| Deviations from intended exposures | Low | Cross-sectional observational design with no intervention to deviate from. |
| Missing data | Low | "Thirty-four subjects were enrolled, and duplicate fecal samples were processed for each subject," with no stated loss or incomplete data. |
| Measurement of outcomes | Low | One of the most rigorous contamination-control setups in this review: "extraction controls (no template) and DNA free water were included to empirically assess environmental and reagent contamination," plus a 3-organism laboratory-generated mock community (*Vibrio campbellii*, *Cryptococcus diffluens*, Lambda phage) as positive controls -- further strengthened by an orthogonal direct-PCR/gel-electrophoresis validation step for specific differentially-represented genes. |
| Selection of the reported result | Moderate | No trial registration applicable (small observational study); the dedicated PCR-validation step for specific findings is a strong methodological-rigor signal against false positives, though no pre-registration exists for this exploratory analysis. |

**Microbiome-methods checklist (every study)**

| Domain | Judgment | Reasoning |
|---|---|---|
| Sample collection and storage method reported | Yes | "Stool was collected by application of two duplicate swabs... The containers were placed immediately into a dry ice ethanol bath and then transferred to a -80degC freezer until processing." |
| DNA extraction method reported | Yes | "DNA was extracted from samples using the DNeasy PowerSoil kit using the manufacturer's instructions (Qiagen, Germantown, MD)." |
| Sequencing depth reported | Not reported | The text states "NGS read depths are listed in Supplemental Table 1," but no specific depth figure is given directly in the paper's own main text. |
| Negative/positive contamination controls reported | Yes | "Extraction controls (no template) and DNA free water were included to empirically assess environmental and reagent contamination. Laboratory-generated mock communities consisting of DNA from *Vibrio campbellii*, *Cryptococcus diffluens*, and Lambda phage were included as positive controls." |
| Compositional-data handling reported | No | "Trimmed mean of M-values normalization" (TMM, via edgeR) was used -- an RNA-seq-derived library-size normalization method, not a named compositional-data-analysis (CoDA) transform such as CLR/ALR; no such method is mentioned anywhere. |

---

## #991 — STRONG Kids 2 vitamin K/microbiome study 2022 (United States)

*Feeding Practice and Delivery Mode Are Determinants of Vitamin K in the Infant Gut: An
Exploratory Analysis.* Curr Dev Nutr. DOI 10.1093/cdn/nzac019

Design: cross-sectional (single timepoint, 6 weeks postpartum), sub-study of the STRONG
Kids 2 birth cohort (same parent cohort as #415), n=46 (23 BF, 23 FF) matched mother-infant
dyads, deliberately co-stratified by delivery mode (10 CS/13 VD within each feeding group) in
a balanced factorial design. Explicitly self-labeled "An Exploratory Analysis."

### J. Risk of bias

*Drafted 26 Oct 2026 from a fresh read of `full_text_md/10.1093_cdn_nzac019/10.1093_cdn_nzac019.md`'s Methods (Selection and description of participants, DNA extraction, Sequencing, Statistical analyses) and Results/Discussion.*

| Field | Value |
|---|---|
| RoB tool applicable | **ROBINS-I** (cross-sectional observational design) |

**ROBINS-I**

| Domain | Judgment | Reasoning |
|---|---|---|
| Confounding | Low | Mother-infant dyads were deliberately "matched for demographic characteristics" between BF and FF groups, and delivery mode was balanced by design within each feeding group (10 CS/13 VD in both), with the statistical model explicitly including feeding, delivery, and their interaction as factors rather than leaving delivery mode confounded with feeding. |
| Selection of participants | Low | The authors transparently disclose a deliberate, power-driven oversampling of cesarean-delivered infants relative to the full STRONG Kids 2 cohort (43% vs. 25.6%) and explicitly discuss its implications in their own Limitations ("this may have introduced some bias and reduced generalizability to the US population") -- a disclosed, by-design stratification choice rather than an undocumented selection artifact. |
| Classification of exposures | Moderate | Groups are clearly labeled "exclusively breastfeeding" or "formula-feeding," but the specific ascertainment method is not restated in this paper's own text (inherited from the parent STRONG Kids 2 cohort protocol). |
| Deviations from intended exposures | Low | Cross-sectional observational design with no intervention to deviate from. |
| Missing data | Low | All 46 planned/matched samples (23 BF + 23 FF) were sequenced and analyzed, with no apparent loss. |
| Measurement of outcomes | Low | A rigorous, objective shotgun-metagenomics pipeline (QIAamp Fast DNA Stool Mini Kit, Illumina NovaSeq, MetaPhlAn2 taxonomic profiling, KneadData/DIAMOND/MEGAN6 functional annotation) with an explicit sequencing-depth range reported. |
| Selection of the reported result | Low | No trial registration applicable (the paper is explicitly self-labeled "An Exploratory Analysis" in its own title); findings are reported comprehensively (taxonomic, functional-gene, and multiple vitamin K forms) alongside a candid Limitations section acknowledging both the relative-abundance-only measurement and the deliberate cesarean-oversampling design choice. |

**Microbiome-methods checklist (every study)**

| Domain | Judgment | Reasoning |
|---|---|---|
| Sample collection and storage method reported | Yes | "Samples for vitamin K analysis were stored at -80degC prior to shipment on dry ice to Tufts University, and then stored again at -80degC until analysis." |
| DNA extraction method reported | Yes | "DNA was extracted from ~200 mg of feces by the QIAamp Fast DNA Stool Mini Kit (Qiagen) in combination with bead beating on the FastPrep-24 System (MP Biomedicals)." |
| Sequencing depth reported | Yes | "Over 1.57 billion sequences (range = 10,980,603-49,565,363 reads per sample) were used for further analysis." |
| Negative/positive contamination controls reported | Not reported | No mention anywhere in the available text of negative extraction/PCR controls or positive/mock-community controls. |
| Compositional-data handling reported | No | "The relative abundance of bacterial species from each sample was log-transformed prior to RDA" -- a plain log transform of relative abundance, not a named compositional-aware method (e.g., CLR/log-ratio with a geometric-mean denominator); the authors themselves note as a limitation that "bacterial data were assessed on a relative abundance basis." |

---
