# 元数据操作日志-meta_log

## 元数据操作日志-主表 t_log_metaoperate

- **表名称：** 元数据操作日志-主表
- **表名：** t_log_metaoperate

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftype | 操作类型 | varchar | 2 |  | √ | '1' | 操作类型,枚举: 1 :设计器 2 :应用导入 3 :页面导入 4 :升级部署 5 :页面删除 6 :应用删除 7 :启用禁用 8 :botp保存 9 :botp删除 10 :botp导入 11 :botp初始化 12 :应用编辑 13 :应用菜单编辑 14 :应用功能分组编辑 15 :应用启用禁用 16 :应用菜单删除 17 :轻扩展暂存 18 :轻扩展发布 19 :轻扩展取消发布 |
| 3 | foperator | 操作人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | foperatetime | 操作时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 操作时间 |
| 5 | fisv | isv | varchar | 8 |  | √ | ' ' | isv |
| 6 | ftaskid | 包ID | int8 | 64 |  | √ | 0 | 包ID |
| 7 | fcontent | 描述 | text | 0 |  |  | null | 描述 |
| 8 | fversion | 版本 | varchar | 18 |  | √ | ' ' | 版本 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_log_metaoperate_pkey |  | fid |
| 2 | idx_log_metaoperate_optime |  | foperatetime |

---

## 单据体-子表 t_log_metaversion

- **表名称：** 单据体-子表
- **表名：** t_log_metaversion

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 1000 |  |  | null | 备注 |
| 3 | fmetaver | 元数据版本 | int8 | 64 |  | √ | 0 | 元数据版本 |
| 4 | ftype | 元数据类型 | bpchar | 1 |  | √ | '1' | 元数据类型,枚举: 1 :表单 2 :应用 3 :多语言 |
| 5 | fmetanumber | 元数据编码 | varchar | 160 |  | √ | '1' | 元数据编码 |
| 6 | fmetaid | 元数据ID | varchar | 36 |  | √ | ' ' | 元数据ID |
| 7 | fdata | 元数据 | text | 0 |  |  | null | 元数据 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fbizappid | 应用 | varchar | 36 |  | √ | ' ' | 业务应用实体 bos_devportal_bizapp |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_log_metaversion_pkey |  | fentryid |
| 2 | idx_t_log_metaversion_metaid |  | fmetaid |
| 3 | idx_log_metaversion_fid |  | fid |
