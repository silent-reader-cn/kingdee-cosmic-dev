# 计划订单变更单日志-mrp_xplanorderlog

## 单据体-子表 t_mrp_xplanorderlogentry

- **表名称：** 单据体-子表
- **表名：** t_mrp_xplanorderlogentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fchangeqty | 订单数量 | varchar | 50 |  | √ | ' ' | 订单数量 |
| 3 | fsrcbillnoentry | 计划订单编号 | varchar | 200 |  | √ | ' ' | 计划订单编号 |
| 4 | fseqfield | 变更行 | int8 | 64 |  | √ | 0 | 变更行 |
| 5 | fchangtracknum | 跟踪号 | varchar | 100 |  | √ | ' ' | 跟踪号 |
| 6 | fchangedate | 可用日期 | varchar | 50 |  | √ | ' ' | 可用日期 |
| 7 | fconfiguredcode | 配置号 | int8 | 64 |  | √ | 0 | 配置号 bd_configuredcode |
| 8 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 9 | fmaterial | 物料编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | funit | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mrp_xplanorderlogentry |  | fid,fseq |
| 2 | pk_mrp_xplanorderlogentry |  | fentryid |

---

## 计划订单变更单日志-主表 t_mrp_xplanorderlog

- **表名称：** 计划订单变更单日志-主表
- **表名：** t_mrp_xplanorderlog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fxbillno | 变更单编号 | varchar | 100 |  | √ | ' ' | 变更单编号 |
| 4 | fsrcbillno | 计划建议编号 | varchar | 100 |  | √ | ' ' | 计划建议编号 |
| 5 | fcreatetime | 变更创建时间 | timestamp | 0 |  |  | null | 变更创建时间 |
| 6 | fproorpurorg | 供应组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fsrcbillid | 计划建议ID | int8 | 64 |  | √ | 0 | 计划建议ID |
| 8 | forgid | 需求组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 9 | fauditdate | 变更审核时间 | timestamp | 0 |  |  | null | 变更审核时间 |
| 10 | fchangetype | 变更方式 | varchar | 30 |  | √ | ' ' | 变更方式,枚举: A :提前 B :延后 C :取消 D :直接挪用 |
| 11 | fxbillid | 变更单ID | int8 | 64 |  | √ | 0 | 变更单ID |
| 12 | fmodifytime | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 13 | fchangestatus | 变更状态 | varchar | 30 |  | √ | ' ' | 变更状态,枚举: A :变更中 B :变更完成 |
| 14 | fcreatorid | 变更创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fauditorid | 变更审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | fxreason | 变更原因 | varchar | 512 |  | √ | ' ' | 变更原因 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mrp_xplanorderlog_xbid |  | fxbillid |
| 2 | idx_mrp_xplanorderlog_src |  | fsrcbillid |
| 3 | pk_mrp_xplanorderlog |  | fid |
