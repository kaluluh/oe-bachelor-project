using ThyroidNoduleLocalizationWebApplication.Models;
using ThyroidNoduleLocalizationWebApplication.Repository.Classes;
using ThyroidNoduleLocalizationWebApplication.Repository.Interfaces;

namespace ThyroidNoduleLocalizationWebApplication.Repository;

public class RepositoryWrapper : IRepositoryWrapper
{
    private DatabaseContext _databaseContext;
    private IPatientCaseRepository _patientCaseRepository;
    private IAdditionalInformationRepository _additionalInformationRepository;

    
    public IPatientCaseRepository PatientCase {
        get {
            if(_patientCaseRepository == null)
            {
                _patientCaseRepository = new PatientCaseRepository(_databaseContext);
            }
            return _patientCaseRepository;
        }
    }
    public IAdditionalInformationRepository AdditionalInformation {
        get {
            if(_additionalInformationRepository == null)
            {
                _additionalInformationRepository = new AdditionalInformationRepositoryRepository(_databaseContext);
            }
            return _additionalInformationRepository;
        }
    }
    public RepositoryWrapper(DatabaseContext databaseContext)
    {
        _databaseContext = databaseContext;
    }
    public void Save()
    {
        _databaseContext.SaveChanges();
    }

}