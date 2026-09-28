# 合规性配置表-rim_verify

## 单据体-子表 t_rim_verify_entry

- **表名称：** 单据体-子表
- **表名：** t_rim_verify_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 4 | forg | 基础资料 | int8 | 64 |  | √ | 0 | 树形组织列表 bdm_org_tree_list |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_rim_verify_entry |  | fentryid |
| 2 | idx_rim_verify_entry_fk |  | fid |

---

## 合规性配置表-主表 t_rim_verify

- **表名称：** 合规性配置表-主表
- **表名：** t_rim_verify

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsensitive_word | 敏感词 | varchar | 2000 |  | √ | ' ' | 敏感词 |
| 3 | fname | 方案名称 | varchar | 50 |  | √ | ' ' | 方案名称 |
| 4 | fbill_type | 业务单据类型 | varchar | 300 |  | √ | ' ' | 业务单据类型,枚举: 1 :应付单 er_dailyreimbursebill :费用报销单 er_tripreimbursebill :差旅报销单 4 :付款申请单 er_publicreimbursebill :对公报销单 |
| 5 | fupdate_time | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 6 | fbase_config | 通用配置 | varchar | 2000 |  | √ | ' ' | 通用配置 |
| 7 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 8 | fstatus | 状态 | varchar | 2 |  | √ | ' ' | 状态,枚举: 0 :禁用 1 :启用 |
| 9 | fcustom_config | 个性化配置 | varchar | 2000 |  | √ | ' ' | 个性化配置 |
| 10 | fcreater | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fcreate_time | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 12 | fcustom_config_tag | 个性化配置_详情 | text | 0 |  |  | '' | 个性化配置_详情 |
| 13 | fsequence_type | 连号发票类型 | varchar | 200 |  | √ | ' ' | 连号发票类型 |
| 14 | fblack_list | 黑名单 | varchar | 2000 |  | √ | ' ' | 黑名单 |
| 15 | fscope | 适用范围 | varchar | 2 |  | √ | ' ' | 适用范围,枚举: 1 :全局共享 2 :指定组织 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_rim_verify |  | fid |
| 2 | idx_rim_verify_name |  | fname |
