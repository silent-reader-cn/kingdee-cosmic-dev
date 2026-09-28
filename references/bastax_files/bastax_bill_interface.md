# 单据接口注册-bastax_bill_interface

## 单据接口注册-多语言表 t_bastax_bill_interface_l

- **表名称：** 单据接口注册-多语言表
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

## 单据接口注册-主表 t_bastax_bill_interface

- **表名称：** 单据接口注册-主表
- **表名：** t_bastax_bill_interface

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftag | ftag | int8 | 64 |  | √ | 0 |  |
| 3 | finternationaltaxkeykey | 税行标识 | varchar | 100 |  | √ | ' ' | 税行标识 |
| 4 | finternationaltaxkey | finternationaltaxkey | int8 | 64 |  | √ | 0 |  |
| 5 | fmethod | 服务方法 | varchar | 50 |  | √ | ' ' | 服务方法,枚举: service :税码计算 wholeService :整单计算 partService :部分计算 |
| 6 | ftaxtypekey | ftaxtypekey | int8 | 64 |  | √ | 0 |  |
| 7 | ftaxtypekeykey | 税行的税种标识 | varchar | 100 |  | √ | ' ' | 税行的税种标识 |
| 8 | forg | forg | int8 | 64 |  | √ | 0 |  |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fcountrykey | 税号注册国 | varchar | 100 |  | √ | ' ' | 税号注册国 |
| 14 | fdate | fdate | int8 | 64 |  | √ | 0 |  |
| 15 | fcombofield1 | fcombofield1 | varchar | 50 |  | √ | ' ' |  |
| 16 | fsysteminit | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 17 | fcombofield2 | fcombofield2 | varchar | 50 |  | √ | ' ' |  |
| 18 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 19 | ftaxbillentrykey | ftaxbillentrykey | int8 | 64 |  | √ | 0 |  |
| 20 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 21 | fbill | 调用单据 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 22 | ftaxcodekey | ftaxcodekey | int8 | 64 |  | √ | 0 |  |
| 23 | ftaxbillentrykeykey | 默认税码所在子单据体 | varchar | 100 |  | √ | ' ' | 默认税码所在子单据体 |
| 24 | ftaxcodekeykey | 税行的税码标识 | varchar | 100 |  | √ | ' ' | 税行的税码标识 |
| 25 | fbasedatafield2 | fbasedatafield2 | int8 | 64 |  | √ | 0 |  |
| 26 | fbasedatafield1 | fbasedatafield1 | int8 | 64 |  | √ | 0 |  |
| 27 | fbasedatafield4 | fbasedatafield4 | int8 | 64 |  | √ | 0 |  |
| 28 | fbasedatafield3 | fbasedatafield3 | int8 | 64 |  | √ | 0 |  |
| 29 | fvat | 单据VAT属性 | varchar | 50 |  | √ | ' ' | 单据VAT属性,枚举: jx :进项 xx :销项 qt :其他 |
| 30 | fdatekey | 业务日期 | varchar | 100 |  | √ | ' ' | 业务日期 |
| 31 | fservicename | 服务类名 | varchar | 50 |  | √ | ' ' | 服务类名,枚举: billTaxService :税码计算服务 billTaxLineService :税行计算服务 |
| 32 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 33 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 34 | forgkey | 税务组织 | varchar | 100 |  | √ | ' ' | 税务组织 |
| 35 | fcountry | fcountry | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bastax_bill_interface |  | fid |
| 2 | idx_bastax_bill_interface |  | forg,fbill |
