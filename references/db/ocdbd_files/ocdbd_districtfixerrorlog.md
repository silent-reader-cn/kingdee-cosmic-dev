# 人员组织变更日志-ocdbd_districtfixerrorlog

## 人员组织变更日志-主表 t_ocdbd_fixerrorlog

- **表名称：** 人员组织变更日志-主表
- **表名：** t_ocdbd_fixerrorlog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsrcbillnumber | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 3 | faregionid | 所属大区(变更后) | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fbregionid | 所属大区(变更前) | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fsrcbillid | 单据主键 | int8 | 64 |  | √ | 0 | 单据主键 |
| 6 | fcreatetime | 变更时间 | timestamp | 0 |  |  | null | 变更时间 |
| 7 | fadepartmentid | 部门(变更后) | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fbuserid | 业务员(变更前) | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fsrcbillentryid | 分录行主键 | int8 | 64 |  | √ | 0 | 分录行主键 |
| 10 | fsrcbillentryseq | 分录行序号 | int4 | 32 |  | √ | 0 | 分录行序号 |
| 11 | faprovinceid | 所属省区(变更后) | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 12 | fcreatorid | 变更人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fbdepartmentid | 部门(变更前) | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 14 | fsrcbillentity | 变更单据 | varchar | 80 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 15 | fbprovinceid | 所属省区(变更前) | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 16 | fauserid | 业务员(变更后) | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdbd_fixerrorlog |  | fid |
| 2 | idx_ocdbd_fixerrorlog_billno |  | fsrcbillnumber |
