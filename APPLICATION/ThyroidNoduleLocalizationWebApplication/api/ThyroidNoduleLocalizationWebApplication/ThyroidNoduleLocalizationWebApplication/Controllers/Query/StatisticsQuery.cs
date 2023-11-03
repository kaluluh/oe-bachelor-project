using System;

namespace ThyroidNoduleLocalizationWebApplication.Controllers.Query;

public class StatisticsQuery
{
    public Nullable<int> AgeFrom { get; set; }
    public Nullable<int>  AgeTo { get; set; }
    public string TiradsScore { get; set; }
    public string Gender { get; set; }
}