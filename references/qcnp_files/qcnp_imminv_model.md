# 执行明细-qcnp_imminv_model

## 执行明细-子表 t_qcnp_iminv_entry

- **表名称：** 执行明细-子表
- **表名：** t_qcnp_iminv_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | freserv2ndqty | 辅助预留数量 | numeric | 23 | 10 | √ | 0 | 辅助预留数量 |
| 3 | favbqty | 可用量 | numeric | 23 | 10 | √ | 0 | 可用量 |
| 4 | fbasejoinqty | 关联数量（基本） | numeric | 23 | 10 | √ | 0 | 关联数量（基本） |
| 5 | flotnumber | 批号 | varchar | 50 |  | √ | ' ' | 批号 |
| 6 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 7 | finspecorgid | 质检组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | funit2ndid | 辅助单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 9 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 10 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 11 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | 配置号 bd_configuredcode |
| 12 | fbaseapplyqty | 基本申请数量 | numeric | 23 | 10 | √ | 0 | 基本申请数量 |
| 13 | finvstatusid | 库存状态 | int8 | 64 |  | √ | 0 | 库存状态 bd_invstatus |
| 14 | fbasereservqty | 基本预留数量 | numeric | 23 | 10 | √ | 0 | 基本预留数量 |
| 15 | fjoinqty | 关联数量 | numeric | 23 | 10 | √ | 0 | 关联数量 |
| 16 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 bd_tracknumber |
| 17 | fownertype | 货主类型 | varchar | 255 |  | √ | ' ' | 货主类型,枚举: bos_org :核算组织 bd_supplier :供应商 bd_customer :客户 |
| 18 | fkeeperid | 保管者 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 19 | fbaseavbqty | 基本可用数量 | numeric | 23 | 10 | √ | 0 | 基本可用数量 |
| 20 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 21 | favb2ndqty | 辅助可用数量 | numeric | 23 | 10 | √ | 0 | 辅助可用数量 |
| 22 | finspres | 请检结果 | varchar | 5 |  | √ | ' ' | 请检结果,枚举: suc :成功 fail :失败 del :删除 |
| 23 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 24 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 25 | fapplyorgid | 申请组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 26 | finvtypeid | 库存类型 | int8 | 64 |  | √ | 0 | 库存类型 bd_invtype |
| 27 | finventoryid | 即时库存ID | int8 | 64 |  | √ | 0 | 即时库存ID |
| 28 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 29 | fkeepertype | 保管者类型 | varchar | 255 |  | √ | ' ' | 保管者类型,枚举: bos_org :库存组织 bd_customer :客户 bd_supplier :供应商 |
| 30 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 31 | finvorgid | 库存组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 32 | freservqty | 预留数量 | numeric | 23 | 10 | √ | 0 | 预留数量 |
| 33 | finvunitid | 库存单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 34 | fqty2nd | 辅助数量 | numeric | 23 | 10 | √ | 0 | 辅助数量 |
| 35 | fownerid | 货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 36 | flocationid | 仓位 | int8 | 64 |  | √ | 0 | 仓位 bd_location |
| 37 | fapplyqty | 申请数量 | numeric | 23 | 10 | √ | 0 | 申请数量 |
| 38 | fexpirydate | 到期日期 | timestamp | 0 |  |  | null | 到期日期 |
| 39 | fmaterialcomid | 物料公共信息 | int8 | 64 |  | √ | 0 | 物料组织公共信息 bd_materialcommon |
| 40 | fproducedate | 生产日期 | timestamp | 0 |  |  | null | 生产日期 |
| 41 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 42 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_qcnp_iminnv_fid |  | fid |
| 2 | idx_qcnp_iminnv_fseq |  | fseq |
| 3 | pk_qcnp_iminv_entry |  | fentryid |

---

## 执行明细-主表 t_qcnp_imminv

- **表名称：** 执行明细-主表
- **表名：** t_qcnp_imminv

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | finvimpschemeid | 执行方案 | int8 | 64 |  | √ | 0 | 执行方案 qcbd_invimpschem |
| 4 | fbillstatus | 单据状态 | varchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 8 | fexedate | 日期 | timestamp | 0 |  |  | null | 日期 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fbiztypeid | 业务类型 | int8 | 64 |  | √ | 0 | 业务类型 bd_biztype |
| 12 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 13 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_qcnp_imminv |  | fid |
| 2 | idx_qcnp_imminv_fcreatetime |  | fcreatetime |
| 3 | idx_qcnp_imminv_fbillno |  | fbillno |
