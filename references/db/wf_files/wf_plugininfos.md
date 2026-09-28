# 插件信息-wf_plugininfos

## 插件信息-主表 t_wf_plugininfos

- **表名称：** 插件信息-主表
- **表名：** t_wf_plugininfos

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fnodename | 节点名称 | varchar | 500 |  | √ | ' ' | 节点名称 |
| 3 | ftype | 类型 | varchar | 50 |  | √ | ' ' | 类型 |
| 4 | fplugin | 插件 | varchar | 255 |  | √ | ' ' | 插件 |
| 5 | fprocnumber | 流程编码 | varchar | 50 |  | √ | ' ' | 流程编码 |
| 6 | fnodenumber | 节点编码 | varchar | 200 |  | √ | ' ' | 节点编码 |
| 7 | fversionstate | 是否最新版 | varchar | 50 |  | √ | ' ' | 是否最新版 |
| 8 | fversion | 版本 | varchar | 50 |  | √ | ' ' | 版本 |
| 9 | fentrabill | 实体编码 | varchar | 50 |  | √ | ' ' | 实体编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_wf_plugininfos_entrabill |  | fentrabill |
| 2 | idx_wf_plugininfos_procnumber |  | fprocnumber |
| 3 | pk_t_wf_plugininfos |  | fid |
