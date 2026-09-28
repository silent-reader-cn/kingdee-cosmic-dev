# 租户用户配置-dfa_tenant_user_conf

## 租户用户配置-主表 t_dfa_tenant_user_conf

- **表名称：** 租户用户配置-主表
- **表名：** t_dfa_tenant_user_conf

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | faccountingsys_name | 核算体系.名称 | varchar | 255 |  | √ | ' ' | 核算体系.名称 |
| 3 | faccountingpolicy_code | 会计政策.编码 | varchar | 50 |  | √ | ' ' | 会计政策.编码 |
| 4 | fcurrency_code | 币种.编码 | varchar | 50 |  | √ | ' ' | 币种.编码 |
| 5 | fconsolidationscheme_code | 合并方案.编码 | varchar | 50 |  | √ | ' ' | 合并方案.编码 |
| 6 | famountunit_code | 金额单位.编码 | varchar | 50 |  | √ | ' ' | 金额单位.编码 |
| 7 | frepo_type | 报表类型 | varchar | 50 |  | √ | ' ' | 报表类型,枚举: REPORT :报表 INDIVIDUAL_REPORT :个别报表 CONSOLIDATED_REPORT :合并报表 |
| 8 | faccountingsys_code | 核算体系.编码 | varchar | 50 |  | √ | ' ' | 核算体系.编码 |
| 9 | faccountingorg_code | 核算组织.编码 | varchar | 50 |  | √ | ' ' | 核算组织.编码 |
| 10 | fcurrency_name | 币种.名称 | varchar | 50 |  | √ | ' ' | 币种.名称 |
| 11 | faccountingorg_name | 核算组织.名称 | varchar | 255 |  | √ | ' ' | 核算组织.名称 |
| 12 | fconsolidationscope_name | 合并范围.名称 | varchar | 255 |  | √ | ' ' | 合并范围.名称 |
| 13 | frepo_cycle_type | 报表周期类型 | varchar | 50 |  | √ | ' ' | 报表周期类型,枚举: MONTHLY :月报 QUARTERLY :季报 SEMI_ANNUAL :半年报 ANNUAL :年报 |
| 14 | fmodifydatefield | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 15 | fconsolidationscope_code | 合并范围.编码 | varchar | 50 |  | √ | ' ' | 合并范围.编码 |
| 16 | fconsolidationscheme_name | 合并方案.名称 | varchar | 255 |  | √ | ' ' | 合并方案.名称 |
| 17 | ftenant_user | 租户登录用户 | int8 | 64 |  | √ | 0 | [租户用户 dfa_tenant_user](../dfa_files/dfa_tenant_user.md) |
| 18 | faccountingpolicy_name | 会计政策.名称 | varchar | 255 |  | √ | ' ' | 会计政策.名称 |
| 19 | famountunit_name | 金额单位.名称 | varchar | 255 |  | √ | ' ' | 金额单位.名称 |
| 20 | finitialized | 是否初始化 | bpchar | 1 |  | √ | ' ' | 是否初始化 |
| 21 | findustry | findustry | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_dfa_tenant_user_conf |  | fid |
| 2 | idx_dfa_tenant_user_conf |  | ftenant_user |

---

## 指标信息-子表 t_dfa_metricsinfo

- **表名称：** 指标信息-子表
- **表名：** t_dfa_metricsinfo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmetricscode | 指标编码 | varchar | 50 |  | √ | ' ' | 指标编码 |
| 3 | fmetricsname | 指标名称 | varchar | 50 |  | √ | ' ' | 指标名称 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fmetricsnumber | fmetricsnumber | varchar | 50 |  | √ | ' ' |  |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | funit | 单位 | varchar | 50 |  | √ | ' ' | 单位 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_dfa_metricsinfo_fk |  | fid |
| 2 | pk_dfa_metricsinfo |  | fentryid |
