# 资源耗用量归集-sca_resourceuse

## 资源耗用量归集-主表 t_sca_resourceuse

- **表名称：** 资源耗用量归集-主表
- **表名：** t_sca_resourceuse

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fmanuorgid | 生产组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fcostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | [成本中心 bos_costcenter](../basedata_files/bos_costcenter.md) |
| 6 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 7 | fpricedate | 取价时间 | timestamp | 0 |  |  | null | 取价时间 |
| 8 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | fresourceid | 资源编码（废弃） | int8 | 64 |  | √ | 0 | [资源维护(废弃) mpdm_resources](../mpdm_files/mpdm_resources.md) |
| 10 | fsrcbillid | 来源单据id | int8 | 64 |  | √ | 0 | 来源单据id |
| 11 | forgid | 核算组织(废弃-230629多核算体系改造) | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 12 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 13 | fappnum | 所属应用 | varchar | 100 |  | √ | ' ' | 所属应用,枚举: sca :标准成本 aca :实际成本 |
| 14 | fsource | 来源 | varchar | 30 |  | √ | ' ' | 来源,枚举: OBJECTRULE :内部系统引入 EXCEL :模板引入 API :API接口 MANUAL :手工录入 CONFIG :按配置方案引入 |
| 15 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 16 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fbizdate | 汇报时间 | timestamp | 0 |  |  | null | 汇报时间 |
| 18 | fcollconfigid | 配置单 | int8 | 64 |  | √ | 0 | [成本归集配置单 cad_costcollectconfig](../aca_files/cad_costcollectconfig.md) |
| 19 | fbookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 20 | fsrcbilltype | 源单类型 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 21 | fbillno | 单据编号 | varchar | 60 |  | √ | ' ' | 单据编号 |
| 22 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_sca_resourceuse_pkey |  | fid |
| 2 | idx_resourceuse_reid |  | fresourceid |
| 3 | index_sca_resourceuse |  | forgid,fcostcenterid |
| 4 | idx_resourceuse_costc |  | fcostcenterid |

---

## 单据体-子表 t_sca_resourceuseentry

- **表名称：** 单据体-子表
- **表名：** t_sca_resourceuseentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flabhours | 实际工时（人工） | numeric | 23 | 2 | √ | 0 | 实际工时（人工） |
| 3 | fproplanid | 工序计划号 | int8 | 64 |  | √ | 0 | [工序计划F7 sfc_processplan_f7](../sfc_files/sfc_processplan_f7.md) |
| 4 | fmaterialid | 产品编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 5 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 6 | fworkwastqty | 工废数量 | numeric | 23 | 10 | √ | 0 | 工废数量 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fversionid | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本（作废） bd_materialversion](../basedata_files/bd_materialversion.md) |
| 9 | fworkhourid | 工时单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 10 | ffacthour | 实际总工时 | numeric | 23 | 10 | √ | 0.0000000000 | 实际总工时 |
| 11 | fproplanentryid | 工序计划分录内码 | int8 | 64 |  | √ | 0 | [工序计划分录F7 sfc_processplanentry_f7](../sfc_files/sfc_processplanentry_f7.md) |
| 12 | ffactbatch | 实际批量 | numeric | 23 | 10 | √ | 0.0000000000 | 实际批量 |
| 13 | fcompleteqty | 完工数量 | numeric | 23 | 10 | √ | 0 | 完工数量 |
| 14 | fopraid | 工序编码（废弃） | int8 | 64 |  | √ | 0 | [标准工序定义(废弃) mpdm_workprocedure](../mpdm_files/mpdm_workprocedure.md) |
| 15 | ffactuse | 实际用量 | numeric | 23 | 10 | √ | 0.0000000000 | 实际用量 |
| 16 | ftimeunit | 工时单位 | varchar | 36 |  | √ | ' ' | 工时单位,枚举: hour :小时 minute :分钟 second :秒 |
| 17 | fmachhours | 实际工时（机器） | numeric | 23 | 2 | √ | 0 | 实际工时（机器） |
| 18 | freworkqty | 待返工数量 | numeric | 23 | 10 | √ | 0 | 待返工数量 |
| 19 | fquaqyt | 合格数量 | numeric | 23 | 10 | √ | 0 | 合格数量 |
| 20 | fcostobjectid | 成本核算对象 | int8 | 64 |  | √ | 0 | [成本核算对象 cad_costobjectf7](../aca_files/cad_costobjectf7.md) |
| 21 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 22 | fstockwastqty | 料废数量 | numeric | 23 | 10 | √ | 0 | 料废数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_reuseentry_costobj |  | fcostobjectid |
| 2 | t_sca_resourceuseentry_pkey |  | fentryid |
| 3 | index_sca_resourceentry |  | fid,fcostobjectid |
