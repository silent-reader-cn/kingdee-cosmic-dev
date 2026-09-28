# 流程模板-wf_proctemplate

## 流程模板-多语言表 t_wf_proctpl_l

- **表名称：** 流程模板-多语言表
- **表名：** t_wf_proctpl_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 模板名称 | varchar | 500 |  | √ | ' ' | 模板名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 模板描述 | varchar | 200 |  | √ | ' ' | 模板描述 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_wf_proctpl_l |  | fpkid |
| 2 | idx_wf_proctpl_l |  | fid,flocaleid |

---

## 流程模板-主表 t_wf_proctpl

- **表名称：** 流程模板-主表
- **表名：** t_wf_proctpl

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 模板名称 | varchar | 500 |  | √ | ' ' | 模板名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fcopyfrom | 复制自 | int8 | 64 |  | √ | 0 | 流程模板 wf_proctemplate |
| 5 | fparentid | 父模板 | int8 | 64 |  | √ | 0 | 流程模板 wf_proctemplate |
| 6 | fresourceid | 模版资源ID | int8 | 64 |  | √ | 0 | 模版资源ID |
| 7 | forgid | 所属组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fentitynumber | 单据 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 9 | fdescription | 模板描述 | varchar | 200 |  | √ | ' ' | 模板描述 |
| 10 | fprocesstype | 流程类型 | varchar | 30 |  | √ | 'AuditFlow' | 流程类型,枚举: AuditFlow :审批流 BizFlow :业务流 |
| 11 | flevel | 模板级别 | varchar | 5 |  | √ | ' ' | 模板级别,枚举: 1 :一级 2 :二级 3 :三级 |
| 12 | fstatus | 使用状态 | varchar | 30 |  | √ | 'disable' | 使用状态,枚举: enable :启用 disable :禁用 |
| 13 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 16 | fpreset | 是否预置 | bpchar | 1 |  | √ | '0' | 是否预置 |
| 17 | fcategoryid | 所属分类 | int8 | 64 |  | √ | 0 | 流程模板分类 wf_proctemplatecategory |
| 18 | fpublish | 是否发布 | bpchar | 1 |  | √ | '0' | 是否发布 |
| 19 | fnumber | 模板编码 | varchar | 50 |  | √ | ' ' | 模板编码 |
| 20 | fidentification | 模板标识 | varchar | 50 |  | √ | ' ' | 模板标识 |
| 21 | fparentversion | 父模板版本 | int4 | 32 |  | √ | 0 | 父模板版本 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_wf_proctpl |  | fid |
| 2 | idx_wf_proctpl_category |  | fcategoryid |
| 3 | idx_wf_proctpl_identifi |  | fidentification |
| 4 | idx_wf_proctpl_number |  | fnumber |
| 5 | idx_wf_proctpl_org |  | forgid |
| 6 | idx_wf_proctpl_entity |  | fentitynumber |
