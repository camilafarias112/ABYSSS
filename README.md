
# ABYSSS
Agent Based ImmunologY SystemS Simulator is a side project associated with the Code Review Meeting, led by Dr. Kyle Bittinger at Upenn. 

AIM: To create something (tools/program/app/workflow/…) that can help professionals in the area of Computational Biology and Bioinformatics to learn aspects of the Immune System.

We would like to model the immunity against Staph Aureus in the keratinocytes. (LINK PAPER)

Our options to implement are: NetLogo, Mesa (Python), DSAIRM (R)

The "compartments" that we would like to model:

S. aureus (SA)
 + Constant rate of replication
 - Neutrophil count

Innate immunity (IL1alpha and chemokines)
 + Levels of s. aureus as a function of distance it has traveled into the skin
 - diffuses out

Neutrophils
 + Rate of increase as a function of innate immunity signals
 - Rate of diffusion out of the skin layer


After we model the homeostasis, we can "distrupt" the system and see if the model behaves appropriately.
1) Injury to the skin- > reduce the thickness
2) Model drug that inhibits innate immunity signaling
3) Host polymorphisms that inhibit innate immunity signaling
