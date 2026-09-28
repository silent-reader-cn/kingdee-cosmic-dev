# 授信额度返还单-cfm_creditreturn

## 授信额度返还单-主表 t_cfm_creditreturn

- **表名称：** 授信额度返还单-主表
- **表名：** t_cfm_creditreturn

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcredittypeid | 授信类别 | int8 | 64 |  | √ | 0 | [授信类别 cfm_credittype](../creditm_files/cfm_credittype.md) |
| 3 | freturnid | 返还ID | varchar | 100 |  | √ | ' ' | 返还ID |
| 4 | fbizamount | 业务返还金额 | numeric | 23 | 10 | √ | 0 | 业务返还金额 |
| 5 | forgid | 使用单位 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fcredituseid | 授信占用单ID | int8 | 64 |  | √ | 0 | 授信占用单ID |
| 7 | famount | 实际返还金额 | numeric | 19 | 6 | √ | 0.000000 | 实际返还金额 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 汇率 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fsourcetype | 单据类型 | varchar | 50 |  | √ | ' ' | 单据类型,枚举: cfm_loanbill :提款单 |
| 12 | fsourcebillno | 源单编号 | varchar | 80 |  | √ | ' ' | 源单编号 |
| 13 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 14 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 16 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 17 | fbizcurrencyid | 业务币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 18 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 19 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 20 | fiscopy | 是否为续授信拷贝单 | bpchar | 1 |  | √ | '0' | 是否为续授信拷贝单 |
| 21 | fcreditrate | 折授信币别汇率 | numeric | 23 | 10 | √ | 0 | 折授信币别汇率 |
| 22 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 23 | fsourcebillid | 源单id | int8 | 64 |  | √ | 0 | 源单id |
| 24 | fcurrencyid | 额度币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 25 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 26 | fcreditlimitid | 授信额度单ID | int8 | 64 |  | √ | 0 | 授信额度单ID |
| 27 | flocamt | 金额折本位币 | numeric | 19 | 6 | √ | 0.000000 | 金额折本位币 |
| 28 | fcompanyid | fcompanyid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cfm_creditreturn_no |  | fbillno |
| 2 | t_cfm_creditreturn_pkey |  | fid |

---

## 授信额度返还单-多语言表 t_cfm_creditreturn_l

- **表名称：** 授信额度返还单-多语言表
- **表名：** t_cfm_creditreturn_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flocaleid | flocaleid | varchar | 50 |  | √ | ' ' | localeid |
| 3 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 4 | fpkid | fpkid | varchar | 80 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cfm_creditreturn_l_pkey |  | fpkid |
| 2 | idx_cfm_creditreturn_l_id |  | fid,flocaleid |
