# 许可证-bd_licence

## 物料信息-多语言表 t_bd_licence_subentry_l

- **表名称：** 物料信息-多语言表
- **表名：** t_bd_licence_subentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fgoodsname | 商品名称 | varchar | 770 |  | √ | ' ' | 商品名称 |
| 2 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 |  |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bd_licence_subentry_l_0 |  | fdetailid,flocaleid |
| 2 | pk_bd_licence_subentry_l |  | fpkid |

---

## 许可证-主表 t_bd_licence

- **表名称：** 许可证-主表
- **表名：** t_bd_licence

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftotalqty | 总数量 | numeric | 23 | 10 | √ | 0 | 总数量 |
| 3 | ftotalamount | 总金额 | numeric | 23 | 10 | √ | 0 | 总金额 |
| 4 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fremarks | 备注 | varchar | 500 |  | √ | ' ' | 备注 |
| 6 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 7 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | faudittime | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 9 | fbiztime | 录入日期 | timestamp | 0 |  |  | null | 录入日期 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fauditor | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fsourcedataid | 原资料id | int8 | 64 |  |  | null | 原资料id |
| 16 | fbitindex | 位图 | int8 | 64 |  |  | null | 位图 |
| 17 | fdisabler | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fofficiallicensenum | 官方许可证号 | varchar | 100 |  | √ | ' ' | 官方许可证号 |
| 19 | fcreateorgid | 许可证所有组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 20 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 21 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 22 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 23 | fcurrency | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 24 | fbiztimeend | 有效期至 | timestamp | 0 |  |  | null | 有效期至 |
| 25 | fctrlstrategy | 控制策略 | varchar | 50 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 |
| 26 | flicensetype | 许可证类型 | int8 | 64 |  | √ | 0 | [许可证类型 bd_licensetype](../sbd_files/bd_licensetype.md) |
| 27 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 28 | fbiztimebegin | 有效期自 | timestamp | 0 |  |  | null | 有效期自 |
| 29 | fnumber | 许可证编号 | varchar | 30 |  | √ | ' ' | 许可证编号 |
| 30 | fsourcebitindex | 原资料位图 | int8 | 64 |  |  | null | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_bd_licence_createorg |  | fcreateorgid |
| 2 | idx_t_bd_licence_master |  | fmasterid |
| 3 | pk_bd_licence |  | fid |
| 4 | idx_bd_licence_m0 |  | fmasterid |

---

## 物料信息-子表 t_bd_licence_subentry

- **表名称：** 物料信息-子表
- **表名：** t_bd_licence_subentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | famount | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 4 | fexecutedqty | 已执行数量 | numeric | 23 | 10 | √ | 0 | 已执行数量 |
| 5 | fcustomsgoodscode | 海关商品编码 | varchar | 50 |  | √ | ' ' | 海关商品编码 |
| 6 | funexecutedqty | 未执行数量 | numeric | 23 | 10 | √ | 0 | 未执行数量 |
| 7 | fbomid | BOM编码 | int8 | 64 |  | √ | 0 | [BOM维护 pdm_mftbom](../fmm_files/pdm_mftbom.md) |
| 8 | fsecondarylegalunit | 法定第二单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 9 | ftariffcode | 关税编码 | varchar | 50 |  | √ | ' ' | 关税编码 |
| 10 | fgoodsname | 商品名称 | varchar | 512 |  | √ | ' ' | 商品名称 |
| 11 | fmaterialversionid | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 12 | fmaterial | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 13 | fprimarylegalunit | 法定第一单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 14 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 15 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 16 | funit | 基本计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bd_licence_subentry |  | fdetailid |
| 2 | idx_bd_licence_subentry_fk |  | fentryid |

---

## 企业及商务伙伴信息-子表 t_bd_licence_entry

- **表名称：** 企业及商务伙伴信息-子表
- **表名：** t_bd_licence_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fpartnertype | 伙伴类型 | varchar | 50 |  | √ | ' ' | 伙伴类型,枚举: bd_supplier :供应商 bd_customer :客户 |
| 3 | forgid | 组织编码 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fbizparterner | 商务伙伴 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bd_licence_entry |  | fentryid |
| 2 | idx_bd_licence_entry_fk |  | fid |

---

## 许可证-使用范围表 t_bd_licence_u

- **表名称：** 许可证-使用范围表
- **表名：** t_bd_licence_u

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fcreateorgid | fcreateorgid | int8 | 64 |  |  | null |  |
| 2 | fdataid | fdataid | int8 | 64 |  | √ | null |  |
| 3 | fuseorgid | fuseorgid | int8 | 64 |  | √ | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdataid | fdataid,fuseorgid |
| 2 | fuseorgid | fdataid,fuseorgid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_bd_licence_u_uo |  | fuseorgid |
| 2 | pk_t_bd_licence_u |  | fdataid,fuseorgid |

---

## 许可证-多语言表 t_bd_licence_l

- **表名称：** 许可证-多语言表
- **表名：** t_bd_licence_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 3 | fremarks | 备注 | varchar | 755 |  | √ | ' ' | 备注 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bd_licence_l_0 |  | fid,flocaleid |
| 2 | pk_bd_licence_l |  | fpkid |
