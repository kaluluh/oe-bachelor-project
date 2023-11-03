using System.Collections.Generic;
using Microsoft.EntityFrameworkCore;
using System.Linq;
using System.Security.Cryptography.X509Certificates;
using ThyroidNoduleLocalizationWebApplication.Controllers.Query;
using ThyroidNoduleLocalizationWebApplication.Models;
using ThyroidNoduleLocalizationWebApplication.Repository.Interfaces;

namespace ThyroidNoduleLocalizationWebApplication.Repository.Classes;

public class PatientCaseRepository : RepositoryBase<PatientCase>, IPatientCaseRepository
{
    public PatientCaseRepository(DatabaseContext databaseContext)
        :base(databaseContext)
    {
    }
    
    public List<PatientCase> RunStatisticsQuery(StatisticsQuery query)
    {
        if (query != null)
        {
            if (query.AgeFrom.Equals(null) && query.AgeTo.Equals(null))
            {
                query.AgeFrom = 0;
                query.AgeTo = 0;
            } 
            query.TiradsScore = "string";
            

            List<PatientCase> patientCases = new List<PatientCase>();
            var allPatientCases = DatabaseContext.PatientCases
                .Include(p=> p.AdditionalInformation)
                .ToList();
            var queryResult = allPatientCases.Where(a => 
                  (query.AgeFrom.GetValueOrDefault() <= a.Age || query.AgeFrom == 0) && 
                  (query.AgeTo.GetValueOrDefault() >= a.Age || query.AgeTo == 0) &&
                  (a.Tirads.Equals(query.TiradsScore) || query.TiradsScore == "string") &&
                  (a.Sex.Equals(query.Gender) || query.Gender == "string"))
                .ToList();
            patientCases.AddRange(queryResult);
            return patientCases;
        }
        
        return null;
    }

    public int GetNextId ()
    {
        var id = DatabaseContext.PatientCases
            .Select(p => p.CaseId)
            .ToList()
            .Select(p => int.Parse(p.Split("_")[0]))
            .ToList()
            .OrderByDescending(id => id)
            .FirstOrDefault();
        return (id + 1);
    }
}