using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using Microsoft.EntityFrameworkCore;
using Newtonsoft.Json;
using Newtonsoft.Json.Linq;
using ThyroidNoduleLocalizationWebApplication.Controllers;
using ThyroidNoduleLocalizationWebApplication.Models;
using ThyroidNoduleLocalizationWebApplication.Repository;

namespace ThyroidNoduleLocalizationWebApplication.Util;

public static class JsonLoader
{
    public static List<PatientCase> LoadCasesJsonToList(String path)
    {
        string json = File.ReadAllText(path);
        JArray jsonArray = JArray.Parse(json);
        List<PatientCase> patientCases = new List<PatientCase>();
        foreach (JObject jsonObject in jsonArray.Children<JObject>())
        {
            var caseId = jsonObject["case_id"].ToString();
            if (!patientCases.Any(c => c.CaseId.Equals(caseId)))
            {
                PatientCase patientCase = new PatientCase()
                {
                    CaseId = caseId,
                    Age = int.Parse(jsonObject["age"].ToString()),
                    BoundingBoxes = jsonObject["bboxes"].ToString(),
                    Tirads = jsonObject["tirads"].ToString(),
                    Sex = jsonObject["sex"].ToString(),
                    Echogenicity = jsonObject["echogenicity"].ToString(),
                    Composition = jsonObject["composition"].ToString(),
                    Margins = jsonObject["margins"].ToString(),
                    Calcifications = jsonObject["calcifications"].ToString(),
                    Reportbacaf = jsonObject["reportbacaf"].ToString(),
                    Reporteco = jsonObject["reporteco"].ToString()
                };
                patientCases.Add(patientCase);
            }
        }

        return !patientCases.Any() ? null : patientCases;
    }
}