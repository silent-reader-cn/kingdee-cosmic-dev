# 节点工具箱-wf_nodetoolbox

## 节点工具箱-主表 t_wf_nodetoolbox

- **表名称：** 节点工具箱-主表
- **表名：** t_wf_nodetoolbox

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fprocesstype | 流程类型 | varchar | 50 |  | √ | 'AuditFlow' | 流程类型,枚举: AuditFlow :审批流 |
| 6 | forg | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fappid | 应用id | varchar | 50 |  | √ | ' ' | 应用id |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fapplicationtype | 应用类型 | varchar | 50 |  | √ | 'common' | 应用类型,枚举: common :通用 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fcloudid | 云ID | varchar | 50 |  | √ | ' ' | 云ID |
| 12 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 13 | fisinitialization | 是否预置 | bpchar | 1 |  | √ | '0' | 是否预置 |
| 14 | fisdefault | 是否缺省 | bpchar | 1 |  | √ | '0' | 是否缺省 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_wf_nodetoolbox_number |  | fnumber |
| 2 | pk_wf_nodetoolbox |  | fid |

---

## 节点工具箱-多语言表 t_wf_nodetoolbox_l

- **表名称：** 节点工具箱-多语言表
- **表名：** t_wf_nodetoolbox_l

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
| 1 | idx_wf_nodetoolbox_l |  | fid,flocaleid |
| 2 | pk_wf_nodetoolbox_l |  | fpkid |

---

## 节点模板-子表 t_wf_nodeboxconfig

- **表名称：** 节点模板-子表
- **表名：** t_wf_nodeboxconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 4 | fnodetemplate | 节点模板 | int8 | 64 |  | √ | 0 | [节点模板库 wf_nodetemplate](../wf_files/wf_nodetemplate.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_wf_nodeboxconfig |  | fid |
| 2 | pk_wf_nodeboxconfig |  | fentryid |
