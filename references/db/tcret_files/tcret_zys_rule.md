# 资源税规则配置-tcret_zys_rule

## 销售数量取数配置取数规则-子表 t_tcret_zys_rule_xssl

- **表名称：** 销售数量取数配置取数规则-子表
- **表名：** t_tcret_zys_rule_xssl

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | famountfield | 金额字段 | int8 | 64 |  | √ | 0 | [数据源字段配置 tctb_datasource_entry](../tctb_files/tctb_datasource_entry.md) |
| 3 | fadvancedconfjson | 高级配置 | text | 0 |  |  | null | 高级配置 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fbizname | 业务名称 | varchar | 200 |  | √ | ' ' | 业务名称 |
| 6 | fconditionjson | 过滤条件 | text | 0 |  |  | null | 过滤条件 |
| 7 | fyzvatrate | 增值税预征率 | numeric | 23 | 10 | √ | 0 | 增值税预征率 |
| 8 | ftable | 数据源 | int8 | 64 |  | √ | 0 | [数据源配置 tctb_custom_datasource](../tctb_files/tctb_custom_datasource.md) |
| 9 | fjsbl | 计税比例 | numeric | 23 | 10 | √ | 0 | 计税比例 |
| 10 | fvatrate | 增值税税率 | numeric | 23 | 10 | √ | 0 | 增值税税率 |
| 11 | fabsolute | 绝对值 | bpchar | 1 |  | √ | '0' | 绝对值 |
| 12 | fadvancedconf | 高级配置文本 | text | 0 |  |  | null | 高级配置文本 |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 14 | ffiltercondition | 过滤条件 | text | 0 |  |  | null | 过滤条件 |
| 15 | fdatadirection | 取数方向 | varchar | 50 |  | √ | ' ' | 取数方向,枚举: positive :正向 reverse :反向 |
| 16 | fdatatype | 取数方式 | varchar | 50 |  | √ | ' ' | 取数方式,枚举: zjqs :直接取数 jsflqs :含税价换算不含税价 cysldsqs :税额换算不含税价 gjqs :高级取数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcret_zys_rule_xssl |  | fentryid |
| 2 | idx_tcret_zys_rule_xssl_fk |  | fid |

---

## 销售额取数配置取数规则-子表 t_tcret_zys_rule_xse

- **表名称：** 销售额取数配置取数规则-子表
- **表名：** t_tcret_zys_rule_xse

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fjsbl1 | 计税比例 | numeric | 23 | 10 | √ | 0 | 计税比例 |
| 3 | famountfield | 金额字段 | int8 | 64 |  | √ | 0 | [数据源字段配置 tctb_datasource_entry](../tctb_files/tctb_datasource_entry.md) |
| 4 | fadvancedconf1 | 高级配置文本 | text | 0 |  |  | null | 高级配置文本 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fconditionjson1 | 过滤条件 | text | 0 |  |  | null | 过滤条件 |
| 7 | fbizname | 业务名称 | varchar | 200 |  | √ | ' ' | 业务名称 |
| 8 | fyzvatrate1 | 增值税预征率 | numeric | 23 | 10 | √ | 0 | 增值税预征率 |
| 9 | fadvancedconfjson1 | 高级配置 | text | 0 |  |  | null | 高级配置 |
| 10 | ftable | 数据源 | int8 | 64 |  | √ | 0 | [数据源配置 tctb_custom_datasource](../tctb_files/tctb_custom_datasource.md) |
| 11 | fabsolute | 绝对值 | bpchar | 1 |  | √ | '0' | 绝对值 |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 13 | ffiltercondition | 过滤条件 | text | 0 |  |  | null | 过滤条件 |
| 14 | fdatadirection | 取数方向 | varchar | 50 |  | √ | ' ' | 取数方向,枚举: positive :正向 reverse :反向 |
| 15 | fdatatype | 取数方式 | varchar | 50 |  | √ | ' ' | 取数方式,枚举: zjqs :直接取数 jsflqs :含税价换算不含税价 cysldsqs :税额换算不含税价 gjqs :高级取数 |
| 16 | fvatrate1 | 增值税税率 | numeric | 23 | 10 | √ | 0 | 增值税税率 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcret_zys_rule_xse |  | fentryid |
| 2 | idx_tcret_zys_rule_xse_fk |  | fid |

