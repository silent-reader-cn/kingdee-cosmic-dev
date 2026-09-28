# 业务扩展插件-bos_bizextplugin

## 业务扩展插件-分表 t_meta_bizextplugin_s

- **表名称：** 业务扩展插件-分表
- **表名：** t_meta_bizextplugin_s

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 1 :已启用 0 :已禁用 |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_meta_bizextplugin_s |  | fentryid |
| 2 | idx_meta_bizextplugin_sid |  | fid |

---

## 业务扩展插件-主表 t_meta_bizextplugin

- **表名称：** 业务扩展插件-主表
- **表名：** t_meta_bizextplugin

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 业务场景编码 | int8 | 64 |  | √ | 0 | [业务扩展场景 bos_bizextcase](../mdl_files/bos_bizextcase.md) |
| 2 | fremark | 扩展实现说明 | varchar | 500 |  | √ | ' ' | 扩展实现说明 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fissysdisable | 系统禁用 | bpchar | 1 |  | √ | '0' | 系统禁用 |
| 5 | fpluginclass | 扩展插件 | varchar | 200 |  | √ | ' ' | 扩展插件 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fseq | 执行顺序 | int4 | 32 |  | √ | 0 | 执行顺序 |
| 8 | fisv | 开发商 | varchar | 200 |  | √ | ' ' | 开发商 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | ftype | 插件类型 | bpchar | 1 |  | √ | '0' | 插件类型,枚举: 0 :Java插件 1 :Js脚本插件 2 :Ts脚本插件 |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 13 | fversion | 版本 | int8 | 64 |  | √ | 0 | 版本 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_meta_bizextplugin_no |  | fpluginclass |
| 2 | pk_meta_bizextplugin |  | fentryid |
| 3 | idx_meta_bizextplugin_id |  | fid |
