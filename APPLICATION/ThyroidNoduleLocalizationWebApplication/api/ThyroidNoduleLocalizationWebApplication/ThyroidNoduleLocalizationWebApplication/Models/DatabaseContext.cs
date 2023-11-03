using Microsoft.AspNetCore.Identity.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore;
using ThyroidNoduleLocalizationWebApplication.Authorization;

namespace ThyroidNoduleLocalizationWebApplication.Models
{
    public class DatabaseContext : IdentityDbContext<User>
    {
        public DbSet<PatientCase> PatientCases { get; set; }

        public DbSet<AdditionalInformation> AdditionalInformations { get; set; }

        public DatabaseContext(DbContextOptions<DatabaseContext> options) : base(options)
        {
        }

        protected override void OnModelCreating(ModelBuilder builder)
        {
            builder.Entity<PatientCase>(entity =>
            {
                entity.HasKey(e => e.CaseId);
                entity.ToTable("PatientCase");
                entity.Property(e => e.Tirads).HasColumnType("nvarchar(2, 0)");
                entity.Property(e => e.BoundingBoxes).HasColumnType("nvarchar(255, 0)");
                entity.Property(e => e.Age).HasColumnType("int");
                entity.Property(e => e.Sex).HasColumnType("nvarchar(2, 0)");
                entity.Property(e => e.Composition).HasColumnType("nvarchar(255, 0)");
                entity.Property(e => e.Echogenicity).HasColumnType("nvarchar(255, 0)");
                entity.Property(e => e.Margins).HasColumnType("nvarchar(255, 0)");
                entity.Property(e => e.Calcifications).HasColumnType("nvarchar(255, 0)");
                entity.Property(e => e.Reportbacaf).HasColumnType("nvarchar(255, 0)");
                entity.Property(e => e.Reporteco).HasColumnType("nvarchar(255, 0)");
            });
            builder.Entity<AdditionalInformation>(entity =>
            {
                entity.HasKey(e => e.CaseId);
                entity.ToTable("AdditionalInformation");
                entity.Property(e => e.MedicalNote).HasColumnType("nvarchar(255, 0)");
                entity.Property(e => e.Radiologist).HasColumnType("nvarchar(255, 0)");
                entity.Property(e => e.Created).HasColumnType("datetime2");
                entity.Property(e => e.MedicalDoctor).HasColumnType("nvarchar(255, 0)");
                entity.Property(e => e.IsDiagnosedByAi).HasColumnType("int");

            });

            builder.Entity<PatientCase>()
                .HasOne(p => p.AdditionalInformation)
                .WithOne(a => a.PatientCase);

            base.OnModelCreating(builder);
        }

    }
}
