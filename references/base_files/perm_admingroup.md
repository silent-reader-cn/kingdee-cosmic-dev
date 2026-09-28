# 管理员分组-perm_admingroup

## 管理员分组-主表 t_perm_admingroup

- **表名称：** 管理员分组-主表
- **表名：** t_perm_admingroup

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fisleaf | 是否叶子 | bpchar | 1 |  | √ | '1' | 是否叶子 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 5 | fadminscheme | 权限控制策略 | int8 | 64 |  | √ | 0 | 管理员权限控制策略 perm_adminscheme |
| 6 | fparentid | 上级管理员分组 | int8 | 64 |  | √ | 0 | 管理员分组 perm_admingroup |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | ffullname | ffullname | varchar | 500 |  | √ | ' ' |  |
| 9 | flongnumber | 长编码 | varchar | 500 |  | √ | ' ' | 长编码 |
| 10 | fdisabledate | fdisabledate | timestamp | 0 |  |  | null |  |
| 11 | fdisablerid | fdisablerid | int8 | 64 |  | √ | 0 |  |
| 12 | fdescription | fdescription | varchar | 500 |  | √ | ' ' |  |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fdomainid | 管理员组领域 | int8 | 64 |  | √ | 0 | 管理员组领域 perm_admindomain |
| 15 | flevel | 级次 | int4 | 32 |  | √ | 0 | 级次 |
| 16 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 17 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 18 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 19 | fisdomain | 是否领域管理员组 | bpchar | 1 |  | √ | '0' | 是否领域管理员组 |
| 20 | foldadminid | foldadminid | varchar | 255 |  | √ | ' ' |  |
| 21 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 22 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 23 | fadmintype | 管理员类型 | int8 | 64 |  | √ | 0 | 虚拟管理员类型 perm_admintype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_perm_admingroup |  | fnumber |
| 2 | pk_t_perm_admingroup |  | fid |

---

## 管理员分组-多语言表 t_perm_admingroup_l

- **表名称：** 管理员分组-多语言表
- **表名：** t_perm_admingroup_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | ffullname | 长名称 | varchar | 500 |  | √ | ' ' | 长名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fdescription | 描述 | varchar | 500 |  | √ | ' ' | 描述 |
| 6 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_perm_admingroup_l |  | fid,flocaleid |
| 2 | pk_t_perm_admingroup_l |  | fpkid |
