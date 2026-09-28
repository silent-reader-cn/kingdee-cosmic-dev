# 工作流角色-wf_role

## 工作流角色-多语言表 t_wf_role_l

- **表名称：** 工作流角色-多语言表
- **表名：** t_wf_role_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 500 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 8 |  | √ | ' ' | localeid |
| 4 | fdescription | 描述 | varchar | 500 |  | √ | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_wf_role_localeid |  | fid,flocaleid |
| 2 | t_wf_role_l_pkey |  | fpkid |

---

## 工作流角色-主表 t_wf_role

- **表名称：** 工作流角色-主表
- **表名：** t_wf_role

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 500 |  | √ | ' ' | 名称 |
| 3 | froledimension | 多维度信息 | varchar | 1000 |  | √ | ' ' | 多维度信息 |
| 4 | fmanager | 管理员 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | fdescription | 描述 | varchar | 500 |  | √ | ' ' | 描述 |
| 7 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | forgunit | 所属组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 9 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fusecount | 被用次数 | int8 | 64 |  | √ | 0 | 被用次数 |
| 11 | fcreater | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | froletype | 角色类型 | varchar | 50 |  | √ | 'user' | 角色类型,枚举: user :人员角色 approvalposition :岗位角色 |
| 13 | fnumber | 编码 | varchar | 36 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_wf_role_number |  | fnumber |
| 2 | t_wf_role_pkey |  | fid |

---

## 人员明细-多语言表 t_wf_roleentry_l

- **表名称：** 人员明细-多语言表
- **表名：** t_wf_roleentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fmulilangdimension1 | 维度1（多语言） | varchar | 500 |  | √ | ' ' | 维度1（多语言） |
| 2 | fmulilangdimension2 | 维度2（多语言） | varchar | 500 |  | √ | ' ' | 维度2（多语言） |
| 3 | fmulilangdimension3 | 维度3（多语言） | varchar | 500 |  | √ | ' ' | 维度3（多语言） |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fmulilangdimension4 | 维度4（多语言） | varchar | 500 |  | √ | ' ' | 维度4（多语言） |
| 6 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_wf_roleentry_l |  | fpkid |
| 2 | idx_wf_roleentry_l |  | fentryid,flocaleid |

---

## 人员明细-子表 t_wf_roleentry

- **表名称：** 人员明细-子表
- **表名：** t_wf_roleentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fparam | 参数 | varchar | 255 |  | √ | ' ' | 参数 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | forg | 审批组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | ffunctiontype | 职能类型 | int8 | 64 |  | √ | 0 | 职能类型 |
| 6 | fposition | fposition | int8 | 64 |  | √ | 0 |  |
| 7 | fapprovalposition | 审批岗位 | int8 | 64 |  | √ | 0 | 岗位 bos_position |
| 8 | falternateuser | 指定处理人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | fdimension1 | 维度1（id） | varchar | 36 |  | √ | ' ' | 维度1（id） |
| 10 | fnumberdimension1 | 维度1（编码） | varchar | 100 |  | √ | ' ' | 维度1（编码） |
| 11 | fnumberdimension2 | 维度2（编码） | varchar | 100 |  | √ | ' ' | 维度2（编码） |
| 12 | fdimension3 | 维度3（id） | varchar | 36 |  | √ | ' ' | 维度3（id） |
| 13 | fdimension2 | 维度2（id） | varchar | 36 |  | √ | ' ' | 维度2（id） |
| 14 | fuser | 审批人员 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fdimension4 | 维度4（id） | varchar | 36 |  | √ | ' ' | 维度4（id） |
| 16 | fnumberdimension3 | 维度3（编码） | varchar | 100 |  | √ | ' ' | 维度3（编码） |
| 17 | fnumberdimension4 | 维度4（编码） | varchar | 100 |  | √ | ' ' | 维度4（编码） |
| 18 | fmulilangdimension1 | 维度1（多语言） | varchar | 500 |  | √ | ' ' | 维度1（多语言） |
| 19 | fmulilangdimension2 | 维度2（多语言） | varchar | 500 |  | √ | ' ' | 维度2（多语言） |
| 20 | fmulilangdimension3 | 维度3（多语言） | varchar | 500 |  | √ | ' ' | 维度3（多语言） |
| 21 | fmulilangdimension4 | 维度4（多语言） | varchar | 500 |  | √ | ' ' | 维度4（多语言） |
| 22 | falternatetype | 审批人员不可用时处理策略 | varchar | 36 |  | √ | ' ' | 审批人员不可用时处理策略,枚举: superior :由组织负责人审批 designatedPerson :由指定人员审批 |
| 23 | ftype | ftype | varchar | 36 |  | √ | ' ' |  |
| 24 | fincludadminsub | 包含行政组织下级 | bpchar | 1 |  | √ | '1' | 包含行政组织下级 |
| 25 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 26 | fuserposition | 审批显示职位 | int8 | 64 |  | √ | 0 | 人员任职 bos_userposition |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_wf_roleentry_id |  | fid |
| 2 | t_wf_roleentry_pkey |  | fentryid |
