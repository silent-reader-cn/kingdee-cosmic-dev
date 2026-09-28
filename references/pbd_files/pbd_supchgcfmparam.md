# 供应商变更生效字段配置-pbd_supchgcfmparam

## 供应商变更生效字段配置-主表 t_pbd_supchgparam

- **表名称：** 供应商变更生效字段配置-主表
- **表名：** t_pbd_supchgparam

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 3 | fnumber | 配置编码 | varchar | 80 |  | √ | ' ' | 配置编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_pbd_supchgparam |  | fid |
| 2 | idx_pbd_supchgparam_fnumber |  | fnumber |

---

## 附件配置分录-子表 t_pbd_supchgattconfig

- **表名称：** 附件配置分录-子表
- **表名：** t_pbd_supchgattconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fadvconapname | 附件所在容器标识 | varchar | 30 |  | √ | ' ' | 附件所在容器标识 |
| 3 | fattachentrynote | 行备注 | varchar | 255 |  | √ | ' ' | 行备注 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | foldattachment | 变更前附件面板标识 | varchar | 30 |  | √ | ' ' | 变更前附件面板标识 |
| 6 | fnewattachment | 变更后附件面板标识 | varchar | 30 |  | √ | ' ' | 变更后附件面板标识 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_pbd_supchgattconfig |  | fentryid |
| 2 | index_pbd_chgconfig_fid_fseq |  | fid,fseq |

---

## 生效字段配置-子表 t_pbd_supchgheadconfig

- **表名称：** 生效字段配置-子表
- **表名：** t_pbd_supchgheadconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsourcefield | 源单字段标识 | varchar | 30 |  | √ | ' ' | 源单字段标识 |
| 3 | ftargetfield | 目标单字段标识 | varchar | 30 |  | √ | ' ' | 目标单字段标识 |
| 4 | ffieldsentrynote | 行备注 | varchar | 255 |  | √ | ' ' | 行备注 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pbd_chgheadconfig_fid_fseq |  | fid,fseq |
| 2 | pk_t_pbd_supchgheadconfig |  | fentryid |
