# 资源耗用量归集-sco_resourceuse

## 资源耗用量归集-主表 t_sco_resourceuse

- **表名称：** 资源耗用量归集-主表
- **表名：** t_sco_resourceuse

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmanuorgid | 生产组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fvouchertype | fvouchertype | varchar | 50 |  | √ | ' ' |  |
| 4 | fsrcentryid | 源单分录(子分录)id | int8 | 64 |  | √ | 0 | 源单分录(子分录)id |
| 5 | fpricedate | 取价时间 | timestamp | 0 |  |  | null | 取价时间 |
| 6 | forgid | 核算组织(废弃-230629多核算体系改造) | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fappnum | 所属应用 | varchar | 10 |  | √ | ' ' | 所属应用,枚举: sca :标准成本 aca :实际成本 |
| 8 | fsource | 来源 | varchar | 30 |  | √ | ' ' | 来源,枚举: OBJECTRULE :内部系统引入 EXCEL :模板引入 API :API接口 MANUAL :手工录入 CONFIG :按配置方案引入 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fworkcenterid | 工作中心 | int8 | 64 |  | √ | 0 | 工作中心 sfc_workcenter |
| 12 | fnsrcauditdate | 来源单据审核日期 | timestamp | 0 |  |  | null | 来源单据审核日期 |
| 13 | fbillno | 单据编号 | varchar | 255 |  | √ | ' ' | 单据编号 |
| 14 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 15 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | fcostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 17 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 18 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 19 | fresourceid | 资源编码 | int8 | 64 |  | √ | 0 | 资源 mpdm_resourceinfo |
| 20 | fsrcbillid | 来源单据id | int8 | 64 |  | √ | 0 | 来源单据id |
| 21 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 22 | fbizdate | 汇报时间 | timestamp | 0 |  |  | null | 汇报时间 |
| 23 | fcollconfigid | 配置单 | int8 | 64 |  | √ | 0 | 成本归集配置单 sco_costcollectconfig |
| 24 | fbookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 25 | fsrcbilltype | 源单类型 | varchar | 50 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 26 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | index_sco_resourceuse |  | forgid,fcostcenterid |
| 2 | idx_resourceuse_bokda |  | fbookdate |
| 3 | pk_sco_resourceuse |  | fid |
| 4 | idx_sco_resource_billno |  | fbillno |

---

## 单据体-子表 t_sco_resourceuseentry

- **表名称：** 单据体-子表
- **表名：** t_sco_resourceuseentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmaterialid | 产品编码 | int8 | 64 |  | √ | 0 | 物料生产信息 bd_materialmftinfo |
| 3 | factivity | 活动名称 | varchar | 10 |  | √ | ' ' | 活动名称,枚举: A :准备活动 B :加工活动 C :其他活动一 D :其他活动二 |
| 4 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fversionid | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本（作废） bd_materialversion |
| 7 | fbasehour | 基准单位工时 | numeric | 23 | 10 | √ | 0 | 基准单位工时 |
| 8 | fdescription | 工序说明 | varchar | 255 |  | √ | ' ' | 工序说明 |
| 9 | fworkhourid | 工时单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 10 | ffacthour | 实际工时 | numeric | 23 | 10 | √ | 0 | 实际工时 |
| 11 | ffactbatch | 实际批量 | numeric | 23 | 10 | √ | 0 | 实际批量 |
| 12 | fopraid | 工序编码 | int8 | 64 |  | √ | 0 | 标准工序 mpdm_normprocess |
| 13 | fbaseworkhour | 基准单位 | varchar | 30 |  | √ | ' ' | 基准单位,枚举: 1 :时 2 :分 3 :秒 |
| 14 | ffactuse | 实际用量 | numeric | 23 | 10 | √ | 0 | 实际用量 |
| 15 | ftimeunit | 工时单位 | varchar | 50 |  | √ | ' ' | 工时单位,枚举: hour :小时 minute :分钟 second :秒 |
| 16 | factivitytype | 活动类型 | varchar | 10 |  | √ | ' ' | 活动类型,枚举: 0 :机器 1 :人工 |
| 17 | fworkhour | 工时单位 | varchar | 30 |  | √ | ' ' | 工时单位,枚举: 1 :时 2 :分 3 :秒 |
| 18 | fcostobjectid | 成本核算对象 | int8 | 64 |  | √ | 0 | 成本核算对象 sco_costobjectf7 |
| 19 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sco_resourceuseentry |  | fentryid |
| 2 | index_sco_resourceentry |  | fid,fcostobjectid |
