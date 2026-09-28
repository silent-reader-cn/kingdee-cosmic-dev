# 历史数据升级登记-xkcts_upgrade_service

## 历史数据升级登记-主表 t_xkcts_upgrade_service

- **表名称：** 历史数据升级登记-主表
- **表名：** t_xkcts_upgrade_service

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ffailures | 失败次数 | int8 | 64 |  | √ | 0 | 失败次数 |
| 3 | flog_tag | 升级日志_详情 | text | 0 |  |  | null | 升级日志_详情 |
| 4 | flog | 升级日志 | varchar | 255 |  | √ | ' ' | 升级日志 |
| 5 | fappid | 应用 | varchar | 36 |  | √ | ' ' | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |
| 6 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 7 | fcreater | 创建人 | varchar | 50 |  | √ | ' ' | 创建人 |
| 8 | bpchar | bpchar | bpchar | 1 |  | √ | '0' |  |
| 9 | fretrycnt | 重试次数 | int8 | 64 |  | √ | 0 | 重试次数 |
| 10 | fupgradedate | 升级日期 | timestamp | 0 |  |  | null | 升级日期 |
| 11 | fplugin | 升级插件 | varchar | 200 |  | √ | ' ' | 升级插件 |
| 12 | fdesc | 描述 | varchar | 200 |  | √ | ' ' | 描述 |
| 13 | fentityid | 业务对象 | varchar | 36 |  | √ | ' ' | [业务对象 bos_objecttype](../mdl_files/bos_objecttype.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkcts_upgrade_service |  | fid |
