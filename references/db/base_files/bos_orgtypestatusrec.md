# 组织职能状态记录-bos_orgtypestatusrec

## 组织职能状态记录-主表 t_org_typestatusrec

- **表名称：** 组织职能状态记录-主表
- **表名：** t_org_typestatusrec

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fviewschemaid | 组织视图 | int8 | 64 |  | √ | 0 | [组织视图方案 bos_org_viewschema](../base_files/bos_org_viewschema.md) |
| 3 | fisstatsum | 统计汇总 | bpchar | 1 |  | √ | '1' | 统计汇总 |
| 4 | fstatus | 状态 | varchar | 10 |  | √ | ' ' | 状态,枚举: A :启用 B :禁用 |
| 5 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | foperatime | 操作时间 | timestamp | 0 |  |  | null | 操作时间 |
| 7 | feffecttime | 生效时间 | timestamp | 0 |  |  | null | 生效时间 |
| 8 | finvalidtime | 失效时间 | timestamp | 0 |  |  | null | 失效时间 |
| 9 | foperatype | 操作类型 | varchar | 10 |  | √ | ' ' | 操作类型,枚举: 1 :启用 2 :禁用 3 :统计汇总 4 :名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_org_typestatrec_org |  | fviewschemaid,forgid,foperatime |
| 2 | t_org_typestatusrec_pkey |  | fid |

---

## 组织职能状态记录-多语言表 t_org_typestatusrec_l

- **表名称：** 组织职能状态记录-多语言表
- **表名：** t_org_typestatusrec_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 组织名称 | varchar | 255 |  | √ | ' ' | 组织名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_org_typestatusrec_l_pkey |  | fpkid |
| 2 | idx_t_org_typestatusrec_l_fid |  | fid,flocaleid |