---

## 资源税规则配置-多语言表 t_tcret_zys_rule_l

- **表名称：** 资源税规则配置-多语言表
- **表名：** t_tcret_zys_rule_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 规则名称 | varchar | 100 |  | √ | ' ' | 规则名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcret_zys_rule_l |  | fpkid |
| 2 | idx_tcret_zys_rule_l_0 |  | fid,flocaleid |

---

## 资源税规则配置-主表 t_tcret_zys_rule

- **表名称：** 资源税规则配置-主表
- **表名：** t_tcret_zys_rule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 规则名称 | varchar | 100 |  | √ | ' ' | 规则名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fsyssyh | 适用税收优惠 | bpchar | 1 |  | √ | '0' | 适用税收优惠 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | ftaxitem | 税目 | int8 | 64 |  | √ | 0 | 资源税税率表分录 tpo_zys_taxitem_entry |
| 7 | ftaxsubitem | 子目 | varchar | 50 |  | √ | ' ' | 子目,枚举: yk :原矿 xk :选矿 |
| 8 | forgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fruletype | 规则类型 | varchar | 50 |  | √ | ' ' | 规则类型,枚举: private :自用规则 public :可分配规则 |
| 10 | flevy | 计征方式 | varchar | 50 |  | √ | ' ' | 计征方式,枚举: cjjz :从价计征 cljz :从量计征 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | ftaxsource | 税源编号 | int8 | 64 |  | √ | 0 | [资源税税源登记信息 tcret_zys_register](../tcret_files/tcret_zys_register.md) |
| 16 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 17 | ftaxdeduction | 减免项目代码及名称 | int8 | 64 |  | √ | 0 | 减免政策代码 tpo_taxdeduction |
| 18 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 19 | frulepurpose | 规则用途 | varchar | 50 |  | √ | ' ' | 规则用途,枚举: nssb :纳税申报 sjjt :税金计提 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcret_zys_rule |  | fid |
| 2 | idx_t_tcret_zys_rule_forgid |  | forgid,ftaxsource,ftaxitem,frulepurpose |

---

## 准予扣减的外购应税产品购进金额取数配置取数规则-子表 t_tcret_zys_rule_gjje

- **表名称：** 准予扣减的外购应税产品购进金额取数配置取数规则-子表
- **表名：** t_tcret_zys_rule_gjje

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fvatrate4 | 增值税税率 | numeric | 23 | 10 | √ | 0 | 增值税税率 |
| 3 | fjsbl4 | 计税比例 | numeric | 23 | 10 | √ | 0 | 计税比例 |
| 4 | famountfield | 金额字段 | int8 | 64 |  | √ | 0 | [数据源字段配置 tctb_datasource_entry](../tctb_files/tctb_datasource_entry.md) |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fbizname | 业务名称 | varchar | 200 |  | √ | ' ' | 业务名称 |
| 7 | fconditionjson4 | 过滤条件 | text | 0 |  |  | null | 过滤条件 |
| 8 | fadvancedconf4 | 高级配置文本 | text | 0 |  |  | null | 高级配置文本 |
| 9 | fadvancedconfjson4 | 高级配置 | text | 0 |  |  | null | 高级配置 |
| 10 | fyzvatrate4 | 增值税预征率 | numeric | 23 | 10 | √ | 0 | 增值税预征率 |
| 11 | ftable | 数据源 | int8 | 64 |  | √ | 0 | [数据源配置 tctb_custom_datasource](../tctb_files/tctb_custom_datasource.md) |
| 12 | fabsolute | 绝对值 | bpchar | 1 |  | √ | '0' | 绝对值 |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 14 | ffiltercondition | 过滤条件 | text | 0 |  |  | null | 过滤条件 |
| 15 | fdatadirection | 取数方向 | varchar | 50 |  | √ | ' ' | 取数方向,枚举: positive :正向 reverse :反向 |
| 16 | fdatatype | 取数方式 | varchar | 50 |  | √ | ' ' | 取数方式,枚举: zjqs :直接取数 jsflqs :含税价换算不含税价 cysldsqs :税额换算不含税价 gjqs :高级取数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcret_zys_rule_gjje |  | fentryid |
| 2 | idx_tcret_zys_rule_gjje_fk |  | fid |

---

