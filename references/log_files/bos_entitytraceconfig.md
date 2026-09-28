# 监控配置-bos_entitytraceconfig

## 监控配置-主表 t_log_etconfig

- **表名称：** 监控配置-主表
- **表名：** t_log_etconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | frealtime | 是否实时监听 | bpchar | 1 |  | √ | '0' | 是否实时监听 |
| 6 | fmodifytime | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_log_etconfig_cr |  | fcreatorid |
| 2 | pk_log_etconfig |  | fid |

---

## 监听方案-子表 t_log_etconfigentry

- **表名称：** 监听方案-子表
- **表名：** t_log_etconfigentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fschemeparam | 监听参数 | text | 0 |  |  | null | 监听参数 |
| 3 | fschemeid | 监听方案标识 | varchar | 100 |  | √ | ' ' | 监听方案标识 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 1 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fschemeenable | 启用 | bpchar | 1 |  | √ | '1' | 启用 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_log_etconfigentry_id |  | fid |
| 2 | pk_log_etconfigentry |  | fentryid |
