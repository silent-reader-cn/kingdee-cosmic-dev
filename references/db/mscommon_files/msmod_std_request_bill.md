# 预留需求模型-msmod_std_request_bill

## 单据体-子表 t_msmod_materialinfo

- **表名称：** 单据体-子表
- **表名：** t_msmod_materialinfo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | f_location_id | 仓位 | int8 | 64 |  | √ | 0 | 仓位 bd_location |
| 3 | f_project_id | 项目 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 4 | f_unit | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 5 | f_base_unit | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 6 | fconfiguredcode | 配置号 | int8 | 64 |  | √ | 0 | 配置号 bd_configuredcode |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fkeeper | 保管者 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 9 | f_lotnumber | 批号 | varchar | 50 |  | √ | ' ' | 批号 |
| 10 | f_base_qty | 基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本数量 |
| 11 | fproductdate | 生产日期 | timestamp | 0 |  |  | null | 生产日期 |
| 12 | finvtype | 库存类型 | int8 | 64 |  | √ | 0 | 库存类型 bd_invtype |
| 13 | f_qty | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 14 | f_ispresent | 赠品 | bpchar | 1 |  | √ | '0' | 赠品 |
| 15 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 bd_tracknumber |
| 16 | f_entry_id | 分录ID | int8 | 64 |  | √ | 0 | 分录ID |
| 17 | fbomversionid | BOM版本号 | int8 | 64 |  | √ | 0 | 物料版本 bd_bomversion_new |
| 18 | f_aux_qty | 辅助数量 | numeric | 23 | 10 | √ | 0.0000000000 | 辅助数量 |
| 19 | f_owner_type | 货主类型 | varchar | 30 |  | √ | ' ' | 货主类型,枚举: bos_org :核算组织 bd_supplier :供应商 bd_customer :客户 |
| 20 | f_owner_id | 货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 21 | fkeepertype | 保管者类型 | varchar | 50 |  | √ | ' ' | 保管者类型,枚举: bos_org :业务单元 bd_customer :客户 bd_supplier :供应商 |
| 22 | f_material_id | 物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 23 | f_aux_unit | 辅助单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 24 | f_warehouse_id | 仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 25 | fexpirydate | 有效期至 | timestamp | 0 |  |  | null | 有效期至 |
| 26 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 27 | fauxpty | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 28 | f_ratio | 比例 | int8 | 64 |  | √ | 1 | 比例 |
| 29 | finvstatus | 库存状态 | int8 | 64 |  | √ | 0 | 库存状态 bd_invstatus |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_msmod_materialinfo |  | fentryid |
| 2 | idx_msmod_materialinfo_id |  | fid |

---

## 预留需求模型-主表 t_msmod_stdrequestbill

- **表名称：** 预留需求模型-主表
- **表名：** t_msmod_stdrequestbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | f_sale_org_id | 需求组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | f_customer_id | 客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 4 | f_bill_no | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 5 | f_operator_id | 需求业务员 | int8 | 64 |  | √ | 0 | 供应链业务员 bd_operator |
| 6 | f_operator_group | 需求业务组 | int8 | 64 |  | √ | 0 | 供应链业务组 bd_operatorgroup |
| 7 | f_biz_date | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 8 | f_sale_dept_id | 需求部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 9 | f_request_date | 要货日期 | timestamp | 0 |  |  | null | 要货日期 |
| 10 | finvorg | 需求库存组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 11 | f_delivery_way | 交货方式 | int8 | 64 |  | √ | 0 | 辅助资料 bos_assistantdata_detail |
| 12 | f_bill_id | 单据ID | int8 | 64 |  | √ | 0 | 单据ID |
| 13 | f_auto_reserve | 自动预留 | bpchar | 1 |  | √ | '0' | 自动预留 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_msmod_stdrequestbill_no |  | f_bill_no |
| 2 | idx_msmod_stdrequestbill_id |  | f_bill_id |
| 3 | pk_t_msmod_stdrequestbill |  | fid |
