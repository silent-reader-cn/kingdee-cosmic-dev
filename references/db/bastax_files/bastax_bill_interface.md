# 计税服务启用-bastax_bill_interface

## 计税服务启用-多语言表 t_bastax_bill_interface_l

- **表名称：** 计税服务启用-多语言表
- **表名：** t_bastax_bill_interface_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bastax_bill_interface_l_0 |  | fid,flocaleid |
| 2 | pk_bastax_bill_interface_l |  | fpkid |

---

## 计税要素单据体-子表 t_bastax_bill_eleentry

- **表名称：** 计税要素单据体-子表
- **表名：** t_bastax_bill_eleentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | felementfiledvalue | 计税要素字段值 | varchar | 100 |  | √ | ' ' | 计税要素字段值 |
| 3 | felementtype | 计税要素类型 | varchar | 50 |  | √ | ' ' | 计税要素类型,枚举: jyf :交易方 jycp :交易产品 jydd :交易地点 other :其他交易信息 |
| 4 | felementrequired | 是否必须 | bpchar | 1 |  | √ | '0' | 是否必须 |
| 5 | felementsource | 来源 | varchar | 50 |  | √ | ' ' | 来源,枚举: head :单据头 entry :单据行 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | felementfiled | 计税要素字段 | int8 | 64 |  | √ | 0 | [条件字段 bdtaxr_where_fields](../bastax_files/bdtaxr_where_fields.md) |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bastax_bill_eleentry |  | fentryid |
| 2 | idx_bastax_bill_eleentry_1 |  | fid,fentryid |

---

## 计税服务启用-主表 t_bastax_bill_interface

