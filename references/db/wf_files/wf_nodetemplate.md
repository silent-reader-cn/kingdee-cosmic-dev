# 节点模板库-wf_nodetemplate

## 节点模板库-主表 t_wf_nodetemplate

- **表名称：** 节点模板库-主表
- **表名：** t_wf_nodetemplate

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fishidden | 是否隐藏 | bpchar | 1 |  | √ | '0' | 是否隐藏 |
| 3 | fgroupid | 所属分组 | int8 | 64 |  | √ | 0 | 节点模板分组 wf_nodetemplategroup |
| 4 | forg | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fappid | 应用至 | varchar | 36 |  | √ | ' ' | 应用至 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fstatus | 数据状态 | varchar | 50 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fbizidentification | 业务标识 | varchar | 50 |  | √ | ' ' | 业务标识 |
| 9 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fdevelopmenttype | 开发类型 | varchar | 50 |  | √ | ' ' | 开发类型,枚举: B :扩展 C :继承 D :复制 |
| 12 | fentityid | 单据 | varchar | 50 |  | √ | ' ' | 单据 |
| 13 | fisextend | 可扩展 | bpchar | 1 |  | √ | '0' | 可扩展 |
| 14 | fversion | 版本 | varchar | 30 |  | √ | 'Premium' | 版本,枚举: Premium :高级版 Standard :标准版 |
| 15 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 16 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 18 | fissystemnode | 系统节点 | bpchar | 1 |  | √ | '0' | 系统节点 |
| 19 | fprocesstype | 流程类型 | varchar | 30 |  | √ | 'AuditFlow' | 流程类型,枚举: AuditFlow :审批流 BizFlow :业务流 |
| 20 | fpropsdefinition | 节点属性定义 | text | 0 |  |  | null | 节点属性定义 |
| 21 | fproperties | 节点属性 | text | 0 |  |  | null | 节点属性 |
| 22 | fcloudid | 云ID | varchar | 36 |  | √ | ' ' | 云ID |
| 23 | fenable | 使用状态 | varchar | 30 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :启用 |
| 24 | fstenciltype | 继承自 | varchar | 50 |  | √ | ' ' | 继承自 |
| 25 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 26 | fisinitialization | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_wf_nodetemplate_number |  | fnumber |
| 2 | pk_t_wf_nodetemplate |  | fid |
| 3 | idx_wf_nodetemplate |  | fcloudid,fstenciltype |

---

## 节点模板库-多语言表 t_wf_nodetemplate_l

- **表名称：** 节点模板库-多语言表
- **表名：** t_wf_nodetemplate_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_wf_nodetemplate_l |  | fid,flocaleid |
| 2 | pk_t_wf_nodetemplate_l |  | fpkid |
