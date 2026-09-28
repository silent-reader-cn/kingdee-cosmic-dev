# 账簿-gl_accountbook

## 应付-多选基础资料表 t_bd_glrefaporgs

- **表名称：** 应付-多选基础资料表
- **表名：** t_bd_glrefaporgs

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_bd_glrefaporgs |  | fpkid |
| 2 | idx_bd_glrefaporgs |  | fid |

---

## 资产账簿-多选基础资料表 t_bd_assetbookentry

- **表名称：** 资产账簿-多选基础资料表
- **表名：** t_bd_assetbookentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 启用期间设置 fa_assetbook |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bd_assetbookentry_pkey |  | fpkid |
| 2 | idx_bd_assetbookentry |  | fid |

---

## 存货核算账簿-多选基础资料表 t_bd_costaccountentry

- **表名称：** 存货核算账簿-多选基础资料表
- **表名：** t_bd_costaccountentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 成本主体 cal_bd_costaccount |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bd_costaccountentry_pkey |  | fpkid |
| 2 | idx_bd_costaccountentry |  | fid |

---

## 应收账簿-多选基础资料表 t_bd_policybookentry

- **表名称：** 应收账簿-多选基础资料表
- **表名：** t_bd_policybookentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 应收政策 ar_policy |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bd_policybookentry_pkey |  | fpkid |
| 2 | idx_bd_policybookentry |  | fid |

---

## 账簿-多语言表 t_bd_accountbooks_l

- **表名称：** 账簿-多语言表
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

## 账簿-主表 t_bd_accountbooks

- **表名称：** 账簿-主表
- **表名：** t_bd_accountbooks

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fyearprofitacctid | 本年利润科目 | int8 | 64 |  | √ | 0 | 会计科目 bd_accountview |
| 3 | fcheckoutstatus | fcheckoutstatus | varchar | 50 |  | √ | ' ' |  |
| 4 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'C' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 7 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 8 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 9 | fcurperiodid | 当前期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 10 | fexratetableid | 汇率表 | int8 | 64 |  | √ | 0 | 汇率表 bd_exratetable |
| 11 | fissyspreset | 是否预置 | bpchar | 1 |  | √ | '0' | 是否预置,枚举: 1 :是 0 :否 |
| 12 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fdefaultvouchertypeid | 默认凭证字 | int8 | 64 |  | √ | 0 | 凭证字 gl_vouchertype |
| 14 | fisendinit | 是否结束初始化 | bpchar | 1 |  | √ | '0' | 是否结束初始化 |
| 15 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 16 | fisendinitcashflow | 是否结束现金流量初始化 | bpchar | 1 |  | √ | '0' | 是否结束现金流量初始化 |
| 17 | fbookstypeid | 账簿类型 | int8 | 64 |  | √ | 0 | 账簿类型 bd_accountbookstype |
| 18 | fstartperiodid | 启用期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 19 | faccounttableid | 科目表 | int8 | 64 |  | √ | 0 | 科目表 bd_accounttable |
| 20 | fcashitemtbid | 现金流量项目表 | int8 | 64 |  | √ | 0 | 现金流量项目表 gl_cashflowitemtb |
| 21 | fpolicyid | 会计政策 | int8 | 64 |  | √ | 0 | 会计政策 xkbd_policy |
| 22 | fperiodtypeid | 会计日历 | int8 | 64 |  | √ | 0 | 会计日历类型 bd_period_type |
| 23 | fbasecurrencyid | 本位币 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 24 | fcashinitperiodid | 现金流量初始化期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 25 | faccountingsys | 核算体系 | int8 | 64 |  | √ | 0 | 核算体系 xkbd_accountingsys |
| 26 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 27 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 28 | fcheckoutmsg | fcheckoutmsg | varchar | 255 |  | √ | ' ' |  |
| 29 | fisbizunit | 是否实体 | bpchar | 1 |  | √ | '0' | 是否实体 |
| 30 | fbooknature | 账簿类型 | bpchar | 1 |  | √ | '0' | 账簿类型,枚举: 1 :主账簿 0 :副账簿 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bd_accountbooks_pkey |  | fid |
| 2 | idx_bd_accountbooks |  | forgid,fbookstypeid |

---

## 出纳-多选基础资料表 t_bd_glrefcasorgs

- **表名称：** 出纳-多选基础资料表
- **表名：** t_bd_glrefcasorgs

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bd_glrefcasorgs |  | fid |
| 2 | pk_t_bd_glrefcasorgs |  | fpkid |
