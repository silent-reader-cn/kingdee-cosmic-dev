# 农产品项目规则-tcvat_ncp_rule

## 农产品项目规则-多语言表 t_tcvat_ncp_rule_l

- **表名称：** 农产品项目规则-多语言表
- **表名：** t_tcvat_ncp_rule_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 业务名称 | varchar | 50 |  | √ | ' ' | 业务名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tcvat_ncp_rule_l_0 |  | fid,flocaleid |
| 2 | pk_tcvat_ncp_rule_l |  | fpkid |

---

## 采购数量取数配置-子表 t_tcvat_ncp_rule_ent

- **表名称：** 采购数量取数配置-子表
- **表名：** t_tcvat_ncp_rule_ent

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffconditionjson | 过滤条件 | text | 0 |  |  | null | 过滤条件 |
| 3 | famountfield | 金额字段 | int8 | 64 |  | √ | 0 | [数据源字段配置 tctb_datasource_entry](../tctb_files/tctb_datasource_entry.md) |
| 4 | ftable | 数据源 | int8 | 64 |  | √ | 0 | [数据源配置 tctb_custom_datasource](../tctb_files/tctb_custom_datasource.md) |
| 5 | fabsolute | 绝对值 | bpchar | 1 |  | √ | '0' | 绝对值 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fbizname | 业务名称 | varchar | 50 |  | √ | ' ' | 业务名称 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | ffiltercondition | 过滤条件 | text | 0 |  |  | null | 过滤条件 |
| 10 | fdatadirection | 取数方向 | varchar | 50 |  | √ | ' ' | 取数方向,枚举: positive :正向 reverse :反向 |
| 11 | fdatatype | 取数方式 | varchar | 50 |  | √ | ' ' | 取数方式,枚举: zjqs :直接取数 jsflqs :价税分离取数 cysldsqs :除以税率倒算取数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tcvat_ncp_rule_ent_fk |  | fid |
| 2 | pk_tcvat_ncp_rule_ent |  | fentryid |

---

## 销售数量取数配置-子表 t_tcvat_ncp_rule_ent2

- **表名称：** 销售数量取数配置-子表
- **表名：** t_tcvat_ncp_rule_ent2

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | famountfield | 金额字段 | int8 | 64 |  | √ | 0 | [数据源字段配置 tctb_datasource_entry](../tctb_files/tctb_datasource_entry.md) |
| 3 | ftable | 数据源 | int8 | 64 |  | √ | 0 | [数据源配置 tctb_custom_datasource](../tctb_files/tctb_custom_datasource.md) |
| 4 | fabsolute | 绝对值 | bpchar | 1 |  | √ | '0' | 绝对值 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fbizname | 业务名称 | varchar | 50 |  | √ | ' ' | 业务名称 |
| 7 | fconditionjson | 过滤条件 | text | 0 |  |  | null | 过滤条件 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | ffiltercondition | 过滤条件 | text | 0 |  |  | null | 过滤条件 |
| 10 | fdatadirection | 取数方向 | varchar | 50 |  | √ | ' ' | 取数方向,枚举: positive :正向 reverse :反向 |
| 11 | fdatatype | 取数方式 | varchar | 50 |  | √ | ' ' | 取数方式,枚举: zjqs :直接取数 jsflqs :价税分离取数 cysldsqs :除以税率倒算取数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcvat_ncp_rule_ent2 |  | fentryid |
| 2 | idx_tcvat_ncp_rule_ent2_fk |  | fid |

---

## 销售金额取数配置-子表 t_tcvat_ncp_rule_ent3

- **表名称：** 销售金额取数配置-子表
- **表名：** t_tcvat_ncp_rule_ent3

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | famountfield | 金额字段 | int8 | 64 |  | √ | 0 | [数据源字段配置 tctb_datasource_entry](../tctb_files/tctb_datasource_entry.md) |
| 3 | ftable | 数据源 | int8 | 64 |  | √ | 0 | [数据源配置 tctb_custom_datasource](../tctb_files/tctb_custom_datasource.md) |
| 4 | fabsolute | 绝对值 | bpchar | 1 |  | √ | '0' | 绝对值 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fbizname | 业务名称 | varchar | 50 |  | √ | ' ' | 业务名称 |
| 7 | fconditionjson | 过滤条件 | text | 0 |  |  | null | 过滤条件 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | ffiltercondition | 过滤条件 | text | 0 |  |  | null | 过滤条件 |
| 10 | fdatadirection | 取数方向 | varchar | 50 |  | √ | ' ' | 取数方向,枚举: positive :正向 reverse :反向 |
| 11 | fdatatype | 取数方式 | varchar | 50 |  | √ | ' ' | 取数方式,枚举: zjqs :直接取数 jsflqs :价税分离取数 cysldsqs :除以税率倒算取数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcvat_ncp_rule_ent3 |  | fentryid |
| 2 | idx_tcvat_ncp_rule_ent3_fk |  | fid |

---

## 采购金额取数配置-子表 t_tcvat_ncp_rule_ent1

- **表名称：** 采购金额取数配置-子表
- **表名：** t_tcvat_ncp_rule_ent1

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | famountfield | 金额字段 | int8 | 64 |  | √ | 0 | [数据源字段配置 tctb_datasource_entry](../tctb_files/tctb_datasource_entry.md) |
| 3 | ftable | 数据源 | int8 | 64 |  | √ | 0 | [数据源配置 tctb_custom_datasource](../tctb_files/tctb_custom_datasource.md) |
| 4 | fabsolute | 绝对值 | bpchar | 1 |  | √ | '0' | 绝对值 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fbizname | 业务名称 | varchar | 50 |  | √ | ' ' | 业务名称 |
| 7 | fconditionjson | 过滤条件 | text | 0 |  |  | null | 过滤条件 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | ffiltercondition | 过滤条件 | text | 0 |  |  | null | 过滤条件 |
| 10 | fdatadirection | 取数方向 | varchar | 50 |  | √ | ' ' | 取数方向,枚举: positive :正向 reverse :反向 |
| 11 | fdatatype | 取数方式 | varchar | 50 |  | √ | ' ' | 取数方式,枚举: zjqs :直接取数 jsflqs :价税分离取数 cysldsqs :除以税率倒算取数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tcvat_ncp_rule_ent1_fk |  | fid |
| 2 | pk_tcvat_ncp_rule_ent1 |  | fentryid |

---

## 农产品项目规则-主表 t_tcvat_ncp_rule

- **表名称：** 农产品项目规则-主表
- **表名：** t_tcvat_ncp_rule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 业务名称 | varchar | 50 |  | √ | ' ' | 业务名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fhyncp | 耗用农产品名称 | int8 | 64 |  | √ | 0 | [耗用农产品名称 tcvat_hyncp_name](../tcvat_files/tcvat_hyncp_name.md) |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fruletype | 规则类型 | varchar | 50 |  | √ | ' ' | 规则类型,枚举: private :自用规则 public :可分配规则 |
| 8 | fylfl | 用途 | varchar | 50 |  | √ | ' ' | 用途,枚举: sjg :深加工 zjxs :直接销售 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fissystem | 系统预设 | varchar | 50 |  | √ | ' ' | 系统预设,枚举: 0 :否 1 :是 |
| 14 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 15 | fnumber | 规则编码 | varchar | 30 |  | √ | ' ' | 规则编码 |
| 16 | frulepurpose | 规则用途 | varchar | 50 |  | √ | ' ' | 规则用途,枚举: nssb :纳税申报 sjjt :税金计提 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_tcvat_ncp_rule |  | forgid,fruletype |
| 2 | pk_tcvat_ncp_rule |  | fid |
