using System.Collections.Generic;
using ThyroidNoduleLocalizationWebApplication.Controllers.Query;
using ThyroidNoduleLocalizationWebApplication.Models;

namespace ThyroidNoduleLocalizationWebApplication.Repository.Interfaces;

public interface IPatientCaseRepository : IRepositoryBase<PatientCase>
{
     List<PatientCase> RunStatisticsQuery(StatisticsQuery query);
     int GetNextId();
}