using System;
using System.ComponentModel.DataAnnotations.Schema;

namespace ThyroidNoduleLocalizationWebApplication.Models;

public class AdditionalInformation
{
    [ForeignKey("PatientCase")]
    public String CaseId { get; set; }
    public String MedicalNote { get; set; }
    public DateTime Created { get; set; }
    public String MedicalDoctor { get; set; }
    public String Radiologist { get; set; }
    public int IsDiagnosedByAi { get; set; }

    public virtual PatientCase PatientCase { get; set; }
}