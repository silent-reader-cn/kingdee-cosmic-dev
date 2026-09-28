# 工作流管理-chatbi_workflow

## 工作流管理-主表 t_cbi_workflow

- **表名称：** 工作流管理-主表
- **表名：** t_cbi_workflow

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 200 |  | √ | ' ' | 名称 |
| 3 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 4 | fmodifydate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 5 | fcontent_tag | 详情 | text | 0 |  |  | null | 详情 |
| 6 | fcreater | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fenable | 状态 | bpchar | 1 |  | √ | ' ' | 状态,枚举: 1 :启用 0 :禁用 |
| 8 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 10 | fcontent |  | text | 0 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cbi_workflow |  | fid |

---

## 单据体-子表 t_cbi_workflow_model

- **表名称：** 单据体-子表
- **表名：** t_cbi_workflow_model

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftitle | 节点标题 | varchar | 200 |  | √ | ' ' | 节点标题 |
| 3 | fmodelnumber | 模型服务编码 | varchar | 100 |  | √ | ' ' | 模型服务编码 |
| 4 | fconfigmodel | model | varchar | 50 |  | √ | ' ' | model |
| 5 | fnodeid | 节点ID | varchar | 50 |  | √ | ' ' | 节点ID |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fdesc | 描述 | varchar | 500 |  | √ | ' ' | 描述 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fbasedatamodel | 模型 | int8 | 64 |  | √ | 0 | [模型服务 aicc_service](../aicc_files/aicc_service.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cbi_workflow_model |  | fentryid |
| 2 | idx_cbi_workflow_model_id |  | fid |

---

## 单据体-子表 t_cbi_workflow_tool

- **表名称：** 单据体-子表
- **表名：** t_cbi_workflow_tool

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftitle | 节点标题 | varchar | 200 |  | √ | ' ' | 节点标题 |
| 3 | ftoolmodel | 工具 | int8 | 64 |  | √ | 0 | [工作流基础资料 chatbi_workflow_base](../chatbi_files/chatbi_workflow_base.md) |
| 4 | fnodeid | 节点ID | varchar | 100 |  | √ | ' ' | 节点ID |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | ftooltype | 工具类型 | varchar | 100 |  | √ | ' ' | 工具类型 |
| 7 | fdesc | 描述 | varchar | 1000 |  | √ | ' ' | 描述 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cbi_workflow_tool_id |  | fid |
| 2 | pk_t_cbi_workflow_tool |  | fentryid |

---

## 单据体-子表 t_cbi_workflow_http

- **表名称：** 单据体-子表
- **表名：** t_cbi_workflow_http

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftitle | 节点标题 | varchar | 200 |  | √ | ' ' | 节点标题 |
| 3 | fnodeid | 节点ID | varchar | 50 |  | √ | ' ' | 节点ID |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | furl | URL | varchar | 500 |  | √ | ' ' | URL |
| 6 | fdesc | 描述 | varchar | 500 |  | √ | ' ' | 描述 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cbi_workflow_http |  | fentryid |
| 2 | idx_cbi_workflow_http_id |  | fid |

---

## 工作流文件-附件表 t_cbi_workflow_file

- **表名称：** 工作流文件-附件表
- **表名：** t_cbi_workflow_file

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [附件字段实体 bd_attachment](../frame_files/bd_attachment.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | FPKID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cbi_workflow_file |  | fpkid |
