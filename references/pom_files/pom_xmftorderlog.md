# 生产工单变更日志-pom_xmftorderlog

## 单据体-子表 t_pom_xmftordermlogentry

- **表名称：** 单据体-子表
- **表名：** t_pom_xmftordermlogentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseqfield | 变更行 | varchar | 50 |  | √ | ' ' | 变更行 |
| 3 | fiscontrolqty | 控制入库数量 | varchar | 50 |  | √ | ' ' | 控制入库数量 |
| 4 | flocation | 仓位 | varchar | 500 |  | √ | ' ' | 仓位 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | frcvinhighlimit | 入库上限允差（%） | varchar | 50 |  | √ | ' ' | 入库上限允差（%） |
| 7 | fchangetype | fchangetype | varchar | 50 |  | √ | ' ' |  |
| 8 | fsrcbillnoentry | 生产工单编号 | varchar | 50 |  | √ | ' ' | 生产工单编号 |
| 9 | finwardept | 入库组织 | varchar | 500 |  | √ | ' ' | 入库组织 |
| 10 | fmaterial | 产品编码 | int8 | 64 |  | √ | 0 | 物料生产信息 bd_materialmftinfo |
| 11 | fplanpreparetime | 计划准备时间 | varchar | 50 |  | √ | ' ' | 计划准备时间 |
| 12 | finwarmin | 入库下限 | varchar | 50 |  | √ | ' ' | 入库下限 |
| 13 | fqty | 数量 | varchar | 50 |  | √ | ' ' | 数量 |
| 14 | fsrcbillseqentry | 生产工单行号 | int8 | 64 |  | √ | 0 | 生产工单行号 |
| 15 | fbatchno | 批号 | varchar | 110 |  | √ | ' ' | 批号 |
| 16 | fchangetypeentity | fchangetypeentity | varchar | 50 |  | √ | ' ' |  |
| 17 | frcvinlowlimit | 入库下限允差（%） | varchar | 50 |  | √ | ' ' | 入库下限允差（%） |
| 18 | funitfield | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 19 | finwarmax | 入库上限 | varchar | 50 |  | √ | ' ' | 入库上限 |
| 20 | fproducttype | 产品类型 | varchar | 50 |  | √ | ' ' | 产品类型,枚举: C :主产品 A :联产品 B :副产品 |
| 21 | fwarehouse | 仓库 | varchar | 500 |  | √ | ' ' | 仓库 |
| 22 | fplanbegintime | 计划开工时间 | varchar | 50 |  | √ | ' ' | 计划开工时间 |
| 23 | fplanendtime | 计划完工时间 | varchar | 50 |  | √ | ' ' | 计划完工时间 |
| 24 | fbaseqty | 基本数量 | varchar | 110 |  | √ | ' ' | 基本数量 |
| 25 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 26 | foutputoperation | 产出工序 | varchar | 110 |  | √ | ' ' | 产出工序 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pom_xmftordermlogentry |  | fentryid |
| 2 | idx_pom_xmftordermlogentry_fid |  | fid |

---

## 生产工单变更日志-主表 t_pom_xmftordermlog

- **表名称：** 生产工单变更日志-主表
- **表名：** t_pom_xmftordermlog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fxbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 3 | fsrcbillno | 生产工单编号 | varchar | 50 |  | √ | ' ' | 生产工单编号 |
| 4 | forgid | 生产组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fxmdjson | 变更md文本 | varchar | 255 |  | √ | ' ' | 变更md文本 |
| 6 | fchangetype | 变更方式 | varchar | 50 |  | √ | ' ' | 变更方式,枚举: A :新增 B :修改 C :取消 |
| 7 | fbiztime | 单据日期 | timestamp | 0 |  |  | null | 单据日期 |
| 8 | fmodifytime | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 9 | fsrcbillentryseq | 生产工单行号 | int8 | 64 |  | √ | 0 | 生产工单行号 |
| 10 | fchangestatus | 变更状态 | varchar | 50 |  | √ | ' ' | 变更状态,枚举: A :变更中 B :变更完成 |
| 11 | fcreatorid | 变更人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fxbilljson_tag | 变更单Json_详情 | text | 0 |  |  | null | 变更单Json_详情 |
| 13 | fsrcbilljson_tag | 订单Json_详情 | text | 0 |  |  | null | 订单Json_详情 |
| 14 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fsrcbillid | 生产工单ID | int8 | 64 |  | √ | 0 | 生产工单ID |
| 16 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 17 | fxbilljson | 变更单Json | varchar | 255 |  | √ | ' ' | 变更单Json |
| 18 | fxmdjson_tag | 变更md文本_详情 | text | 0 |  |  | null | 变更md文本_详情 |
| 19 | fsrcbillversion | 生产工单版本 | int8 | 64 |  | √ | 0 | 生产工单版本 |
| 20 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 21 | fxbillid | 变更单ID | int8 | 64 |  | √ | 0 | 变更单ID |
| 22 | fsrcbilljson | 订单Json | varchar | 255 |  | √ | ' ' | 订单Json |
| 23 | fsrcbillentryid | 生产工单分录ID | int8 | 64 |  | √ | 0 | 生产工单分录ID |
| 24 | fxbillentryseq | 变更单分录行号 | int8 | 64 |  | √ | 0 | 变更单分录行号 |
| 25 | fbeginbookdate | 开工记账日期 | timestamp | 0 |  |  | null | 开工记账日期 |
| 26 | fxbillentryid | 变更单分录ID | int8 | 64 |  | √ | 0 | 变更单分录ID |
| 27 | fxreason | 变更原因 | varchar | 255 |  | √ | ' ' | 变更原因 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | index_pom_xmftorderml_xbilleid |  | fxbillentryid |
| 2 | pk_t_pom_xmftordermlog |  | fid |
