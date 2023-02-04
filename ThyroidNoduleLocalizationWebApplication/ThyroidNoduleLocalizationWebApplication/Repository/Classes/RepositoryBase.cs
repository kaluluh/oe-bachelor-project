using System;
using System.Linq;
using System.Linq.Expressions;
using Microsoft.EntityFrameworkCore;
using ThyroidNoduleLocalizationWebApplication.Models;
using ThyroidNoduleLocalizationWebApplication.Repository.Interfaces;

namespace ThyroidNoduleLocalizationWebApplication.Repository.Classes;

public abstract class RepositoryBase<T> : IRepositoryBase<T> where T : class
{
    protected DatabaseContext DatabaseContext { get; set; } 
    public RepositoryBase(DatabaseContext databaseContext) 
    {
        DatabaseContext = databaseContext; 
    }
    public IQueryable<T> FindAll() => DatabaseContext.Set<T>().AsNoTracking();
    public IQueryable<T> FindByCondition(Expression<Func<T, bool>> expression) => 
        DatabaseContext.Set<T>().Where(expression).AsNoTracking();
    public void Create(T entity) => DatabaseContext.Set<T>().Add(entity);
    public void Update(T entity) => DatabaseContext.Set<T>().Update(entity);
    public void Delete(T entity) => DatabaseContext.Set<T>().Remove(entity);
    public void Save() => DatabaseContext.SaveChanges();
}