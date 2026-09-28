# 生成凭证插件-ai_buildvchplugin

## 生成凭证插件-主表 t_ai_buildvchplugin

- **表名称：** 生成凭证插件-主表
- **表名：** t_ai_buildvchplugin

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fplugin | 插件类 | varchar | 100 |  |  | ' ' | 插件类 |
| 3 | fdesc | 插件描述 | varchar | 255 |  |  | ' ' | 插件描述 |
| 4 | fenabled | 启用 | bpchar | 1 |  | √ | '0' | 启用 |
| 5 | fissyspreset | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 6 | fsourcebill | 单据 | varchar | 36 |  | √ | ' ' | [业务对象 bos_objecttype](../mdl_files/bos_objecttype.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_ai_buildvchplugin_pkey |  | fid |
| 2 | idx_ai_buildvchplugin_sb |  | fsourcebill |
