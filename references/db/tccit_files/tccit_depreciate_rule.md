# 资产加速折旧摊销取数规则-tccit_depreciate_rule

## 资产加速折旧摊销取数规则-多语言表 t_tccit_depreciate_rule_l

- **表名称：** 资产加速折旧摊销取数规则-多语言表
- **表名：** t_tccit_depreciate_rule_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tccit_depreciate_rule_l_0 |  | fid,flocaleid |
| 2 | pk_tccit_depreciate_rule_l |  | fpkid |

---

## 快速取数规则-子表 t_tccit_depreciate_quick

- **表名称：** 快速取数规则-子表
- **表名：** t_tccit_depreciate_quick

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffconditionjson | 过滤条件 | text | 0 |  |  | null | 过滤条件 |
| 3 | fexratejson | 汇率转换 | varchar | 255 |  | √ | ' ' | 汇率转换 |
| 4 | famountfield | 金额字段 | int8 | 64 |  | √ | 0 | [数据源字段配置 tctb_datasource_entry](../tctb_files/tctb_datasource_entry.md) |
| 5 | fadvancedconfjson | 取数逻辑 | text | 0 |  |  | null | 取数逻辑 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fbizname | 业务名称 | varchar | 50 |  | √ | ' ' | 业务名称 |
| 8 | ftable | 数据源 | int8 | 64 |  | √ | 0 | [数据源配置 tctb_custom_datasource](../tctb_files/tctb_custom_datasource.md) |
| 9 | fabsolute | 绝对值 | bpchar | 1 |  | √ | ' ' | 绝对值 |
| 10 | fiscustomtable | fiscustomtable | bpchar | 1 |  | √ | ' ' |  |
| 11 | fadvancedconf | 取数逻辑 | text | 0 |  |  | null | 取数逻辑 |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 13 | ffiltercondition | 过滤条件 | text | 0 |  |  | null | 过滤条件 |
| 14 | fdatadirection | 取数方向 | varchar | 30 |  | √ | ' ' | 取数方向,枚举: positive :正向 reverse :反向 |
| 15 | fdatatype | 取数方式 | varchar | 30 |  | √ | ' ' | 取数方式,枚举: zjqs :直接取数 jsflqs :价税分离取数 cysldsqs :除以税率倒算取数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tccit_depreciate_quick |  | fentryid |
| 2 | idx_tccit_depreciate_quick_fk |  | fid |

---

## 会计取数规则-子表 t_tccit_depreciate_accoun

- **表名称：** 会计取数规则-子表
- **表名：** t_tccit_depreciate_accoun

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffconditionjson | 过滤条件 | text | 0 |  |  | null | 过滤条件 |
| 3 | fexratejson | 汇率转换 | varchar | 255 |  | √ | ' ' | 汇率转换 |
| 4 | famountfield | 金额字段 | int8 | 64 |  | √ | 0 | [数据源字段配置 tctb_datasource_entry](../tctb_files/tctb_datasource_entry.md) |
| 5 | fadvancedconfjson | 取数逻辑 | text | 0 |  |  | null | 取数逻辑 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fbizname | 业务名称 | varchar | 50 |  | √ | ' ' | 业务名称 |
| 8 | ftable | 数据源 | int8 | 64 |  | √ | 0 | [数据源配置 tctb_custom_datasource](../tctb_files/tctb_custom_datasource.md) |
| 9 | fabsolute | 绝对值 | bpchar | 1 |  | √ | ' ' | 绝对值 |
| 10 | fiscustomtable | fiscustomtable | bpchar | 1 |  | √ | ' ' |  |
| 11 | fadvancedconf | 取数逻辑 | text | 0 |  |  | null | 取数逻辑 |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 13 | ffiltercondition | 过滤条件 | text | 0 |  |  | null | 过滤条件 |
| 14 | fdatadirection | 取数方向 | varchar | 30 |  | √ | ' ' | 取数方向,枚举: positive :正向 reverse :反向 |
| 15 | fdatatype | 取数方式 | varchar | 30 |  | √ | ' ' | 取数方式,枚举: zjqs :直接取数 jsflqs :价税分离取数 cysldsqs :除以税率倒算取数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tccit_depreciate_accoun |  | fentryid |
| 2 | idx_tccit_depreciate_accoun_fk |  | fid |

---

