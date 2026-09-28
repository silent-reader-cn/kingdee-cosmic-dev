# 供需匹配明细-invp_match_detail

## 供需匹配明细-主表 t_invp_matchdetail

- **表名称：** 供需匹配明细-主表
- **表名：** t_invp_matchdetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fplanschemeid | 计划方案编码 | int8 | 64 |  | √ | 0 | 库存计划方案 invp_scheme |
| 3 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 4 | fplanorgid | 计划组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fplancalnum | 计划运算号 | varchar | 50 |  | √ | ' ' | 计划运算号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_invp_matchdetail |  | fid |
| 2 | idx_invp_detail_org_date |  | fplanorgid,fcreatedate |

---

## 单据体-子表 t_invp_matchdetail_entry

- **表名称：** 单据体-子表
- **表名：** t_invp_matchdetail_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsupplybillno | 供应单据编码 | varchar | 50 |  | √ | ' ' | 供应单据编码 |
| 3 | fsrcsupplyqty | 供应基本数量 | numeric | 23 | 10 | √ | 0 | 供应基本数量 |
| 4 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 5 | fsupplydate | 供应日期 | timestamp | 0 |  |  | null | 供应日期 |
| 6 | fexception_tag | 例外信息_详情 | text | 0 |  |  | null | 例外信息_详情 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fexceptionnumid | 例外信息编码 | int8 | 64 |  | √ | 0 | 例外信息组 mrp_exceptiongroup |
| 9 | fadjustqty | 调整基本数量 | numeric | 23 | 10 | √ | 0 | 调整基本数量 |
| 10 | fdemanddate | 需求日期 | timestamp | 0 |  |  | null | 需求日期 |
| 11 | fadjustsuggest | 调整建议 | varchar | 50 |  | √ | ' ' | 调整建议,枚举: A :不调整 B :建议提前 D :建议延后 F :建议取消 |
| 12 | fadjustdate | 调整日期 | timestamp | 0 |  |  | null | 调整日期 |
| 13 | fsrcdemandqty | 需求基本数量 | numeric | 23 | 10 | √ | 0 | 需求基本数量 |
| 14 | fsupplybillseq | 供应单据行号 | int8 | 64 |  | √ | 0 | 供应单据行号 |
| 15 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 16 | fdemandorgid | 需求组织编码 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 17 | fbillno | 需求单据编码 | varchar | 50 |  | √ | ' ' | 需求单据编码 |
| 18 | fdembilltypeid | 需求单据类型 | varchar | 50 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 19 | fwarehouseid | 供应仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 20 | fsupplyqty | 供应匹配基本数量 | numeric | 23 | 10 | √ | 0 | 供应匹配基本数量 |
| 21 | fdembillseq | 需求单据行号 | int8 | 64 |  | √ | 0 | 需求单据行号 |
| 22 | fsupplybilltypeid | 供应单据类型 | varchar | 50 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 23 | flocationid | 供应仓位 | int8 | 64 |  | √ | 0 | 仓位 bd_location |
| 24 | fsupinvtypeid | 供应库存类型 | int8 | 64 |  | √ | 0 | 库存类型 bd_invtype |
| 25 | fdemandwarehouseid | 需求仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 26 | fsupplyremainqty | 供应剩余基本数量 | int8 | 64 |  | √ | 0 | 供应剩余基本数量 |
| 27 | fdemandqty | 需求匹配基本数量 | numeric | 23 | 10 | √ | 0 | 需求匹配基本数量 |
| 28 | fexception | 例外信息 | varchar | 255 |  | √ | ' ' | 例外信息 |
| 29 | fsupplyorgid | 供应组织编码 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 30 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 31 | fsupinvstatusid | 供应库存状态 | int8 | 64 |  | √ | 0 | 库存状态 bd_invstatus |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_invp_detailentry_id |  | fid,fentryid |
| 2 | pk_invp_matchdetail_entry |  | fentryid |
