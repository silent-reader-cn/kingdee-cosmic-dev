# 即征即退进项税额规则-tcvat_rule_jzjt_jxse

## 即征即退进项税额规则-多语言表 t_tcvat_rule_jzjt_jxse_l

- **表名称：** 即征即退进项税额规则-多语言表
- **表名：** t_tcvat_rule_jzjt_jxse_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 业务名称 | varchar | 100 |  | √ | ' ' | 业务名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcvat_rule_jzjt_jxse_l |  | fpkid |
| 2 | idx_tcvat_rule_jzjt_jxse_l_0 |  | fid,flocaleid |

---

## 无法划分的即征即退进项税额取数配置-子表 t_tcvat_rule_jzjt_entn

- **表名称：** 无法划分的即征即退进项税额取数配置-子表
- **表名：** t_tcvat_rule_jzjt_entn

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | famountfield | 金额字段 | int8 | 64 |  | √ | 0 | [数据源字段配置 tctb_datasource_entry](../tctb_files/tctb_datasource_entry.md) |
| 3 | ftable | 数据源 | int8 | 64 |  | √ | 0 | [数据源配置 tctb_custom_datasource](../tctb_files/tctb_custom_datasource.md) |
| 4 | fvatrate | 增值税税率/征收率 | numeric | 23 | 10 | √ | 0 | 增值税税率/征收率 |
| 5 | fabsolute | 绝对值 | bpchar | 1 |  | √ | '0' | 绝对值 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fbizname | 业务名称 | varchar | 50 |  | √ | ' ' | 业务名称 |
| 8 | fconditionjson | 过滤条件 | text | 0 |  |  | null | 过滤条件 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | ffiltercondition | 过滤条件 | text | 0 |  |  | null | 过滤条件 |
| 11 | fdatadirection | 取数方向 | varchar | 50 |  | √ | ' ' | 取数方向,枚举: positive :正向 reverse :反向 |
| 12 | fdatatype | 取数方式 | varchar | 50 |  | √ | ' ' | 取数方式,枚举: zjqs :直接取数 jsflqs :含税价换算不含税价 cysldsqs :税额换算不含税价 hsjhsse :含税价换算税额 bhsjhsse :不含税价换算税额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcvat_rule_jzjt_entn |  | fentryid |
| 2 | idx_tcvat_rule_jzjt_entn_fk |  | fid |

---

## 即征即退税额取数配置-子表 t_tcvat_rule_jzjt_entj

- **表名称：** 即征即退税额取数配置-子表
- **表名：** t_tcvat_rule_jzjt_entj

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | famountfield | 金额字段 | int8 | 64 |  | √ | 0 | [数据源字段配置 tctb_datasource_entry](../tctb_files/tctb_datasource_entry.md) |
| 3 | ftable | 数据源 | int8 | 64 |  | √ | 0 | [数据源配置 tctb_custom_datasource](../tctb_files/tctb_custom_datasource.md) |
| 4 | fvatrate | 增值税税率/征收率 | numeric | 23 | 10 | √ | 0 | 增值税税率/征收率 |
| 5 | fabsolute | 绝对值 | bpchar | 1 |  | √ | '0' | 绝对值 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fbizname | 业务名称 | varchar | 50 |  | √ | ' ' | 业务名称 |
| 8 | fconditionjson | 过滤条件 | text | 0 |  |  | null | 过滤条件 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | ffiltercondition | 过滤条件 | text | 0 |  |  | null | 过滤条件 |
| 11 | fdatadirection | 取数方向 | varchar | 50 |  | √ | ' ' | 取数方向,枚举: positive :正向 reverse :反向 |
| 12 | fdatatype | 取数方式 | varchar | 50 |  | √ | ' ' | 取数方式,枚举: zjqs :直接取数 jsflqs :含税价换算不含税价 cysldsqs :税额换算不含税价 hsjhsse :含税价换算税额 bhsjhsse :不含税价换算税额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tcvat_rule_jzjt_entj_fk |  | fid |
| 2 | pk_tcvat_rule_jzjt_entj |  | fentryid |

---

## 即征即退进项税额规则-主表 t_tcvat_rule_jzjt_jxse

- **表名称：** 即征即退进项税额规则-主表
- **表名：** t_tcvat_rule_jzjt_jxse

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 业务名称 | varchar | 100 |  | √ | ' ' | 业务名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | forgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fruletype | 规则类型 | varchar | 50 |  | √ | ' ' | 规则类型,枚举: private :自用规则 public :可分配规则 |
| 7 | fjzjtlx | 即征即退类型 | varchar | 50 |  | √ | ' ' | 即征即退类型,枚举: jzjt :即征即退 wfhf :无法划分 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fissystem | 系统预设 | varchar | 50 |  | √ | ' ' | 系统预设,枚举: 0 :否 1 :是 |
| 13 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 14 | ftaxpayertype | 适用纳税人类型 | varchar | 50 |  | √ | ' ' | 适用纳税人类型,枚举: ybnsr :一般纳税人 xgmnsr :小规模纳税人 |
| 15 | fnumber | 规则编码 | varchar | 30 |  | √ | ' ' | 规则编码 |
| 16 | frulepurpose | 规则用途 | varchar | 50 |  | √ | ' ' | 规则用途,枚举: nssb :纳税申报 sjjt :税金计提 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_tcvat_rule_jzjt_jxse_1 |  | fnumber |
| 2 | pk_tcvat_rule_jzjt_jxse |  | fid |
