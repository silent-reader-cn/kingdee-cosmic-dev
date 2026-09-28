# 租户数据中心-dfa_tenant_datacenter

## 租户数据中心-多语言表 t_dfa_tenant_datacenter_l

- **表名称：** 租户数据中心-多语言表
- **表名：** t_dfa_tenant_datacenter_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 数据中心名称 | varchar | 50 |  | √ | ' ' | 数据中心名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_dfa_tenant_datacenter_l |  | fpkid |
| 2 | idx_dfa_tenant_datacenter_l_0 |  | fid |

---

## 租户数据中心-主表 t_dfa_tenant_datacenter

- **表名称：** 租户数据中心-主表
- **表名：** t_dfa_tenant_datacenter

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fevaluate_model | 财务健康评价模型(一般报表) | int8 | 64 |  | √ | 0 | [财务健康度评价模型类型 dfa_health_evaluate_type](../dfa_files/dfa_health_evaluate_type.md) |
| 3 | fname | 数据中心名称 | varchar | 50 |  | √ | ' ' | 数据中心名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fgroupid | 租户 | int8 | 64 |  | √ | 0 | [租户信息 dfa_tenant_info](../dfa_files/dfa_tenant_info.md) |
| 6 | frepo_group_code | 报表分组.编码 | varchar | 50 |  | √ | ' ' | 报表分组.编码 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fuser | 用户 | varchar | 50 |  | √ | ' ' | 用户 |
| 9 | frepo_group_name | 报表分组.名称 | varchar | 255 |  | √ | ' ' | 报表分组.名称 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fappid | 应用ID | varchar | 255 |  | √ | ' ' | 应用ID |
| 12 | fendpoint | 访问地址 | varchar | 512 |  | √ | ' ' | 访问地址 |
| 13 | fdatacenter | 数据中心ID | varchar | 50 |  | √ | ' ' | 数据中心ID |
| 14 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 15 | fevaluate_model_con | 财务健康评价模型(合并报表) | int8 | 64 |  | √ | 0 | [财务健康度评价模型类型 dfa_health_evaluate_type](../dfa_files/dfa_health_evaluate_type.md) |
| 16 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 18 | fappsec | 应用秘钥 | varchar | 255 |  | √ | ' ' | 应用秘钥 |
| 19 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 20 | fnumber | 数据中心编码 | varchar | 30 |  | √ | ' ' | 数据中心编码 |
| 21 | findustry | 行业 | int8 | 64 |  | √ | 0 | [证监会行业 csrc_industry_info](../ipobase_files/csrc_industry_info.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_dfa_tenant_datacenter |  | fnumber |
| 2 | pk_dfa_tenant_datacenter |  | fid |
