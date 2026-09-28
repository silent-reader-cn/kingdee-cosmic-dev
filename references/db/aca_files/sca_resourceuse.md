# 资源耗用量归集-sca_resourceuse

## 资源耗用量归集-主表 t_sca_resourceuse

- **表名称：** 资源耗用量归集-主表
- **表名：** t_sca_resourceuse

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fmanuorgid | 生产组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fcostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 6 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 7 | fpricedate | 取价时间 | timestamp | 0 |  |  | null | 取价时间 |
| 8 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | fresourceid | 资源编码 | int8 | 64 |  | √ | 0 | 资源维护(废弃) mpdm_resources |
| 10 | fsrcbillid | 来源单据id | int8 | 64 |  | √ | 0 | 来源单据id |
| 11 | forgid | 核算组织(废弃-230629多核算体系改造) | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 12 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 13 | fappnum | 所属应用 | varchar | 100 |  | √ | ' ' | 所属应用,枚举: sca :标准成本 aca :实际成本 |
| 14 | fsource | 来源 | varchar | 30 |  | √ | ' ' | 来源,枚举: OBJECTRULE :内部系统引入 EXCEL :模板引入 API :API接口 MANUAL :手工录入 CONFIG :按配置方案引入 |
| 15 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 16 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | fbizdate | 汇报时间 | timestamp | 0 |  |  | null | 汇报时间 |
| 18 | fcollconfigid | 配置单 | int8 | 64 |  | √ | 0 | 成本归集配置单 cad_costcollectconfig |
| 19 | fbookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 20 | fsrcbilltype | 源单类型 | varchar | 50 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 21 | fbillno | 单据编号 | varchar | 60 |  | √ | ' ' | 单据编号 |
| 22 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

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
| 2 | fmaterialid | 产品编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 3 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fversionid | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本（作废） bd_materialversion |
| 6 | fworkhourid | 工时单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 7 | ffacthour | 实际工时 | numeric | 23 | 10 | √ | 0.0000000000 | 实际工时 |
| 8 | ffactbatch | 实际批量 | numeric | 23 | 10 | √ | 0.0000000000 | 实际批量 |
| 9 | fopraid | 工序编码 | int8 | 64 |  | √ | 0 | 标准工序定义(废弃) mpdm_workprocedure |
| 10 | ffactuse | 实际用量 | numeric | 23 | 10 | √ | 0.0000000000 | 实际用量 |
| 11 | ftimeunit | 工时单位 | varchar | 36 |  | √ | ' ' | 工时单位,枚举: hour :小时 minute :分钟 second :秒 |
| 12 | fcostobjectid | 成本核算对象 | int8 | 64 |  | √ | 0 | 成本核算对象 cad_costobjectf7 |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

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
