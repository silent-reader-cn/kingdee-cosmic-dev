# 水土保持补偿费应缴费基数规则-totf_rule_stbcbcf

## 水土保持补偿费应缴费基数规则-多语言表 t_totf_rule_stbcbcf_l

- **表名称：** 水土保持补偿费应缴费基数规则-多语言表
- **表名：** t_totf_rule_stbcbcf_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 规则名称 | varchar | 200 |  | √ | ' ' | 规则名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_totf_rule_stbcbcf_l_0 |  | fid,flocaleid |
| 2 | pk_totf_rule_stbcbcf_l |  | fpkid |

---

## 水土保持补偿费应缴费基数规则-主表 t_totf_rule_stbcbcf

- **表名称：** 水土保持补偿费应缴费基数规则-主表
- **表名：** t_totf_rule_stbcbcf

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 规则名称 | varchar | 200 |  | √ | ' ' | 规则名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fzszm | 征收子目 | int8 | 64 |  | √ | 0 | 业务定义分录 tpo_tysbsf_bizdef_entry |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fruletype | 规则类型 | varchar | 50 |  | √ | ' ' | 规则类型,枚举: private :自用规则 public :可分配规则 |
| 8 | fcollectionitem | 征收品目 | int8 | 64 |  | √ | 0 | 征收品目 tpo_zspm |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fissystem | 系统预设 | varchar | 50 |  | √ | ' ' | 系统预设,枚举: 0 :否 1 :是 |
| 14 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 15 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 16 | frulepurpose | 规则用途 | varchar | 50 |  | √ | ' ' | 规则用途,枚举: nssb :纳税申报 sjjt :税金计提 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_rule_stbcbcf_forgid |  | forgid,frulepurpose,fcollectionitem,fzszm,fenable |
| 2 | pk_totf_rule_stbcbcf |  | fid |

---

## 取数规则-子表 t_totf_rule_stbcbcf_entry

- **表名称：** 取数规则-子表
- **表名：** t_totf_rule_stbcbcf_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffconditionjson | 过滤条件 | text | 0 |  |  | null | 过滤条件 |
| 3 | famountfield | 金额字段 | int8 | 64 |  | √ | 0 | [数据源字段配置 tctb_datasource_entry](../tctb_files/tctb_datasource_entry.md) |
| 4 | fadvancedconfjson | 取数逻辑 | text | 0 |  |  | null | 取数逻辑 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fbizname | 业务名称 | varchar | 200 |  | √ | ' ' | 业务名称 |
| 7 | ftable | 数据源 | int8 | 64 |  | √ | 0 | [数据源配置 tctb_custom_datasource](../tctb_files/tctb_custom_datasource.md) |
| 8 | fvatrate | 增值税税率 | numeric | 23 | 10 | √ | 0 | 增值税税率 |
| 9 | fjsbl | 计税比例 | numeric | 23 | 10 | √ | 0 | 计税比例 |
| 10 | fabsolute | 绝对值 | bpchar | 1 |  | √ | '0' | 绝对值 |
| 11 | fadvancedconf | 取数逻辑 | text | 0 |  |  | null | 取数逻辑 |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 13 | ffiltercondition | 过滤条件 | text | 0 |  |  | null | 过滤条件 |
| 14 | fdatadirection | 取数方向 | varchar | 50 |  | √ | ' ' | 取数方向,枚举: positive :正向 reverse :反向 |
| 15 | fdatatype | 取数方式 | varchar | 50 |  | √ | ' ' | 取数方式,枚举: zjqs :直接取数 gjqs :高级取数 cysldsqs :税额换算不含税价 jsflqs :含税价换算不含税价 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_rule_stbcbcf_entry_fid |  | fid |
| 2 | pk_totf_rule_stbcbcf_entry |  | fentryid |