## 准予扣除的运杂费取数配置取数规则-子表 t_tcret_zys_rule_yzf

- **表名称：** 准予扣除的运杂费取数配置取数规则-子表
- **表名：** t_tcret_zys_rule_yzf

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fjsbl2 | 计税比例 | numeric | 23 | 10 | √ | 0 | 计税比例 |
| 3 | famountfield | 金额字段 | int8 | 64 |  | √ | 0 | [数据源字段配置 tctb_datasource_entry](../tctb_files/tctb_datasource_entry.md) |
| 4 | fadvancedconf2 | 高级配置文本 | text | 0 |  |  | null | 高级配置文本 |
| 5 | fconditionjson2 | 过滤条件 | text | 0 |  |  | null | 过滤条件 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fbizname | 业务名称 | varchar | 200 |  | √ | ' ' | 业务名称 |
| 8 | fyzvatrate2 | 增值税预征率 | numeric | 23 | 10 | √ | 0 | 增值税预征率 |
| 9 | fadvancedconfjson2 | 高级配置 | text | 0 |  |  | null | 高级配置 |
| 10 | ftable | 数据源 | int8 | 64 |  | √ | 0 | [数据源配置 tctb_custom_datasource](../tctb_files/tctb_custom_datasource.md) |
| 11 | fabsolute | 绝对值 | bpchar | 1 |  | √ | '0' | 绝对值 |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 13 | ffiltercondition | 过滤条件 | text | 0 |  |  | null | 过滤条件 |
| 14 | fdatadirection | 取数方向 | varchar | 50 |  | √ | ' ' | 取数方向,枚举: positive :正向 reverse :反向 |
| 15 | fvatrate2 | 增值税税率 | numeric | 23 | 10 | √ | 0 | 增值税税率 |
| 16 | fdatatype | 取数方式 | varchar | 50 |  | √ | ' ' | 取数方式,枚举: zjqs :直接取数 jsflqs :含税价换算不含税价 cysldsqs :税额换算不含税价 gjqs :高级取数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcret_zys_rule_yzf |  | fentryid |
| 2 | idx_tcret_zys_rule_yzf_fk |  | fid |

---

## 准予扣减的外购应税产品购进数量取数配置取数规则-子表 t_tcret_zys_rule_gjsl

- **表名称：** 准予扣减的外购应税产品购进数量取数配置取数规则-子表
- **表名：** t_tcret_zys_rule_gjsl

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fvatrate3 | 增值税税率 | numeric | 23 | 10 | √ | 0 | 增值税税率 |
| 3 | fjsbl3 | 计税比例 | numeric | 23 | 10 | √ | 0 | 计税比例 |
| 4 | famountfield | 金额字段 | int8 | 64 |  | √ | 0 | [数据源字段配置 tctb_datasource_entry](../tctb_files/tctb_datasource_entry.md) |
| 5 | fadvancedconf3 | 高级配置文本 | text | 0 |  |  | null | 高级配置文本 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fbizname | 业务名称 | varchar | 200 |  | √ | ' ' | 业务名称 |
| 8 | fconditionjson3 | 过滤条件 | text | 0 |  |  | null | 过滤条件 |
| 9 | fadvancedconfjson3 | 高级配置 | text | 0 |  |  | null | 高级配置 |
| 10 | fyzvatrate3 | 增值税预征率 | numeric | 23 | 10 | √ | 0 | 增值税预征率 |
| 11 | ftable | 数据源 | int8 | 64 |  | √ | 0 | [数据源配置 tctb_custom_datasource](../tctb_files/tctb_custom_datasource.md) |
| 12 | fabsolute | 绝对值 | bpchar | 1 |  | √ | '0' | 绝对值 |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 14 | ffiltercondition | 过滤条件 | text | 0 |  |  | null | 过滤条件 |
| 15 | fdatadirection | 取数方向 | varchar | 50 |  | √ | ' ' | 取数方向,枚举: positive :正向 reverse :反向 |
| 16 | fdatatype | 取数方式 | varchar | 50 |  | √ | ' ' | 取数方式,枚举: zjqs :直接取数 jsflqs :含税价换算不含税价 cysldsqs :税额换算不含税价 gjqs :高级取数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcret_zys_rule_gjsl |  | fentryid |
| 2 | idx_tcret_zys_rule_gjsl_fk |  | fid |
