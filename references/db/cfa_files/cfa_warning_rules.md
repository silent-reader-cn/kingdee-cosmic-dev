# 预警规则-cfa_warning_rules

## 预警规则-多语言表 t_cfa_warning_rules_l

- **表名称：** 预警规则-多语言表
- **表名：** t_cfa_warning_rules_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cfa_warning_rules_l |  | fpkid |
| 2 | idx_cfa_warning_rules_l |  | fname |

---

## 预警规则明细-子表 t_warning_rule_detail

- **表名称：** 预警规则明细-子表
- **表名：** t_warning_rule_detail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fvalue | 值 | varchar | 50 |  | √ | ' ' | 值 |
| 3 | frightparenthesis |  | varchar | 50 |  | √ | ' ' | ,枚举: |
| 4 | fleftparenthesis |  | varchar | 50 |  | √ | ' ' | ,枚举: |
| 5 | ffield | 字段 | varchar | 50 |  | √ | ' ' | 字段,枚举: 1 :连续N期上升 2 :连续N期下降 3 :连续N期值同时 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fnequal | N= | varchar | 50 |  | √ | ' ' | N= |
| 8 | fcondition | 条件 | varchar | 50 |  | √ | ' ' | 条件,枚举: = :等于 != :不等于 > :大于 >= :大于等于 < :小于 <= :小于等于 |
| 9 | flogic | 逻辑 | varchar | 50 |  | √ | ' ' | 逻辑,枚举: |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | fwarningrulesdetail | 预警规则 | varchar | 50 |  | √ | ' ' | 预警规则 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_warning_rule_detail |  | fentryid |
| 2 | idx_warning_rule_detail_fk |  | fid |

---

## 预警规则-主表 t_cfa_warning_rules

- **表名称：** 预警规则-主表
- **表名：** t_cfa_warning_rules

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | frptitemdatatype | 项目数据类型 | int8 | 64 |  | √ | 0 | [项目数据类型 xkbd_rptitemdatatype](../fibd_files/xkbd_rptitemdatatype.md) |
| 3 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fwarningobject | 预警对象 | varchar | 50 |  | √ | ' ' | 预警对象,枚举: reportitem :报表项目 quota :指标 |
| 6 | fenablerules | 启用规则 | bpchar | 1 |  | √ | '1' | 启用规则 |
| 7 | fexpression | 预警提示语表达式 | varchar | 600 |  | √ | ' ' | 预警提示语表达式 |
| 8 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | fwarningruletype | 预警规则类型 | bpchar | 1 |  | √ | '1' | 预警规则类型,枚举: 1 :常规预警 2 :连续多期趋势预警 3 :目标达成预警 4 :消息设置 |
| 10 | fwarningprompttitle | 预警提示语(解析后) | varchar | 500 |  | √ | ' ' | 预警提示语(解析后) |
| 11 | frptitemgroup | 报表项目分组 | int8 | 64 |  | √ | 0 | [报表项目分组 xkbd_rptitemgroup](../fibd_files/xkbd_rptitemgroup.md) |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fquotainfo | 指标 | int8 | 64 |  | √ | 0 | [指标库 ipo_quota_info](../ipobase_files/ipo_quota_info.md) |
| 14 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 15 | frptitem | 项目 | int8 | 64 |  | √ | 0 | [报表项目 xkbd_rptitem](../fibd_files/xkbd_rptitem.md) |
| 16 | fwarningcolor | 预警颜色 | varchar | 50 |  | √ | 'red' | 预警颜色,枚举: red :红 orange :橙 yellow :黄 |
| 17 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 19 | fwarningrules | 预警规则 | varchar | 500 |  | √ | ' ' | 预警规则 |
| 20 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 21 | fwarningtype | 预警分类 | bpchar | 1 |  | √ | '0' | 预警分类,枚举: 1 :资金风险 2 :偿债风险 3 :增长风险 4 :盈利风险 5 :运营风险 6 :费控风险 7 :其他风险 |
| 22 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 23 | fimportancelevel | 重要程度 | bpchar | 1 |  | √ | '0' | 重要程度,枚举: 1 :一般重要 2 :非常重要 3 :及其重要 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | index_cfa_warning_rules |  | fnumber |
| 2 | pk_cfa_warning_rules |  | fid |
