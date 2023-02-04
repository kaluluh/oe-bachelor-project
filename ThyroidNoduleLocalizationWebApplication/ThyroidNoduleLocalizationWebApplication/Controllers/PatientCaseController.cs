using System;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using ThyroidNoduleLocalizationWebApplication.Models;
using ThyroidNoduleLocalizationWebApplication.Repository;


namespace ThyroidNoduleLocalizationWebApplication.Controllers
{
    //[Authorize]
    [Route("api/[controller]")]
    [ApiController]
    public class PatientCaseController : Controller
    {
        private IRepositoryWrapper _repository;

        public PatientCaseController(IRepositoryWrapper repository)
        {
            _repository = repository;
        }

        [HttpGet]
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

        [HttpGet("{id}")]
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

        [HttpDelete("{id}")]
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

        [HttpPost]
        public JsonResult CreatePatientCase(PatientCase patientCase)
        {
            try
            {
                _repository.PatientCase.Create(patientCase);
                _repository.PatientCase.Save();
                return new JsonResult("Case successfully created.");
            }
            catch (Exception e)
            {
                return new JsonResult(e.Message);
            }
        }
    }
}
