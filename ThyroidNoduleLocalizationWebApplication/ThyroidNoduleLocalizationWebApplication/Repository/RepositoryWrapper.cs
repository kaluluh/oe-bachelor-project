using ThyroidNoduleLocalizationWebApplication.Models;
using ThyroidNoduleLocalizationWebApplication.Repository.Classes;
using ThyroidNoduleLocalizationWebApplication.Repository.Interfaces;

namespace ThyroidNoduleLocalizationWebApplication.Repository;

public class RepositoryWrapper : IRepositoryWrapper
{
    private DatabaseContext _databaseContext;
    private IPatientCaseRepository _patientCaseRepository;
    
    public IPatientCaseRepository PatientCase {
        get {
            if(_patientCaseRepository == null)
            {
                _patientCaseRepository = new PatientCaseRepository(_databaseContext);
            }
            return _patientCaseRepository;
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