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
| 6 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 7 | finspecorgid | 质检组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | funit2ndid | 辅助单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 9 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 10 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 11 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | [配置号（废弃） bd_configuredcode](../sbd_files/bd_configuredcode.md) |
| 12 | fassunit2id | 辅助单位(2) | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 13 | fbonded | 保税 | bpchar | 1 |  | √ | '0' | 保税 |
| 14 | fbaseapplyqty | 基本申请数量 | numeric | 23 | 10 | √ | 0 | 基本申请数量 |
| 15 | finvstatusid | 库存状态 | int8 | 64 |  | √ | 0 | [库存状态 bd_invstatus](../sbd_files/bd_invstatus.md) |
| 16 | fbasereservqty | 基本预留数量 | numeric | 23 | 10 | √ | 0 | 基本预留数量 |
| 17 | fjoinqty | 关联数量 | numeric | 23 | 10 | √ | 0 | 关联数量 |
| 18 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 19 | fownertype | 货主类型 | varchar | 255 |  | √ | ' ' | 货主类型,枚举: bos_org :核算组织 bd_supplier :供应商 bd_customer :客户 |
| 20 | fkeeperid | 保管者 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 21 | fbaseavbqty | 基本可用数量 | numeric | 23 | 10 | √ | 0 | 基本可用数量 |
| 22 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 23 | favb2ndqty | 辅助可用数量 | numeric | 23 | 10 | √ | 0 | 辅助可用数量 |
| 24 | finspres | 请检结果 | varchar | 5 |  | √ | ' ' | 请检结果,枚举: suc :成功 fail :失败 del :删除 |
| 25 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 26 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 27 | fapplyorgid | 申请组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 28 | finvtypeid | 库存类型 | int8 | 64 |  | √ | 0 | [库存类型 bd_invtype](../sbd_files/bd_invtype.md) |
| 29 | finventoryid | 即时库存ID | int8 | 64 |  | √ | 0 | 即时库存ID |
| 30 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 31 | fmversion | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 32 | flicensenoid | 许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |
| 33 | fkeepertype | 保管者类型 | varchar | 255 |  | √ | ' ' | 保管者类型,枚举: bos_org :库存组织 bd_customer :客户 bd_supplier :供应商 |
| 34 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 35 | fassqty2 | 辅助数量(2) | numeric | 23 | 10 | √ | 0 | 辅助数量(2) |
| 36 | finvorgid | 库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 37 | freservqty | 预留数量 | numeric | 23 | 10 | √ | 0 | 预留数量 |
| 38 | finvunitid | 库存单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 39 | fqty2nd | 辅助数量 | numeric | 23 | 10 | √ | 0 | 辅助数量 |
| 40 | fownerid | 货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 41 | flotid | 批号主档 | int8 | 64 |  | √ | 0 | [批号主档 bd_lot](../sbd_files/bd_lot.md) |
| 42 | flocationid | 仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 43 | fapplyqty | 申请数量 | numeric | 23 | 10 | √ | 0 | 申请数量 |
| 44 | fexpirydate | 到期日期 | timestamp | 0 |  |  | null | 到期日期 |
| 45 | fmaterialcomid | 物料公共信息 | int8 | 64 |  | √ | 0 | [物料组织公共信息 bd_materialcommon](../basedata_files/bd_materialcommon.md) |
| 46 | fproducedate | 生产日期 | timestamp | 0 |  |  | null | 生产日期 |
| 47 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 48 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

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
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | finvimpschemeid | 执行方案 | int8 | 64 |  | √ | 0 | [执行方案 qcbd_invimpschem](../qcbd_files/qcbd_invimpschem.md) |
| 4 | fbillstatus | 单据状态 | varchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 8 | fexedate | 日期 | timestamp | 0 |  |  | null | 日期 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fbiztypeid | 业务类型 | int8 | 64 |  | √ | 0 | [业务类型 bd_biztype](../sbd_files/bd_biztype.md) |
| 12 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 13 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
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
