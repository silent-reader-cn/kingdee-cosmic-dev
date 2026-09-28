# 插件执行耗时统计-wf_pluginexesummary

## 插件执行耗时统计-主表 t_wf_pluginexesummary

- **表名称：** 插件执行耗时统计-主表
- **表名：** t_wf_pluginexesummary

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fexecutedtimes | 执行次数 | int4 | 32 |  | √ | 0 | 执行次数 |
| 3 | fpluginno | 插件编码 | varchar | 255 |  | √ | ' ' | 插件编码 |
| 4 | ftotalduration | 插件执行总耗时(s) | int8 | 64 |  | √ | 0 | 插件执行总耗时(s) |
| 5 | faverageduration | 平均耗时(s) | int8 | 64 |  | √ | 0 | 平均耗时(s) |
| 6 | fpluginname | 插件名称 | varchar | 500 |  | √ | ' ' | 插件名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_wf_pluginexesumy_pluginno |  | fpluginno |
| 2 | pk_wf_pluginexesummary |  | fid |
| 3 | idx_wf_pluginexesumy_plugname |  | fpluginname |

---

## 插件执行耗时统计-多语言表 t_wf_pluginexesummary_l

- **表名称：** 插件执行耗时统计-多语言表
- **表名：** t_wf_pluginexesummary_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fpluginname | 插件名称 | varchar | 500 |  | √ | ' ' | 插件名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_wf_pluginexesummary_l |  | fpkid |
| 2 | idx_wf_pluginexesummary_l |  | fid,flocaleid |
