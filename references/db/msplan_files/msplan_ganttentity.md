# 视图方案-msplan_ganttentity

## 视图方案-主表 t_msplan_entity

- **表名称：** 视图方案-主表
- **表名：** t_msplan_entity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftaskentityflagdesc | ftaskentityflagdesc | varchar | 255 |  | √ | ' ' |  |
| 3 | fgroupentityid | fgroupentityid | varchar | 255 |  | √ | 0 |  |
| 4 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 5 | fdefaultview | fdefaultview | bpchar | 1 |  | √ | '0' |  |
| 6 | fjoinfilter | fjoinfilter | bpchar | 1 |  | √ | '0' |  |
| 7 | fgroupfielddesc | fgroupfielddesc | varchar | 50 |  | √ | ' ' |  |
| 8 | ffiltertext | ffiltertext | varchar | 50 |  | √ | ' ' |  |
| 9 | ffilter | ffilter | varchar | 255 |  | √ | ' ' |  |
| 10 | fentityid | 实体 | varchar | 255 |  | √ | 0 | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 11 | ftimefielddesc | ftimefielddesc | varchar | 50 |  | √ | ' ' |  |
| 12 | fupgroupfield | fupgroupfield | varchar | 50 |  | √ | ' ' |  |
| 13 | fupupgroupfield | fupupgroupfield | varchar | 50 |  | √ | ' ' |  |
| 14 | ftaskentityflag | ftaskentityflag | varchar | 255 |  | √ | ' ' |  |
| 15 | fupgroupfielddesc | fupgroupfielddesc | varchar | 50 |  | √ | ' ' |  |
| 16 | fviewid | 视图id | int8 | 64 |  | √ | 0 | 视图id |
| 17 | ffilter_tag | ffilter_tag | text | 0 |  |  | '' |  |
| 18 | fgroupfield | fgroupfield | varchar | 50 |  | √ | ' ' |  |
| 19 | fupupgroupentityid | fupupgroupentityid | varchar | 255 |  | √ | 0 |  |
| 20 | fupupgroupfielddesc | fupupgroupfielddesc | varchar | 50 |  | √ | ' ' |  |
| 21 | ftimefield | 任务对应时间 | varchar | 50 |  | √ | ' ' | 任务对应时间 |
| 22 | fismappingentity | fismappingentity | bpchar | 1 |  | √ | '0' |  |
| 23 | fupgroupentityid | fupgroupentityid | varchar | 255 |  | √ | 0 |  |
| 24 | fviewalias | 别名 | varchar | 50 |  | √ | ' ' | 别名 |
| 25 | fentryid | 主键 | int8 | 64 |  | √ | 0 | 主键 |
| 26 | fgantttype | 视图类型 | varchar | 5 |  | √ | ' ' | 视图类型,枚举: A :资源 B :任务 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_msplan_entity_fseq |  | fseq |
| 2 | idx_msplan_entity_fid |  | fid |
| 3 | pk_msplan_entity |  | fentryid |
