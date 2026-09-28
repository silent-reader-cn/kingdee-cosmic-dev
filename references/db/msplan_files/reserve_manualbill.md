# 预留单-reserve_manualbill

## 预留单-主表 t_reserve_manualbill

- **表名称：** 预留单-主表
- **表名：** t_reserve_manualbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcomment | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | forgid | 需求组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 9 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 10 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 11 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_reserve_manualbill |  | fid |
| 2 | idx_t_reserve_manualbill_no |  | fbillno |

---

## 物料明细-子表 t_reserve_manualbillentry

- **表名称：** 物料明细-子表
- **表名：** t_reserve_manualbillentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | freserveobjtype | 预留对象类型 | varchar | 50 |  | √ | ' ' | 预留对象类型,枚举: bd_customer :客户 bd_operator :业务员 bos_adminorg :部门 |
| 3 | flotnumber | 批号 | varchar | 50 |  | √ | ' ' | 批号 |
| 4 | freservetype | 预留类型 | varchar | 10 |  | √ | ' ' | 预留类型,枚举: 1 :强预留 0 :弱预留 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | 配置号 bd_configuredcode |
| 7 | fbaseunit | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 8 | finvstatusid | 库存状态 | int8 | 64 |  | √ | 0 | 库存状态 bd_invstatus |
| 9 | finvorg | 库存组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 10 | fownertype | 货主类型 | varchar | 50 |  | √ | ' ' | 货主类型,枚举: bos_org :业务组织 bd_supplier :供应商 bd_customer :客户 |
| 11 | fkeeperid | 保管者 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 12 | fmaterial | 物料编码 | int8 | 64 |  | √ | 0 | 物料库存信息 bd_materialinventoryinfo |
| 13 | fbomversionid | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本 bd_bomversion_new |
| 14 | funit2nd | 辅助单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 15 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 16 | fprojectid | 项目号 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 17 | finvtypeid | 库存类型 | int8 | 64 |  | √ | 0 | 库存类型 bd_invtype |
| 18 | freserveinvaliddate | 预留至日期 | timestamp | 0 |  |  | null | 预留至日期 |
| 19 | freserveobj | 预留对象 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 20 | fkeepertype | 保管者类型 | varchar | 50 |  | √ | ' ' | 保管者类型,枚举: bos_org :库存组织 bd_supplier :供应商 bd_customer :客户 |
| 21 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 22 | fqtyunit2nd | 辅助数量 | numeric | 23 | 10 | √ | 0 | 辅助数量 |
| 23 | fownerid | 货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 24 | flotid | 批号主档 | int8 | 64 |  | √ | 0 | 批号主档 bd_lot |
| 25 | flocationid | 仓位 | int8 | 64 |  | √ | 0 | 仓位 bd_location |
| 26 | fentrycomment | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 27 | fexpirydate | 到期日期 | timestamp | 0 |  |  | null | 到期日期 |
| 28 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 29 | fproducedate | 生产日期 | timestamp | 0 |  |  | null | 生产日期 |
| 30 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 31 | fauxpty | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 32 | funit | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_reserve_manualbillentry |  | fentryid |
| 2 | idx_reserve_manualbil_e_fid |  | fid |

---

## 预留单-多语言表 t_reserve_manualbill_l

- **表名称：** 预留单-多语言表
- **表名：** t_reserve_manualbill_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcomment | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_reserve_manualbill_l |  | fid,flocaleid |
| 2 | pk_t_reserve_manualbill_l |  | fpkid |
