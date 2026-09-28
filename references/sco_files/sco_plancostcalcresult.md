# 计划成本计算结果单-sco_plancostcalcresult

## 计划成本计算结果单-主表 t_sco_plancostcalcresult

- **表名称：** 计划成本计算结果单-主表
- **表名：** t_sco_plancostcalcresult

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmanuorgid | 生产组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fprocessrouteid | 工艺路线 | int8 | 64 |  | √ | 0 | 工艺路线维护（废弃） pdm_route |
| 4 | fplanqty | 工单计划数量 | numeric | 23 | 10 | √ | 0 | 工单计划数量 |
| 5 | foutqty | 产品委外数量 | numeric | 23 | 10 | √ | 0 | 产品委外数量 |
| 6 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 7 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fexpdate | 失效日期 | timestamp | 0 |  |  | null | 失效日期 |
| 9 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | 配置号 bd_configuredcode |
| 10 | feffectdate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 11 | forderentryid | 工单分录id | int8 | 64 |  | √ | 0 | 工单分录id |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 bd_tracknumber |
| 15 | fkeycolid | 卷算维度数据 | int8 | 64 |  | √ | 0 | 卷算维度数据表 cad_keycol |
| 16 | forderentryseq | 工单行号 | int8 | 64 |  | √ | 0 | 工单行号 |
| 17 | fbillno | 单据编号 | varchar | 255 |  | √ | ' ' | 单据编号 |
| 18 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 19 | fbillstatus | 状态 | varchar | 30 |  | √ | ' ' | 状态,枚举: A :失败 B :成功 |
| 20 | foutamount | 产品委外金额 | numeric | 23 | 10 | √ | 0 | 产品委外金额 |
| 21 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 22 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 23 | fcalcdate | 计算日期 | timestamp | 0 |  |  | null | 计算日期 |
| 24 | forderno | 工单编号 | varchar | 50 |  | √ | ' ' | 工单编号 |
| 25 | fcosttypeid | 标准成本方案 | int8 | 64 |  | √ | 0 | 标准成本方案 cad_costtype |
| 26 | fbilltype | 单据类型 | varchar | 30 |  | √ | ' ' | 单据类型,枚举: pom_mftorder :生产工单 om_mftorder :委外工单 |
| 27 | funit | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 28 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 29 | fkeycol | 维度字段 | varchar | 50 |  | √ | ' ' | 维度字段 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plancostorderseq |  | forderentryseq |
| 2 | idx_plancostentryid |  | forderentryid |
| 3 | idx_plancostordernum |  | forderno |
| 4 | pk_sco_plancostcalcresult |  | fid |
| 5 | idx_sco_plancostcalcresult_kc |  | fkeycol |

---

## 单据体-子表 t_sco_planresultentry

- **表名称：** 单据体-子表
- **表名：** t_sco_planresultentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsubelementid | 成本子要素 | int8 | 64 |  | √ | 0 | 成本子要素 cad_subelement |
| 3 | fresourceid | 资源 | int8 | 64 |  | √ | 0 | 资源维护(废弃) mpdm_resources |
| 4 | fneedqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fcalcbasis | 数据类别 | varchar | 30 |  | √ | ' ' | 数据类别,枚举: 0 :本层成本 1 :下级成本 |
| 7 | fcaltype | 计算依据 | varchar | 10 |  | √ | ' ' | 计算依据,枚举: 001 :资源工时 002 :物料 003 :批次 |
| 8 | fprice | 单价 | numeric | 23 | 10 | √ | 0 | 单价 |
| 9 | fsrcqty | 资源基本数量 | numeric | 23 | 10 | √ | 0 | 资源基本数量 |
| 10 | fneedamount | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 11 | fsubmaterialid | 组件物料编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 12 | fsrcamount | 资源成本 | numeric | 23 | 10 | √ | 0 | 资源成本 |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sco_planresultentry |  | fentryid |
| 2 | idx_sco_planresultentry |  | fid |
