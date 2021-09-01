/*this code works to query the testing data in relation to sample name and specimen ID - does not fix problem with dimensions */

select  
    d.DataFloat, d.DataInt, d.DataText, d.RelatedItemId, d.DatumColumnId,
    dco.DatumColumnId, dco.UserLabelId, dco.DataTagId,
    ul.UserLabelId, ul.Label,
    dt.DataTagId, dt.Description, dt.DataCategoryId,
    dca.DataCategoryId, dca.Description,
    sa.Guid, sa.Name,
    sp.Guid, sp.SampleId,
    t.Guid, t.SpecimenId, t.CreateDate

from Ids.Data as d
left join Ids.DataColumns as dco
on d.DatumColumnId = dco.DatumColumnId
left join Ids.UserLabels as ul
on ul.UserLabelId = dco.UserLabelId
left join Ids.DataTags as dt
on dt.DataTagId = dco.DataTagId
left join Ids.DataCategories as dca
on dca.DataCategoryId = dt.DataCategoryId
left join Ids.Tests as t
on t.Guid = d.RelatedItemId
left join Ids.Specimens as sp 
on t.SpecimenId = sp.Guid
left join Ids.Samples as sa
on sp.SampleId = sa.Guid

