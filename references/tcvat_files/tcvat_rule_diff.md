# 差额扣除规则-tcvat_rule_diff

## 差额扣除规则-主表 t_tcvat_rule_diff

- **表名称：** 差额扣除规则-主表
- **表名：** t_tcvat_rule_diff

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fqzkce | 取自扣除额 (本期发生) | bpchar | 1 |  | √ | '0' | 取自扣除额 (本期发生) |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | forgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fruletype | 规则类型 | varchar | 30 |  | √ | ' ' | 规则类型,枚举: private :自用规则 public :可分配规则 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fjzjt | 即征即退业务 | varchar | 30 |  | √ | ' ' | 即征即退业务,枚举: 0 :否 1 :是 |
| 9 | fdifftype | 差额扣除类型 | int8 | 64 |  | √ | 0 | 业务定义分录 tpo_tcvat_bizdef_entity |
| 10 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 14 | ftaxpayertype | 适用纳税人类型 | varchar | 30 |  | √ | ' ' | 适用纳税人类型,枚举: ybnsr :一般纳税人 xgmnsr :小规模纳税人 |
| 15 | fnumber | 编码 | varchar | 60 |  | √ | ' ' | 编码 |
| 16 | fdeductiontype | 免税项目代码及名称 | int8 | 64 |  | √ | 0 | 减免政策代码 tpo_taxdeduction |
| 17 | frulepurpose | 规则用途 | varchar | 50 |  | √ | ' ' | 规则用途,枚举: nssb :纳税申报 sjjt :税金计提 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tcvat_rule_diff_pkey |  | fid |
| 2 | idx_tcvat_rule_diff |  | fnumber |

---

## 本期发生取数规则-子表 t_tcvat_rule_entry

- **表名称：** 本期发生取数规则-子表
- **表名：** t_tcvat_rule_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffconditionjson | 过滤条件 | text | 0 |  |  | null | 过滤条件 |
| 3 | fentryentityconf | fentryentityconf | varchar | 2000 |  | √ | ' ' |  |
| 4 | fexratejson | fexratejson | varchar | 255 |  | √ | ' ' |  |
| 5 | famountfield | 金额字段 | int8 | 64 |  | √ | 0 | 数据源字段配置 tctb_datasource_entry |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fbizname | 业务名称 | varchar | 100 |  | √ | ' ' | 业务名称 |
| 8 | fentryentityconfjson | fentryentityconfjson | varchar | 2000 |  | √ | ' ' |  |
| 9 | ftable | 数据源 | int8 | 64 |  | √ | 0 | 数据源配置 tctb_custom_datasource |
| 10 | fvatrate | fvatrate | numeric | 23 | 10 | √ | 0 |  |
| 11 | fabsolute | 绝对值 | bpchar | 1 |  | √ | ' ' | 绝对值 |
| 12 | fiscustomtable | fiscustomtable | bpchar | 1 |  | √ | ' ' |  |
| 13 | fdifferenceinvoice | fdifferenceinvoice | bpchar | 1 |  | √ | '0' |  |
| 14 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 15 | ffiltercondition | 过滤条件 | text | 0 |  |  | null | 过滤条件 |
| 16 | fdatadirection | 取数方向 | varchar | 30 |  | √ | ' ' | 取数方向,枚举: positive :正向 reverse :反向 |
| 17 | fdatatype | 取数方式 | varchar | 30 |  | √ | ' ' | 取数方式,枚举: zjqs :直接取数 jsflqs :含税价换算不含税价 cysldsqs :税额换算不含税价 sehshsj :税额换算含税价 bhsjhshsj :不含税价换算含税价 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tcvat_rule_entry_pkey |  | fentryid |
| 2 | idx_tcvat_rule_entry |  | fid |

---

## 实际扣除额取数规则-子表 t_tcvat_rule_diff_entry

- **表名称：** 实际扣除额取数规则-子表
- **表名：** t_tcvat_rule_diff_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | famountfield | 金额字段 | int8 | 64 |  | √ | 0 | 数据源字段配置 tctb_datasource_entry |
| 3 | ftable | 数据源 | int8 | 64 |  | √ | 0 | 数据源配置 tctb_custom_datasource |
| 4 | fabsolute | 绝对值 | bpchar | 1 |  | √ | '0' | 绝对值 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fbizname | 业务名称 | varchar | 50 |  | √ | ' ' | 业务名称 |
| 7 | fconditionjson | 过滤条件 | varchar | 4000 |  | √ | ' ' | 过滤条件 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | ffiltercondition | 过滤条件 | varchar | 4000 |  | √ | ' ' | 过滤条件 |
| 10 | fdatadirection | 取数方向 | varchar | 50 |  | √ | ' ' | 取数方向,枚举: positive :正向 reverse :反向 |
| 11 | fdatatype | 取数方式 | varchar | 50 |  | √ | ' ' | 取数方式,枚举: zjqs :直接取数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcvat_rule_diff_entry |  | fentryid |
| 2 | idx_tcvat_rule_diff_entry_fk |  | fid |

---

## 差额扣除规则-多语言表 t_tcvat_rule_diff_l

- **表名称：** 差额扣除规则-多语言表
- **表名：** t_tcvat_rule_diff_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tcvat_rule_diff_l_pkey |  | fpkid |
| 2 | idx_tcvat_rule_diff_l_0 |  | fid,flocaleid |
