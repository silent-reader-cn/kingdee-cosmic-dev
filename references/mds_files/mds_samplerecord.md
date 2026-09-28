# 样本历史使用数据-mds_samplerecord

## 样本历史使用数据-主表 t_mds_samplehisrecord

- **表名称：** 样本历史使用数据-主表
- **表名：** t_mds_samplehisrecord

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fchecktypedesc | 检修级别名称 | varchar | 255 |  | √ | ' ' | 检修级别名称 |
| 3 | fbillqty | 单据数量 | numeric | 23 | 10 | √ | 0 | 单据数量 |
| 4 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | funitchange | 是否单位转换 | bpchar | 1 |  | √ | '0' | 是否单位转换 |
| 6 | forderid | 工单ID | int8 | 64 |  | √ | 0 | 工单ID |
| 7 | flogid | 计算日志 | int8 | 64 |  | √ | 0 | 用量概率计算日志 mds_probabilitylog |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fchecktype | 检修级别 | int8 | 64 |  | √ | 0 | 检修级别 mpdm_checktype |
| 10 | fuse | 是否选择 | bpchar | 1 |  | √ | '0' | 是否选择 |
| 11 | fbiztype | 业务类型 | int8 | 64 |  | √ | 0 | 业务类型 bd_biztype |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fconmtypenumber | 合同类型编码 | varchar | 2000 |  | √ | ' ' | 合同类型编码 |
| 14 | fsysuse | 系统选择 | bpchar | 1 |  | √ | '0' | 系统选择 |
| 15 | fmaterial | 物料编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 16 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 17 | facreg | 检修设备 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 18 | fqty | 转换数量 | numeric | 23 | 10 | √ | 0 | 转换数量 |
| 19 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 20 | fcustomer | 客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 21 | fusedate | 单据时间 | timestamp | 0 |  |  | null | 单据时间 |
| 22 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 23 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 24 | fcardtype | 工卡类型 | int8 | 64 |  | √ | 0 | 工卡类型 mpdm_jobcardtype |
| 25 | fbackupproject | 备货项目 | int8 | 64 |  | √ | 0 | 项目 pmpd_project |
| 26 | fconmtypename | 合同类型名称 | varchar | 2000 |  | √ | ' ' | 合同类型名称 |
| 27 | factype | 检修设备类型 | int8 | 64 |  | √ | 0 | 检修设备类型 mpdm_mrtype |
| 28 | fplanno | 计划号 | varchar | 50 |  | √ | ' ' | 计划号 |
| 29 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 30 | fconmtypeid | 合同类型ID | varchar | 2000 |  | √ | ' ' | 合同类型ID |
| 31 | fmaterialtype | 物料类型 | int8 | 64 |  | √ | 0 | 物料分类 bd_materialgroup |
| 32 | fsupplyresp | 供货责任 | varchar | 5 |  | √ | ' ' | 供货责任,枚举: 0 :库存组织 1 :客户 2 :VMI供应商 3 :非VMI供应商 |
| 33 | fatachapterno | 章节号 | int8 | 64 |  | √ | 0 | ATA章节号 mpdm_atachapterno |
| 34 | fanalysisdim | 分析维度 | varchar | 50 |  | √ | ' ' | 分析维度,枚举: A :客户+检修设备类型+检修级别 B :客户+检修设备类型 C :检修设备类型 |
| 35 | fbeforematerial | 转换前物料编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 36 | fmaterialchange | 是否物料转换 | bpchar | 1 |  | √ | '0' | 是否物料转换 |
| 37 | fproject | 项目号 | int8 | 64 |  | √ | 0 | 项目 pmpd_project |
| 38 | fcard | 工卡号 | int8 | 64 |  | √ | 0 | 工卡 mpdm_mrocardroute |
| 39 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 40 | facregtext | facregtext | varchar | 255 |  | √ | ' ' |  |
| 41 | funit | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 42 | fbeforeunit | 转换前计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 43 | fatanumber | 章节编码 | varchar | 80 |  | √ | ' ' | 章节编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mds_samplehisrecord |  | fid |
| 2 | idx_mds_samplehisrecord |  | flogid |
