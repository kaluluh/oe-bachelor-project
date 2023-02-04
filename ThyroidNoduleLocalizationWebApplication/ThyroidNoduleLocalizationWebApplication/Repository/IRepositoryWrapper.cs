using ThyroidNoduleLocalizationWebApplication.Repository.Interfaces;

namespace ThyroidNoduleLocalizationWebApplication.Repository;

public interface IRepositoryWrapper
{
    IPatientCaseRepository PatientCase { get; }
}