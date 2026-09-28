# 携程主&#x2f;子账户设置-er_corpaccountsetting

## 携程主&#x2f;子账户设置-主表 t_er_corpaccountsetting

- **表名称：** 携程主&#x2f;子账户设置-主表
- **表名：** t_er_corpaccountsetting

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fstatus | 数据状态 | varchar | 5 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 5 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 8 | fnumber | 公司编码（CorporationID） | varchar | 80 |  | √ | ' ' | 公司编码（CorporationID） |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_er_corpaccountsetting_pkey |  | fid |
| 2 | index_er_corpacc_num |  | fnumber |

---

## 携程主&#x2f;子账户设置-多语言表 t_er_corpaccountsetting_l

- **表名称：** 携程主&#x2f;子账户设置-多语言表
- **表名：** t_er_corpaccountsetting_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_er_corpaccountsetting_l_pkey |  | fpkid |
| 2 | idx_er_corpacc_l_fid |  | fid,flocaleid |

---

## 单据体-子表 t_er_corpaccountsetentry

- **表名称：** 单据体-子表
- **表名：** t_er_corpaccountsetentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsubaccountname | 子账户 | varchar | 100 |  | √ | ' ' | 子账户 |
| 3 | fgeneratetimestr | 生成员工子账户时间 | varchar | 50 |  | √ | ' ' | 生成员工子账户时间 |
| 4 | faccountrelorg | 关联组织 | int8 | 64 |  | √ | 0 | 行政组织（部门） bos_adminorg |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fmainaccountname | 主账户 | varchar | 100 |  | √ | ' ' | 主账户 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | index_er_corpaccentry_org |  | faccountrelorg |
| 2 | index_er_corpaccentry_subacc |  | fsubaccountname |
| 3 | t_er_corpaccountsetentry_pkey |  | fentryid |
| 4 | index_er_corpaccentry_seq |  | fid,fseq |
