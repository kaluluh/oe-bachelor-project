using ThyroidNoduleLocalizationWebApplication.Models;
using ThyroidNoduleLocalizationWebApplication.Repository.Interfaces;

namespace ThyroidNoduleLocalizationWebApplication.Repository.Classes;

public class AdditionalInformationRepositoryRepository: RepositoryBase<AdditionalInformation>, IAdditionalInformationRepository
{
    public AdditionalInformationRepositoryRepository(DatabaseContext databaseContext)
        :base(databaseContext)
    {
    }
}