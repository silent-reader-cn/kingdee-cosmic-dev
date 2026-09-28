# 尾盘申报项取数规则配置-tcret_wp_rule

## 尾盘申报项取数规则配置-主表 t_tcret_wp_rule

- **表名称：** 尾盘申报项取数规则配置-主表
- **表名：** t_tcret_wp_rule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbuildingtype | 房产类型 | int8 | 64 |  | √ | 0 | 业务定义分录 tpo_tdzzs_bizdef_entry |
| 3 | fname | 规则名称 | varchar | 100 |  | √ | ' ' | 规则名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fprojectid | 土地增值税项目 | int8 | 64 |  | √ | 0 | [土地增值税项目 tdm_tdzzs_clearing_unit](../tdm_files/tdm_tdzzs_clearing_unit.md) |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fdeclareitem | 尾盘申报项目 | int8 | 64 |  | √ | 0 | 业务定义分录 tpo_tdzzs_bizdef_entry |
| 8 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fruletype | 规则类型 | varchar | 50 |  | √ | ' ' | 规则类型,枚举: private :自用规则 public :可分配规则 |
| 10 | fdeclaretype | 申报类型 | int8 | 64 |  | √ | 0 | 业务定义分录 tpo_tdzzs_bizdef_entry |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 16 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_tcret_wp_rule |  | fnumber |
| 2 | pk_tcret_wp_rule |  | fid |

---

## 尾盘申报项取数规则配置-多语言表 t_tcret_wp_rule_l

- **表名称：** 尾盘申报项取数规则配置-多语言表
- **表名：** t_tcret_wp_rule_l

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
| 1 | pk_tcret_wp_rule_l |  | fpkid |
| 2 | idx_tcret_wp_rule_l_0 |  | fid,flocaleid |

---

## 取数规则-子表 t_tcret_wp_rule_item

- **表名称：** 取数规则-子表
- **表名：** t_tcret_wp_rule_item

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | famountfield | 金额字段 | int8 | 64 |  | √ | 0 | [数据源字段配置 tctb_datasource_entry](../tctb_files/tctb_datasource_entry.md) |
| 3 | fadvancedconfjson | 高级配置 | varchar | 2000 |  | √ | ' ' | 高级配置 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fbizname | 业务名称 | varchar | 200 |  | √ | ' ' | 业务名称 |
| 6 | fconditionjson | 过滤条件 | text | 0 |  |  | null | 过滤条件 |
| 7 | fyzvatrate | 增值税预征率11 | numeric | 23 | 10 | √ | 0 | 增值税预征率11 |
| 8 | ftable | 数据源 | int8 | 64 |  | √ | 0 | [数据源配置 tctb_custom_datasource](../tctb_files/tctb_custom_datasource.md) |
| 9 | fjsbl | 计税比例 | numeric | 23 | 10 | √ | 0 | 计税比例 |
| 10 | fvatrate | 增值税税率 | numeric | 23 | 10 | √ | 0 | 增值税税率 |
| 11 | fabsolute | 绝对值 | bpchar | 1 |  | √ | '0' | 绝对值 |
| 12 | fadvancedconf | 高级配置文本 | varchar | 2000 |  | √ | ' ' | 高级配置文本 |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 14 | ffiltercondition | 过滤条件 | text | 0 |  |  | null | 过滤条件 |
| 15 | fdatadirection | 取数方向 | varchar | 50 |  | √ | ' ' | 取数方向,枚举: positive :正向 reverse :反向 |
| 16 | fdatatype | 取数方式 | varchar | 50 |  | √ | ' ' | 取数方式,枚举: zjqs :直接取数 gjqs :高级取数 jsflqs :含税价换算不含税价 cysldsqs :税额换算不含税价 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_tcret_wp_rule_item |  | fid |
| 2 | pk_tcret_wp_rule_item |  | fentryid |
