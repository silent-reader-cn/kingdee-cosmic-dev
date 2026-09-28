# 样本数据-mds_sample

## 样本数据-主表 t_mds_sample

- **表名称：** 样本数据-主表
- **表名：** t_mds_sample

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | factualintime | 进场时间 | timestamp | 0 |  |  | null | 进场时间 |
| 3 | fconfiguration | 客舱构型 | int8 | 64 |  | √ | 0 | [客舱构型 mpdm_cabinconfig](../mpdm_files/mpdm_cabinconfig.md) |
| 4 | fchecktypedesc | 检修级别名称 | varchar | 255 |  | √ | ' ' | 检修级别名称 |
| 5 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | flogid | 计算日志 | int8 | 64 |  | √ | 0 | [用量概率计算日志 mds_probabilitylog](../mds_files/mds_probabilitylog.md) |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fchecktype | 检修级别 | int8 | 64 |  | √ | 0 | [检修级别 mpdm_checktype](../mpdm_files/mpdm_checktype.md) |
| 9 | fuse | 是否选择 | bpchar | 1 |  | √ | '0' | 是否选择 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fsysuse | 系统选择 | bpchar | 1 |  | √ | '0' | 系统选择 |
| 12 | factualleavetime | 离场时间 | timestamp | 0 |  |  | null | 离场时间 |
| 13 | fbillno | 计划号 | varchar | 80 |  | √ | ' ' | 计划号 |
| 14 | facreg | 检修设备 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 15 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fcustomer | 客户 | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |
| 17 | fpolarisstatus | 客舱改装状态 | int8 | 64 |  | √ | 0 | [客舱改装状态 mds_polarisstatus](../mds_files/mds_polarisstatus.md) |
| 18 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 19 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 20 | fbackupproject | 备货项目 | int8 | 64 |  | √ | 0 | [项目 pmpd_project](../fmm_files/pmpd_project.md) |
| 21 | factype | 检修设备类型 | int8 | 64 |  | √ | 0 | [检修设备类型 mpdm_mrtype](../mpdm_files/mpdm_mrtype.md) |
| 22 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 23 | fanalysisdim | 分析维度 | varchar | 50 |  | √ | ' ' | 分析维度,枚举: A :客户+检修设备类型+检修级别 B :客户+检修设备类型 C :检修设备类型 |
| 24 | fprojectcreatetime | 项目创建时间 | timestamp | 0 |  |  | null | 项目创建时间 |
| 25 | fproject | 项目号 | int8 | 64 |  | √ | 0 | [项目 pmpd_project](../fmm_files/pmpd_project.md) |
| 26 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 27 | facregtext | facregtext | varchar | 255 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mds_sample |  | fid |
| 2 | idx_mds_sample |  | flogid |
