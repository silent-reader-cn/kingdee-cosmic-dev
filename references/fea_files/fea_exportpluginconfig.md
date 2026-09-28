# 导出元素插件服务配置-fea_exportpluginconfig

## 导出元素插件服务配置-主表 t_fea_exportpluginconfig

- **表名称：** 导出元素插件服务配置-主表
- **表名：** t_fea_exportpluginconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fentityid | 单据类型 | varchar | 255 |  | √ | ' ' | 单据主实体 bos_billmainentity |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fea_exporpluginconfig |  | fentityid |
| 2 | pk_t_fea_exportpluginconfig |  | fid |

---

## 单据体-子表 t_fea_configentry

- **表名称：** 单据体-子表
- **表名：** t_fea_configentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftype | 插件类型 | varchar | 255 |  | √ | ' ' | 插件类型,枚举: ks :ks ksjava :ksjava java :java |
| 3 | fpluginvalue_tag | 插件代码_详情 | text | 0 |  |  | null | 插件代码_详情 |
| 4 | ffiletype | 文件格式 | bpchar | 1 |  | √ | '0' | 文件格式,枚举: 2 :通用 0 :xml 1 :csv |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fenable | 是否启用 | bpchar | 1 |  | √ | '0' | 是否启用 |
| 7 | fpluginvalue | 插件代码 | varchar | 255 |  | √ | ' ' | 插件代码 |
| 8 | fplugin | 插件 | varchar | 255 |  | √ | ' ' | 插件 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fea_configentry |  | fentryid |
| 2 | idx_fea_configentry |  | fid |
