# 库存预警方案-im_earlywarn_scheme

## 库存预警方案-多语言表 t_im_earlywarnscheme_l

- **表名称：** 库存预警方案-多语言表
- **表名：** t_im_earlywarnscheme_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 方案名称 | varchar | 80 |  | √ | ' ' | 方案名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 描述 | varchar | 155 |  | √ | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_im_earlywarnscheme_l_0 |  | fid,flocaleid |
| 2 | pk_im_earlywarnscheme_l |  | fpkid |

---

## 库存预警方案-主表 t_im_earlywarnscheme

- **表名称：** 库存预警方案-主表
- **表名：** t_im_earlywarnscheme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fname | 方案名称 | varchar | 50 |  | √ | ' ' | 方案名称 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fdimensionid | 库存预警维度 | int8 | 64 |  | √ | 0 | [库存预警维度 im_earlywarn_dimension](../im_files/im_earlywarn_dimension.md) |
| 6 | forgid | 库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fisinputbymonitor | 根据库存监控信息录入 | bpchar | 1 |  | √ | '0' | 根据库存监控信息录入 |
| 8 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 9 | fdescription | 描述 | varchar | 100 |  | √ | ' ' | 描述 |
| 10 | fbillcretype | 单据生成类型 | bpchar | 1 |  | √ | '0' | 单据生成类型,枚举: 0 :手工生成 1 :导入生成 |
| 11 | faudittime | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 17 | fdisabler | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fisinputinvunitqty | 录入库存单位数量 | bpchar | 1 |  | √ | '0' | 录入库存单位数量 |
| 19 | fnumber | 方案编码 | varchar | 30 |  | √ | ' ' | 方案编码 |
| 20 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_im_earlywarnscheme_m0 |  | fmasterid |
| 2 | pk_im_earlywarnscheme |  | fid |

---

## 预警明细-子表 t_im_earlywarnschemeentry

- **表名称：** 预警明细-子表
- **表名：** t_im_earlywarnschemeentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料库存信息 bd_materialinventoryinfo](../sbd_files/bd_materialinventoryinfo.md) |
| 3 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 4 | fmversionid | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fsaftyqty | 安全库存（库存） | numeric | 23 | 10 | √ | 0 | 安全库存（库存） |
| 7 | finvstatusid | 库存状态 | int8 | 64 |  | √ | 0 | [库存状态 bd_invstatus](../sbd_files/bd_invstatus.md) |
| 8 | fbasereorderqty | 再订货点（基本） | numeric | 23 | 10 | √ | 0 | 再订货点（基本） |
| 9 | fbasesaftyqty | 安全库存（基本） | numeric | 23 | 10 | √ | 0 | 安全库存（基本） |
| 10 | fownertype | 货主类型 | varchar | 50 |  | √ | ' ' | 货主类型,枚举: bos_org :业务单元 bd_supplier :供应商 bd_customer :客户 |
| 11 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 12 | fkeeperid | 保管者 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 13 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 14 | flotnum | 批号编码 | varchar | 50 |  | √ | ' ' | 批号编码 |
| 15 | fprojectid | 项目号 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 16 | freorderqty | 再订货点（库存） | numeric | 23 | 10 | √ | 0 | 再订货点（库存） |
| 17 | finvtypeid | 库存类型 | int8 | 64 |  | √ | 0 | [库存类型 bd_invtype](../sbd_files/bd_invtype.md) |
| 18 | funitid | 库存单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 19 | fkeepertype | 保管者类型 | varchar | 50 |  | √ | ' ' | 保管者类型,枚举: bos_org :库存组织 bd_customer :客户 bd_supplier :供应商 |
| 20 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 21 | fmaterialmasterid | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 22 | fownerid | 货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 23 | flotid | 批号 | int8 | 64 |  | √ | 0 | [批号主档 bd_lot](../sbd_files/bd_lot.md) |
| 24 | fmaxqty | 最大库存（库存） | numeric | 23 | 10 | √ | 0 | 最大库存（库存） |
| 25 | flocationid | 仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 26 | fbaseminqty | 最小库存（基本） | numeric | 23 | 10 | √ | 0 | 最小库存（基本） |
| 27 | fminqty | 最小库存（库存） | numeric | 23 | 10 | √ | 0 | 最小库存（库存） |
| 28 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 29 | fbasemaxqty | 最大库存（基本） | numeric | 23 | 10 | √ | 0 | 最大库存（基本） |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_im_ewschemeentry_mat |  | fmaterialid |
| 2 | pk_im_earlywarnschemeentry |  | fentryid |
| 3 | idx_im_earlywarnschemeentry_fk |  | fid |
