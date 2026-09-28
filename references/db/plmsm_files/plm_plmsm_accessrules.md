# 访问策略规则-plm_plmsm_accessrules

## 访问策略规则-多语言表 t_plmsm_accesspolicyrule_l

- **表名称：** 访问策略规则-多语言表
- **表名：** t_plmsm_accesspolicyrule_l

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
| 1 | pk_plmsm_accesspolicyrule_l |  | fpkid |
| 2 | idx_policyrule_id_lcl |  | fid,flocaleid |

---

## 访问策略规则-主表 t_plmsm_accesspolicyrule

- **表名称：** 访问策略规则-主表
- **表名：** t_plmsm_accesspolicyrule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdomainid | 所属域 | int8 | 64 |  | √ | 0 | [域 plm_plmsm_domain](../plmsm_files/plm_plmsm_domain.md) |
| 3 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 4 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 8 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 10 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plmsm_accesspolicyrule |  | fid |
| 2 | idx_plmsm_plc_rl_number |  | fnumber |
| 3 | idx_plmsm_plc_rl_name |  | fname |

---

## 访问控制单据体-子表 t_plmsm_aclentry

- **表名称：** 访问控制单据体-子表
- **表名：** t_plmsm_aclentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flcstatusid | 状态 | int8 | 64 |  | √ | 0 | [流程状态 plm_lc_status](../plmsm_files/plm_lc_status.md) |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fpermissiontype | 权限类型 | varchar | 50 |  | √ | ' ' | 权限类型,枚举: A :授权 B :拒绝 |
| 5 | fpdmmodelid | 类型 | int8 | 64 |  | √ | 0 | [PDM模型 plm_plmsm_modeltreedata](../plmsm_files/plm_plmsm_modeltreedata.md) |
| 6 | fdomainid | fdomainid | int8 | 64 |  | √ | 0 |  |
| 7 | fapplyto | 应用于 | varchar | 50 |  | √ | ' ' | 应用于,枚举: A :参与者 B :全部（选定参与者除外） |
| 8 | fparticipanttype | 参与者类型 | varchar | 50 |  | √ | ' ' | 参与者类型,枚举: bos_user :用户 plm_plmsm_role :PLM角色 bos_usergroup :用户组 |
| 9 | fparticipantid | 参与者 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 | pid |
| 11 | fdomainofbelongid | 所属域 | int8 | 64 |  | √ | 0 | [域 plm_plmsm_domain](../plmsm_files/plm_plmsm_domain.md) |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 13 | fpermissionmask | 授予权限 | int8 | 64 |  | √ | 0 | 授予权限 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plmsm_aclentry_fid |  | fid |
| 2 | pk_plmsm_aclentry |  | fentryid |
| 3 | idx_plmsm_aclentry_peid |  | fparententryid |
