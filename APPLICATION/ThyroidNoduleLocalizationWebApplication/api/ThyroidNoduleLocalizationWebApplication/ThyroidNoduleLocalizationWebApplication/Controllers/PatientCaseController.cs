using System;
using System.Collections.Generic;
using System.Globalization;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using ThyroidNoduleLocalizationWebApplication.Controllers.DTO;
using ThyroidNoduleLocalizationWebApplication.Controllers.Query;
using ThyroidNoduleLocalizationWebApplication.Models;
using ThyroidNoduleLocalizationWebApplication.Repository;


namespace ThyroidNoduleLocalizationWebApplication.Controllers
{
    //[Authorize]
    [Route("case")]
    [ApiController]
    public class PatientCaseController : Controller
    {
        private IRepositoryWrapper _repository;

        public PatientCaseController(IRepositoryWrapper repository)
        {
            _repository = repository;
        }

        [HttpGet("get-all")]
        public JsonResult GetAll()
        {
            try
            {
                var patientCases = _repository.PatientCase.FindAll().ToList();
                return new JsonResult(patientCases);
            }
            catch (Exception e)
            {
                return new JsonResult(e.Message);
            }
        }

        [HttpGet("get-by-id/{id}")]
        public JsonResult GetCaseById(String id)
        {
            try
            {
                var patientCase = _repository.PatientCase
                    .FindByCondition(c => c.CaseId.Equals(id)).FirstOrDefault();
                return new JsonResult(patientCase);
            }
            catch (Exception e)
            {
                return new JsonResult(e.Message);
            }
        }

        [HttpDelete("delete/{id}")]
        public Task<JsonResult> DeletePatientCase(String id)
        {
            try
            {
                var patientCase = _repository.PatientCase
                    .FindByCondition(c => c.CaseId.Equals(id)).FirstOrDefault();

                if (patientCase == null) return Task.FromResult(new JsonResult("Case id is not found."));
                _repository.PatientCase.Delete(patientCase);
                _repository.PatientCase.Save();
                return Task.FromResult(new JsonResult("Case deleted successfully"));
            }
            catch (Exception e)
            {
                return Task.FromResult(new JsonResult(e.Message));
            }
        }

        [HttpPost("create")]
        public JsonResult CreatePatientCase(PatientCaseDTO patientCaseDto)
        {
            try
            {
                String nextId = _repository.PatientCase.GetNextId().ToString();
                PatientCase patientCase = new PatientCase
                {
                    CaseId = nextId,
                    Age = patientCaseDto.Age,
                    Tirads = patientCaseDto.Tirads,
                    Sex = patientCaseDto.Sex,
                    AdditionalInformation = new AdditionalInformation
                    {
                        IsDiagnosedByAi = (int)patientCaseDto.IsDiagnosedByAi,
                        Created = DateTime.Now,
                        MedicalDoctor = patientCaseDto.MedicalDoctor,
                        MedicalNote = patientCaseDto.MedicalNote,
                        Radiologist = patientCaseDto.Radiologist,
                    }
                };
                _repository.PatientCase.Create(patientCase);
                _repository.PatientCase.Save();
                return new JsonResult("Case successfully created.");
            }
            catch (Exception e)
            {
                return new JsonResult(e.Message);
            }
        }
        
        [HttpPost("update")]
        public JsonResult UpdatePatientCase(PatientCaseDTO patientCaseDto)
        {
            try
            {
                var oldPatientCase = _repository.PatientCase
                    .FindByCondition(c => c.CaseId
                        .Equals(patientCaseDto.CaseId))
                    .Include(p=> p!.AdditionalInformation)
                    .FirstOrDefault();
                PatientCase newPatientCase = new PatientCase
                {
                    CaseId = patientCaseDto.CaseId,
                    Margins = oldPatientCase!.Margins,
                    BoundingBoxes = oldPatientCase.BoundingBoxes,
                    Echogenicity = oldPatientCase!.Echogenicity,
                    Calcifications = oldPatientCase!.Calcifications,
                    Reportbacaf = oldPatientCase!.Reportbacaf,
                    Reporteco = oldPatientCase!.Reporteco,
                    Age = patientCaseDto.Age,
                    Tirads = patientCaseDto.Tirads,
                    Sex = patientCaseDto.Sex,
                    Composition = oldPatientCase.Composition,
                    AdditionalInformation = new AdditionalInformation
                    {
                        IsDiagnosedByAi = patientCaseDto.IsDiagnosedByAi ?? 0,
                        Created = DateTime.Now,
                        MedicalDoctor = patientCaseDto.MedicalDoctor ?? "",
                        MedicalNote = patientCaseDto.MedicalNote ?? "",
                        Radiologist = patientCaseDto.Radiologist ?? "",
                    }
                };
                if (oldPatientCase.AdditionalInformation != null)
                {
                    _repository.AdditionalInformation.Delete(oldPatientCase.AdditionalInformation);
                }
                _repository.PatientCase.Delete(oldPatientCase);
                _repository.PatientCase.Create(newPatientCase);
                _repository.PatientCase.Save();
                return new JsonResult("Case successfully updated.");
            }
            catch (Exception e)
            {
                return new JsonResult(e.Message);
            }
        }
        
        [HttpPost("run-statistics-query")]
        public JsonResult RunStatisticsQuery([FromBody]StatisticsQuery query)
        {
            try
            {
                var patientCases = _repository.PatientCase.RunStatisticsQuery(query);
                var patientCaseDtos = patientCases.Select(p => new PatientCaseDTO
                {
                    Tirads = p.Tirads,
                    CaseId = p.CaseId,
                    Age = p.Age,
                    Sex = p.Sex,
                    MedicalNote = p.AdditionalInformation?.MedicalNote,
                    // Created = p.AdditionalInformation?.Created.ToString(CultureInfo.CurrentCulture) ?? "unknown",
                    Created = p.AdditionalInformation?.Created.ToString(CultureInfo.CurrentCulture) 
                              ?? new DateTime(2023, 03, 06).ToString(CultureInfo.CurrentCulture), 
                    MedicalDoctor = p.AdditionalInformation?.MedicalDoctor,
                    Radiologist = p.AdditionalInformation?.Radiologist,
                    IsDiagnosedByAi = p.AdditionalInformation?.IsDiagnosedByAi
                }).ToList();
                var positive = patientCaseDtos.Count(a => Int32.Parse(a.Tirads.Substring(0, 1)) > 3);
                var negative = patientCaseDtos.Count(a => Int32.Parse(a.Tirads.Substring(0, 1)) < 4);
                var all = patientCaseDtos.Count;
                var respond = new
                {
                    patientCasesList = patientCaseDtos,
                    positiveCount = positive,
                    negativeCount = negative,
                    allCount = all
                };

                return new JsonResult(respond);
            }
            catch (Exception e)
            {
                return new JsonResult(e.Message);
            }
        }
        
        [HttpGet("get-all-additional-information")]
        public JsonResult GetAllAdditionalInformation()
        {
            try
            {
                var result = _repository.AdditionalInformation.FindAll().ToList();
                return new JsonResult(result);
            }
            catch (Exception e)
            {
                return new JsonResult(e.Message);
            }
        }
    }
}
