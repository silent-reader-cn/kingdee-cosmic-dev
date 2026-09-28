# 委外工单变更日志-om_xmftorderlog

## 单据体-子表 t_om_xmftordermlogentry

- **表名称：** 单据体-子表
- **表名：** t_om_xmftordermlogentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseqfield | 变更行 | varchar | 50 |  | √ | ' ' | 变更行 |
| 3 | fiscontrolqty | 控制入库数量 | varchar | 50 |  | √ | ' ' | 控制入库数量 |
| 4 | flocation | 仓位 | varchar | 50 |  | √ | ' ' | 仓位 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | frcvinhighlimit | 入库上限允差（%） | varchar | 50 |  | √ | ' ' | 入库上限允差（%） |
| 7 | fchangetype | fchangetype | varchar | 50 |  | √ | ' ' |  |
| 8 | fsrcbillnoentry | 委外工单编号 | varchar | 50 |  | √ | ' ' | 委外工单编号 |
| 9 | finwardept | 入库组织 | varchar | 50 |  | √ | ' ' | 入库组织 |
| 10 | fmaterial | 产品编码 | int8 | 64 |  | √ | 0 | [物料生产信息 bd_materialmftinfo](../sbd_files/bd_materialmftinfo.md) |
| 11 | fplanpreparetime | 计划准备时间 | varchar | 50 |  | √ | ' ' | 计划准备时间 |
| 12 | finwarmin | 入库下限 | varchar | 50 |  | √ | ' ' | 入库下限 |
| 13 | fqty | 数量 | varchar | 50 |  | √ | ' ' | 数量 |
| 14 | fsrcbillseqentry | 委外工单行号 | int8 | 64 |  | √ | 0 | 委外工单行号 |
| 15 | fchangetypeentity | fchangetypeentity | varchar | 50 |  | √ | ' ' |  |
| 16 | frcvinlowlimit | 入库下限允差（%） | varchar | 50 |  | √ | ' ' | 入库下限允差（%） |
| 17 | funitfield | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 18 | finwarmax | 入库上限 | varchar | 50 |  | √ | ' ' | 入库上限 |
| 19 | fproducttype | 产品类型 | varchar | 50 |  | √ | ' ' | 产品类型,枚举: C :主产品 A :联产品 B :副产品 |
| 20 | fwarehouse | 仓库 | varchar | 50 |  | √ | ' ' | 仓库 |
| 21 | fplanbegintime | 计划开工时间 | varchar | 50 |  | √ | ' ' | 计划开工时间 |
| 22 | fplanendtime | 计划完工时间 | varchar | 50 |  | √ | ' ' | 计划完工时间 |
| 23 | fbaseqty | 基本数量 | varchar | 110 |  | √ | ' ' | 基本数量 |
| 24 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 25 | foutputoperation | 产出工序 | varchar | 110 |  | √ | ' ' | 产出工序 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_om_xmftordermlogentry |  | fentryid |
| 2 | idx_om_xmftordermlogentry_fid |  | fid |

---

## 委外工单变更日志-主表 t_om_xmftordermlog

- **表名称：** 委外工单变更日志-主表
- **表名：** t_om_xmftordermlog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fxbillno | 变更单编号 | varchar | 50 |  | √ | ' ' | 变更单编号 |
| 3 | fsrcbillno | 委外工单编号 | varchar | 50 |  | √ | ' ' | 委外工单编号 |
| 4 | fisproduction | 是否投产 | bpchar | 1 |  | √ | '0' | 是否投产 |
| 5 | forgid | 生产组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fxmdjson | 变更md文本 | varchar | 255 |  | √ | ' ' | 变更md文本 |
| 7 | fchangetype | 变更方式 | varchar | 50 |  | √ | ' ' | 变更方式,枚举: A :新增 B :修改 C :取消 |
| 8 | fbiztime | 变更单日期 | timestamp | 0 |  |  | null | 变更单日期 |
| 9 | fmodifytime | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 10 | fsrcbillentryseq | 委外工单行号 | int8 | 64 |  | √ | 0 | 委外工单行号 |
| 11 | fchangestatus | 变更状态 | varchar | 50 |  | √ | ' ' | 变更状态,枚举: A :变更中 B :变更完成 |
| 12 | fclosebookdate | fclosebookdate | timestamp | 0 |  |  | null |  |
| 13 | fcreatorid | 变更人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fxbilljson_tag | 变更单Json_详情 | text | 0 |  |  | null | 变更单Json_详情 |
| 15 | fsrcbilljson_tag | 订单Json_详情 | text | 0 |  |  | null | 订单Json_详情 |
| 16 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fsrcbillid | 委外工单ID | int8 | 64 |  | √ | 0 | 委外工单ID |
| 18 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 19 | fxbilljson | 变更单Json | varchar | 255 |  | √ | ' ' | 变更单Json |
| 20 | fxmdjson_tag | 变更md文本_详情 | text | 0 |  |  | null | 变更md文本_详情 |
| 21 | fsrcbillversion | 生产工单版本 | int8 | 64 |  | √ | 0 | 生产工单版本 |
| 22 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 23 | fxbillid | 变更单ID | int8 | 64 |  | √ | 0 | 变更单ID |
| 24 | fsrcbilljson | 订单Json | varchar | 255 |  | √ | ' ' | 订单Json |
| 25 | fsrcbillentryid | 委外工单分录ID | int8 | 64 |  | √ | 0 | 委外工单分录ID |
| 26 | fxbillentryseq | 变更单分录行号 | int8 | 64 |  | √ | 0 | 变更单分录行号 |
| 27 | fbeginbookdate | 投产记账日期 | timestamp | 0 |  |  | null | 投产记账日期 |
| 28 | fxbillentryid | 变更单分录ID | int8 | 64 |  | √ | 0 | 变更单分录ID |
| 29 | fxreason | 变更原因 | varchar | 255 |  | √ | ' ' | 变更原因 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_om_xmftordermlog |  | fid |
| 2 | index_om_xmftorderml_xbilleid |  | fxbillentryid |
