using System;

namespace ThyroidNoduleLocalizationWebApplication.Controllers.DTO;

public class PatientCaseDTO
{
    public String CaseId { get; set; }
    public String Tirads { get; set; }
    public int Age { get; set; }
    public String Sex { get; set; }
    public String MedicalNote { get; set; }
    public String Created { get; set; }
    public String MedicalDoctor { get; set; }
    public String Radiologist { get; set; }
    public int? IsDiagnosedByAi { get; set; }
}