- **表名称：** 计税服务启用-主表
- **表名：** t_bastax_bill_interface

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fentityidkeybd | 上游单据分录行主键ID标识 | int8 | 64 |  | √ | 0 | [条件字段 bdtaxr_where_fields](../bastax_files/bdtaxr_where_fields.md) |
| 3 | fshkdksjbd | 税行可抵扣税金标识 | int8 | 64 |  | √ | 0 | [条件字段 bdtaxr_where_fields](../bastax_files/bdtaxr_where_fields.md) |
| 4 | fentitykeyvalue | 上游单据标识值 | varchar | 100 |  | √ | ' ' | 上游单据标识值 |
| 5 | finternationaltaxkey | finternationaltaxkey | int8 | 64 |  | √ | 0 |  |
| 6 | fshslzvalue | 税行税率值标识值 | varchar | 100 |  | √ | ' ' | 税行税率值标识值 |
| 7 | ftaxtypekeykey | 税行的税种标识值 | varchar | 100 |  | √ | ' ' | 税行的税种标识值 |
| 8 | fshsmyxjvalue | 税行税码优先级标识值 | varchar | 100 |  | √ | ' ' | 税行税码优先级标识值 |
| 9 | forg | forg | int8 | 64 |  | √ | 0 |  |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fshxgvalue | 税行修改标识值 | varchar | 100 |  | √ | ' ' | 税行修改标识值 |
| 12 | fcountrykey | 开票地 | varchar | 100 |  | √ | ' ' | 开票地 |
| 13 | fcombofield1 | fcombofield1 | varchar | 50 |  | √ | ' ' |  |
| 14 | fcombofield2 | fcombofield2 | varchar | 50 |  | √ | ' ' |  |
| 15 | fbill | 计税单据 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 16 | ftaxdetails | 计税明细行 | int8 | 64 |  | √ | 0 | [条件字段 bdtaxr_where_fields](../bastax_files/bdtaxr_where_fields.md) |
| 17 | fshsebd | 税行税额标识 | int8 | 64 |  | √ | 0 | [条件字段 bdtaxr_where_fields](../bastax_files/bdtaxr_where_fields.md) |
| 18 | ftaxcodekey | ftaxcodekey | int8 | 64 |  | √ | 0 |  |
| 19 | fshsevalue | 税行税额标识值 | varchar | 100 |  | √ | ' ' | 税行税额标识值 |
| 20 | finternationaltaxkeykeybd | 税行标识 | int8 | 64 |  | √ | 0 | [条件字段 bdtaxr_where_fields](../bastax_files/bdtaxr_where_fields.md) |
| 21 | ftaxbillentrykeykey | 计税明细行值 | varchar | 100 |  | √ | ' ' | 计税明细行值 |
| 22 | fshsmyxjbd | 税行税码优先级标识 | int8 | 64 |  | √ | 0 | [条件字段 bdtaxr_where_fields](../bastax_files/bdtaxr_where_fields.md) |
| 23 | fshbkdksjbd | 税行不可抵扣税金标识 | int8 | 64 |  | √ | 0 | [条件字段 bdtaxr_where_fields](../bastax_files/bdtaxr_where_fields.md) |
| 24 | fvat | 单据VAT属性 | varchar | 50 |  | √ | ' ' | 单据VAT属性,枚举: jx :进项 xx :销项 qt :其他 |
| 25 | fshbkdksjvalue | 税行不可抵扣税金标识值 | varchar | 100 |  | √ | ' ' | 税行不可抵扣税金标识值 |
| 26 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 27 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 28 | fcountry | fcountry | int8 | 64 |  | √ | 0 |  |
| 29 | fshslvalue | 税行税率标识值 | varchar | 100 |  | √ | ' ' | 税行税率标识值 |
| 30 | ftag | ftag | int8 | 64 |  | √ | 0 |  |
| 31 | finternationaltaxkeykey | 税行标识值 | varchar | 100 |  | √ | ' ' | 税行标识值 |
| 32 | fmethod | 服务方法 | varchar | 50 |  | √ | ' ' | 服务方法,枚举: service :税码计算 wholeService :整单计算 partService :部分计算 |
| 33 | fshxgbd | 税行修改标识 | int8 | 64 |  | √ | 0 | [条件字段 bdtaxr_where_fields](../bastax_files/bdtaxr_where_fields.md) |
| 34 | fentityrowkeyvalue | 上游单据分录行标识值 | varchar | 100 |  | √ | ' ' | 上游单据分录行标识值 |
| 35 | ftaxtypekey | ftaxtypekey | int8 | 64 |  | √ | 0 |  |
| 36 | fshslzbd | 税行税率值标识 | int8 | 64 |  | √ | 0 | [条件字段 bdtaxr_where_fields](../bastax_files/bdtaxr_where_fields.md) |
| 37 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 38 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 39 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 40 | fcalbutton | 计税按钮 | varchar | 500 |  | √ | ' ' | 计税按钮,枚举: |
| 41 | fcountrykeybd | 开票地 | int8 | 64 |  | √ | 0 | [条件字段 bdtaxr_where_fields](../bastax_files/bdtaxr_where_fields.md) |
| 42 | fdate | fdate | int8 | 64 |  | √ | 0 |  |
| 43 | ftaxcodekeykeybd | 税行税码标识 | int8 | 64 |  | √ | 0 | [条件字段 bdtaxr_where_fields](../bastax_files/bdtaxr_where_fields.md) |
| 44 | fdatekeybd | 业务日期 | int8 | 64 |  | √ | 0 | [条件字段 bdtaxr_where_fields](../bastax_files/bdtaxr_where_fields.md) |
| 45 | fentityidkeyvalue | 上游单据分录行主键ID标识值 | varchar | 100 |  | √ | ' ' | 上游单据分录行主键ID标识值 |
| 46 | fidkeybd | 上游单据主键ID标识 | int8 | 64 |  | √ | 0 | [条件字段 bdtaxr_where_fields](../bastax_files/bdtaxr_where_fields.md) |
| 47 | fsysteminit | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 48 | forgbd | 组织 | int8 | 64 |  | √ | 0 | [条件字段 bdtaxr_where_fields](../bastax_files/bdtaxr_where_fields.md) |
| 49 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 50 | ftaxbillentrykey | ftaxbillentrykey | int8 | 64 |  | √ | 0 |  |
| 51 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 52 | fidkeyvalue | 上游单据主键ID标识值 | varchar | 100 |  | √ | ' ' | 上游单据主键ID标识值 |
| 53 | ftaxcodekeykey | 税行税码标识值 | varchar | 100 |  | √ | ' ' | 税行税码标识值 |
| 54 | fbasedatafield2 | fbasedatafield2 | int8 | 64 |  | √ | 0 |  |
| 55 | fbasedatafield1 | fbasedatafield1 | int8 | 64 |  | √ | 0 |  |
| 56 | fbasedatafield4 | fbasedatafield4 | int8 | 64 |  | √ | 0 |  |
| 57 | fbasedatafield3 | fbasedatafield3 | int8 | 64 |  | √ | 0 |  |
| 58 | fshkdksjvalue | 税行可抵扣税金标识值 | varchar | 100 |  | √ | ' ' | 税行可抵扣税金标识值 |
| 59 | fentityrowkeybd | 上游单据分录行标识 | int8 | 64 |  | √ | 0 | [条件字段 bdtaxr_where_fields](../bastax_files/bdtaxr_where_fields.md) |
| 60 | fdatekey | 业务日期值 | varchar | 100 |  | √ | ' ' | 业务日期值 |
| 61 | fentitykeybd | 上游单据标识 | int8 | 64 |  | √ | 0 | [条件字段 bdtaxr_where_fields](../bastax_files/bdtaxr_where_fields.md) |
| 62 | fservicename | 服务类名 | varchar | 50 |  | √ | ' ' | 服务类名,枚举: billTaxService :税码计算服务 billTaxLineService :税行计算服务 |
| 63 | forgkey | 组织文本 | varchar | 100 |  | √ | ' ' | 组织文本 |
| 64 | fshslbd | 税行税率标识 | int8 | 64 |  | √ | 0 | [条件字段 bdtaxr_where_fields](../bastax_files/bdtaxr_where_fields.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bastax_bill_interface |  | fid |
| 2 | idx_bastax_bill_interface |  | forg,fbill |

---

## 计税税基单据体-子表 t_bastax_bill_baseentry

- **表名称：** 计税税基单据体-子表
- **表名：** t_bastax_bill_baseentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasesource | 来源 | varchar | 50 |  | √ | ' ' | 来源,枚举: head :单据头 entry :单据行 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fbasefiledvalue | 计税要素字段值 | varchar | 100 |  | √ | ' ' | 计税要素字段值 |
| 5 | fbaserequired | 是否必须 | bpchar | 1 |  | √ | '0' | 是否必须 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fbasefiled | 计税税基字段 | int8 | 64 |  | √ | 0 | [条件字段 bdtaxr_where_fields](../bastax_files/bdtaxr_where_fields.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bastax_bill_baseentry_1 |  | fid,fentryid |
| 2 | pk_bastax_bill_baseentry |  | fentryid |
