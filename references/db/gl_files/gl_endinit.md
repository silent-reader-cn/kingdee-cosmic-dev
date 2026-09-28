# 总账初始化-gl_endinit

## 总账初始化-多语言表 t_bd_accountbooks_l

- **表名称：** 总账初始化-多语言表
- **表名：** t_bd_accountbooks_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | ffullname | ffullname | varchar | 255 |  | √ | ' ' |  |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bd_accountbooks_l_pkey |  | fpkid |
| 2 | idx_bd_accountbooks_l |  | fid,flocaleid |

---

## 总账初始化-主表 t_bd_accountbooks

- **表名称：** 总账初始化-主表
- **表名：** t_bd_accountbooks

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 账簿 | int8 | 64 |  | √ | 0 | 账簿 gl_accountbook |
| 2 | fyearprofitacctid | fyearprofitacctid | int8 | 64 |  | √ | 0 |  |
| 3 | fcheckoutstatus | fcheckoutstatus | varchar | 50 |  | √ | ' ' |  |
| 4 | forgid | 公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'C' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 7 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 8 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 9 | fcurperiodid | 当前期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 10 | fexratetableid | 基本核算汇率表 | int8 | 64 |  | √ | 0 | 汇率表 bd_exratetable |
| 11 | fissyspreset | fissyspreset | bpchar | 1 |  | √ | '0' |  |
| 12 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fdefaultvouchertypeid | 默认凭证类型 | int8 | 64 |  | √ | 0 | 凭证字 gl_vouchertype |
| 14 | fisendinit | 余额结束初始化 | bpchar | 1 |  | √ | '0' | 余额结束初始化 |
| 15 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 16 | fisendinitcashflow | 现金流量结束初始化 | bpchar | 1 |  | √ | '0' | 现金流量结束初始化 |
| 17 | fbookstypeid | 账簿类型 | int8 | 64 |  | √ | 0 | 账簿类型 bd_accountbookstype |
| 18 | fstartperiodid | 启用期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 19 | faccounttableid | 科目表 | int8 | 64 |  | √ | 0 | 科目表 bd_accounttable |
| 20 | fcashitemtbid | fcashitemtbid | int8 | 64 |  | √ | 0 |  |
| 21 | fpolicyid | fpolicyid | int8 | 64 |  | √ | 0 |  |
| 22 | fperiodtypeid | 期间类型 | int8 | 64 |  | √ | 0 | 会计日历类型 bd_period_type |
| 23 | fbasecurrencyid | 本位币 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 24 | fcashinitperiodid | 现金流量启用期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 25 | faccountingsys | faccountingsys | int8 | 64 |  | √ | 0 |  |
| 26 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 27 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 28 | fcheckoutmsg | fcheckoutmsg | varchar | 255 |  | √ | ' ' |  |
| 29 | fisbizunit | 是否实体 | bpchar | 1 |  | √ | '0' | 是否实体 |
| 30 | fbooknature | fbooknature | bpchar | 1 |  | √ | '0' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bd_accountbooks_pkey |  | fid |
| 2 | idx_bd_accountbooks |  | forgid,fbookstypeid |
