# 已废弃-预缴项目规则配置（共享）-tcvat_rule_prepay_inh

## 扣除额取数规则-子表 t_tcvat_rule_prepay_deduc

- **表名称：** 扣除额取数规则-子表
- **表名：** t_tcvat_rule_prepay_deduc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffconditionjson | 过滤条件 | text | 0 |  |  | null | 过滤条件 |
| 3 | famountfield | 金额字段 | int8 | 64 |  | √ | 0 | [数据源字段配置 tctb_datasource_entry](../tctb_files/tctb_datasource_entry.md) |
| 4 | ftable | 数据源 | int8 | 64 |  | √ | 0 | [数据源配置 tctb_custom_datasource](../tctb_files/tctb_custom_datasource.md) |
| 5 | fabsolute | 绝对值 | bpchar | 1 |  | √ | ' ' | 绝对值 |
| 6 | fiscustomtable | fiscustomtable | bpchar | 1 |  | √ | ' ' |  |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fbizname | 业务名称 | varchar | 50 |  | √ | ' ' | 业务名称 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | ffiltercondition | 过滤条件 | text | 0 |  |  | null | 过滤条件 |
| 11 | fdatadirection | 取数方向 | varchar | 30 |  | √ | ' ' | 取数方向,枚举: positive :正向 reverse :反向 |
| 12 | fdatatype | 取数方式 | varchar | 30 |  | √ | ' ' | 取数方式,枚举: zjqs :直接取数 prejsflqs :不含税价换算含税价 precysldsqs :税额换算含税价 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcvat_rule_prepay_deduc |  | fentryid |
| 2 | idx_tcvat_rule_prepay_deduc_fk |  | fid |

---

## 已废弃-预缴项目规则配置（共享）-主表 t_tcvat_rule_prepay

- **表名称：** 已废弃-预缴项目规则配置（共享）-主表
- **表名：** t_tcvat_rule_prepay

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 4 | forgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fruletype | 规则类型 | varchar | 30 |  | √ | ' ' | 规则类型,枚举: private :自用规则 public :可分配规则 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 10 | fprepaytype | fprepaytype | varchar | 30 |  | √ | ' ' |  |
| 11 | ftaxrateid | 税率 | int8 | 64 |  | √ | 0 | 税率模板 tpo_tcvat_taxrates |
| 12 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 13 | ftaxpayertype | ftaxpayertype | varchar | 30 |  | √ | ' ' |  |
| 14 | fnumber | 规则编码 | varchar | 30 |  | √ | ' ' | 规则编码 |
| 15 | fprepayproject | 预缴项目名称 | int8 | 64 |  | √ | 0 | [预缴项目信息 tcvat_prepay_project_info](../tcvat_files/tcvat_prepay_project_info.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tcvat_rule_prepay |  | fnumber,forgid |
| 2 | pk_tcvat_rule_prepay |  | fid |

---

## 已废弃-预缴项目规则配置（共享）-多语言表 t_tcvat_rule_prepay_l

- **表名称：** 已废弃-预缴项目规则配置（共享）-多语言表
- **表名：** t_tcvat_rule_prepay_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 规则名称 | varchar | 100 |  | √ | ' ' | 规则名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tcvat_rule_prepay_l_0 |  | fid,flocaleid |
| 2 | pk_tcvat_rule_prepay_l |  | fpkid |

---

## 销售额取数规则-子表 t_tcvat_rule_prepay_entry

- **表名称：** 销售额取数规则-子表
- **表名：** t_tcvat_rule_prepay_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffconditionjson | 过滤条件 | text | 0 |  |  | null | 过滤条件 |
| 3 | famountfield | 金额字段 | int8 | 64 |  | √ | 0 | [数据源字段配置 tctb_datasource_entry](../tctb_files/tctb_datasource_entry.md) |
| 4 | ftable | 数据源 | int8 | 64 |  | √ | 0 | [数据源配置 tctb_custom_datasource](../tctb_files/tctb_custom_datasource.md) |
| 5 | fabsolute | 绝对值 | bpchar | 1 |  | √ | ' ' | 绝对值 |
| 6 | fiscustomtable | fiscustomtable | bpchar | 1 |  | √ | ' ' |  |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fbizname | 业务名称 | varchar | 50 |  | √ | ' ' | 业务名称 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | ffiltercondition | 过滤条件 | text | 0 |  |  | null | 过滤条件 |
| 11 | fdatadirection | 取数方向 | varchar | 30 |  | √ | ' ' | 取数方向,枚举: positive :正向 reverse :反向 |
| 12 | fdatatype | 取数方式 | varchar | 30 |  | √ | ' ' | 取数方式,枚举: zjqs :直接取数 prejsflqs :不含税价换算含税价 precysldsqs :税额换算含税价 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcvat_rule_prepay_entry |  | fentryid |
| 2 | idx_tcvat_rule_prepay_entry_fk |  | fid |