## 资产加速折旧摊销取数规则-主表 t_tccit_depreciate_rule

- **表名称：** 资产加速折旧摊销取数规则-主表
- **表名：** t_tccit_depreciate_rule

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
| 10 | fdepreciatetypeid | 加速折旧摊销类型 | int8 | 64 |  | √ | 0 | 项目取数（树） tpo_yearitems_tree |
| 11 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 12 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 13 | frulepurpose | 规则用途 | varchar | 50 |  | √ | ' ' | 规则用途,枚举: nssb :纳税申报 sjjt :税金计提 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tccit_depreciate_rule |  | fid |
| 2 | idx_tccit_depreciate_rule |  | forgid |

---

## 一般取数规则-子表 t_tccit_depreciate_normal

- **表名称：** 一般取数规则-子表
- **表名：** t_tccit_depreciate_normal

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffconditionjson | 过滤条件 | text | 0 |  |  | null | 过滤条件 |
| 3 | fexratejson | 汇率转换 | varchar | 255 |  | √ | ' ' | 汇率转换 |
| 4 | famountfield | 金额字段 | int8 | 64 |  | √ | 0 | [数据源字段配置 tctb_datasource_entry](../tctb_files/tctb_datasource_entry.md) |
| 5 | fadvancedconfjson | 取数逻辑 | text | 0 |  |  | null | 取数逻辑 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fbizname | 业务名称 | varchar | 50 |  | √ | ' ' | 业务名称 |
| 8 | ftable | 数据源 | int8 | 64 |  | √ | 0 | [数据源配置 tctb_custom_datasource](../tctb_files/tctb_custom_datasource.md) |
| 9 | fabsolute | 绝对值 | bpchar | 1 |  | √ | ' ' | 绝对值 |
| 10 | fiscustomtable | fiscustomtable | bpchar | 1 |  | √ | ' ' |  |
| 11 | fadvancedconf | 取数逻辑 | text | 0 |  |  | null | 取数逻辑 |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 13 | ffiltercondition | 过滤条件 | text | 0 |  |  | null | 过滤条件 |
| 14 | fdatadirection | 取数方向 | varchar | 30 |  | √ | ' ' | 取数方向,枚举: positive :正向 reverse :反向 |
| 15 | fdatatype | 取数方式 | varchar | 30 |  | √ | ' ' | 取数方式,枚举: zjqs :直接取数 jsflqs :价税分离取数 cysldsqs :除以税率倒算取数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tccit_depreciate_normal_fk |  | fid |
| 2 | pk_tccit_depreciate_normal |  | fentryid |

---

## 原值取数规则-子表 t_tccit_depreciate_origin

- **表名称：** 原值取数规则-子表
- **表名：** t_tccit_depreciate_origin

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fexratejson | 汇率转换 | varchar | 255 |  | √ | ' ' | 汇率转换 |
| 3 | famountfield | 金额字段 | int8 | 64 |  | √ | 0 | [数据源字段配置 tctb_datasource_entry](../tctb_files/tctb_datasource_entry.md) |
| 4 | fadvancedconfjson | 取数逻辑 | text | 0 |  |  | null | 取数逻辑 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fbizname | 业务名称 | varchar | 50 |  | √ | ' ' | 业务名称 |
| 7 | fconditionjson | 过滤条件 | text | 0 |  |  | null | 过滤条件 |
| 8 | ftable | 数据源 | int8 | 64 |  | √ | 0 | [数据源配置 tctb_custom_datasource](../tctb_files/tctb_custom_datasource.md) |
| 9 | fabsolute | 绝对值 | bpchar | 1 |  | √ | '0' | 绝对值 |
| 10 | fadvancedconf | 取数逻辑 | text | 0 |  |  | null | 取数逻辑 |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 12 | ffiltercondition | 过滤条件 | text | 0 |  |  | null | 过滤条件 |
| 13 | fdatadirection | 取数方向 | varchar | 50 |  | √ | ' ' | 取数方向,枚举: positive :正向 reverse :反向 |
| 14 | fdatatype | 取数方式 | varchar | 50 |  | √ | ' ' | 取数方式,枚举: zjqs :直接取数 jsflqs :价税分离取数 cysldsqs :除以税率倒算取数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tccit_depreciate_origin_fk |  | fid |
| 2 | pk_tccit_depreciate_origin |  | fentryid |
