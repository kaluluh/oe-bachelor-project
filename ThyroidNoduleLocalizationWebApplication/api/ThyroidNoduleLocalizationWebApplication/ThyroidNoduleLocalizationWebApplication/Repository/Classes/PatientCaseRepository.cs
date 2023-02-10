using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using ThyroidNoduleLocalizationWebApplication.Models;
using ThyroidNoduleLocalizationWebApplication.Repository.Interfaces;

namespace ThyroidNoduleLocalizationWebApplication.Repository.Classes;

public class PatientCaseRepository : RepositoryBase<PatientCase>, IPatientCaseRepository
{
    public PatientCaseRepository(DatabaseContext databaseContext)
        :base(databaseContext)
    {
    }
}