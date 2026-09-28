# 备货状态确认-mds_stockupstatus

## 备货状态确认-主表 t_mds_stockupstatus

- **表名称：** 备货状态确认-主表
- **表名：** t_mds_stockupstatus

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | factualintime | 实际进场时间 | timestamp | 0 |  |  | null | 实际进场时间 |
| 3 | fcabinconfig | 客舱构型 | int8 | 64 |  | √ | 0 | [客舱构型 mpdm_cabinconfig](../mpdm_files/mpdm_cabinconfig.md) |
| 4 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 5 | fchecktype | 检修级别 | int8 | 64 |  | √ | 0 | [检修级别 mpdm_checktype](../mpdm_files/mpdm_checktype.md) |
| 6 | fplanid | 计划id | int8 | 64 |  | √ | 0 | 计划id |
| 7 | fplanmodifier | 计划修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | fstockupscheme | 备货方案 | int8 | 64 |  | √ | 0 | [备货方案定义 mds_stockupscheme](../mds_files/mds_stockupscheme.md) |
| 9 | flistmodifier | 清单修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | flistcreatetime | 清单创建时间 | timestamp | 0 |  |  | null | 清单创建时间 |
| 11 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 12 | fcustomer | 客户编码 | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |
| 13 | fschedulestarttime | 预计开工时间 | timestamp | 0 |  |  | null | 预计开工时间 |
| 14 | fpolarisstatus | 客舱改装状态 | int8 | 64 |  | √ | 0 | [客舱改装状态 mds_polarisstatus](../mds_files/mds_polarisstatus.md) |
| 15 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | [项目 pmpd_project](../fmm_files/pmpd_project.md) |
| 16 | fsourcebilltype | 来源单据类型 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 17 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 18 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 19 | fworkscopeid | 工作内容 | int8 | 64 |  | √ | 0 | [工作内容 mpdm_workscopeins](../mpdm_files/mpdm_workscopeins.md) |
| 20 | frepaircycle | 计划检修周期 | numeric | 23 | 10 | √ | 0 | 计划检修周期 |
| 21 | fworkcenter | 检修工作中心 | int8 | 64 |  | √ | 0 | [工作中心检修信息 mpdm_workcenter_info](../mpdm_files/mpdm_workcenter_info.md) |
| 22 | fworkrepaircycle | 工作工期 | numeric | 23 | 10 | √ | 0 | 工作工期 |
| 23 | fprojectstatus | 项目状态 | int8 | 64 |  | √ | 0 | [项目状态 bd_projectstatus](../basedata_files/bd_projectstatus.md) |
| 24 | fpreapproachtime | 开工时间 | timestamp | 0 |  |  | null | 开工时间 |
| 25 | fsampleqty | 样本数 | numeric | 23 | 10 | √ | 0 | 样本数 |
| 26 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 27 | fplanmodifytime | 计划修改时间 | timestamp | 0 |  |  | null | 计划修改时间 |
| 28 | fscheduleleavetime | 预计离场时间 | timestamp | 0 |  |  | null | 预计离场时间 |
| 29 | frepaircyclesplit | 计划检修周期（拆分） | varchar | 50 |  | √ | ' ' | 计划检修周期（拆分） |
| 30 | fschedulefinishtime | 预计完工时间 | timestamp | 0 |  |  | null | 预计完工时间 |
| 31 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 32 | fplancode | 计划号 | varchar | 80 |  | √ | ' ' | 计划号 |
| 33 | foverdevice | 检修设备注册号 | int8 | 64 |  | √ | 0 | [物料检修信息 mpdm_materialmtcinfo](../mpdm_files/mpdm_materialmtcinfo.md) |
| 34 | factualleavetime | 实际离场时间 | timestamp | 0 |  |  | null | 实际离场时间 |
| 35 | fconstructionunit | 工期单位 | int8 | 64 |  | √ | 0 | [工期单位 pmpd_timeunit](../fmm_files/pmpd_timeunit.md) |
| 36 | flistcreator | 清单创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 37 | faircraftplayid | 机位 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 38 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 39 | fplancreatetime | 计划创建时间 | timestamp | 0 |  |  | null | 计划创建时间 |
| 40 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 41 | fstockupmode | 备货方式 | varchar | 5 |  | √ | ' ' | 备货方式,枚举: 0 :按BOM备货 1 :按历史用量备货 2 :按客户需求备货 |
| 42 | fpredeparttime | 完工时间 | timestamp | 0 |  |  | null | 完工时间 |
| 43 | flistmodifytime | 清单修改时间 | timestamp | 0 |  |  | null | 清单修改时间 |
| 44 | fschdstatus | 资源计划状态 | int8 | 64 |  | √ | 0 | [资源计划状态 mpdm_resource_plan_status](../mpdm_files/mpdm_resource_plan_status.md) |
| 45 | fplancreator | 计划创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 46 | fforecastversion | 预测版本 | varchar | 80 |  | √ | ' ' | 预测版本 |
| 47 | fscheduleintime | 预计进场时间 | timestamp | 0 |  |  | null | 预计进场时间 |
| 48 | fmrtype | 检修设备类型 | int8 | 64 |  | √ | 0 | [检修设备类型 mpdm_mrtype](../mpdm_files/mpdm_mrtype.md) |
| 49 | fbilltype | 单据类型 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mds_stockupstatus_billno |  | fbillno |
| 2 | pk_mds_stockupstatus |  | fid |
