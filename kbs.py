from experta import *
import schema
class a_fact(Fact):
    name = Field(str, mandatory=True)
    cf = Field(float, default=100.0)
    answer = Field(str, mandatory=True)


class questionnaire(Fact):
    a_fact = Field(str,mandatory=True)
    the_questionnaire= Field(str,mandatory=True)
    already_asked=Field(schema.Or(True, False),default=False)
    

    
class JOBEX(KnowledgeEngine):
    def __init__(self):
        self.max_cf = 0.0
        super().__init__()
    
    @DefFacts()
    def init(self):
        yield questionnaire(a_fact="Q9",
                           the_questionnaire="Tooth pain when chewing? ")
        yield questionnaire(a_fact="Q10",
                            the_questionnaire="fever? ")
        yield questionnaire(a_fact="Q11",
                            the_questionnaire="wooth pain when there is a contact with the tongue? ")
        yield questionnaire(a_fact="Q12",
                            the_questionnaire="pain reaches the temple of the ear of eye? ")
        yield questionnaire(a_fact="Q13",
                            the_questionnaire="cavities experience pain when eating? ")
        yield questionnaire(a_fact="Q14",
                            the_questionnaire="teeth feel throbbing? ")
        yield questionnaire(a_fact="Q15",
                            the_questionnaire="there is a deep and large hole in the tooth? ")
        yield questionnaire(a_fact="Q16",
                            the_questionnaire="sensitive teeth? ")
        yield questionnaire(a_fact="Q17",
                            the_questionnaire="pain when biting food? ")
        yield questionnaire(a_fact="Q18",
                            the_questionnaire="small hole in the tooth? ")
        yield questionnaire(a_fact="Q19",
                            the_questionnaire="blackish or brownsish stuns in the tooth? ")
      
    @Rule(salience = 10000)
    def start(self):
        print(""+"\n")
        print("The JOBEX career quiz will help you decide the sort of jobs that will suit you best:"+"\n")
        print("-------------------------------------"+"\n")
        print("Accepted replies:"+"\n")
        print(" Value           Meaning "+"\n")
        print("-------------------------------------"+"\n")
        print("  0              Not sure at all "+"\n")
        print("  0.4            Maybe "+"\n")
        print("  0.6            Probably "+"\n")
        print("  0.8            Almost certainly "+"\n")
        print("  1              Definitely "+"\n")
        print(""+"\n")
        
        
        
    @Rule(
    AS.f << questionnaire(a_fact=MATCH.the_fact,
                           the_questionnaire=MATCH.the_question,
                           already_asked=False)
                            )
    def ask_a_questionnaire(self, f, the_fact, the_question):
        self.modify(f, already_asked=True)
        accepted = [0, 0.4, 0.6, 0.8, 1.0]
        result = self.next_questionnaire(the_question, accepted)
        if result[0] is not None:
            certainty = result[0]
            fanswer = result[1]
            self.declare(a_fact(name=the_fact, cf=certainty, answer=fanswer))
    def next_questionnaire(self,questionnaire,allowed_values):
        print(["Yes, No"])
        print(questionnaire, "\n")
        answer = input()
        if answer.lower() == "yes" or answer.lower() == "y":
            print("reply: ", "\n")
            try:
                reply = float(input())
            except:
                reply = 10000
            while reply not in allowed_values:
                print(questionnaire, "\n")
                print("reply: ", "\n")
                try:
                    reply = float(input())
                except:
                    reply = 1000
                print("\n")
            return [float(reply), answer]
        else:
            return [0.00,answer]

    @Rule( 
            a_fact(name = "Q16",cf= MATCH.cf2, answer ="yes"),
          ) 
    def rule51(self,cf2):
        cf_ = cf2*0.7
        self.declare(a_fact(name="Detal caries11",cf=cf_, answer = "None"))
        
    @Rule( 
            a_fact(name = "Q17",cf= MATCH.cf2, answer ="yes"), 
         )
    def rule52(self,cf2):
        cf_ = cf2*0.85
        self.declare(a_fact(name="Detal caries12",cf=cf_, answer = "None"))
        
    @Rule( 
            a_fact(name = "Q18",cf= MATCH.cf2, answer ="yes")
         )
    def rule53(self,cf2):
        cf_ = cf2*0.8
        self.declare(a_fact(name="Detal caries13",cf=cf_, answer = "None"))
    
    @Rule( 
            a_fact(name = "Q19",cf= MATCH.cf2, answer ="yes"),
         )
    def rule54(self,cf2):
        cf_ = cf2*0.95
        self.declare(a_fact(name="Detal caries14",cf=cf_, answer = "None"))
    
    @Rule( 
            a_fact(name = "Q15",cf= MATCH.cf2, answer ="yes"),
         )
    
    def rule55(self,cf2):
        cf_ = cf2*0.95
        self.declare(a_fact(name="Reverse01",cf=cf_, answer = "None"))
        
    @Rule( 
            a_fact(name = "Q14",cf= MATCH.cf2, answer ="yes"),
         )
    
    def rule56(self,cf2):
        cf_ = cf2*0.95
        self.declare(a_fact(name="Reverse02",cf=cf_, answer = "None"))
        
    @Rule( 
            a_fact(name = "Q13",cf= MATCH.cf2, answer ="yes"),
         )
    
    def rule57(self,cf2):
        cf_ = cf2*0.95
        self.declare(a_fact(name="Reverse03",cf=cf_, answer = "None"))
        
    @Rule( 
            a_fact(name = "Q12",cf= MATCH.cf2, answer ="yes"),
         )
    
    def rule58(self,cf2):
        cf_ = cf2*0.95
        self.declare(a_fact(name="Reverse04",cf=cf_, answer = "None"))
        
    @Rule( 
            a_fact(name = "Q11",cf= MATCH.cf2, answer ="yes"),
         )
    
    def rule59(self,cf2):
        cf_ = cf2*0.95
        self.declare(a_fact(name="Reverse05",cf=cf_, answer = "None"))
        

   
   


   
    @Rule(
        AND(
            a_fact(name = "Q19",cf= MATCH.cf19, answer ="yes"),
            a_fact(name = "Q18",cf= MATCH.cf18, answer ="yes"),
            a_fact(name = "Q17",cf= MATCH.cf17, answer ="yes"),
            a_fact(name = "Q16",cf= MATCH.cf16, answer ="yes"),

          )
         )
    def rule1(self,cf19,cf18,cf17,cf16):
        cf19 = cf19*0.8
        cf18 = cf18*0.8
        cf17 = cf17*0.9
        cf16 = cf16*0.95
        cf22 = cf19+cf18-(cf19*cf18)
        cf11 = cf16+cf17-(cf16*cf17)
        cf = cf11+cf22-(cf11*cf22)
        print("-------------------------------------"+"\n")
        print(" The diagnose is Detal caries with  cf ",cf)
        print("-------------------------------------"+"\n\n")
        self.halt()
            
    @Rule( 
        
        AND(
            a_fact(name = "Q19",cf= MATCH.cf1, answer ="yes"),
            a_fact(name = "Q17",cf= MATCH.cf2, answer ="yes"),
            a_fact(name = "Q16",cf= MATCH.cf3, answer ="yes"),
          )
        )  
         
    def rule2(self,cf1,cf2,cf3):
        cf1 = cf1*0.8
        cf2 = cf2*0.8
        cf3 = cf3*0.8
        cf11 = cf1+cf2-(cf1*cf2)
        cf_ = cf11+cf3-(cf3*cf11)
        self.declare(a_fact(name="Detal caries",cf=cf_, answer = "None"))

        


    @Rule( 
        AND (
            a_fact(name = "Q18",cf= MATCH.cf1, answer ="yes"),
            a_fact(name = "Q17",cf= MATCH.cf2, answer ="yes"),
            a_fact(name = "Q19",cf= MATCH.cf3, answer ="yes"),
          )
        )  
    def rule3(self,cf1,cf2,cf3):
        print("here")
        cf1 = cf1*0.8
        cf2 = cf2*0.8
        cf3 = cf3*0.8
        cf11 = cf1+cf2-(cf1*cf2)
        cf_ = cf11+cf3-(cf3*cf11)
        self.declare(a_fact(name="Detal caries1",cf=cf_,answer = "None"))
    

    @Rule( 
         AND(
            a_fact(name = "Q18",cf= MATCH.cf1, answer ="yes"),
            a_fact(name = "Q17",cf= MATCH.cf2, answer ="yes"),
            a_fact(name = "Q16",cf= MATCH.cf1, answer ="yes"),
          ) 
        )  
    def rule4(self,cf1,cf2,cf3):
        cf1 = cf1*0.8
        cf2 = cf2*0.8
        cf3 = cf3*0.8
        cf11 = cf1+cf2-(cf1*cf2)
        cf_ = cf11+cf3-(cf3*cf11)
        self.declare(a_fact(name="Detal caries2",cf=cf_, answer = "None"))
    
    @Rule( 
        AND(
            a_fact(name = "Q18",cf= MATCH.cf1, answer ="yes"),
            a_fact(name = "Q16",cf= MATCH.cf2, answer ="yes"),
          ) 
         )
    def rule21(self,cf1,cf2):
        cf1 = cf1*0.8
        cf2 = cf2*0.8
        cf_ = cf1+cf2-(cf2*cf1)
        self.declare(a_fact(name="Detal caries3",cf=cf_, answer = "None"))
    
    @Rule( 
        AND(
            a_fact(name = "Q18",cf= MATCH.cf1, answer ="yes"),
            a_fact(name = "Q19",cf= MATCH.cf2, answer ="yes"),
          ) 
         )
    def rule21(self,cf1,cf2):
        print("here")
        cf1 = cf1*0.8
        cf2 = cf2*0.8
        cf_ = cf1+cf2-(cf2*cf1)
        self.declare(a_fact(name="Detal caries7",cf=cf_, answer = "None"))
    
    
    
    @Rule( 
        AND(
            a_fact(name = "Q18",cf= MATCH.cf1, answer ="yes"),
            a_fact(name = "Q17",cf= MATCH.cf2, answer ="yes"),
          )
         )
    def rule6(self,cf1,cf2):
        print("here") 
        cf1 = cf1*0.8
        cf2 = cf2*0.8
        cf_ = cf1+cf2-(cf2*cf1)
        self.declare(a_fact(name="Detal caries4",cf=cf_, answer = "None"))
    
    @Rule( 
        AND(
            a_fact(name = "Q19",cf= MATCH.cf1, answer ="yes"),
            a_fact(name = "Q16",cf= MATCH.cf2, answer ="yes"),
          )
         )
    def rule7(self,cf1,cf2):
        cf1 = cf1*0.8
        cf2 = cf2*0.8
        cf_ = cf1+cf2-(cf2*cf1)
        self.declare(a_fact(name="Detal caries5",cf=cf_,answer = "None"))
    


    @Rule( 
        AND(
            a_fact(name = "Q16",cf= MATCH.cf1, answer ="yes"),
            a_fact(name = "Q17",cf= MATCH.cf2, answer ="yes"),
          )
         )
    def rule8(self,cf1,cf2):
        cf1 = cf1*0.8
        cf2 = cf2*0.8
        cf_ = cf1+cf2-(cf2*cf1)
        self.declare(a_fact(name="Detal caries6",cf=cf_,answer = "None"))

    
    @Rule(
        AND(
            a_fact(name = "Q15",cf= MATCH.cf17, answer ="yes"),
            a_fact(name = "Q16",cf= MATCH.cf16, answer ="No"),

          )
         )
    def rule9(self,cf16,cf17):
        cf11 = cf16+cf17(cf16*cf17)
        cf_ = 0.95+cf11-(cf11*0.95)
        self.declare(a_fact(name="Reverse",cf=cf_, answer = "None"))
        
    
        
    @Rule(
        AND(
            
            a_fact(name = "Q14",cf= MATCH.cf5, answer ="yes"),
            a_fact(name = "Q13",cf= MATCH.cf4, answer ="yes"),
            a_fact(name = "Q12",cf= MATCH.cf3, answer ="yes"),
            a_fact(name = "Q11",cf= MATCH.cf2, answer ="yes"),
            a_fact(name = "Q10",cf= MATCH.cf1, answer ="yes"),

          )
         )
    def rule10(self,cf1,cf2,cf3,cf4,cf5):
        cf1 = cf1*0.75
        cf2 = cf2*0.95
        cf3 = cf3*0.9
        cf4 = cf4*0.95
        cf5 = cf5*0.7
        cf11 = cf1+cf2-(cf2*cf1)
        cf22 = cf3+cf4-(cf3*cf4)
        cf33 = cf22+cf11-(cf11*cf22)
        cf_ = cf33+cf5-(cf5*cf33)
        print("-------------------------------------"+"\n")
        print(" The diagnose is Irrevesable pulpitis with  cf ",cf_)
        print("-------------------------------------"+"\n\n")
        self.halt()
    


    @Rule(
         AND(  
            a_fact(name = "Q13",cf= MATCH.cf4, answer ="yes"),
            a_fact(name = "Q12",cf= MATCH.cf3, answer ="yes"),
            a_fact(name = "Q11",cf= MATCH.cf2, answer ="yes"),
            a_fact(name = "Q10",cf= MATCH.cf1, answer ="yes"),

          )
               
        )
    def rule11(self,cf1,cf2,cf3,cf4):
        cf1 = cf1*0.75
        cf2 = cf2*0.8
        cf3 = cf3*0.9
        cf4 = cf4*0.85
        cf11 = cf1+cf2-(cf2*cf1)
        cf22 = cf3+cf4-(cf3*cf4)
        cf_ = cf22+cf11-(cf11*cf22)
        self.declare(a_fact(name="Irreversible",cf=cf_,answer = "None"))
    
    @Rule(
        AND(
            a_fact(name = "Q13",cf= MATCH.cf4, answer ="yes"),
            a_fact(name = "Q12",cf= MATCH.cf3, answer ="yes"),
            a_fact(name = "Q14",cf= MATCH.cf2, answer ="yes"),
            a_fact(name = "Q10",cf= MATCH.cf1, answer ="yes"),

          )
               
        )
    def rule12(self,cf1,cf2,cf3,cf4):
        cf1 = cf1*0.75
        cf2 = cf2*0.8
        cf3 = cf3*0.9
        cf4 = cf4*0.85
        cf11 = cf1+cf2-(cf2*cf1)
        cf22 = cf3+cf4-(cf3*cf4)
        cf_ = cf22+cf11-(cf11*cf22)
        self.declare(a_fact(name="Irreversible1",cf=cf_, answer = "None"))


    @Rule(
        AND(         
            a_fact(name = "Q14",cf= MATCH.cf4, answer ="yes"),
            a_fact(name = "Q12",cf= MATCH.cf3, answer ="yes"),
            a_fact(name = "Q11",cf= MATCH.cf2, answer ="yes"),
            a_fact(name = "Q10",cf= MATCH.cf1, answer ="yes"),

          )
               
        )
    def rule13(self,cf1,cf2,cf3,cf4):
        cf1 = cf1*0.75
        cf2 = cf2*0.8
        cf3 = cf3*0.9
        cf4 = cf4*0.85
        cf11 = cf1+cf2-(cf2*cf1)
        cf22 = cf3+cf4-(cf3*cf4)
        cf_ = cf22+cf11-(cf11*cf22)
        self.declare(a_fact(name="Irreversible2",cf=cf_, answer = "None"))
     
    @Rule(
        AND(
                  
            a_fact(name = "Q13",cf= MATCH.cf4, answer ="yes"),
            a_fact(name = "Q12",cf= MATCH.cf3, answer ="yes"),
            a_fact(name = "Q11",cf= MATCH.cf2, answer ="yes"),
            a_fact(name = "Q10",cf= MATCH.cf1, answer ="yes"),

          )
               
        )
    def rule14(self,cf1,cf2,cf3,cf4):
        cf1 = cf1*0.75
        cf2 = cf2*0.8
        cf3 = cf3*0.9
        cf4 = cf4*0.85
        cf11 = cf1+cf2-(cf2*cf1)
        cf22 = cf3+cf4-(cf3*cf4)
        cf_ = cf22+cf11-(cf11*cf22)
        self.declare(a_fact(name="Irreversible3",cf=cf_, answer = "None"))


    @Rule(
        AND(
              
            a_fact(name = "Q13",cf= MATCH.cf3, answer ="yes"),
            a_fact(name = "Q11",cf= MATCH.cf2, answer ="yes"),
            a_fact(name = "Q10",cf= MATCH.cf1, answer ="yes"),

          )
                
        )
    def rule15(self,cf1,cf2,cf3):
        cf1 = cf1*0.85
        cf2 = cf2*0.7
        cf3 = cf3*0.95
        cf11 = cf1+cf2-(cf2*cf1)
        cf_ = cf11+cf3-(cf11*cf3)
        self.declare(a_fact(name="Irreversible4",cf=cf_, answer = "None"))
    

    @Rule(
        AND(
            
            a_fact(name = "Q13",cf= MATCH.cf3, answer ="yes"),
            a_fact(name = "Q12",cf= MATCH.cf2, answer ="yes"),
            a_fact(name = "Q10",cf= MATCH.cf1, answer ="yes"),

          )
                
        )
    def rule16(self,cf1,cf2,cf3):
        cf1 = cf1*0.85
        cf2 = cf2*0.7
        cf3 = cf3*0.95
        cf11 = cf1+cf2-(cf2*cf1)
        cf_ = cf11+cf3-(cf11*cf3)
        self.declare(a_fact(name="Irreversible5",cf=cf_,answer = "None"))

    
    @Rule(
        AND(  
            a_fact(name = "Q14",cf= MATCH.cf3, answer ="yes"),
            a_fact(name = "Q12",cf= MATCH.cf2, answer ="yes"),
            a_fact(name = "Q11",cf= MATCH.cf1, answer ="yes"),

          )
                
        )
    def rule17(self,cf1,cf2,cf3):
        cf1 = cf1*0.85
        cf2 = cf2*0.7
        cf3 = cf3*0.95
        cf11 = cf1+cf2-(cf2*cf1)
        cf_ = cf11+cf3-(cf11*cf3)
        self.declare(a_fact(name="Irreversible6",cf=cf_,answer = "None"))
    
    @Rule(
         
        AND(
            
            a_fact(name = "Q13",cf= MATCH.cf2, answer ="yes"),
            a_fact(name = "Q11",cf= MATCH.cf1, answer ="yes"),

          )
    )
    def rule18(self,cf1,cf2):
        cf1 = cf1*0.9
        cf2 = cf2*0.75
        cf_ = cf1+cf2-(cf2*cf1)
        self.declare(a_fact(name="Irreversible7",cf=cf_, answer = "None"))
    
    @Rule(
         
        AND(
            a_fact(name = "Q13",cf= MATCH.cf2, answer ="yes"),
            a_fact(name = "Q12",cf= MATCH.cf1, answer ="yes"),

          )
    )
    def rule19(self,cf1,cf2):
        cf1 = cf1*0.9
        cf2 = cf2*0.75
        cf_ = cf1+cf2-(cf2*cf1)
        self.declare(a_fact(name="Irreversible8",cf=cf_,answer = "None"))
    

    @Rule(
         
        AND(
          
            a_fact(name = "Q12",cf= MATCH.cf2, answer ="yes"),
            a_fact(name = "Q11",cf= MATCH.cf1, answer ="yes"),

          )
    )
    def rule20(self,cf1,cf2):
        cf1 = cf1*0.9
        cf2 = cf2*0.75
        cf_ = cf1+cf2-(cf2*cf1)
        self.declare(a_fact(name="Irreversible9",cf=cf_, answer = "None"))
        
    @Rule(
          
            a_fact(name = "Q9",cf= MATCH.cf1, answer ="yes"),

     )
    def rule22(self,cf1):
        cf_ = cf1*0.95
        self.declare(a_fact(name="periapical",cf=cf_, answer = "None"))
        
        
    @Rule(a_fact(name = "Q9",cf= MATCH.cf1,answer = "no"))
    def  print_results(self,cf1):
        self.declare(Fact("finished"))
    
    @Rule(a_fact(name = "Q9",cf= MATCH.cf1, answer = "yes"))
    def  print_results2(self,cf1):
        self.declare(Fact("finished"))
    
    
    
    @Rule(Fact("finished"),
          a_fact(name = "Detal caries11",cf= MATCH.cf,answer = "None")
         )
    def job_selection_rule_18(self,cf):
        if cf > self.max_cf:
            self.max_cf = cf
        self.retract_or_not(Fact("finished"))
        self.declare(Fact("next"))
        
    @Rule(Fact("finished"),
          a_fact(name = "Detal caries12",cf= MATCH.cf,answer = "None")
         )
    def job_selection_rule_19(self,cf):
        if cf > self.max_cf:
            self.max_cf = cf
        self.retract_or_not(Fact("finished"))
        self.declare(Fact("next"))
    
    @Rule(Fact("finished"),
          a_fact(name = "Detal caries13",cf= MATCH.cf,answer = "None")
         )
    def job_selection_rule_20(self,cf):
        if cf > self.max_cf:
            self.max_cf = cf
        self.retract_or_not(Fact("finished"))
        self.declare(Fact("next"))
        
    @Rule(Fact("finished"),
          a_fact(name = "Detal caries14",cf= MATCH.cf,answer = "None")
         )
    def job_selection_rule_21(self,cf):
        if cf > self.max_cf:
            self.max_cf = cf
        self.retract_or_not(Fact("finished"))
        self.declare(Fact("next"))
        
    
    @Rule(Fact("finished"),
          a_fact(name = "Detal caries",cf= MATCH.cf,answer = "None")
         )
    def job_selection_rule_1(self,cf): 
        if cf > self.max_cf:
            self.max_cf = cf
        self.retract_or_not(Fact("finished"))
        self.declare(Fact("next"))
   
    @Rule(Fact("finished"),
          a_fact(name = "Detal caries1",cf= MATCH.cf,answer = "None")
         )
    def job_selection_rule_2(self,cf):  
        if cf > self.max_cf:
            self.max_cf = cf
        self.retract_or_not(Fact("finished"))
        self.declare(Fact("next"))
    @Rule(Fact("finished"),
          a_fact(name = "Detal caries2",cf= MATCH.cf,answer = "None")
         )
    def job_selection_rule_3(self,cf):
        if cf > self.max_cf:
            self.max_cf = cf
        self.retract_or_not(Fact("finished"))
        self.declare(Fact("next"))
    @Rule(Fact("finished"),
          a_fact(name = "Detal caries3",cf= MATCH.cf,answer = "None")
         )
    def job_selection_rule_4(self,cf):
        if cf > self.max_cf:
            self.max_cf = cf
        self.retract_or_not(Fact("finished"))
        self.declare(Fact("next"))
    
    @Rule(Fact("finished"),
          a_fact(name = "Detal caries4",cf= MATCH.cf,answer = "None")
         )
    def job_selection_rule_5(self,cf):
        if cf > self.max_cf:
            self.max_cf = cf
        self.retract_or_not(Fact("finished"))
        self.declare(Fact("next"))
        
    @Rule(Fact("finished"),
          a_fact(name = "Detal caries5",cf= MATCH.cf,answer = "None")
         )
    def job_selection_rule_6(self,cf):
        if cf > self.max_cf:
            self.max_cf = cf
        self.retract_or_not(Fact("finished"))
        self.declare(Fact("next"))
        
    @Rule(Fact("finished"),
          a_fact(name = "Detal caries6",cf= MATCH.cf,answer = "None")
         )
    def job_selection_rule_6(self,cf):
        if cf > self.max_cf:
            self.max_cf = cf
        self.retract_or_not(Fact("finished"))
        self.declare(Fact("next"))
    @Rule(Fact("finished"),
          a_fact(name = "Detal caries7",cf= MATCH.cf,answer = "None")
         )
    def job_selection_rule_66(self,cf):
        if cf > self.max_cf:
            self.max_cf = cf
        self.retract_or_not(Fact("finished"))
        self.declare(Fact("next"))
        
    def retract_or_not(self, fact):
        if fact in self.facts:
            self.retract(fact)
            
        
    @Rule(Fact("next"))
    def print_diagnosis(self):
        print("-------------------------------------")
        print("The diagnose is Detal caries with ", self.max_cf)
        print("-------------------------------------\n")
       # self.halt()
        
    @Rule(Fact("finished"),
          a_fact(name = "Reverse",cf= MATCH.cf,answer = "None")
         )
    def job_selection_rule_7(self,cf):
            print("-------------------------------------"+"\n")
            print("The diagnose is Reversible pulpities with  ",cf)
            print("-------------------------------------"+"\n\n")
    
    @Rule(Fact("finished"),
          a_fact(name = "Irreversible1",cf= MATCH.cf,answer = "None")
         )
    def job_selection_rule_8(self,cf):
            print("-------------------------------------"+"\n")
            print("The diagnose is Reversible pulpities with  ",cf)
            print("-------------------------------------"+"\n\n")
    
    @Rule(Fact("finished"),
          a_fact(name = "Irreversible2",cf= MATCH.cf,answer = "None")
         )
    def job_selection_rule_9(self,cf):
            print("-------------------------------------"+"\n")
            print("The diagnose is Reversible pulpities with  ",cf)
            print("-------------------------------------"+"\n\n")
    
    
    @Rule(Fact("finished"),
          a_fact(name = "Irreversible3",cf= MATCH.cf,answer = "None")
         )
    def job_selection_rule_10(self,cf):
            print("-------------------------------------"+"\n")
            print("The diagnose is Reversible pulpities with  ",cf)
            print("-------------------------------------"+"\n\n")
    
    @Rule(Fact("finished"),
          a_fact(name = "Irreversible4",cf= MATCH.cf,answer = "None")
         )
    def job_selection_rule_11(self,cf):
            print("-------------------------------------"+"\n")
            print("The diagnose is Reversible pulpities with  ",cf)
            print("-------------------------------------"+"\n\n")
    
    @Rule(Fact("finished"),
          a_fact(name = "Irreversible5",cf= MATCH.cf,answer = "None")
         )
    def job_selection_rule_12(self,cf):
            print("-------------------------------------"+"\n")
            print("The diagnose is Reversible pulpities with  ",cf)
            print("-------------------------------------"+"\n\n")
    
    
    @Rule(Fact("finished"),
          a_fact(name = "Irreversible6",cf= MATCH.cf,answer = "None")
         )
    def job_selection_rule_13(self,cf):
            print("-------------------------------------"+"\n")
            print("The diagnose is Reversible pulpities with  ",cf)
            print("-------------------------------------"+"\n\n")
    
    @Rule(Fact("finished"),
          a_fact(name = "Irreversible7",cf= MATCH.cf,answer = "None")
         )
    def job_selection_rule_14(self,cf):
            print("-------------------------------------"+"\n")
            print("The diagnose is Reversible pulpities with  ",cf)
            print("-------------------------------------"+"\n\n")
    @Rule(Fact("finished"),
          a_fact(name = "Irreversible8",cf= MATCH.cf,answer = "None")
         )
    def job_selection_rule_15(self,cf):
            print("-------------------------------------"+"\n")
            print("The diagnose is Reversible pulpities with  ",cf)
            print("-------------------------------------"+"\n\n")
    
    @Rule(Fact("finished"),
          a_fact(name = "Irreversible9",cf= MATCH.cf,answer = "None")
         )
    def job_selection_rule_16(self,cf):
            print("-------------------------------------"+"\n")
            print("The diagnose is Reversible pulpities with  ",cf)
            print("-------------------------------------"+"\n\n")
            
    @Rule(Fact("finished"),
          a_fact(name = "periapical",cf= MATCH.cf,answer = "None")
         )
    def job_selection_rule_17(self,cf):
            print("-------------------------------------"+"\n")
            print("The diagnose is periapical abscess with  ",cf)
            print("-------------------------------------"+"\n\n")

    

        


        
ke= JOBEX()
ke.reset()
ke.run()