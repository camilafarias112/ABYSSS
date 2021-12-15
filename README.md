
# ABYSSS
Agent Based ImmunologY SystemS Simulator is a side project associated with the Code Review Meeting, led by Dr. Kyle Bittinger at Upenn. 

AIM: We would like to model the immunity against Staphylococcus aureus in the keratinocytes as it's described in the [review paper](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5868361/) by Miller et al usign agent based modeling. We are especially interested in modeling the cascade of events illustrated in Figures 3a and 3b.

We have 3 platforms to use for this purpose: NetLogo, Mesa (Python), DSAIRM (R)

We have simplified a quite complicated cascade into three compartments that we can more easily model. The "+" sign represents the events that increase the levels and the "-" sign represents the events that lead to a decrease.

1) S. aureus (SA)

 \+ Constant rate of replication
 
 \- Neutrophil count

2) Innate immunity signals (IL1alpha and chemokines)

 \+ Levels of s. aureus as a function of distance it has traveled into the skin

\- diffuses out

3) Neutrophils

\+ Rate of increase as a function of innate immunity signals

\- Rate of diffusion out of the skin layer



After we model the homeostasis, we can "distrupt" the system and see if the model behaves appropriately.
1) Injury to the skin -> reduce the thickness
2) Model drug that inhibits innate immunity signaling or host polymorphisms that inhibit innate immunity signaling
3) A different strain of S. aureus that replicates faster
