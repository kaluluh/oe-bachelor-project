using System;

namespace ThyroidNoduleLocalizationWebApplication.Models
{
    public class PatientCase
    {
        public String CaseId { get; set; }
        public String Tirads { get; set; }
        public String BoundingBoxes { get; set; }
        public int Age { get; set; }
        public String Sex { get; set; }
        public String Composition { get; set; }
        public String Echogenicity { get; set; }
        public String Margins { get; set; }
        public String Calcifications { get; set; }
        public String Reportbacaf { get; set; }
        public String Reporteco { get; set; }

        public virtual AdditionalInformation AdditionalInformation { get; set; }
    }
}
